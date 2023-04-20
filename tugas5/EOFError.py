try:
    name = input("masukan nama: ")
    if not name:
        raise EOFError("tidak ada input yang diterima masuk")
    print("Hello, " + name)
except EOFError as error:
    print(error)
