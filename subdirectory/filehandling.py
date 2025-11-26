f=open("filestudyn.txt") #sadece open yaparsan mode belirtmeden, sadece okuyabilirisin

#if file is in different loc you have to specify the path.
with open("filestudyn.txt","w") as x: #deletes all content and writes again
    #with blogundan cıkınca dosya kapanır, yeniden açman gerekir. 
    x.write("new content\nhelllooo")

for line in f:
    print(line.strip())#this is important to read lines without \n. without strip, reader assumes \n at the end of each line and it also removes the blanks.
#otherwise it will print with new lines each time when moving to a new line.
f.seek(0)
y=f.readlines() 
print(y)

f.seek(0)
print(f.readline().strip())

f.close()
#with "with" statement, you dont need to close a file
with open("files2.txt","w+") as new: #with open append ve write ile dosya yoksa oluşturabilirsin. varsa da üstüne yazar.
    new.write("yenikayit")
    writethese=["merhaba","nasilsin"]
    new.writelines(writethese)#write dan farkı kendisi satır eklemez.

    
    writethese=["\nmerhaba\n","nasilsin"]
    new.writelines(writethese)#write dan farkı kendisi satır eklemez.
    
    listy=["new","words"]
    new.writelines("\n"+s for s in listy)
    new.seek(0)
    lines=new.readlines()#satır sonu n ile birlikte gelir.

    new.seek(0)
    print(new.read())

print(lines)

print()
print("new file openin")
print()

with open("files2.txt","r+") as x: #being different than w+, it doesnt delete all the content and allows you to write as your read. but w+ deletes everything and write from the beginning.

    
    print(f"before i change: {x.readline()}")
    x.seek(0)
    x.write("changed")
    x.seek(0)
    print(f"after i change: {x.readline()}")

# Absolute path
with open(r"C:\Users\sdnza\OneDrive\Masaüstü\pythonworks\files2.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Relative path (script ile aynı klasörde)
with open("files2.txt", "r", encoding="utf-8") as f:
    print(f.read())



#with open("resim.png","rb") as img: #Bir image’ı Python’da read veya benzeri bir fonksiyonla okuduğunda resmin 
    #piksel verilerini ham olarak okumuş olursun, yani görselin kendisini değil, dosyanın binary (ikili) içeriğini alırsın.

    #print(img.read())
data = b"Hello_x0000_"
print(type(data))  # <class 'bytes'>
with open("newbin.bin","wb") as bin:
    bin.write(data)

size = 10

with open('newbin.bin', 'rb') as f:
    while True:
        chunk = f.read(size)
        if not chunk:
            break
        
        print(chunk)

#copying a file into a file
with open("subdirectory\ewtext.txt","r") as source:
    with open("newbin.bin","a+") as target : #append direkt satırın sonuna gider ve oradan yazmaya başlar. write baştn başlar.
        target.write(source.read())
        target.seek(0)
        print(target.read())
        


import pickle #Python’da pickle modülü, Python nesnelerini bir dosyaya veya byte dizisine dönüştürüp saklamaya ve daha sonra geri yüklemeye yarar.
#Yani nesneleri serialize (serileştirmek) ve deserialize (tersine çevirmek) etmek için kullanılır.

#importing text to another bin file
with open("subdirectory\ewtext.txt","r") as source:
    data=source.read()

with open("target.bin","wb") as target:#binary calısacagımız icin binary yazdik. wb yazdıgında illa ki içine binarysel bir şeyler atmalısın.
    #normal string yazarsan hata verir
    pickle.dump(data,target)
    pickle.dump("hi",target)
    target.write(b"hello")
    
print()
with open("target.bin", "rb") as f:
    print(pickle.load(f)) #it starts searching for something of pickle type. if it finds, it returns it
    print(pickle.load(f))#if there are more than one, it returns each of them.btw pointer moves too.
    print(f.tell())
    f.seek(0)
    print(f.read())

#OS BASICS
import os
print(os.getcwd())
print(os.listdir())
print(os.listdir("subdirectory"))
print(os.path.exists("subdirectory/subsubdirectory"))
#os.mkdir("mydir") #creating a folder
#os.rmdir("mydir") #deletes folders but onyl empty ones. error if there is something inside.
print(os.listdir("mydir"))

x=os.path.join("subdirectory","things")
print(x)

for root, dirs, files in os.walk("..\pythonworks\subdirectory"):
    print(root, dirs, files)

try:
    int("helo")
except ValueError:
    print("couldnt converted")

x=["mylist",2,31]

try:
    x[0]/0
except ZeroDivisionError:
    print("zero division btch")
except IndexError:
    print("no index like this")
except:
    print("something catched it")
finally: #this always runs even the exception is handled, not handled or no exceptin happened. this i different than normal print.
    #if there was a normal print, it wouldnt work if there is an exception which is not handled and it d stop executing. but in this case,
    #even not handledit executes.
    print("dıdıdı")

#catching any kind of error:
try:
    pass
except Exception as e:
    print(f"your exception is {e}")

try:
    3/0
except ZeroDivisionError as message:
    print("the problem is: ", message)


try:
    print("Try: Hata olabilecek kod")
except ZeroDivisionError:
    print("Except: Hata olursa")
else: #eğer ki exceptin tutamadıgı bir hata olursa else calısmaz.
    print("Else: Hiç hata olmadı")
finally:
    print("Finally: Her zaman çalışır")

#raise NameError("böyle bir değişken yok")


def namecontroller(name):
    if name != "ibrahim":
        raise Exception("only ibos allowed")
#namecontroller("ibos")

#re-raising the exception again
"""try:
    1 / 0
except ZeroDivisionError:
    print("Hata yakalandı ama tekrar fırlatıyorum")
    raise  # orijinal ZeroDivisionError tekrar fırlatılır"""

import sys #python yorumlayıcısı ile ilgili sistem özelliklerine erişim sağlar

print(sys.argv) #komut satırından scripte verilen liste