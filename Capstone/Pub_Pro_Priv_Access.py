#Public Access modifier
class Public:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayAge(self):
        print("age:",self.age)
obj=Public("yasmin",21)
print("name:",obj.name)
obj.displayAge()

#Protected Access modifier
class Protect_Student:
    _name=None
    _roll=None
    _branch=None
    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def _displayRollandBranch(self):
        print("roll:",self._roll)
        print("branch:",self._branch)
class Derived(Protect_Student):
    def __init__(self,name,roll,branch):
        Protect_Student.__init__(self,name,roll,branch)
    def displayDetails(self):
        print("name:",self._name)
        self._displayRollandBranch()
obj=Derived("yasmin",18428,"ECE")
obj.displayDetails()

#Private Access modifier
class Private_Student:
    __name=None
    __roll=None
    __branch=None
    def __init__(self,name,roll,branch):
        self.__name=name
        self.__roll=roll
        self.__branch=branch
    def __displayDetails(self):
        print("name:",self.__name)
        print("roll:",self.__roll)
        print("branch:",self.__branch)
    def accessprivatefunction(self):
        self.__displayDetails()
obj=Private_Student("yasmin",18428,"ECE")
obj.accessprivatefunction()


