class MyClass:
    def __init__(self, x):
        self.x = x
    
    def my_method(self):
        print("Halo!")

my_object = MyClass(10)

try:
    my_object.my_attr
except AttributeError:
    print("Attribute tidak ditemukan! pastikan attribute sudah ada di dalam class.")
