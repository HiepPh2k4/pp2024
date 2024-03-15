import zipfile
import os

def compress():
    with zipfile.ZipFile("C:\\Users\\phamh\\pp2024\\pw6\\student.dat", "w") as zipf:
        zipf.write("C:\\Users\\phamh\\pp2024\\pw6\\students.pkl", "student.pkl")
        zipf.write("C:\\Users\\phamh\\pp2024\\pw6\\courses.pkl","courses.pkl")
        zipf.write("C:\\Users\\phamh\\pp2024\\pw6\\marks.pkl","mark.pkl")
    
def decompress():
    with zipfile.ZipFile ("C:\\Users\\phamh\\pp2024\\pw6\\student.dat","r") as zipf:
        zipf.extractall()
        
def check():
    return "student.dat" in os.listdir()
