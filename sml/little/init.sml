(*Control.Print.printDepth := 20;*)

datatype seasoning =
    Salt
    | Pepper

(* This defines a type *)
datatype num =
    Zero
    | One_more_than of num

(* This defines a shape of types (generics) *)
datatype 'a open_faced_sandwich =
    Bread of 'a
    | Slice of 'a open_faced_sandwich

datatype shish_kebab =
    Skewer
    | Onion of shish_kebab
    | Lamb of shish_kebab
    | Tomato of shish_kebab


(* The type of a function: shish_kebab -> bool
   The number and order of the patterns in the definition of a fun
   should match that of the definition of the consumed datatype *)
fun only_onions(Skewer) = true
    | only_onions(Onion(x)) = only_onions(x)
    | only_onions(Lamb(x)) = false
    | only_onions(Tomato(x)) = false

fun is_vegetarian(Skewer) = true
    | is_vegetarian(Onion(x)) = is_vegetarian(x)
    | is_vegetarian(Lamb(x)) = false
    | is_vegetarian(Tomato(x)) = is_vegetarian(x)

(* now Onion is `shish` *)
datatype 'a shish =
    Bottom of 'a
    | Onion of 'a shish
    | Lamb of 'a shish
    | Tomato of 'a shish

(* 刀，叉，剑 *)
datatype rod =
    Dagger
    | Fork
    | Sword

datatype plate =
    Gold_plate
    | Silver_plate
    | Brass_plate

fun is_veggie (Bottom(x)) = true
    | is_veggie(Onion(x)) = is_veggie(x)
    | is_veggie(Lamb(x)) = false
    | is_veggie(Tomato(x)) = is_veggie(x);

is_veggie:
    'a shish -> bool;

fun what_bottom (Bottom(x)) = x
    | what_bottom(Onion(x)) = what_bottom(x)
    | what_bottom(Lamb(x)) = what_bottom(x)
    | what_bottom(Tomato(x)) = what_bottom(x);

what_bottom:
    'a shish -> 'a;

(* ch 03 *)
datatype pizza =
    Crust
    | Cheese of pizza
    | Onion of pizza
    | Anchovy of pizza
    | Sausage of pizza

fun remove_anchovy (Crust) = Crust
    | remove_anchovy(Cheese(x)) = Cheese(remove_anchovy x)
    | remove_anchovy(Onion(x)) = Onion(remove_anchovy x)
    | remove_anchovy(Anchovy(x)) = remove_anchovy x
    | remove_anchovy(Sausage(x)) = Sausage(remove_anchovy x)


(* ch04 starts *)
datatype meza =
    Shrimp
    | Calamari
    | Escargots
    | Hummus

datatype main =
    Steak
    | Ravioli
    | Chicken
    | Eggplant

datatype salad =
    Green
    | Cucumber
    | Greek

datatype dessert =
    Sundae
    | Mousse
    | Torte

fun add_a_steak (m: meza) =
    (m, Steak)

fun eq_main (Steak, Steak) = true
    | eq_main (Ravioli, Ravioli) = true
    | eq_main (Chicken, Chicken) = true
    | eq_main (Eggplant, Eggplant) = true
    | eq_main (a_main, another) = false

fun has_steak (a: meza, Steak, d: dessert) = true
    | has_steak (a: meza, a_main, d: dessert) = false

(* ch05 *)
datatype 'a pizza =
    Bottom
    | Topping of ('a * ('a pizza))

datatype fish =
    Anchovy
    | Lox
    | Tuna

fun rem_anchovy (Bottom): fish pizza = Bottom
    | rem_anchovy (Topping(Anchovy, p)) = rem_anchovy(p)
    | rem_anchovy (Topping(f, p)) = Topping(f, rem_anchovy(p))

(* always order the patterns according to the alternatives,
   so don't combine them like the above one *)
fun rem_tuna (Bottom) = Bottom
    | rem_tuna (Topping(Anchovy, p)) = Topping(Anchovy, rem_tuna(p))
    | rem_tuna (Topping(Tuna, p)) = rem_tuna(p)
    | rem_tuna (Topping(Lox, p)) = Topping(Lox, rem_tuna(p))

fun eq_fish (Anchovy, Anchovy) = true
    | eq_fish (Lox, Lox) = true
    | eq_fish (Tuna, Tuna) = true
    | eq_fish (a_fish, another) = false

fun rem_fish (Bottom, f) = Bottom
    | rem_fish (Topping(t, p), f) =
        if eq_fish(t, f)
        then rem_fish (p, f)
        else Topping(t, rem_fish (p, f))

fun subst_fish (new, old, Bottom) = Bottom
    | subst_fish (new, old, Topping(t, p)) =
        if eq_fish(t, old)
        then Topping(new, subst_fish (new, old, p))
        else Topping(t, subst_fish (new, old, p))

(* ch06 *)
datatype fruit =
    Peach
    | Apple
    | Pear
    | Lemon
    | Fig

datatype tree =
    Bud
    | Flat of fruit * tree
    | Split of tree * tree

fun flat_only (Bud) = true
    | flat_only (Flat (f, t)) = flat_only(t)
    | flat_only (Split(t1, t2)) = false

fun split_only (Bud) = true
    | split_only (Flat (f, t)) = false
    | split_only (Split(t1, t2)) =
        split_only (t1) andalso split_only (t2)

fun contains_fruit (x) =
    not(split_only(x))

fun height (Bud) = 0
    | height (Flat (f, t)) = 1 + height (t)
    | height (Split (t1, t2)) = 1 + Int.max(height(t1), height(t2))

fun eq_fruit (Peach, Peach) = true
    | eq_fruit (Apple, Apple) = true
    | eq_fruit (Pear, Pear) = true
    | eq_fruit (Lemon, Lemon) = true
    | eq_fruit (Fig, Fig) = true
    | eq_fruit (f1, f2) = false

(* the 1st refers to the 2nd, and the 2nd refers to the 1st *)
datatype
    'a slist =
        Empty
        | Scons of (('a sexp) * ('a slist))
and
    'a sexp =
    An_atom of 'a
    | A_slist of ('a slist)

fun occurs_in_slist (a, Empty)
    = 0
    | occurs_in_slist (a, Scons(s, ss))
        = occurs_in_sexp (a, s) + occurs_in_slist (a, ss)
and occurs_in_sexp (a, An_atom(b))
    = if eq_fruit (a, b) then 1 else 0
    | occurs_in_sexp (a, A_slist (ss)) = occurs_in_slist (a, ss)

(* ch07 *)
fun identity (x) = x

fun true_maker (x) = true

(* Hot is a function: bool -> bool_or_int *)
datatype bool_or_int =
    Hot of bool
    | Cold of int

fun help (f) =
    Hot(true_maker(
            if true_maker(5)
            then f
            else true_maker))

(* A type def that has only one alternative *)
datatype chain =
    Link of (int * (int -> chain))

fun ints (n) =
    Link(n+1, ints)

fun skips (n) =
    Link(n+2, skips)





















