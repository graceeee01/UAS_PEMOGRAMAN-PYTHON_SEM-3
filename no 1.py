class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            print(f"Tugas '{task}' berhasil ditambahkan.")
        else:
            print("Tugas tidak boleh kosong!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Tugas '{task}' berhasil dihapus.")
        else:
            print(f"Tugas '{task}' tidak ditemukan di daftar.")

    def display_tasks(self):
        if self.tasks:
            print("\nDaftar Tugas:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("\nDaftar tugas kosong!")

    def search_task(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.lower()]
        if results:
            print("\nHasil pencarian:")
            for task in results:
                print(f"- {task}")
        else:
            print(f"Tidak ada tugas yang mengandung kata kunci '{keyword}'.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n=== Menu Manajemen To-Do List ===")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tampilkan Semua Tugas")
        print("4. Cari Tugas")
        print("5. Keluar")
        choice = input("Pilih menu (1-5): ")

        if choice == "1":
            task = input("Masukkan nama tugas: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Masukkan nama tugas yang akan dihapus: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            keyword = input("Masukkan kata kunci untuk mencari tugas: ")
            todo_list.search_task(keyword)
        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi To-Do List!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
