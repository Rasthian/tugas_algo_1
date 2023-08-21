inputkalimat = input("inputkan kalimat = ")
kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']

jmlhuruf = len(inputkalimat)

for i in range ( jmlhuruf):
    huruf1 = inputkalimat[i-1]
    huruf2 = inputkalimat[i]
    
    cekhuruf1 = huruf1 in kiri
    cekhuruf2 = inputkalimat[i] in kiri
    
    cekhuruf = cekhuruf2 ^ cekhuruf1
        
    if not cekhuruf:
        print(cekhuruf)
        if cekhuruf2:
            print(f"penjelasan : karakter yang berdempetan yakni {huruf1} dan {huruf2} berada di satu tangan (kiri)")
            break
        else:
            print(f"penjelasan : karakter yang berdempetan yakni {huruf1} dan {huruf2} berada di satu tangan (kanan)")
            break
else:   
    if cekhuruf:
        cekhuruf = True
        print(cekhuruf)
        print("Penjelasan: Setiap karakater selalu bergantian tangan.")