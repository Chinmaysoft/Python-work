class Student:

    def get_stdno(self):
        return self.stdno

    def set_stdno(self,sno):
        if sno <= 0:
            raise Exception("Number is less than 0")
        self.stdno=sno


    def get_stdname(self):
        return self.stdname

    def set_stdname(self, sname):
        self.stdname = sname


    def get_sclass(self):
        return self.sclass

    def set_sclass(self, scls):
        self.sclass = scls

    def get_totalmarks(self):
        return self.totalmarks

    def set_totalmarks(self, marks):
        self.totalmarks = marks

    def Display(self):
        print(f"Hi\n Studnet details are... \n Sno :{self.stdno}"
              f"\n Sname :{self.stdname} \n Class :{self.sclass} and Total marks :{self.totalmarks}")