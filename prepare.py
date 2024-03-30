file_path = "../venv/Scripts/activate.bat"

# Open the file in read mode
with open(file_path, "r") as file:
    # Read the contents of the file
    contents = file.read()

list_files = ['run.bat','backup_db.bat']

for i in list_files:
    with open(i,'a')as f:
        f.write(contents+" \n")
        if i =="run.bat":
            f.write("python run.py")
        elif i=="backup_db.bat" :
            f.write("python backup.py") 


################################################

print("Your files has been added..")            
