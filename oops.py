class Car:
    someclassdummyvar="dummy"
    def simple_car_instance_method(self, a):
        print(a)
        print(self.someclassdummyvar)
carObj=Car()
carObj.simple_car_instance_method("hello again!")
carObj2=Car()
carObj2.simple_car_instance_method(2)
############################################################################
class Carsimple:
    dummyvar1="dummyvar1"
    dummyvar2="dummyvar2"
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def displaycardetails(self):
        print(self.name)
        print(self.model)
carObj=Carsimple("audi","A5")
carObj.displaycardetails()
##############################################################################
#static method
class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y):
        return x+y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y
staticObj=StaticClass()
output_add=staticObj.sample_static_method_addition(2,3)
output_mul=staticObj.sample_static_method_multiplication(2,3)
print(output_add,output_mul)
StaticClass.sample_static_method_addition(2,3)
############################################################################
#class method
class ClassMethodExample:
    classvar1=False
    classvar2="ON"
    @classmethod
    def sample_class_method(cls):
        cls.classvar1=True
        cls.classvar2="OFF"
        print(cls.classvar1)
        print(cls.classvar2)
classObj=ClassMethodExample()
classObj.sample_class_method()
############################################################################
x = "global"
class Program:
    classvar = "ClassVar1"
    def __init__(self, a):
        self.a = a
        print(self.a)
    def simple_code(self,a):
        sample_method = "world"
        global x
        x = "local"
        print(x)
        print(a)
        print(sample_method)
        print(self.classvar)
    def method_wihtout_self(self):
        print(self.classvar)
        print(self.a)
        print("Without Self")
classObj=Program("Hello")
classObj.simple_code("Hello Again")
classObj.method_wihtout_self()
###########################################################################
class Product:
    def __init__(self,name,price,deal_price):
        self.name=name
        self.price=price
        self.deal_price=deal_price
    def get_product(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
class Electronic:
    def __init__(self,warrenty):
        self.warrenty=warrenty
    def get_warrenty(self):
        print(self.warrenty)
        pass
class Grossery:
    def __init__(self,expiry_date,packing_date):
        self.expiry_date=expiry_date
        self.packing_date=packing_date
    def get_expiry(self):
        print(self.expiry_date)
        pass
    def get_packing(self):
        #print(self.packing_date)
        pass #means it executes empty code
class1=Product("laptop",34000,45000)
class1.get_product()
class2=Electronic("1 year")
class2.get_warrenty()
class3=Grossery("12/2023","10/2022")
class3.get_expiry()
class3.get_packing()
############################################################################
class Car:
    def Yasmin(self,color,max_speed,acceleration,type_friction,start_engine,current_speed):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.type_friction=type_friction
        self.start_engine=start_engine
        self.current_speed=current_speed
        if(self.start_engine==True):
            Car.start_engine(self,start_engine,color,current_speed,tyre_friction)
        else:
            Car.stop_engine(self,start_engine,self.color)
        @classmethod
        def start_engine(cls,ce,co,c,d):
            print("car engine is started",ce)
            print("car color is:",co)
            Car.apply_break(c,d)
            Car.sound_horn()
        @classmethod
        def stop_engine(cls,z,x):
            print("car color is:",x)
            print("car engine is not started",z)
        @classmethod
        def apply_breaks(cls,current_speed,tyre_friction):
            if(current_speed>0):
                print("previous speed is:",current_speed)
                current_speed-=tyre_friction
                print("current speed is:",current_speed)
        @classmethod
        def sound_horn(s):
            print("beep! beep!")
car=Car()
car.Yasmin("blue",100,20,5,True,15)
################################################################################
class Car:
    color="orange"
    maxspeed=120
    acceleration=30
    tyre_triction=10
    start_engine=False
    currentspeed=65
    def startEngine(self):
        self.start_engine=True
        print("the car color is:",self.color)
        print("engine started")
        print("car is started")
    def stop_engine(self):
        self.stop_engine=False
        print("engine stopped")
        print("car not started yet")
    def sound_horn(self):
        if(self.start_engine):
            print("beep! beep!")
        else:
            print("engine is not started")
    def apply_breaks(self):
        if self.currrentspeed>0 and self.currentspeed>=self.tyre_friction:
            self.current_speed-=self.tyre_friction
            print("applying breaks")
            print("current speed:",self.currentspeed)
        else:
            print("not applicable breaks")
    def apply_acceleration(self):
        if self.currentspeed<self.maxspeed:
            self.currentspeed+=self.acceleration
            print("applied acceleration")
        else:
            print("not applied acceleration")
carObj=Car()
carObj.startEngine()
carObj.stop_engine()
carObj=sound_horn()
carObj=apply_breaks()
carObj=apply_acceleration()




