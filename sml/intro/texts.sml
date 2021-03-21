val chars = [ord #"a", ord #"b", ord #"c"]

fun toString cs =
    String.implode (List.map (fn c => chr c) cs);

val s = toString chars;
