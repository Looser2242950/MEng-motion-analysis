# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:50:00 2020

@author: JLooser
"""
import sqlite3
import os
import csv
"""Start SQLite Connection

Make sure this matches the database file where the data is stored""" 
conn = sqlite3.connect('MAD.db')
c=conn.cursor()

"All functions are commented out. Uncomment the function you would like to use"""



"""-------------------EXPORTING TO CSV--------------------------------"""


"""To export all the tables to csv files, run this function.
Each table in the SQLite database will be a new csv file"""

Tablelist= []
def export_all_tables_to_csv():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    print("Table Names: ")
    for row in rows:
        Tablelist.append(row[0])
        print(row)
    
    for table in Tablelist:
        c.execute(f"""select * from {table}""")
        with open(f"""{table}.csv""", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)
        
        dirpath = os.getcwd() + """/{table}.csv"""
        print ("Data exported Successfully into {}".format(dirpath))

# export_all_tables_to_csv()




"""if you want to seperate cvs for each visit"""
Tablelist= []
def export_each_visit_tables_to_csv():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    for row in rows:
        Tablelist.append(row[0])
        print(row)
    for num in [1,2,3,4,5,6]:    
        for table in Tablelist:
            c.execute(f"""select * from {table} where Visit_Number = {num}""")
            with open(f"""{table}visit{num}.csv""", "w") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=",")
                csv_writer.writerow([i[0] for i in c.description])
                csv_writer.writerows(c)
            
            dirpath2 = os.getcwd() + """/{table}visit{num}.csv"""
            print ("Data exported Successfully into {}".format(dirpath2))
#export_each_visit_tables_to_csv()


"""--------------VIEWING DATA and SELECTING DATA-----------------------
This can be helpful for figuring out names of tables and rows"""



"""Select and print the names of all the tables in the database"""

def select_table_names():
    TableNames = []
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    for row in rows:
        TableNames.append(row)
    return TableNames
   
# TableNames = select_table_names()
# print(TableNames) 

"""Print the names of the columns in any given Table. Change 'TableName' 
to the desired table"""

def select_column_names(Table):
    reader = c.execute("SELECT * FROM {}".format(Table))
    names =  [x[0] for x in reader.description] 
    return names
# TableName = "Gait_Max_Min_Table"
# ColumnNames  = select_column_names(TableName)
# print(ColumnNames)


"""Select and print the values of all rows in a certain column and table"""
def select_column_data():
    c.execute(f"""SELECT {variable} FROM {table}""")
    coldata = c.fetchall()
    return coldata
variable = "min_Right_Hip_Angle_x_swing"
table = "Gait_Max_Min_Table"
columndata = select_column_data()


"""Select and print the all values in a row and table
in which a value in a collumn is a specifc value.
For example, view everythign from a certian ID"""
def select_data_conditional():
    c.execute(f"""SELECT * FROM {table} WHERE {variable} == {value}""")
    coldata = c.fetchall()
    return coldata
# variable = "ID"
# table = "Gait_Table"
# value = "123"
# data = select_data_conditional()



"""---------------------DELETING-------------------------"""

"""Delete Data based on two criteria
Example, delete from table where ID = x and vistnumber =y"""
def delete():
   c.execute(f"""DELETE FROM {table} WHERE {variable1} == {value1} AND {variable2}== {value2}""") 
# table = "Gait_Table"
# variable1 = "ID"
# value1 = "1234"
# variable2 = "Visit_Number"
# value2 = 3
# delete()



"""----------CONVRTING BACK TO FLOATING POINT NUMBERS--------"""
"""this converts the values to a dictionary where each value is a list of float numbers
used for selecting an entire column where each cell contains a dataset (ie not maxmin)"""
data={}
def splitdata():
    for i in range(len(columndata)):
        data.update({i: columndata[i][0].split(", ")})
    for key in data.keys():
        for i in range(len(data[key])):
              data[key][i] = float(data[key][i])
# splitdata()

"""Close SQLite Connection"""
conn.commit()
conn.close() 