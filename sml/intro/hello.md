# Introduction to SML

# 1. Getting Started

Use [Standard ML of New Jersey](https://www.smlnj.org/)
* SML has a REPL interface.

# 1.1 Hello

The fundamental principle of FP:
> A program is an expression that evaluates to a value.

因此，`"Hello World!";` 就是一个完整的程序，它是一个 `value literal`（or `atomic expression`）。ML 总是会推断（infer）程序的类型（type），这里是 `string`。

PS: 符号用 `~1` 这样来表示，取模用 `22 mod 7` 表示，除法用 `div`。

# 1.2 Conditional and Boolean Expressions

> A conditional program is also an expression.
> Expressions can be freely combined as far as they are type correct.

```ml
- if true then 1 else 2;
# val it = 1 : int

- (7 mod 2) = (if false then 1 else 2);
# val it = false : bool
```

# 1.3 Chars and Strings

```ml
- if #"A" > #"a" then ord #"A" else ord #"a";
# val it = 97 : int

- chr 97;
# val it = #"a" : char

- str it;
# it = "a" : string

- "SML" > "Ocaml";
# val it = true : bool

- "Standard " ^ "ML";
# val it = "Standard ML" : string
```

# 1.4 Reading Programs from a File

`use "file";`

The system performs the following:
* open the file
* compile, eval, and print;
* close the file
* return to the top-level

# 1.5 No type cast or overloading

To achieve **complete static type checking**, there is no type cast nor overloading.

Make it explicit:

```ml
- real 10 * 3.14;
# val it = 31.4 : real
```

# 2. Value Binding and Function Definitions

# 2.1 Variable binding

To name an exp and use it in the subsequent context.

```ml
- val pi = 3.14;
# val pi = 3.14 : real
```

A name can be one of the following identifiers:

* alphabetical
* symbolic

# 2.2 Function Definitions

```ml
# fun f p = body;

# - fun double x = x * 2;
# val double = fn : int -> int

- double 3 + 1;
# val it = 7 : int
```

`p` is the formal parameter.

求值时从左边开始，`(double 3) + 1;`。

### 2.2.1 函数求值过程

形参作为”扩展了的“ binding，在函数内的 context 是可用的。

# 3. Recursive and High-Order Functions

```ml
fun f p = body;
```

如果 `body` 中包含了对 `f` 的调用，`f` 是递归的。

Tail recursive functions do not consume stack space and therefore more  efficient.

## 3.1 Let Exp

`let` exp introduces local defs.

```sml
let
    val x = 1
in
    x + 1
end;

fun factorial n =
    let
        fun fact n a = if n = 0 then a
                       else fact (n-1) (n*a)
    in
        fact n 1
    end;
(* val it = 2 : int 
val factorial = fn : int -> int *)
```

`let` is an expression.

## 3.2 Local Defs

```sml
local
    val x = 1;
in
    val y = x * 2;
end;
(* val y = 2 : int *)
```

## 3.3 High-Order Functions

```sml
fun power1 (m, n) =
    if m = 0 then 1
    else n * power1(m-1, n);

fun power2 m n =
    if m = 0 then 1
    else n * power2 (m-1) n;

val ans1 = power1(3, 2);
val ans2 = power2 3 2;

(* power2 can take only one parameter, and produces a new function *)
val cube = power2 3;
val ans3 = cube 2;

(*
val power1 = fn : int * int -> int
val power2 = fn : int -> int -> int
val cube = fn : int -> int
*)

(* fun as parameters *)
fun sum f n =
    if n = 1 then f 1
    else f n + sum f (n-1)

val sumOfCubes = sum cube;
val ans4 = sumOfCubes 3; (* 36 *)

val sumOfSquares = sum (power2 2);
val ans5 = sumOfSquares 5; (* 55 *)
```

`power2` 可以仅接受一个参数，”生成“一个新函数。`sum` 接受一个函数，返回另一个函数，核心在于**抽象**的能力。

优先级：

* f a b => (f(a)) b
* int -> int -> int => int -> (int -> int)

## 3.4 Function Expressions

A function is a value, and therefore representable by expressions.

## 3.5 Static Scoping

In general, defining a name hide the previous definition.

* val
* fun
* fn x => e

```sml
val x = 1
val y = x + 1
val x = y + 1
and y = x + 1
(* x = 3, y = 2 *)

val x = 10
val y = 20
fun f x = x + y;
val ans1 = f 3;

val y = 99;
val ans2 = f 3;
(* ans1 = ans2 = 23 *)
```

## 3.6 Binary Operators

In ML, operators are functions that **only take one argument**.

`e1 op e2 => op(e1, e2)`

```sml
fun power (m, n) =
    if m = 0 then 1
    else n * power(m-1, n);

infix 8 power;

val ans1 = 2 power 3 + 10;

(*op power;*)
op power(2, 3);
```

# 4. Type System

Two most notable features of ML type system:

* auto infers a type for **any** expression
* supports polymorphism.

```sml
fun id x = x;
(* val id = fn : 'a -> 'a *)
```

`'a` is type variable which is **instantiated** when the program is used.

```sml
fun twice f x =
    f (f x)

val f = fn x => twice twice x;
val ans2 = f (fn x => x + 1) 1;

(* val twice = fn : ('a -> 'a) -> 'a -> 'a or ('a -> 'a) -> ('a -> 'a)
val f = fn : ('a -> 'a) -> 'a -> 'a *)
```

# 5. Predifined Data Types

# 5.1 Unit Type

`unit` type contains `()` as its only value.

```sml
- 1 before print "one\n";
(* one
val it = 1 : int *)

- ignore 3;
(* val it = () : unit *)
```

## 5.2 Booleans

* not
* andalso
* orelse
* if ... then ... else

## 5.3 Integers

* 123
* 0x123
* ~123

* ~
* +/-/*/div/mod
* >/>=/</<=
* abs

## 5.4 Reals

* 3.14
* 2.99E8

* abs
* real
* floor/ceil/round/trunc

* inf
* nan

## 5.5 Chars

* #"c"

* chr/ord/str
* <= ...

## 5.6 Strings

* "abc"
* "This is a single \
    \string constant."
    
* size
* substring
* explode/implode
* concat
* ^
* print

# 6. Records

## 6.1 Records

```sml
val myMalt = {
    Brand = "Glen Moray",
    Distiller = "Glenlivet",
    Region = "the Highlands",
    Age = 28
}

(* interesting fun name *)
fun createGlen'sMalt (name, age) =
    {
        Brand = name,
        Distiller = "Glenlivet",
        Region = "the Highlands",
        Age = age
    }

(* record as parameter *)
fun isOldMalt {Brand, Distiller, Region, Age} =
    Age > 18

val isOld = isOldMalt myMalt;

(* extract fields *)
val name = #Distiller myMalt;
val {Brand = brand, Distiller = distiller,
     Age = age, Region = region} = myMalt;

(* partial fields *)
val {Region = region2, ...} = myMalt;

(*
val myMalt =
  {Age=28,Brand="Glen Moray",Distiller="Glenlivet",Region="the Highlands"} :
  {Age:int, Brand:string, Distiller:string, Region:string}
val createGlen'sMalt = fn :
  'a * 'b -> {Age:'b, Brand:'a, Distiller:string, Region:string}
val isOldMalt = fn : {Age:int, Brand:'a, Distiller:'b, Region:'c} -> bool
val isOld = true : bool
val name = "Glenlivet" : string
val age = 28 : int
val brand = "Glen Moray" : string
val distiller = "Glenlivet" : string
val region = "the Highlands" : string
val region2 = "the Highlands" : string
*)
```

## 6.2 Tuples

Tuples are special case of records whose labels are numbers.

`(2, 3) => {1=2, 2=3}`

```sml
val p = (2, 3);

fun f (x, y) =
    x + y

val ans1 = f p;

val first = #1 p;
val ans2 = f {1=2, 2=3};
```

# 7. Programming with Lists

## 7.1 Lists

A list is represented by a pointer, so it seems like a `linked list`.

A list can also be regarded as a nested pairs, this is how we build it.

`(1, (2, (3, nil)))`

```sml
- 1 :: 2 :: 3 :: nil;
(* val it = [1,2,3] : int list *)

- [[1], [2, 3]];
(* val it = [[1],[2,3]] : int list list *)
- [fn x => x];
(* val it = [fn] : ('a -> 'a) list *)
```

## 7.2 Decomposing a List with Patterns

The basic operation on a list if pattern matching.

```sml
fun length L =
    case L of nil => 0
    | (h::t) => 1 + length t;

fun zip x =
    case x of (h1::t1, h2::t2) =>
        (h1, h2) :: zip (t1, t2)
    | _ => nil

fun unzip x =
    case x of (h1, h2) :: t =>
        let val (L1, L2) = unzip t
        in (h1::L1, h2::L2)
        end
    | _ => (nil, nil)
```

## 7.3 Built-in Functions for Lists

```sml
(* built-ins *)
val concated = [1] @ [2, 3];
val isNull = null nil;
val head = hd [1, 2];
val tail = tl [1];
val reversed = rev [1, 2, 3];
val mapped = map (fn x => x + 1) [1, 2];
```

## 7.4 General List Function

fold ...

# 8. Datatype Definitions

# 9. Imperative Features

## 9.1 References

Refs are imperative data structure, for which the order matters.

```sml
local
    val state = ref nil : int list ref
    fun toString codes = String.implode (List.map (fn c => chr c) codes)
    fun next nil = [ord #"a"]
             | next (h :: t) = if h = ord #"z" then
                                   ord #"a" :: (next t)
                               else (h+1 :: t)
in
    fun gensym() =
        (state := next (!state);
         toString (!state))
end

val s1 = gensym();
val s2 = gensym();

(*
a
b
*)
```

# 10. Module System

