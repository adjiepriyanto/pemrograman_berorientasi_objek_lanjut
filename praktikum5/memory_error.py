try:
    big_list = [1] * (10**9)
except MemoryError:
    print("Terjadi MemoryError. List terlalu banyak untuk di-pegang!")
