
from pprint import pprint
from pathlib import Path


def get_cats_info(path):
    

    cat_list = []  

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                
                cat_info = {
                    'id': cat_id,
                    'name': cat_name,
                    'age': int(cat_age)  
                }
                
                cat_list.append(cat_info)

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

    return cat_list

relative_path = Path("cats_info.txt")
absolute_path = relative_path.absolute()

cats_info_file = get_cats_info(absolute_path)

pprint(get_cats_info('cat_info.txt'))


    


            


    