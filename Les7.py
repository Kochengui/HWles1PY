import os

def group_rename_files(target_name, num_digits, source_ext, target_ext, name_range=(0, -1)):
    files = [f for f in os.listdir() if f.endswith(source_ext)]
    count = 1
    for file in files:
        name_part = file[name_range[0]:name_range[1]]
        new_name = f"{name_part}_{target_name}_{str(count).zfill(num_digits)}.{target_ext}"
        os.rename(file, new_name)
        count += 1

# Пример использования функции
group_rename_files("newname", 3, ".txt", "csv", (3, 6))
