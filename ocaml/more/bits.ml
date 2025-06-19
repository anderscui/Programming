open Input

(* input: this bit stream is base upon *)
type input_bits = {
  input: input;
  mutable byte: int;
  mutable bit: int
}

let input_bits_of_input i = {
  input = i;
  byte = 0;
  bit = 0
}

let rec getbit b =
  if b.bit = 0 then
    begin
      b.byte <- int_of_char (b.input.input_char ());
      b.bit <- 128;
      getbit b
    end
  else
    let r = b.byte land b.bit > 0 in
      b.bit <- b.bit / 2;
      r

let align b = 
  b.bit <- 0

let getval b n =
  if n <= 0 || n > 31 then
    raise (Invalid_argument "getval")
  else
    let r = ref 0 in
      for x = n - 1 downto 0 do
        r := !r lor ((if getbit b then 1 else 0) lsl x)
      done;
      !r

let getval_32 b n =
  if n < 0 then raise (Invalid_argument "getval_32")
  else if n = 0 then 0l
  else
    let r = ref Int32.zero in
      for x = n - 1 downto 0 do
        r :=
          Int32.logor !r
            (Int32.shift_left (Int32.of_int (if getbit b then 1 else 0)) x)
      done;
      !r

let print_header filename =
  let ch = open_in_bin filename in
  let i = input_of_channel ch in
  let b = input_bits_of_input i in
    let src_port = getval b 16 in
    let dest_port = getval b 16 in
    let seq_number = getval_32 b 32 in
    let ack_number = getval_32 b 32 in
    let data_offset = getval b 4 in
    let reserved = getval b 6 in
    let urgent = getbit b in
    let ack = getbit b in
    let push = getbit b in
    let reset = getbit b in
    let syn = getbit b in
    let fin = getbit b in
    let receive = getval b 16 in
    let checksum = getval b 16 in
    let urgent_pointer = getval b 16 in
      print_string "Source port = ";
      print_int src_port;
      print_string "\nDestination = ";
      print_int dest_port;
      print_string "\nSequence = ";
      print_string (Int32.to_string seq_number);
      print_string "\nAcknowledgement Number = ";
      print_string (Int32.to_string ack_number);
      print_string "\ndata offset = ";
      print_int data_offset;
      print_string "\nreserved = ";
      print_int reserved;
      let print_bool b = print_string (string_of_bool b) in
        print_string "\nFlags:\n Urgent = "; print_bool urgent;
        print_string "\n Ack = "; print_bool ack;
        print_string "\n Push = "; print_bool push;
        print_string "\n Reset = "; print_bool reset;
        print_string "\n Syn = "; print_bool syn;
        print_string "\n Fin = "; print_bool fin;
        print_string "\nReceive window size = ";
        print_int receive;
        print_string "\nChecksum = ";
        print_int checksum;
        print_string "\nUrgent pointer = ";
        print_int urgent_pointer;
        print_string "\n";
        close_in ch

let input_example () = print_header "packet.bin"

(* let () = print_string "hello\n" *)
(* let () = Printf.printf "system word size: %d\n" Sys.word_size *)

