message = input('메시지를 입력하세요: ')
def length_of_message(message):
    a = len(message)
    if a <= 20:
        return '요금은 50원입니다.'
    elif a > 20:
        return '요금은 100원입니다.'

print (length_of_message(message))