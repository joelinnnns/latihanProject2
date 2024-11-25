import random
import os
class ceritaKu:
    def __init__(self):
        orang = [ "chelsea", "monic", "lia", "mishel", "callista"]
        randomOrang = random.choice(orang)
        tujuanAwal = [ "terminal", "taman", "bandara" ]
        randomtujuanAwal = random.choice(tujuanAwal)
        orangLain = [ "denil", "nelsen", "amelia"]
        randomorangLain = random.choice(orangLain)
        tujuanAkhir = [ "jepang", "korea", "jakarta" ]
        randomtujuanAkhir = random.choice(tujuanAkhir)
        os.system("cls")
        print(f"{randomOrang} pergi ke {randomtujuanAwal} untuk bertemu dengan {randomorangLain} lalu mereka bersama sama pergi ke {randomtujuanAkhir}")
def main():
    run = ceritaKu()
if __name__ == "__main__":
    main()