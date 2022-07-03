def printuser():
    """This function is return the count of list items and list is typecast into tuple"""
    lis=[]
    val=int(input("Enter total number of fruits you want to add :"))
    for i in range(val):
        fname=input("Enter fruit name:")
        lis.append(fname)

    print(f"list is {tuple(lis)} \n Total list items {len(lis)}")




if __name__ == '__main__':
    printuser()

