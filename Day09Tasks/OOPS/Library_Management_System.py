# Library Management System (Constructor & Inheritance)

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author


class EBook(Book):
    def __init__(self,title,author,filesize):
         super().__init__(title,author)
         self.filesize=filesize

    def display(self):
        print("Book Title:",self.title)
        print("Author:",self.author)
        print("File Size:",self.filesize,"MB")

title=input("Enter Book Title:")
author=input("Enter Author Name:")
filesize=int(input("Enter File Size (MB):"))

e=EBook(title,author,filesize)
e.display()
    
