my_list = ["c", "d", "e"]

try:
    print(my_list[3])
except IndexError:
    print("Index tidak ditemukan!  pastikan index sudah ada di dalam list.")
