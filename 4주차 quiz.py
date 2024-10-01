#1
user_input = input("입력: ")

if user_input == "안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요.")

#2
user_input = int(input("값을 입력하세요: "))

result = user_input + 100

if result >= 150:
    print(result)
else:
    print("값이 부족합니다.")

#3
numbers = [100, 200, 300]
result = []

for price in numbers:
    tax_included_price = price * 1.1
    result.append(int(tax_included_price))

print(result)

#4
numbers = [3, 100, 23, 33, 72, 94]
result = []

for num in numbers:
    if num % 3 == 0:
        result.append(num)

print(result)


#5
waiting_number = 1
max_number = 1000

while waiting_number <= max_number:
    print(f"대기번호: {waiting_number}")
    waiting_number += 1

#6
num = 1
sum_of_odds = 0

while num <= 100:
    if num % 2 != 0:
        sum_of_odds += num
    num += 1

print(f"1부터 100까지의 홀수의 합: {sum_of_odds}")
