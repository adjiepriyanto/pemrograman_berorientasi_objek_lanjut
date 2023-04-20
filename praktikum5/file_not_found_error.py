try:
    file = open("file_tidak_ada.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File tidak ditemukan! pastikan file sudah ada di dipenyimpanan yang benar.")
