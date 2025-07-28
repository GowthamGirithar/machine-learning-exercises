import os
from pathlib import Path



print(os.getcwd())

home = Path.home()
print(home)

new_folder = os.path.join(os.getcwd(), "test")
print(new_folder)

try:
    new_folder.mkdir(exist_ok=True)
    print(f"Folder created (or exists): {new_folder}")
except Exception as e:
    print("Failed to create folder:", e)


a= 5
print(f"Folder created (or exists): {a}")
print(f"the value a {a} is good {a}")

