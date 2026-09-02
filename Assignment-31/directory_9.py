# Count total number of files
import os

def main():    
    path = "."
    fileCount = 0
    
    for root, dirs, files in os.walk(path):
        for file in files:
            fileCount += 1
            
    print(f"Total number of files: {fileCount}")
    
if __name__ == "__main__":
    main()