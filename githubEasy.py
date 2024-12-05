# you should name the folder you run this from exactly like your github repository
# your github repository adress should be https://github.com/<USERNAME>/<FOLDERNAME>

import os
import time

username = input("Enter github username \n") # you can modify this to use your github username automatically

# Get the current working directory
current_directory = os.getcwd()

# Extract the current folder name
# You can either use the folder_name as repository name or ask the user for input for the repository name
folder_name = os.path.basename(current_directory)
#folder_name = input("Enter your repository name \n")


# this will automatically add githubEasy.py to your .gitignore
with open(".gitignore", "r") as file:
    if "githubEasy.py" in file.read():
        print("hi")
        pass
    else:
        with open(".gitignore", "a") as fileWrite:
            fileWrite.write("\ngithubEasy.py\n")


# Github
init_command = "git init"
print(init_command)
os.system(init_command)

add_command = "git add ."
print(add_command)
os.system(add_command)

message_command = 'git commit -m "first commit - made with githubEasy"'
print(message_command)
os.system(message_command)

main_command = "git branch -M main"
print(main_command)
os.system(main_command)

origin_command = f"git remote add origin https://github.com/{username}/{folder_name}.git"
print(origin_command)
os.system(origin_command)

upload_command = "git push -u origin main"
print(upload_command)
os.system(upload_command)


print("This window will automatically close in 5 secs")
time.sleep(5)