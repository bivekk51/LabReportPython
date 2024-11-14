class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
book1=Book("Prog","Ank",2060)
print(f"{book1.title} is the title of book")
print(f"{book1.author} is the author of book")
print(f"{book1.year} is the year of publication of book")