class Student:
    marks_bonus=2
    somevalue=""
    def __init__(self,first,last,marks,year,class_name):
        self.first=first
        self.last=last
        self.marks=marks
        self.year=year
        self.class_name=class_name
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{}.{}'.format(self.first,self.last)
    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)
    def dummy(self):
        self.year+=1
    def dummy1(self):
        self.class_name=int(self.class_name)
    def something(self,middlename):
        self.somevalue=self.email + self.fullname + middlename
    def something1(self):
    #    return '{}.{}@gmail.com{}.{}'.format(self.first,self.last,self.first,self.last)
         print("hcl.tech@gmail.comhcl.tech")


