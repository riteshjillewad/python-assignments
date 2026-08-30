# os.listdir() -> gives the names of files and directories
# It does not tell if it is a file or directory

import os

def main():
    
    path = "."
    
    items = os.listdir(path)
    for item in items:
        print(item)
    
if __name__ == "__main__":
    main()