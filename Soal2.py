inputsapi = int(input("masukkan jumlah sapi = "))
print("="*80)
print("1. Sapi Warrior : 690 hari \n2. Sapi Mage : 420 hari \n3. Sapi Assasin : 530 hari \n4. Sapi Nolep : 330 hari")
print("="*80)
jenis=[] 
for perulangan1 in range(inputsapi):
    inputjenis = int(input("pilih jenis sapi = "))
    if inputjenis == 1:
         jenis.append(690)
    elif inputjenis == 2:
         jenis.append(420)
    elif inputjenis == 3:
        jenis.append(530)
    elif inputjenis ==4:
        jenis.append(330)
    else :
        continue
    
jenis = sum(jenis)
tahun = jenis % 365
jmltahun = int(jenis/365)
bulan = int(tahun % 30)
jmlbulan = int(tahun/30)
hari = bulan
    
    
print(f"jumlah hari yang diperlukan ialah : {jmltahun} tahun, {jmlbulan} bulan, dan {hari}")
