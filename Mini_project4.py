def Search_myname():
    import time
    try:
        with open("employees.txt") as f:
            time.sleep(4)
            names=f.read()
        while True:
            txt = (yield)

            names.strip('\n')
            if txt in names:
                print("Your name in this file")
            else: print("Your name is not present in this file")


    except Exception as e:
        print(e)


if __name__ == '__main__':
    name = input("Please enter your name :")
    search = Search_myname()
    print("Opening a file...")
    next(search)
    print("Searching your name")
    search.send(name)