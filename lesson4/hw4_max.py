import pathlib
import sys

pic=[]
vid=[]
doc=[]
musc=[]
arch=[]
unknown=[]
file_type=set()
unknown_type=set()

def sort_files(path):
    result = ''
    global pic
    global vid
    global doc
    global musc
    global arch
    global unknown
    global file_type
    global unknown_type
    if path.is_dir():
        for element in path.iterdir():
            sort_files(element)
    else:
        if path.suffix in ('.jpg', '.png', '.jpeg', '.svg'):
            pic.append(path.name)
            file_type.add(path.suffix)
        elif path.suffix in ('.avi', '.mp4', '.mov', '.mkv'):
            vid.append(path.name)
            file_type.add(path.suffix)
        elif path.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
            doc.append(path.name)
            file_type.add(path.suffix)
        elif path.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
            musc.append(path.name)
            file_type.add(path.suffix)
        elif path.suffix in ('.zip', '.gz', '.tar'):
            arch.append(path.name)
            file_type.add(path.suffix)
        else:
            unknown.append(path.name)
            unknown_type.add(path.suffix)
    result = f"В папке лежат файлы с известными расширениями: {file_type} \nи неизвестными расширениями: {unknown_type} \nИз них картинки:\n{pic}\nвидео:\n{vid}\nдокументы:\n{doc}\nархивы:\n{arch}\nмузыка:\n{musc}\nнепонятные файлы:\n{unknown}"
    return result


def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    print(sort_files(path))


if __name__ == '__main__':
    main()