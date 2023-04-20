my_dict = {"nama": "cristiano ronaldo", "umur": 37}

try:
    print(my_dict["alamat"])
except KeyError:
    print("Key tidak ditemukan!  pastikan key sudah ada di dalam dictionary.")
