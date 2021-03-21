use "init.sml";

val num1 = Zero
val num2 = One_more_than(Zero)

(* Zeor != 0, they belongs to diff types. *)

(*val sk1 = Skewer
val sk2 = Onion (Lamb (Onion Skewer))

val onions_only = only_onions(Onion (Onion Skewer))

val is_vegetable1 = is_vegetarian(Tomato (Onion (Tomato Skewer)))
val is_vegetable2 = is_vegetarian(Tomato (Lamb (Tomato Skewer)))*)

(* rod shishi
val shish1 = Onion (Tomato (Bottom Dagger))

val is_veggie1 = is_veggie(shish1);

val bottom1 = what_bottom (Bottom 52);

val removed_anchovy = remove_anchovy(Cheese (Anchovy (Cheese Crust)))*)

(* ch04 *)
val hasSteak1 = has_steak(Hummus, Ravioli, Sundae);
val hasSteak2 = has_steak(Hummus, Steak, Sundae);

(* ch05 *)
val fishPizza = Topping(Anchovy,
                    Topping(Tuna,
                        Topping(Anchovy,
                            Bottom)))

val subst1 = subst_fish (Lox, Anchovy,
                Topping(Anchovy,
                    Topping(Tuna,
                        Topping(Anchovy,
                            Bottom))))
(* The fifth moral
   Write the first draft of a function following all the morals,
   when it is correct and no sooner, simplify *)

(* ch06 *)
val splitOnly1 = split_only Bud;
val splitOnly2 = split_only (Split (Split(Bud,
                                         Bud),
                                   Split(Bud,
                                         Bud)))

val h1 = height(Flat(Fig,
                     Flat(Lemon,
                          Flat(Apple,
                               Bud))));

val o1 = occurs_in_sexp(Fig,
    A_slist(
        Scons(An_atom(Fig),
            Scons(An_atom(Peach),
                Empty))));

val hot1 = Hot true;
val cold1 = Cold 0;

(* the fun that produces a fun *)
fun hot_maker (x) = Hot

val ints1 = ints(0);



