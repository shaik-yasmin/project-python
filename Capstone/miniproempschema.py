import miniproemp #Accessing miniproemp classes amd it's methods
#database connectivity
import pyodbc
server = 'HCL-02-127\SQLEXPRESS'
database = 'File1_Search_Result'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Ex(Exception):
    pass
class Not_in_Range(Exception):
    pass
class Emp_data:
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,Name,Salary,Project,Emp_Id):
        self.Name=Name
        self.Salary=Salary
        self.Project=Project
        self.Emp_Id=Emp_Id
    def Insert_values(self): #inserting employee values into database table
        query = '''  
                            INSERT INTO Emp_Details_Table (Name, Salary, Project,Emp_Id)
                            VALUES
                            ('{0}',{1},'{2}',{3})  '''

        insertQuery = query.format(self.Name, self.Salary, self.Project,self.Emp_Id)
        cursor.execute( insertQuery) #it executes  the current data
        cnxn.commit() #saving the data into database
        print("1 row inserted")

    def Update_Salary(self,Up_Salary,Name): #here updating employee details into database
        try:
            self.Up_Salary = Up_Salary
            self.Name=Name
            if self.Up_Salary != self.Salary:
                fileinfoQuery = '''
                                                Update Emp_Details_Table SET Salary ='{0}' WHERE Name = '{1}'
                                                '''
                updateQuery = fileinfoQuery.format(Up_Salary,self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise Ex
        except Ex:
            print("No Change in Salary")
    def Adding_Bonus(self,bonus,Name):
        self.bonus=bonus
        self.Name=Name
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise Not_in_Range
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update Emp_Details_Table SET Salary ='{0}' WHERE Name = '{1}'
                                                                '''
                updateQuery = Query.format(self.Salary, self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
        except Not_in_Range:
            print("Bonus is Not in Range")
    def Change_Emp_Project(self,project,Name):
        self.project=project
        self.Name=Name

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Emp_Details_Table SET Project ='{0}' WHERE Name = '{1}' '''
                updateQuery = Query.format(project, Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Display_Emp_details(self):
        query=''' select * from Emp_Details_Table WHERE Name='{0}' '''
        query1=query.format(self.Name)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}".format(details.Name , details.Salary , details.Project))
    def Delete_Emp_table(self):
        Query = ''' delete from Emp_Details_Table where Name='yasmin'  '''
        cursor.execute(Query)
        cursor.commit()
        print("Employee has been deleted")
#calling the methods
obj1=Emp_data('yasmin',60000,'Java',1)
obj1.Insert_values()
obj=miniproemp.emp_schema()
obj.emp_table()
obj1.Insert_values()
obj1.Update_Salary(35000,'yasmin')
obj1.Adding_Bonus(1,'yasmin')
obj1.Change_Emp_Project('python','Java')
obj1.Display_Emp_details()
obj1.Delete_Emp_table()
