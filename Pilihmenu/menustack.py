import os
from mainstack import Stack

def MainMenu():
    s = Stack()
    #s = ClassStack.MainStack()
    #t = ClassStack.Tambahan()
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("|Menu Aplikasi Stack|")
        print("1. Push Object")
        print("2. Pop Object")
        print("3. Cek Empty")
        print("4. Tampil Objek Terakhir")
        print("5. Panjang Dari Stack")
        print("6. Keluar Aplikasi")
        print("===================")

        pilihan = input("Masukkan Pilihan : ")
        if pilihan == "1":
            obj = input("Objek yang ingin ditambahkan : ")
            s.Push(obj)
            print(f"Objek '{obj}' telah ditambahkan")
        elif pilihan == "2":
            pop = s.Pop()
            if pop is not None:
                print(f"Objek '{pop}' dihapus")
            else:
                print("Stack kosong, tidak ada yang bisa dihapus.")
        elif pilihan == "3":
            print("Stack kosong?" , s.IsEmpty())
        elif pilihan == "4":
            atas = s.Peek()
            if atas is not None:
                print(f"Objek Terakhir : {atas}")
            else:
                print("Stack kosong")
        elif pilihan == "5":
            print(f"Panjang dari Stack adalah : {s.Size()}")
        elif pilihan == "6":
            print("Terima kasih sudah memakai aplikasi Stack.")
            break
        else:
            print("Pilihan tidak valid, pilih antara 1-6")

        input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    MainMenu()
