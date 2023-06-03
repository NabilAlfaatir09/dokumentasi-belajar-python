import random

pilihan = "y"

while pilihan.lower() == "y":
    list = ["gunting", "batu", "kertas"]
    komputer = random.choice(list)

    print()
    print("="*30)
    print("Game Suit Gunting Batu Kertas")
    print("="*30, "\n")
    pemain = input("Masukkan pilihan Gunting, Batu, Kertas ? : ")
    if pemain.lower() == komputer:
        print()
        print("="*30)
        print("Hasil suit Seri!")
        print("="*30, "\n")
    elif pemain.lower() == "gunting":
        if komputer == "batu":
            print()
            print("="*30)
            print("Yahh kamu kalah :(")
            print("Kamu     =", pemain, "\nKomputer = ", komputer)
            print("="*30, "\n")
        else:
            print()
            print("="*30)
            print("Horee kamu menang :)")
            print("Kamu     =", pemain, "\nKomputer = ", komputer)
            print("="*30, "\n")
    elif pemain.lower() == "batu":
        if komputer == "kertas":
            print()
            print("="*30)
            print("Yahh kamu kalah :(")
            print("Kamu      =", pemain, "\nKomputer = ", komputer)
            print("="*30, "\n")
        else:
            print()
            print("="*30)
            print("Horee kamu menang :)")
            print("Kamu     =", pemain, "\nKomputer = ", komputer)
            print("="*30, "\n")
    elif pemain.lower() == "kertas":
        if komputer == "gunting":
            print()
            print("="*30)
            print("Yahh kamu kalah :(")
            print("Kamu     =", pemain, "\nKomputer = ", komputer)
            print("="*30, "\n")
        else:
            print()
            print("="*30)
            print("Horee kamu menang :)")
            print("Kamu     =", pemain, "\nKomputer = ", komputer)
            print("="*30, "\n")
    else:
        print("Pilihan yang kamu masukan salah...")

    pilihan = input("Apakah kamu ingin bermain kembali? Y/N = ")
