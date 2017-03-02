from random import randint, choice

def rand_phone():
    num = '0123456789'
    phone = ''
    rand_num = randint(12, 15)
    for i in range(0, rand_num):
        phone += choice(num)
    return phone
print(rand_phone())