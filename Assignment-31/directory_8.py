# Finding only .py files

import os

def main():    
    path = "."
    
    for root, dirs, files in os.walk(path):
        
        for file in files:
            if file.endswith(".py"):
                print(os.path.join(root, file))             # Will give answer in form /foldername/.py_file_name
    
if __name__ == "__main__":
    main()