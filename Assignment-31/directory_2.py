# os.listdir() -> os.path.isfile() + os.path.isdir()
# combining both to determine if the item is file or directory

import os

def main():
    
    path = "."
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        
        if os.path.isfile(full_path):
            print(f"{item} is a file")
        elif os.path.isdir(full_path):
            print(f"{item} is directory")
    
if __name__ == "__main__":
    main()