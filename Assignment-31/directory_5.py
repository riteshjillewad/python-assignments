# os.walk() -> recursively traverse a directory
# only subfolders

import os

def main():    
    path = "."
    
    print(f"LIST OF SUBFOLDERS")
    for folderName, subFolder, fileName in os.walk(path):
        print(f"Sub-folder names: {subFolder}")
    
if __name__ == "__main__":
    main()