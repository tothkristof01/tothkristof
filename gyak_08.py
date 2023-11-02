from tkinter import *
from tkinter import messagebox

import gyak_09

def belepes_ablak():
    def ok_gomb_kezelese():
        belepes.destroy()

    def reg_gomb_kezelese():
        belepes.destroy()

    belepes = Tk()
    belepes.title("Felhasználó beléptetése")

    felh_nev_cimke = Label(belepes, text="Felhaszmnáló neve (email):")
    felh_jelszo_cimke = Label(belepes, text="Jelszó:")

    felh_nev = Entry(belepes, width=30)
    felh_jelszo = Entry(belepes, width=20)

    gomb_ok = Button(belepes, text="OK", command=ok_gomb_kezelese, width=10)
    gomb_reg = Button(belepes, text="Regisztráció", command=reg_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0, padx=10, pady=20, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, sticky=E, padx=10)
    felh_nev.grid(row=0, column=1, padx=10, sticky=W)
    felh_jelszo.grid(row=1, column=1, sticky=W, padx=10)
    gomb_ok.grid(row=2, column=0, pady=20)
    gomb_reg.grid(row=2, column=1)

    belepes.mainloop()

def reg_ablak():
    def ok_gomb_kezelese():
        if jsz.get() == jsz2.get():
            regisztracio.destroy()
        else:
            messagebox.showerror("Hiba", "Nem egyezik a két jelszó")




    def jelszo_gomb_kezelese():
        pw.jelszo_generalasa()
        jsz.set(pw.jelszo)
        jsz2.set(pw.jelszo)

    pw = gyak_09.Jelszo()

    regisztracio = Tk()
    regisztracio.title("Regisztráció")

    felh_nev_cimke = Label(regisztracio, text="Felhasználó neve (email):")
    felh_jelszo_cimke =Label(regisztracio, text="Jelszó:")
    felh_jelszo2_cimke = Label(regisztracio, text="A jelszó ismét:")

    felh_nev = Entry(regisztracio, width=30)
    jsz = StringVar()
    jsz.set("")
    felh_jelszo = Entry(regisztracio, textvariable=jsz, width=20)
    jsz2 = StringVar()
    jsz2.set("")
    felh_jelszo2 = Entry(regisztracio, textvariable=jsz2, width=20)

    gomb_ok = Button(regisztracio, text="OK", command=ok_gomb_kezelese, width=15)
    gomb_jelszo = Button(regisztracio, text="Jelszó generálása!", command=jelszo_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0)
    felh_jelszo_cimke.grid(row=1, column=0)
    felh_jelszo2_cimke.grid(row=2, column=0)
    felh_nev.grid(row=0, column=1)
    felh_jelszo.grid(row=1, column=1)
    felh_jelszo2.grid(row=2, column=1)
    gomb_ok.grid(row=3, column=0, columnspan=3, pady=10)
    gomb_jelszo.grid(row=1, column=2)

    regisztracio.mainloop()

#belepes_ablak()
reg_ablak()