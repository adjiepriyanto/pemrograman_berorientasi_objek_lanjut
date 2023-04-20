class Animal:
    def sound(self):
        raise NotImplementedError("Method 'sound' belum diimplementasikan")

class Tiger(Animal):
    def sound(self):
        return "Rarw"

class Buffalo(Animal):
    pass

def make_sound(animal):
    try:
        return animal.sound()
    except NotImplementedError as error:
        print(error)

Tiger = Tiger()
Buffalo = Buffalo()

print(make_sound(Tiger))
print(make_sound(Buffalo))
