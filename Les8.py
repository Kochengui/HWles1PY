import os
import json
import csv
import pickle

def get_directory_info(directory):
    def get_size(path):
        if os.path.isfile(path):
            return os.path.getsize(path)
        elif os.path.isdir(path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            return total_size

    def process_directory(dir_path):
        directory_info = {
            "name": os.path.basename(dir_path),
            "type": "directory",
            "size": get_size(dir_path)
        }
        return directory_info

    def process_file(file_path):
        file_info = {
            "name": os.path.basename(file_path),
            "type": "file",
            "size": get_size(file_path)
        }
        return file_info

    def save_to_json(data, output_file):
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def save_to_csv(data, output_file):
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def save_to_pickle(data, output_file):
        with open(output_file, 'wb') as pickle_file:
            pickle.dump(data, pickle_file)

    result = []
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            result.append(process_directory(os.path.join(root, d)))
        for f in files:
            result.append(process_file(os.path.join(root, f)))

    save_to_json(result, "directory_info.json")
    save_to_csv(result, "directory_info.csv")
    save_to_pickle(result, "directory_info.pickle")

# Пример использования функции
get_directory_info("/path/to/directory")
