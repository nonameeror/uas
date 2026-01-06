nama_file = "datasiswa.txt"


try:
    with open(nama_file, "r") as f:
        data = f.readlines()
except FileNotFoundError:
    data = []

while True:
    print("\n===== MENU MAHASISWA =====")
    print("1. Tambah")
    print("2. Tampil")
    print("3. Cari Mahasiswa (NIM)")
    print("4.hapus Mahasiswa")
    print("5.keluar")
    pilih = input("Pilih menu: ")


    if pilih == "1":
        nim = input("NIM   : ")
        nama = input("Nama  : ")
        prodi = input("Prodi : ")
        

        baris_baru = f"{nim},{nama},{prodi}\n"
        data.append(baris_baru)
        
        # Simpan ke file
        with open(nama_file, "w") as f:
            f.writelines(data)
        print("Data berhasil disimpan!")


    elif pilih == "2":
        print("\n--- Daftar Mahasiswa ---")
        for baris in data:
            print(baris.strip().replace(",", " | "))


    elif pilih == "3":
        cari_nim = input("Cari NIM: ")
        ketemu = False
        for baris in data:
            if baris.startswith(cari_nim + ","):
                print("Ditemukan:", baris.strip().replace(",", " | "))
                ketemu = True
                break
        if not ketemu:
            print("Data tidak ditemukan.")

    elif pilih == "4":
        hapus_nim = input("Hapus NIM: ")
        data_baru = [baris for baris in data if not baris.startswith(hapus_nim + ",")]
        
        if len(data_baru) < len(data):
            data = data_baru
            with open(nama_file, "w") as f:
                f.writelines(data)
            print("Data berhasil dihapus.")
        else:
            print("NIM tidak ditemukan.")


    elif pilih == "5":
        print("Selesai.")
        break
        
    else:
        print("Pilihan salah.")
