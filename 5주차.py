# Quiz 1
def add(a, b, c, d):
    return a + b + c + d

def multiply(a, b, c, d):
    return a * b * c * d

print(add(1, 2, 3, 4))
print(multiply(1, 2, 3, 4))

# Quiz 2
def odd_or_even(number):
    return "홀수" if number % 2 != 0 else "짝수"

result = odd_or_even(5)
print(f"결과: {result}")

# Quiz 3
def calculate_average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst) if len(lst) > 0 else 0

average_result = calculate_average([10, 20, 30, 40])
print(f"평균: {average_result}")

# Quiz 4
class GameCharacter:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")

character = GameCharacter("Player1", "Male", "Warrior")
character.attack()

# Quiz 5
class RealEstate:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def show_info(self):
        print(f"위치: {self.location}, 평수: {self.size}, 건물 종류: {self.building_type}, "
              f"가격: {self.price}, 건축년도: {self.year_built}")

property_info = RealEstate("Seoul", 85, "Apartment", 500000000, 2015)
property_info.show_info()
