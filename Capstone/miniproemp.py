import pyodbc
server = 'HCL-02-127\SQLEXPRESS'
database = 'File1_Search_Result'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
#creating an employee schema
class emp_schema:
    def emp_table(self):
        try:
            query1 = cursor.execute('''use File1_Search_Result''')
            query2 = cursor.execute('''create table Emp_Details_Table
                                                   (
                                                   Emp_Id int NOT NULL,
                                                   Name varchar(50),
                                                   project varchar(50),
                                                   salary int,
                                                   primary key (Emp_Id)
                                                   )
                                                   ''')
            query3 = cursor.execute('''select * from Emp_Details_Table''')
            cnxn.commit()
            print("Table created sucessfully")
        except:
            print("Table already exist")
#callings the methods
obj=emp_schema()
obj.emp_table()
