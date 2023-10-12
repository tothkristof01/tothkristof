# Beléptetőrendszer

def regisztracio():
    ok_regisztracio = True
    felhasznalo_email = felhasznalonev()
    felhasznalo_jelszo = jelszo_keres()

    if not jelszo_ellenorzes(felhasznalo_jelszo, 3):
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


def jelszo_ellenorzes(felhasznalo_jelszo, probalkozas):
    i = 1
    jelszo2 = input("Kérem ismét a jelszót: ")
    while jelszo2 != felhasznalo_jelszo and i < probalkozas:
        jelszo2 = input("Kérem ismét a jelszót: ")
        i += 1
    if jelszo2 == felhasznalo_jelszo:
        ok_jelszo = True
    else:
        ok_jelszo = False
    return ok_jelszo


def beleptetes():
    pass


# Innen indul a program
if regisztracio():
    print("Sikerült a regisztráció\n")
    beleptetes()
else:
    print("Sikertelen regisztráció\nPróbálja újra")
