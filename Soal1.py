inputjmlkalimat=int(input("inputkan jumlah kata = "))
listkata=[]
while inputjmlkalimat > 0:
    inputkalimat = input("inputkan kalimat = ")
    listkata.append(inputkalimat)
    inputjmlkalimat -=1

for kalimat in listkata:
    print("Hasil: ")
    for i in range(0, len(kalimat)):
        if i == 0:
            continue
        huruf1 = kalimat[i-1]
        huruf2 = kalimat[i]
        
        selisihurufkalimat = ord(huruf1)-ord(huruf2)
        if selisihurufkalimat < 0:
            selisihurufkalimat = -(selisihurufkalimat)
        if ord(huruf1) < ord(huruf2):
            print(f"{huruf1} kurang dari {huruf2} selisihnya ialah {selisihurufkalimat}")
        else:
            print(f"{huruf1} lebih dari {huruf2} selisihnya ialah {selisihurufkalimat}")