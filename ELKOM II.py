mahasiswa=[['Joni',75,80,65,],['Edwin',85,85,90,],['Reina',50,60,60,],['Daniel',90,85,95,],['Zachy',50,50,50]]

def baca_data():
    print("[1. Baca data]\n")
    print("NAMA |","PRAK 1 |","PRAK 2 |","PRAK 3")
    for i in mahasiswa:
        print(i[0],"\t",i[1],"\t ",i[2],"\t  ",i[3])
    menu()

def cari_nilai():
    print("[2. Mencari nilai rata-rata praktikum]")
    for i in range(len(mahasiswa)):
        total=mahasiswa[i][1]+mahasiswa[i][2]+mahasiswa[i][3]
        print(mahasiswa[i][0],"\t=","%0.1f"%(total/3))
    menu()

def update_nilai():
    print("[3. Update nilai praktikum]")
    update=input("Masukkan nama mahasiswa : ")
    nilai=int(input("Ingin update nilai praktikum ke- : "))
    nilai_baru=int(input("Nilai baru : "))
    for i in mahasiswa:
        if i [0]==update:
            i[nilai]=nilai_baru
            print("Data berhasil di update")
    menu()

def simpan_nilai():
    print("[4. Simpan perubahan nilai]")
    print("Perubahan berhasil disimpan")
    menu()

def menu():
    print("\nMENU")
    print("1. Baca data")
    print("2. Mencari nilai rata-rata praktikum")
    print("3. Update nilai praktikum")
    print("4. Simpan perubahan nilai")
    print("5. Exit")
    menu=int(input("Pilih menu yang tersedia : "))
    if menu==1:
        baca_data()
    elif menu==2:
        cari_nilai()
    elif menu==3:
        update_nilai()
    elif menu==4:
       simpan_nilai()
    elif menu==5:
        print("Terima kasih!")
        exit()
    else:
        print("Menu tidak tersedia!")
        menu=int(input("Pilih menu yang tersedia : "))
menu()