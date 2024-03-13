import random
class Domanda:
    def __init__(self, testo, difficolta, rGiusta):
        self.testo = testo
        self.difficolta = difficolta
        self.rGiusta = rGiusta
        self.risposte = []
    def append(self,risposta):
        self.risposte.append(risposta)
    def __str__(self):
        random.shuffle(self.risposte)
        print(f"Livello {self.difficolta}) {self.testo} \n1. {self.risposte[0]} \n2. {self.risposte[1]} \n3. {self.risposte[2]} \n4. {self.risposte[3]}")

file = open("domande.txt", "r")
f = file.readlines() #lista in cui ogni elemento è riga\n
domande = []
conta = 0
for i in range(0,len(f),7):
    f[i] = f[i].strip()
    d1 = Domanda(f[i], int(f[i+1].strip()), f[i+2].strip())
    d1.risposte.append(f[i+2].strip())
    d1.risposte.append(f[i+3].strip())
    d1.risposte.append(f[i + 4].strip())
    d1.risposte.append(f[i + 5].strip())
    #d1.__str__()
    domande.append(d1)
corretto = True
livelloMax = 0
for d in domande:
    if d.difficolta > livelloMax:
        livelloMax = d.difficolta
while (corretto == True):
    if conta > livelloMax:
        break
    domandeTemp = []
    for d in domande:
        if d.difficolta == conta:
            domandeTemp.append(d)

    random.shuffle(domandeTemp)
    domandeTemp[0].__str__()
    nGiusto = 0
    for i in range(0,len(domandeTemp[0].risposte)):
        r = domandeTemp[0].risposte[i]
        if r == domandeTemp[0].rGiusta:
            nGiusto = i + 1
    risposta = int(input("Inserisci la risposta: "))
    if(risposta == nGiusto):
        print("Risposta corretta")
        corretto = True
        conta = conta + 1

    else:
        print("Risposta sbagliata")
        corretto = False
print("Punteggio ottenuto: ", conta)
nick = input("Inserisci il tuo nickname: ")
file = open("punti.txt","r")
s = conta
f = file.readlines()
punteggi = []
campi=[]
for i in range(0,len(f)):
    campi=f[i].strip().split()
    if(len(campi) > 0):
        tupla = (campi[0],int(campi[1].strip()))
        punteggi.append(tupla)
tupla = (nick,conta)
punteggi.append(tupla)
punteggi.sort(key = lambda x : x[1], reverse = True)
file.close()
file2 = open("punti.txt","w")
for tupla in punteggi:
    file2.write(tupla[0]+" "+str(tupla[1])+ "\n")