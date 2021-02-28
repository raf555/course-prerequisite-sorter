#from util import concat, removefromgraf, updategraf, matching, mappingsemester, printgraf

# python gabole pake angka di file utk import so yea
util = __import__("13519194-util")
concat = util.concat
removefromgraf = util.removefromgraf
updategraf = util.updategraf
matching = util.matching
mappingsemester = util.mappingsemester
printgraf = util.printgraf

def toso(graf):
  # implementasi pendekatan topological sort
  # dengan decrease and conquer (rekursi)

  # basis
  if(len(graf)==1):
    return graf
  # rekuren
  else:
    # akan dipilih simpul tanpa sisi masuk
    for data in graf:
      if len(data["masuk"])==0:
        simpul = data["simpul"]
        # decreasing
        decrease = updategraf(removefromgraf(graf, simpul), simpul)
        # conquering + recursion
        return concat([data], toso(decrease))

def parse(file):
  '''
  parsing file

  contoh isi file = A,B,C. dengan A adalah simpul dan B,C adalah simpul adjacent yang menuju A.
  A adalah mata kuliah dengan B dan C adalah prerequisite-nya.

  Akan di-parse menjadi tipe data berikut, misal Graf
  {
    simpul: nama simpul (misal A),
    masuk: array of simpul bersebelahan dengan A yang masuk ke simpul A
  }

  Seluruh baris harus diakhiri dengan titik (spek soal) dan enter atau new line.

  Asumsi input adalah Directed Acrylic Graph

  Output berupa Graf.
  '''
  
  copy = file.readlines()

  # menghapus spasi, new line, dan titik
  # return 1 jika tidak ada titik di akhir baris
  for i in range(len(copy)):
    if copy[i][len(copy[i])-2] != ".":
      return 1
    copy[i] = copy[i].replace(" ", "").replace("\n","").replace(".","")

  out = []
  # mengolah baris-baris fail tadi lalu dipindahkan ke struktur data
  for simpul in copy:
    split = simpul.split(",")
    data = {
      "simpul": split[0],
      "masuk": []
    }
    for i, masuk in enumerate(split):
      if i>0:
        data["masuk"].append(masuk)
    out.append(data)

  return out

def intro():
  print("Selamat datang di Penentu Pengambilan Mata Kuliah!\n")
  print("Anda bingung mau ngambil kuliah apa dulu karena kebanyakan prerequisite?\nGampang! Masukin aja daftar kuliahnya beserta prerequisite-nya ke program ini, nanti bakal dikasih urutan pengambilan dalam bentuk tiap-tiap semester!")
  print("========================")
  print("Contoh isi file:\n[nama kuliah] [, prerequisite 1] [, prerequisite 2].")
  print("A.\nB, C, A.\nC, A.")
  print("========================")
  print("Program dikerjakan oleh Rezda A.F 13519194\n")

def start(nointro = False, showsorted = False):
  '''
  Menjalankan program dengan flow sbb.

  1. Meminta nama fail dan direktori jika ada
  2. Mem-parsing fail jika tidak ada error
  3. Memprosesnya jika tidak ada error
  4. Mengurutkan graf dengan pendekatan topological sort
  5. Mapping graf yang sudah diurutkan ke semester yang sesuai
  6. Mengeluarkannya ke layar
  '''

  if not nointro: intro()

  nama_file = input("Masukkan nama fail dengan ekstensinya (dan foldernya jika ada)\n> ")
  if nama_file=="exit": return

  try:
    file = open(nama_file, "r")
  except:
    print ("Error, terjadi kesalahan saat membaca fail.\n")
    start(True)
    return
  
  # parsing fail
  parsed = parse(file)

  # error handling
  if type(parsed) is int and parsed == 1:
    print ("Error, format isi fail salah!\nSetiap baris harus diakhiri titik.\n")
    start(True)
    return

  # membuka kembali fail untuk ditampilkan ke layar
  # dan untuk mencocokkan data graf yang sudah diurutkan
  file = open(nama_file, "r")
  parsed2 = parse(file)

  print("\nMata Kuliah beserta prerequisite-nya: ")
  printgraf(parsed2)

  sortedgraf = matching(parsed2, toso(parsed))

  if showsorted:
    print("\nMata Kuliah setelah diurutkan: ")
    printgraf(sortedgraf)

  # mapping semester
  semester = mappingsemester(sortedgraf)

  # menampilkan hasilnya ke layar
  i = 0
  print("\nUrutan pengambilan dalam semester:")
  for i, listmatkul in enumerate(semester):
    print("Semester", str(i+1), ":", end=" ")
    for i, matkul in enumerate(listmatkul):
      print (matkul, end=", " if i < len(listmatkul)-1 else "\n")