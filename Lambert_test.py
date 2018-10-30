R = 6371.11

zobrazeni = input("Zadej typ zobrazeni")


if zobrazeni == "L":
    print("Lambertovo zobrazeni")
    m = int(input("Zadej meritko ve formatu 1:(tvoje zadane cislo)"))
    if m <= 0:
        sys.exit("meritko musi byt vetsi nez 0")
    vypocet = input("Chces vypocitat vsechny poledniky v intervalech, nebo jen jeden? (zadej ALL pro vsechny, ONE pro jeden")
    if vypocet == "ONE":
        v = int(input("Zadej souradnici poledniku ve stupnich"))
        if v <= 0:
            sys.exit("souradnice poledniku musi byt vetsi nez 0")
        a = R * v / m
        print("nakresli polednik", a/m*100000, "cm od stredu")
    if vypocet == "ALL":
        v = int(input("Zadej interval poledniku ve stupnich"))
        if v <= 0:
                sys.exit("interval poledniku musi byt vetsi nez 0")
        a = R * v / m
        a2 = R * (2*v)/ m
        a3 = R * (3*v)/ m
        a4 = R * (4*v)/ m
        a5 = R * (5*v)/ m
        a6 = R * (6*v)/ m
        a7 = R * (7*v)/ m
        a8 = R * (8*v)/ m
        a9 = R * (9*v)/ m
        print("nakresli polednik", a/m*100000, "cm od stredu")
        print("nakresli polednik", a2/m*100000, "cm od stredu")
        print("nakresli polednik", a3/m*100000, "cm od stredu")
        print("nakresli polednik", a4/m*100000, "cm od stredu")
        print("nakresli polednik", a5/m*100000, "cm od stredu")
        print("nakresli polednik", a6/m*100000, "cm od stredu")
        print("nakresli polednik", a7/m*100000, "cm od stredu")
        print("nakresli polednik", a8/m * 100000, "cm od stredu")
        print("nakresli polednik", a9/m * 100000, "cm od stredu")
    u = int(input("Zadej zemepisnou souradnici rovnobezky"))
    b = R * math.sin(u*math.pi/180)
    #ted potrebuji prevest cislo a na centimetry na papire

    print("nakresli rovnobezku", b/m*100,"cm od stredu" )