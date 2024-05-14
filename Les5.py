# import os

# def split_path(file_path):
#     path, file_name = os.path.split(file_path)
#     file_name, file_extension = os.path.splitext(file_name)
#     return path, file_name, file_extension

# # Пример использования функции
# file_path = "/home/user/documents/example.txt"
# path, file_name, file_extension = split_path(file_path)
# print("Путь:", path)
# print("Имя файла:", file_name)
# print("Расширение файла:", file_extension)


names = ["Alice", "Bob", "Charlie"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "5.50%", "8.75%"]

result_dict = {name: rate + rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result_dict)
