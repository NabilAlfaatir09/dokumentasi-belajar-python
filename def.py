from functools import total_ordering


def sapa(nama):
    print("HI, " + nama + ". Apa kabar?")


sapa("Jamal")


def print_info(nama, usia):
    print("Nama : ", nama)
    print("Usia : ", usia)


print_info(usia=99, nama="budi")


def asal(arg1, *vartuple):
    print("Output nya adalah : ")
    print(arg1)

    for var in vartuple:
        print(var)


asal(10)
asal(10, 20, 30, 50, 70)


def sum(arg1, arg2):
    total = arg1 + arg2
    print("Didalam fungsi total : ", total)
    return total


sum(10, 20)
print("Di luar fungsi, nilai total : ")
