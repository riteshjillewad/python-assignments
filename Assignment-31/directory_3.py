# os.scandir() -> it gives us directory entry objects.
# Each entry is treated as a DirEntry object.

import os

def main():

    path = "."
    items = os.scandir(path)

    for item in items:
        if item.is_file():
            print(f"{item.name} is a file")
        elif item.is_dir():
            print(f"{item.name} is directory")

if __name__ == "__main__":
    main()