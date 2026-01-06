# --- Bagian 1: Definisi Function Operasi Aritmatika ---
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol"
    return a / b

# --- Bagian 2: Function untuk Menampilkan Menu ---
def tampilkan_menu():
    print("\n===== MENU KALKULATOR =====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

# --- Bagian 3: Program Utama (Main Loop) ---
def main():
    while True:
        tampilkan_menu()
        
        # Meminta input pilihan menu
        pilihan = input("Pilih menu (1-5): ")

        # Cek jika user ingin keluar
        if pilihan == '5':
            print("Terima kasih, program selesai.")
            break

        # Cek jika pilihan valid (1-4)
        if pilihan in ('1', '2', '3', '4'):
            try:
                # Meminta input angka (menggunakan float agar hasil ada .0 nya seperti di gambar)
                bil1 = float(input("Masukkan bilangan pertama: "))
                bil2 = float(input("Masukkan bilangan kedua: "))
                
                # Logika pemilihan operasi
                if pilihan == '1':
                    hasil = tambah(bil1, bil2)
                    print(f"Hasil penjumlahan: {hasil}")
                    
                elif pilihan == '2':
                    hasil = kurang(bil1, bil2)
                    print(f"Hasil pengurangan: {hasil}")
                    
                elif pilihan == '3':
                    hasil = kali(bil1, bil2)
                    print(f"Hasil perkalian: {hasil}")
                    
                elif pilihan == '4':
                    hasil = bagi(bil1, bil2)
                    print(f"Hasil pembagian: {hasil}")
            
            except ValueError:
                print("Error: Harap masukkan angka yang valid!")
        else:
            print("Pilihan tidak valid, silakan pilih 1-5.")

# Menjalankan program
if __name__ == "__main__":
    main()
