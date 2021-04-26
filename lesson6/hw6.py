import pathlib
import sys
import re
import shutil
import os

# Присваивание имен файлам

def normalize(text):
    symbol_map = {ord('А'): "A",
    ord('Б'): "B",
    ord('В'): "V",
    ord('Г'): "G",
    ord('Д'): "D",
    ord('Е'): "E",
    ord('Ё'): "Yo",
    ord('Ж'): "Zh",
    ord('З'): "Z",
    ord('И'): "I",
    ord('Й'): "Y",
    ord('К'): "K",
    ord('Л'): "L",
    ord('М'): "M",
    ord('Н'): "N",
    ord('О'): "O",
    ord('П'): "P",
    ord('Р'): "R",
    ord('С'): "S",
    ord('Т'): "T",
    ord('У'): "U",
    ord('Ф'): "F",
    ord('Х'): "Kh",
    ord('Ц'): "Ts",
    ord('Ч'): "Ch",
    ord('Ш'): "Sh",
    ord('Щ'): "Shch",
    ord('Э'): "E",
    ord('Ю'): "Yu",
    ord('Я'): "Ya",
    ord('Ы'): "I",
    ord('Ь'): "'",
    ord('Ъ'): "",
    ord('a'): "a",
    ord('б'): "b",
    ord('в'): "v",
    ord('г'): "g",
    ord('д'): "d",
    ord('е'): "e",
    ord('ё'): "yo",
    ord('ж'): "zh",
    ord('з'): "z",
    ord('и'): "i",
    ord('й'): "y",
    ord('к'): "k",
    ord('л'): "l",
    ord('м'): "m",
    ord('н'): "n",
    ord('о'): "o",
    ord('п'): "p",
    ord('р'): "r",
    ord('с'): "s",
    ord('т'): "t",
    ord('у'): "u",
    ord('ф'): "f",
    ord('х'): "kh",
    ord('ц'): "ts",
    ord('ч'): "ch",
    ord('ш'): "sh",
    ord('щ'): "shch",
    ord('э'): "e",
    ord('ю'): "yu",
    ord('я'): "ya",
    ord('ы'): "i",
    ord('ь'): "'",
    ord('ъ'): ""}
    text_with_no_symbols = re.sub("\W", "_", text)
    fixed_text = text_with_no_symbols.translate(symbol_map)
    return fixed_text

# Сортировка файлов

def sort_files(path, destination_folder):
    if not os.path.exists(f'{destination_folder}/images'):
        os.mkdir(f'{destination_folder}/images')
    if not os.path.exists(f'{destination_folder}/video'):
        os.mkdir(f'{destination_folder}/video')
    if not os.path.exists(f'{destination_folder}/documents'):
        os.mkdir(f'{destination_folder}/documents')
    if not os.path.exists(f'{destination_folder}/archives'):
        os.mkdir(f'{destination_folder}/archives')
    if not os.path.exists(f'{destination_folder}/music'):
        os.mkdir(f'{destination_folder}/music')
    if path.is_dir():
        for element in path.iterdir():
            if element.name in ('video', 'documents', 'archives', 'music', 'images'):
                pass
            else:
                if not os.listdir(path):
                    os.remove(element)
                else:
                    sort_files(element,destination_folder)
    else:
        new_file_name = normalize(pathlib.Path(path).resolve().stem)
        if path.suffix in ('.jpg', '.png', '.jpeg', '.svg'): 
            new_path = f'{destination_folder}/images/{new_file_name}{path.suffix}'
            os.rename(path,new_path)
        elif path.suffix in ('.avi', '.mp4', '.mov', '.mkv'):                
            new_path = f'{destination_folder}/video/{new_file_name}{path.suffix}'
            os.rename(path,new_path)
        elif path.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):  
            new_path = f'{destination_folder}/documents/{new_file_name}{path.suffix}'
            os.rename(path,new_path)
        elif path.suffix in ('.mp3', '.ogg', '.wav', '.amr'):   
            new_path = f'{destination_folder}/music/{new_file_name}{path.suffix}'
            os.rename(path,new_path)
        elif path.suffix in ('.zip', '.gz', '.tar'):   
            new_path = f'{destination_folder}/archives/{new_file_name}'
            shutil.unpack_archive(path,new_path)
            os.remove(path)
    
        
            


#Блок вызова функций
def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    destination_folder = sys.argv[2]
    destination_folder = pathlib.Path(path)
    sort_files(path,destination_folder)
if __name__ == '__main__':
    main()