import os
import datetime

class Buku:
  def __init__(self,judul,penulis,liris):
    self.judul = judul
    self.__penulis = penulis
    self.__liris = liris
    self.__status = "Tersedia"
  
  def pinjam_buku(self):
    if self.__status == "Tersedia":
      self.__status = "Di Pinjam"
      return False
    return True
    
  def pengembalian(self):
    if self.__status == "Di Pinjam":
      self.__status = "Tersedia"
      return True
    return False
    
  def detail_buku(self):
    return f"{40*'-'}\n Judul Buku: {self.judul}\n Penulis: {self.__penulis}\n Tahun Liris: {self.__liris}\n Status: {self.__status}"
    
class Library:
  def __init__(self):
    self.books = []
    
  def tambah_buku(self,buku):
    self.books.append(buku)
    
  def hapus_buku(self,buku):
    self.books.remove(buku)
    
  def info_buku(self):
    if len(self.books) == 0:
      print("Buku Sedang Kosong")
    else:
      for buku in self.books:
        print(buku.detail_buku())

if __name__ == "__main__":
  device_name = os.name
  data_buku = []
  buku_pinjaman = []
  while True:
    match device_name:
      case "posix": os.system("clear")
      case "nt": os.system("cls")
    
    print(f"{'SISTEM PERPUSTAKAAN':>30}")
    print(40*"=")
    print(f"1.Membuat Buku\n2.Meminjam Buku\n3.Mengembalikan Buku\n4.Melihat Informasi Buku")
    operasi = int(input("\nSilahkan Masukkan Operasi Yang Ingin DiLakukan: "))
    if operasi == 1:
      judul = input("\nMasukkan Judul Buku: ")
      penulis = input("Masukkan Nama Penulis: ")
      liris = input("Masukkan Tahun Liris: ")
      obj_buku = Buku(judul,penulis,liris)
      data_buku.append(obj_buku)
      print("\nBuku Telah Di Buat,berikut detail buku\nanda:")
      print(obj_buku.detail_buku())
    elif operasi == 2:
      if len(data_buku) == 0:
        print("Buku Belum Tersedia,Silahkan Buat Dulu")
      else:
        judul = input("Masukkan Buku Yang Ingin Di Pinjam: ")
        for dt in data_buku:
          if dt.judul == judul:
            dt.pinjam_buku()
            buku_pinjaman.append(dt.judul)
            print("Buku Berhasil Di Pinjam")
          else:
            print("Buku Tidak Tersedia,Masukkan Judul Yang Valid")
    elif operasi == 3:
      if len(buku_pinjaman) == 0:
        print("Anda Belum Meminjam Buku Apapun")
      else:
        judul = input("Masukkan Judul Buku Yang Ingin Dikembalikan: ")
        if judul not in buku_pinjaman:
          print("Buku Tersebut Tidak Dipinjam")
        else:
          for dt in data_buku:
            for i in buku_pinjaman:
              if dt.judul == i:
                dt.pengembalian()
                print("Buku Berhasil Dikembalikan")
          
    elif operasi == 4:
      if len(data_buku) == 0:
        print("Buku Tidak Tersedia")
      for dt in data_buku:
        print(dt.detail_buku())
    
    exit = input("\nSelesai(y/n): ")
    if exit.upper() == "Y":
      break
  print("\nProgram Selesai\n")
  for bk in data_buku:
    print(bk.__dict__)
  print(buku_pinjaman)
