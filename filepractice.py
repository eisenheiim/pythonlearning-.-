import os
import sys

x=os.getcwd()
print(x)
print(os.listdir())
print(os.listdir("subdirectory"))
print(os.path.exists("subdirectory/ewtext.txt"))

for root, dirs, files in os.walk(x): #yani pythonworks ten başlayıp en içteki klasöre kadar gidiyor. her seferinde bir tuple döndürür
    #root o an dolaştığın klasörün alt yolu.
    #dirs o roottaki klsörler
    #o klasördeki files dosyalar.
    print(f"root rn: {root}")
    print(f"subdirectories: {dirs}")
    print(f"files: {files}")
    print("--------")


#FINDING SAME CONTENT

content={}
for root, dirs, files in os.walk(x):
    for x in files:
        if x.endswith(".txt"):
            loc=os.path.join(root, x)
            with open(loc,"r") as file:
                y=file.read()
            if y in content:
                content[y].append(x)
            else:
                content[y]=[x]

for key,value in content.items():
    if len(value)>1:
        print(value)


#2. Find the files that contain the same set of characters. Print out the file names and the corresponding set of characters. While printing out, use alphabetical ordering in the file names, and ASCII table ordering in the character list.

sames=[]
chars={}
for root,dirs, files in os.walk("."):
    for file in files:
        if file.endswith("txt"):
            loc=os.path.join(root,file)
            
            with open(loc,"r") as y:
                context=y.read()
            new=[]
            
            for ch in context:
                if ch not in new:
                    new.append(ch)
            x="".join(sorted(new))
            print(x)
            if x in chars:
                chars[x].append(file)
            else:
                chars[x]=[file]
for key,value in chars.items():
    if len(value)>1:
        print(key)
        print(value)


            
#Print-out all file and directory names in the current directory and in the most immediate sub-directories.
allfiles=[]

print(os.getcwd())
print(os.listdir())

#appending the ones in the curr dir.
for fd in os.listdir():
    allfiles.append(fd)
for root,dirs,files in os.walk("."):
    for dir in dirs:
        path=os.path.join(root,dir)
        allfiles.extend(os.listdir(path))
print(allfiles)

