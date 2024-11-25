import random

angkaBenar = random.randrange(10)
print( angkaBenar )

print("___________ TEBAK ANGKA ________________")
print("Kesempatan anda hanya 7x")
kesempatan = 0
while True:
    angkaJawab = int( input("Angka Tebakan Anda : ") )
    if angkaJawab != angkaBenar and kesempatan == 7:
        print(f"LOSSER... TEBAKAN ANDA SALAH... {angkaBenar} ")
        break
    elif angkaJawab < angkaBenar:
        print("Angka yang kamu jawab lebih kecil dari angka tebakan")
        kesempatan += 1
    elif angkaJawab > angkaBenar:
        print("Angka yang kamu jawab lebih besar dari angka tebakan")
        kesempatan += 1
    elif angkaBenar == angkaJawab:
        print("SELAMAT ANDA PEMENANG ... ")