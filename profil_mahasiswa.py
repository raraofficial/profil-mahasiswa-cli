def profil_mahasiswa(nama, nim, prodi, hobi):
  """Profil mahasiswa."""
  print(f"Mahasiswa Prodi {prodi} UNJANI Yogyakarta")
  print(f"Dengan nama {nama}")
  print(f"Mempunyai NIM {nim}")
  print(f"Memiliki Hobi {hobi}")

nama = input("Nama: ")
nim = input("NIM: ")
prodi = input("Prodi: ")
hobi = input("Hobi: ")

profil_mahasiswa(nama=nama, nim=nim, prodi=prodi, hobi=hobi)