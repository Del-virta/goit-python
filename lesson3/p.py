import pathlib
import sys


def main():
    if len(sys.argv) < 2:
        user_input = ""
    else:
        user_input = sys.argv[1]
    path = pathlib.Path(user_input)
    if path.exists():
        if path.is_dir():
            for element in path.iterdir():
                print(element.name)
        else:
            print(f'{path} is file')
    else:
        print(f'path {path.absolute()} not exists')


if __name__ == "__main__":
    main()
