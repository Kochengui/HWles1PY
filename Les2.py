def to_hex(num):
    hex_digits = "0123456789ABCDEF"
    hex_str = ""
    
    while num > 0:
        remainder = num % 16
        hex_str = hex_digits[remainder] + hex_str
        num = num // 16
    
    return hex_str

num = int(input("Введите целое число: "))
hex_str = to_hex(num)

print(f"Шестнадцатеричное представление числа {num}: {hex_str}")


if hex_str == hex(num)[2:]:
    print("Результат верный")
else:
    print("Результат неверный")



from fractions import Fraction

def calculate_fraction_operations(fraction1, fraction2):
  
    num1, denom1 = map(int, fraction1.split("/"))
    num2, denom2 = map(int, fraction2.split("/"))
    
 
    frac1 = Fraction(num1, denom1)
    frac2 = Fraction(num2, denom2)
   

    sum_fraction = frac1 + frac2

    product_fraction = frac1 * frac2
    
    return sum_fraction, product_fraction

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

sum_result, product_result = calculate_fraction_operations(fraction1, fraction2)

print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")

