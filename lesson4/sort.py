import pathlib
import sys

def sort_files(path):
    images_types = ('.jpeg','.jpg','.png','.svg')
    video_types = ('.avi','.mp4','.mov','.mkv')
    docs_types = ('.doc','.docx','.txt','.pdf','.xlsx','.pptx')
    music_types = ('.mp3','.ogg','.waw','.amr')
    archives_types = ('.tar','.gz','.zip')
    unknown_types, images_types_indir, video_types_indir, docs_types_indir, music_types_indir, archives_types_indir = [],[],[],[],[],[] 
    images, video, music, docs, archives, unknown = [],[],[],[],[],[]
    if path.exists():
        if path.is_dir():
            for element in path.iterdir():
                if element.name.endswith(images_types):
                    images.append(element.name)
                    images.append('\n')
                    images_types_indir.append(element.suffix)
                elif element.name.endswith(video_types):
                    video.append(element.name)
                    video.append('\n')
                    video_types_indir.append(element.suffix)
                elif element.name.endswith(docs_types):
                    docs.append(element.name)
                    docs.append('\n')
                    docs_types_indir.append(element.suffix)
                elif element.name.endswith(music_types):
                    music.append(element.name)
                    music.append('\n')
                    music_types_indir.append(element.suffix)
                elif element.name.endswith(archives_types):
                    archives.append(element.name)
                    archives.append('\n')
                    archives_types_indir.append(element.suffix)
                else:
                    unknown.append(element.name)
                    unknown.append('\n') 
                    unknown_types.append(element.suffix)                     
                sort_files(element)
            if len(images)>0:
                print(f"Картинки c расширениями {set(images_types_indir)}:\n{''.join(images)}") 
            if len(video)>0:
                print(f"Видео c расширениями {set(video_types_indir)}:\n{''.join(video)}")
            if len(docs)>0:
                print(f"Документы c расширениями {set(docs_types_indir)}:\n{''.join(docs)}")
            if len(music)>0:
                print(f"Музыка c расширениями {set(music_types_indir)}:\n{''.join(music)}")
            if len(archives)>0:
                print(f"Архивы c расширениями {set(archives_types_indir)}:\n{''.join(archives)}")
            if len(unknown)>0:
                print(f"Неопределенные файлы расширениями {set(unknown_types)}:\n{''.join(unknown)}")
    else:
        print(f'Папки {path.absolute()} не существует!')

def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    sort_files(path)
    
if __name__ == "__main__":
    main()