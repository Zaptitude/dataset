from pathlib import Path
import os
import text_to_image
import shutil
import random

path = Path("Injected")
shellPath = Path("Webshell")
cleanPath = Path("Clean")

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
            # else:
            #     print(f"deleting {filename}")
            #     os.remove(os.path.join(root, filename))
    for filename in all_files:
        print(f"Moving {filename} to {filename+'.txt'}")
        shutil.move(filename, str(destination)+"/"+filename.split("\\")[-1]+".txt")

#move(path)

def image(destination):
    all_files = []
    first_loop_pass = True
    for root, _dirs, files in os.walk(destination):
        if first_loop_pass:
            first_loop_pass = False
            continue
        for filename in files:
            if not filename.startswith(".") and filename.endswith(".txt"):
                all_files.append(os.path.join(root, filename))
            else:
                print(f"skipping {filename}")
    failCount = 0
    for filename in all_files:
        try:
            text_to_image.encode_file(filename, f"{filename}.png", 65536)
        except Exception as e:
            print(e)
            failCount += 1
        
    print(f"Fail Count: {failCount}")

image(".")
image(shellPath)
image(cleanPath)

def createInjected():
    for x in range(2000):
        try:
            randWebShell = random.choice(os.listdir(shellPath))
            randClean = random.choice(os.listdir(cleanPath))
            
            shellInjected = False
            with open(shellPath/randWebShell, "r") as shellFile:
                injectionChance = sum(1 for _ in shellFile) 

            with open(path/f"injected{x}.txt", "w") as injFile:
                with open(cleanPath/randClean, "r") as cleanFile:
                    for line in cleanFile:
                        injFile.write(line)
                        inj = random.randint(1, injectionChance)
                        if inj == injectionChance and shellInjected == False:
                            with open(shellPath/randWebShell, "r") as shellFile:
                                for shellLine in shellFile:
                                    injFile.write(shellLine)
                            shellInjected = True
                    
                    if shellInjected == False:
                        with open(shellPath/randWebShell, "r") as shellFile:
                            for shellLine in shellFile:
                                injFile.write(shellLine)
        except:
            continue



#createInjected()