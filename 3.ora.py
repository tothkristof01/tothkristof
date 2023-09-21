# Jövedelemszámítás
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy?"))
if kor > 25:
    gyerek = input("Van 3 gyereked és nő vagy (igen/nem)?")
    while gyerek not in ["igen", "Igen", "i", "I", "Nem", "nem", "n"]:
        gyerek = input("HIBA!!!\nVan 3 gyereked és nő vagy (igen/nem)?")

brutto = int(input("Mennyi a bruttód?"))

if kor <= 25 or gyerek in ["igen", "Igen", "i", "I"]:
    if brutto > 500000:
        szja = (brutto - 500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15
print("Fizetendő adó".center(40))
print("SZJA:".ljust(30, "_"), str(int(szja)).rjust(10, "_"), sep="")
print("Nyugdíj:".ljust(30, "_"), str(int(brutto * 0.1)).rjust(10, "_"), sep="")
print("TB:".ljust(30, "_"), str(int(brutto * 0.07)).rjust(10, "_"), sep="")
print("MKnélkül:".ljust(30, "_"), str(int(brutto * 0.015)).rjust(10, "_"), sep="")
print("")
print("Nettó:".ljust(30, "_"), str(int(brutto - brutto * 0.0185 - szja)).rjust(10, "_"), sep="")





