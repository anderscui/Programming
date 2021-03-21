val myMalt = {
    Brand = "Glen Moray",
    Distiller = "Glenlivet",
    Region = "the Highlands",
    Age = 28
}

fun createGlen'sMalt (name, age) =
    {
        Brand = name,
        Distiller = "Glenlivet",
        Region = "the Highlands",
        Age = age
    }

fun isOldMalt {Brand, Distiller, Region, Age} =
    Age > 18

val isOld = isOldMalt myMalt;

val name = #Distiller myMalt;
val {Brand = brand, Distiller = distiller,
     Age = age, Region = region} = myMalt;

val {Region = region2, ...} = myMalt;
