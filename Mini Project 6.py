from Student import Student

if __name__ == '__main__':

    sno = int(input("Enter Std no :"))
    sname = input("Enter Student name :")
    sclass = input("Enter Student class :")
    marks = input("Enter Total marks :")

    s = Student()

    s.set_stdno(sno)
    s.set_stdname(sname)
    s.set_sclass(sclass)
    s.set_totalmarks(marks)

    s.Display()