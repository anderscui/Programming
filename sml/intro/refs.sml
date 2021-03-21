val x = ref 1;
val x2 = !x;
x := 2;
val x2 = !x;

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
