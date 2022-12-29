import win32api
availableDrives=win32api.GetLogicalDriveStrings()
print(availableDrives)
drives=[drivestr for drivestr in availableDrives.split('\000') if drivestr]
#drives=drives.split('\000')[:-1]
print(drives)
#############################################################################################3
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server=HCL-02-127\SQLEXPRESS;'
                    'Database=FileSearchResults1;'
                    'Trusted_Connection=yes;')
cursor=conn.cursor()
cursor.execute('''
INSERT INTO FileSearchResults_table1(File_Location,SearchCount,NameOfFile)
VALUES
('C:\ new_A\ new_sub1\ new_sub2',1,'demo.txt'),
('C:\ new_A\ new_sub1\ new_sub2',3,'demo.txt')''')
conn.commit();
cursor.execute('Select * FromFileSearchResults_table1')


