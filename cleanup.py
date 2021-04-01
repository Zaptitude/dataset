from pathlib import Path
import os
import shutil

path = Path("Clean")

def move(destination):
    all_files = []
    first_loop_pass = True
    for root, _dirs, files in os.walk(destination):
        if first_loop_pass:
            first_loop_pass = False
            continue
        for filename in files:
            if filename.endswith(".txt") or filename.startswith(".git"):
                continue
            if not filename.startswith(".") and filename.endswith(".php"):
                all_files.append(os.path.join(root, filename))
            else:
                print(f"deleting {filename}")
                os.remove(os.path.join(root, filename))
    for filename in all_files:
        print(f"Moving {filename} to {filename+'.txt'}")
        shutil.move(filename, str(destination)+"/"+filename.split("\\")[-1]+".txt")

move(path)

