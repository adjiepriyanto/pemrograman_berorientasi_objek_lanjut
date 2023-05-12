def create_beratbadan():
    class beratbadan:
        def __init__(self, weight, height):
            self.weight = weight
            self.height = height

        def calculate_beratbadan(self):
            return self.weight / (self.height ** 2)

        def get_category(self):
            bmi = self.calculate_beratbadan()
            if bmi < 0.00185:
                return "Underweight"
            elif 0.00185 <= beratbadan < 0.0025:
                return "Normal Weight"
            elif 0.0025 <= beratbadan < 0.0030:
                return "Overweight"
            else:
                return "Obese"

    def input_data():
        weight = float(input("Masukkan berat badan (kg):100 "))
        height = float(input("Masukkan tinggi badan (m):175  "))
        return weight, height

    def calculate_beratbadan():
        weight, height = input_data()
        beratbadan = beratbadan(weight, height)
        return beratbadan.calculate_beratbadan(), beratbadan.get_category()

    return calculate_beratbadan



beratbadan = create_beratbadan()


result, category = beratbadan()
print("beratbadan Anda adalah:", result)
print("Kategori beratbadan Anda:", category)
16