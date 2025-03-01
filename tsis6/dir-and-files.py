import os
import string
import shutil

#1
def list_items(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return
    
    print("Only Directories:")
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print(directories)

    print("\nOnly Files:")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)
    
    print("\nAll Directories and Files:")
    all_items = os.listdir(path)
    print(all_items)


path = input("Enter the path: ")
list_items(path)


#2
def check_access(path):
    print(f"Path exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

path = input("Enter the path: ")
check_access(path)


#3
def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory part:", os.path.dirname(path))
        print("File part:", os.path.basename(path))
    else:
        print("Path does not exist.")

path = input("Enter the path: ")
check_path(path)


#4
filename = input("Enter filename: ")
if os.path.exists(filename): print("Number of lines:", len(open(filename).readlines()))
else: print("File not found.") 


#5
f = "output.txt"
data = ["calculus1", "calculus2", "calculus3"]
with open(f, 'w') as file:
    for item in data:
        file.write(str(item) + '\n')
        
print(f"List written to {f}")


#6
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as file:
        file.write(f"This is file {letter}.txt")
print("26 text files created.")


#7
shutil.copyfile('output.txt','ex.txt')


#8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} has been deleted.")
        else:
            print("Permission denied: File is not writable.")
    else:
        print("File does not exist.")

path = input("Enter file path to delete: ")
delete_file(path)
