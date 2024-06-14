import os
import datetime

if __name__ == "__main__":
  sistem_operasi = os.name
  data_buku = []
  while True:
    match sistem_operasi:
      case "posix" :
        os.system("clear")
      case "nt" :
        os.system("cls")
    nama = input("Nama Penulis: ")
    judul = input("Judul Buku  : ")
    while True:
      try:
        tahun = int(input("Tahun Terbit  : "))
        bulan = int(input("Bulan Terbit  : "))
        tanggal = int(input("Tanggal Terbit : "))
        terbit = datetime.datetime(tahun,bulan,tanggal)
        if type(tahun) == int and type(bulan) == int and type(tanggal) == int:
          break
      except Exception as e:
        if "must be in 1..12" in str(e):
          print("Bulan Harus Di Antara 1-12,Terima Kasih")
        elif "day is out of range" in str(e):
          print("Tanggal Harus Di Antara 1-31,Terima Kasih")
        else:
          print("Format Terbit Harus Angka,Terima Kasih")
    buku = [nama,judul,terbit.strftime('%y/%m/%d')]
    data_buku.append(buku)
    print(f"\nBerikut Data Buku Yang Di Input: ")
    print(41*"=")
    print(f"{'No.':^2} | {'Penulis':^8} | {'Judul Buku':^12} | {'Tahun':^6}")
    print(41*"-")
    for i,j in enumerate(data_buku):
      print(f"{i+1:^3} | {data_buku[i][0]:^8} | {data_buku[i][1]:^12} | {data_buku[i][2]:^6}")
    print(41*"=")
    done = input("\nApakah Input Data Telah Selesai?(y/n): ")
    if done == "Y" or done == "y":
      break
  print("\nAkhir Dari Program,Terima Kasih :)\n")


