# számológép

def adatkeres(tipus):
    valasz = 0
    if tipus == "sz":
        valasz = input("Kérek egy számot: ")
        while not valasz.isnumeric():
            print("Rossz érték")
            valasz = input("Kérek egy számot: ")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Kérem a műveleti jelet (+,-,/,*): ")
        while valasz not in ["+", "-", "/", "*"]:
            print("Nem érvényes műveleti jel!")
            valasz = input("Kérem a műveleti jelet (+,-,/,*): ")
    return valasz


def muveletvegre():
    eredmeny = 0
    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "/":
        eredmeny = szam1 / szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    return eredmeny


# A program eleje
print("Számológép")
szam1 = adatkeres("sz")
muvelet = adatkeres("m")
szam2 = adatkeres("sz")
vegeredmeny = muveletvegre()

print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("".rjust(50, "_"))
print(str(vegeredmeny).rjust(50))
