# Beléptetőrendszer

def regisztracio():
    ok_regisztracio = True
    felhasznalonev()
    jelszo_keres()
    ciklus = 1
    while not jelszo_ellenorzes():
        ciklus += 1
        if ciklus > 3:
            ok_regisztracio = False
            break
    return ok_regisztracio


def felhasznalonev():
    felhasznalo_email = input("Kérem az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem jó email!! \nKérem az email címét: ")


def jelszo_keres():
    felhasznalo_jelszo = input("Kérek egy jelszót (1,a,A, min 8 karakter): ")
    ok_jelszo = True
    while ok_jelszo:
        if len(felhasznalo_jelszo) < 8:
            ok_jelszo = False
        szamjegy = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isnumeric():
                szamjegy += 1
        if szamjegy == 0:
            ok_jelszo = False
        if not ok_jelszo:
            felhasznalo_jelszo = input("Nem megfelelő jelszó!!! \nKérek egy jelszót (1,a,A, min 8 karakter): ")
            ok_jelszo = True
        else:
            ok_jelszo = False


def jelszo_ellenorzes():
    ok_jelszo = True
    return ok_jelszo


def beleptetes():
    pass


# Innen indul a program

felhasznalo_email = ""
felhasznalo_jelszo = ""
jelszo_keres()
if regisztracio():
    beleptetes()
