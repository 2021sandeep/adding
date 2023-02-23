 '''import os

folder_path = "C:\\Users\\sandeep\\OneDrive\\Documents"

for filename in os.listdir(folder_path):
    if filename == "qualcoom.txt":
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as file:
            content = file.read()
            print(content)'''

import os
import re

folder_path = "C:\\Users\\sandeep\\OneDrive\\Documents"

for filename in os.listdir(folder_path):
    if re.match(r"qualcoom.*\.txt", filename):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as file:
            content = file.read()
            print(content)

