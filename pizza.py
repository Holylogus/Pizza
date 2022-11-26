rendelesek = []
meretek = []
feltetek = []
arak = []


def adatbekeres():
    print("Választható pizzák: sajtos, sonkás, gombás,")
    print("Választható méretek: kicsi, közepes, nagy")
    potlas = ""
    while potlas != "N":
        rendeles = input("Adja meg milyen pizzát kér:")
        rendelesek.append(rendeles)
        meret = input("Adja meg a pizza méretét:")
        meretek.append(meret)
        feltet = input("Kére felétet? ,I, ha igen ,N, ha nem")
        feltetek.append(feltet)
        potlas = input("Szeretne még rendelni? ,I, ha igen ,N, ha nem:")


def szamolas():
    cv = 0
    alapar()
    meret()
    feltet()
    print(arak)


def alapar():
    cv = 0
    while cv < len(rendelesek):
        if rendelesek[cv] == "sajtos":
            arak.append(1000)
        elif rendelesek[cv] == "sonkás":
            arak.append(1100)
        elif rendelesek[cv] == "gombás":
            arak.append(1200)
        cv += 1


def meret():
    cv = 0
    while cv < len(rendelesek):
        if meretek[cv] == "kicsi":
            arak[cv] *= 0.9
        elif meretek[cv] == "közepes":
            arak[cv] *= 1
        elif meretek[cv] == "nagy":
            arak[cv] *= 1.1
        cv += 1


def feltet():
    cv = 0
    while cv < len(rendelesek):
        if feltetek[cv] == "I":
            arak[cv] += 50
        cv += 1


def kiiras():
    osszeg = 0
    cv = 0
    while cv < (len(arak)):
        osszeg += arak[cv]
        cv += 1
    print(f"Az ön rendelésének értéke: {osszeg},-Ft")
