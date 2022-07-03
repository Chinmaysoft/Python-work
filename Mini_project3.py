class Library:
    mydic ={}

    def __init__(self,books,lname):
        self.books=books
        self.lname=lname

    def display_book(self):
        mylist=self.books
        return  mylist

    def land_book(self):
        user = input("Enter your name")
        lend=input("Enter book name")
        for i in self.books:
            if lend==i:
                self.mydic[lend]=user
                self.books.remove(i)
        print(self.mydic)

    def add_book(self,ab):
        self.books.append(ab)
        print(self.books)

if __name__ == '__main__':
    cjlibrary=Library(['c','c++','java','python','node','sql'],'cj')

    print(cjlibrary.display_book())