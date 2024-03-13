import zipfile
import os

def compress():
    with zipfile.ZipFile("C:\\Users\\phamh\\pp2024\\pw5\\student.dat", "w") as zipf:
        zipf.write("C:\\Users\\phamh\\pp2024\\pw5\\students.txt", "student.txt")
        zipf.write("C:\\Users\\phamh\\pp2024\\pw5\\courses.txt","courses.txt")
        zipf.write("C:\\Users\\phamh\\pp2024\\pw5\\marks.txt","mark.txt")
    
def decompress():
    with zipfile.ZipFile ("student.dat","r") as zipf:
        zipf.extractall()
        
def check():
    return "student.dat" in os.listdir()
