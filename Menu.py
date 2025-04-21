from main import Queue
def MainMenu():
    q = Queue();
    while True:
        print("|Menu Aplikasi Queue|");
        print("1. Nambah Object");
        print("2. Hapus Object");
        print("3. Cek Empty");
        print("4. Panjang Dari Queue");
        print("5. Keluar Aplikasi Queue");
        print("===================");

        pilihan = str(input("Masukkan Pilihan : "));
        if pilihan == "1":
            enq = str(input("Objek yang ingin ditambahkan : "));
            q.Enqueue(enq);
            print("Objek " + enq + " telah ditambahkan");
        elif pilihan == "2":
            dequeue = q.Dequeue();
            if dequeue is not None:
                print(f"Objek '{dequeue}' dihapus");
            else:
                print("Stack kosong, tidak ada yang bisa dihapus.");
        elif pilihan == "3":
            print(q.IsEmpty());
        elif pilihan == "4":
            print("Panjang dari Queue adalah : " + str(q.Size()));
        elif pilihan == "5":
            print("Terima kasih sudah memakai aplikasi Queue.");
            break
        else:
            print("Pilihan tidak valid");
if __name__ == "__main__":
    MainMenu();