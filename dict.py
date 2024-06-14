import string
import random

def get_student_data():
    while True:
        try:
            name = input("Masukkan Nama Anda: ")
            nim = int(input("Masukkan Nim Anda: "))
            ipk = float(input("Masukkan IPK Anda: "))
            return {"nama": name, "nim": nim, "ipk": ipk}
        except ValueError:
            print("Input must be a number (integer or float) for NIM and IPK.")

def clear_screen():
    import os
    os.system("clear" if os.name == "posix" else "cls")  # Concise cross-platform clear

def display_students(students):
    print("=" * 40)
    print(f"{'KEY':^6} | {'Nama':^14} | {'Nim':^6} | {'IPK':^4}")
    print(40 * "-")
    for key, data in students.items():
        print(f"{key:^6} | {data['nama']:^14} | {data['nim']:^6} | {data['ipk']:^4.2f}")  # Format IPK to 2 decimal places
    print(40 * "=")

if __name__ == "__main__":
    students = {}
    clear_screen()

    while True:
        data = get_student_data()
        key = "".join(random.choice(string.ascii_uppercase) for _ in range(6))
        students[key] = data

        print()
        display_students(students)

        stop = input("\nApakah Input Data Telah Selesai(y/n): ")
        if stop.upper() == "Y":
            break
        else:
          clear_screen()
    print("\nProgram Selesai\n")
