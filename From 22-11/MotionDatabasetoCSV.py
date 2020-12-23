# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:50:00 2020

@author: JLooser
"""
import sqlite3
import os
import csv
"""Start SQLite Connection""" 
##conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('MotionAnalysis.db')
c=conn.cursor()
Tablelist= []
def select_all():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    for row in rows:
        Tablelist.append(row[0])
        print(row)
select_all()

print( "Exporting data into CSV............")

for table in Tablelist:
    c.execute(f"""select * from {table}""")
    with open(f"""{table}.csv""", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in c.description])
        csv_writer.writerows(c)
    
    dirpath = os.getcwd() + """/{table}.csv"""
    print ("Data exported Successfully into {}".format(dirpath))


# """if you want to seperate cvs for each visit"""
# for num in [1,2,3,4,5,6]:    
#     for table in Tablelist:
#         c.execute(f"""select * from {table} where Visit_Number = {num}""")
#         with open(f"""{table}visit{num}.csv""", "w") as csv_file:
#             csv_writer = csv.writer(csv_file, delimiter=",")
#             csv_writer.writerow([i[0] for i in c.description])
#             csv_writer.writerows(c)
        
#         dirpath2 = os.getcwd() + """/{table}visit{num}.csv"""
#         print ("Data exported Successfully into {}".format(dirpath2))






"""Close SQLite Connection"""
conn.commit()
conn.close() 