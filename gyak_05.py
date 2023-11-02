# Beléptetőrendszer

def regisztracio():
    ok_regisztracio = True
    felhasznalo_email = felhasznalonev()
    # jelszó automatikus generálása
    felhasznalo_jelszo = jelszo_keres()

    if not jelszo_ellenorzes(felhasznalo_jelszo, 3, "Kérem ismét a jelszót: "):
        ok_regisztracio = False

    if ok_regisztracio:
        with open("jelszo.txt", "a", encoding="utf-8") as fajl:
            fajl.write(felhasznalo_email + ";" + felhasznalo_jelszo + "\n")

    return ok_regisztracio


def felhasznalonev():
    felhasznalo_email = input("Kérem az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem jó email!! \nKérem az email címét: ")
    return felhasznalo_email


def jelszo_keres():
    felhasznalo_jelszo = input("Kérek egy jelszót (1,a,A, min 8 karakter): ")
    ok_jelszo = True
    while ok_jelszo:
        if len(felhasznalo_jelszo) < 8:
            ok_jelszo = False

        van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isnumeric():
                van += 1
        if van == 0:
            ok_jelszo = False

        van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isupper():
                van += 1
        if van == 0:
            ok_jelszo = False

        van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].islower():
                van += 1
        if van == 0:
            ok_jelszo = False

        if not ok_jelszo:
            felhasznalo_jelszo = input("Nem megfelelő jelszó!!! \nKérek egy jelszót (1,a,A, min 8 karakter): ")
            ok_jelszo = True
        else:
            ok_jelszo = False
    return felhasznalo_jelszo


def jelszo_ellenorzes(felhasznalo_jelszo, probalkozas, uzenet):
    i = 1
    jelszo2 = input(uzenet)
    while jelszo2 != felhasznalo_jelszo and i < probalkozas:
        jelszo2 = input(uzenet)
        i += 1
    if jelszo2 == felhasznalo_jelszo:
        ok_jelszo = True
    else:
        ok_jelszo = False
    return ok_jelszo


def felhasznalo_ellenorzese(felhasznalo):
    jelszo = ""
    with open("jelszo.txt", "r", encoding="UTF-8") as fajl:
        for sor in fajl:
            lista = sor.strip()
            user = lista.split(";")
            if user[0] == felhasznalo:
                jelszo = user[1]
    return jelszo


def beleptetes():
    ok_belepes = True
    jelszo = felhasznalo_ellenorzese(felhasznalonev())
    if jelszo == "":
        print("Nincs ilyen felhasználó, regisztálj:")
        ok_belepes = False
    else:
        if not jelszo_ellenorzes(jelszo, 3, "Kérem a jelszót"):
            print("Nem megfelelő a jelszó!")
            ok_belepes = False
    return ok_belepes


def jelszo_generalasa(hossz, kisbetu, nagybetu, szam):
    import string
    import random
    jelszo = ""
    karaktersor = ""
    if kisbetu:
        karaktersor = karaktersor + string.ascii_lowercase
    if nagybetu:
        karaktersor = karaktersor + string.ascii_uppercase
    if szam:
        karaktersor = karaktersor + string.digits
    for _ in range(hossz):
        jelszo = jelszo + karaktersor[random.randint(0, len(karaktersor) - 1)]
    return jelszo


# Innen indul a program
if __name__ == "__main__":
    if regisztracio():
        print("Sikerült a regisztráció\n")
        if beleptetes():
            print("Üdv a fedélzeten!")
        else:
            print("nem sikerült a belépés")
    else:
        print("Sikertelen regisztráció\nPróbálja újra")

