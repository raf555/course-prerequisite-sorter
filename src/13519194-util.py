def printgraf(graf):
  # print graf
  for simpul1 in graf:
    print(simpul1["simpul"] + ": ", end="")
    if len(simpul1["masuk"]) == 0:
      print("-")
    else:
      for i, simpul2 in enumerate(simpul1["masuk"]):
        print (simpul2, end=", " if i < len(simpul1["masuk"])-1 else "\n")

def copyarr(a):
  # copy array
  b = []
  for data in a:
    b.append(data)
  return b

def concat(a,b):
  # konkatenasi array
  c = copyarr(a)
  for data in b:
    c.append(data)
  return c

def removefromgraf(arr, dat):
  # menghapus simpul dat dari graf arr
  out = []
  for data in arr:
    if data["simpul"]!=dat:
      out.append(data)
  return out

def removefrom(arr, dat):
  # menghapus string dat dari array arr
  out = []
  for data in arr:
    if data!=dat:
      out.append(data)
  return out

def updategraf(arr, dat):
  # mengupdate simpul masuk tiap-tiap simpul dengan
  # menghapus simpul dat
  for i in range(len(arr)):
    arr[i]["masuk"] = removefrom(arr[i]["masuk"], dat)
  return arr
  
def matching(inn, out):
  # merestore data pada graf out dari graf inn
  # karena graf yang diurutkan menjadi graf dengan simpul masuk kosong
  for data in inn:
    for i in range (len(out)):
      simpul = out[i]["simpul"]
      if(simpul == data["simpul"]):
        out[i]["masuk"] = data["masuk"]
  return out

def isinmasuk(a, simpul):
  # mengecek apakah simpul merupakan simpul yang masuk ke suatu simpul a
  for simp in a["masuk"]:
    if (simp==simpul):
      return True
  return False

def isprereqtaken(kuliah, semester):
  # mengecek prerequisite untuk suatu simpul (kuliah) pada array semester
  c = 0
  for i, listmatkul in enumerate(semester):
    if i < len(semester)-1:
      for matkul in listmatkul:
        #print(matkul)
        if isinmasuk(kuliah, matkul):
          c += 1
  return len(kuliah["masuk"])==c

def mappingsemester(kuliah):
  # me-map graf kuliah yang sudah diurutkan ke tiap-tiap semester
  # asumsi tidak ada batas bawah dan atas untuk jumlah kuliah
  # asumsi tiap input selalu cukup untuk 8 semester (tidak lebih)

  '''
  cara kerja mapping semester
  1. Jika semester 1, maka seluruh kuliah (simpul) tanpa prerequisite akan dimasukkan, simpul tsb dihapus dari graf.
  2. Jika bukan semester 1, kuliah pertama yang didapat pada graf yang prereqnya sudah diambil akan dimasukkan, kuliah tersebut dihapus dari graf.
  3. Masih lanjutan nomor 2, kemudian akan dicek apakah kuliah lainnya memenuhi syarat untuk dimasukkan ke semester sekarang, yaitu jika tidak bersamaan dengan prereqnya dan prereqnya sudah diambil di semester sebelumnya, proses ini dilanjutkan sampai seluruh kuliah (simpul) pada graf sudah semuanya di-map.
  '''
  
  semester = []
  i = 0
  while len(kuliah)>0:
    semester.append([])
    for data in kuliah:
      if i == 0:
        if len(data["masuk"])==0:
          if isprereqtaken(data, semester):
            semester[i].append(data["simpul"])
            kuliah = removefromgraf(kuliah, data["simpul"])
      else:
        if len(semester[i])==0:
          semester[i].append(data["simpul"])
          kuliah = removefromgraf(kuliah, data["simpul"])
        else:
          for matkul in semester[i]:
            if not isinmasuk(data, matkul) and isprereqtaken(data, semester):
              semester[i].append(data["simpul"])
              kuliah = removefromgraf(kuliah, data["simpul"])
              break
    i += 1
  return semester