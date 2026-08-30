# Printing every files recursively

import os

def main():    
    path = "."
    
    print(f"LIST OF ALL FILES: ")
    for folderName, subFolder, fileName in os.walk(path):
        for file in fileName:
            print(os.path.join(folderName, file))
    
if __name__ == "__main__":
    main()