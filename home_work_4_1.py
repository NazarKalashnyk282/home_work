from pathlib import Path


def total_salary(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            salaries = [int(line.strip().split(',')[1]) for line in lines]
            total_sum = sum(salaries)
            average_salary = total_sum // len(salaries)
            return total_sum, average_salary
    except FileNotFoundError:
        return None

relative_path = Path("text.txt")
absolute_path = relative_path.absolute()

text_info = total_salary(absolute_path)
# file_path = 'home_work_4/text.txt'
# text_info = total_salary(file_path)
if text_info:
    total_sum, average_salary = text_info
    print(f"Загальна сума зарплат: {total_sum}")
    print(f"Середня заробітна плата: {average_salary}")
else:
    print("Файл не знайдено.")
