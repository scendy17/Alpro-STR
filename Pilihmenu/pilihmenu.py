from Menu import MainMenu
from menustack import MainMenu

def main():
    while True:
        print("=== PILIH APLIKASI ===")
        print("1. Aplikasi Queue")
        print("2. Aplikasi Stack")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            MainMenu()
        elif pilihan == "2":
            MainMenu()
        elif pilihan == "3":
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
