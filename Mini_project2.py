"""write a program to get the student data from user like (Student name , percentage) not creating new user define function
and stored the data student data into dic{} like key and value peres and then write only one single function
to search the student in dic{}.
"""

school={}
info=int(input("Enter student numbers of class :"))
i=1
while i<=info:
    sname=input("Enter student name :")
    per=float(input("Enter student percentage :"))
    school[sname]=per
    i+=1

Findstudent =lambda sc: print(f"Student Precentage Info are :{school[sc]}")

if __name__ == '__main__':
    ue=input("\nEnter student name to find percentage :")
    Findstudent(ue)