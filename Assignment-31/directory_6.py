# os.walk() -> recursively traverse a directory
# only files

import os

def main():    
    path = "."
    
    print(f"LIST OF FILES: ")
    for folderName, subFolder, fileName in os.walk(path):
        print(f"Files   : {fileName}")
    
if __name__ == "__main__":
    main()