

# def chek_triangle(a:float ,b:float ,c:float) -> float:
    
#     if (a + b) > c and (a + c) > b and (b + c) > a :
#                 print('Треугольник существует')
#     else:
#            print('Треугольника с такими сторонами не существует')

#     if a == b == c :
#             print('Правильный треугольник')

#     elif a == b or b == c or c == a:
#             print('Равнобедренный')

#     elif a != b and b != c and c != a:
#             print('Разносторонний')
            

    

# a = float(input())
# b = float(input())
# c = float(input())

# chek_triangle(a ,b ,c)



# def chek_num(n:int) -> int:
        
#         if n > 1 and n <= 100000:
#             count = 0
#             for i in range(1, n + 1):
#                     if n % i == 0:
#                         count += 1
#             print('Простое число 'if count == 2 else 'Составное число')

#         else:
#               print('введите число положительное и меньше 100к')
        
# n = int(input())

# chek_num(n)



from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10


for at in range(attempts): 
     mynum = int(input('Введите число '))
     if mynum > num:
          print('Введите число меньше')
     elif mynum < num:
          print('Введите число больше')
     else:
          print('Вы угадали')








