# os.walk() -> recursively traverse a directory

import os

def main():    
    path = "."
    
    for folderName, subFolder, fileName in os.walk(path):
        print(f"Folder name     : {folderName}")
        print(f"Sub-folder names: {subFolder}")
        print(f"File-names      : {fileName}")
    
if __name__ == "__main__":
    main()