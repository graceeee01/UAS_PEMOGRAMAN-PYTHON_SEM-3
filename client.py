import requests

BASE_URL = "http://127.0.0.1:5000/books"

def display_books():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        books = response.json().get("books", [])
        print("\n=== Daftar Buku ===")
        for book in books:
            print(f"ID: {book['id']}, Judul: {book['title']}, Penulis: {book['author']}")
    else:
        print("Gagal mengambil data buku.")

def add_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan penulis buku: ")
    data = {"title": title, "author": author}
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("Buku berhasil ditambahkan!")
    else:
        print("Gagal menambahkan buku.")

def update_book():
    book_id = int(input("Masukkan ID buku yang ingin diperbarui: "))
    title = input("Masukkan judul baru: ")
    author = input("Masukkan penulis baru: ")
    data = {"title": title, "author": author}
    response = requests.put(f"{BASE_URL}/{book_id}", json=data)
    if response.status_code == 200:
        print("Buku berhasil diperbarui!")
    else:
        print("Gagal memperbarui buku. Buku mungkin tidak ditemukan.")

def delete_book():
    book_id = int(input("Masukkan ID buku yang ingin dihapus: "))
    response = requests.delete(f"{BASE_URL}/{book_id}")
    if response.status_code == 200:
        print("Buku berhasil dihapus!")
    else:
        print("Gagal menghapus buku. Buku mungkin tidak ditemukan.")

def main():
    while True:
        print("\n=== Menu Manajemen Buku ===")
        print("1. Tampilkan Daftar Buku")
        print("2. Tambah Buku Baru")
        print("3. Perbarui Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        choice = input("Pilih menu (1-5): ")

        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
