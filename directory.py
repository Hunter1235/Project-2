# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:51:46 2021
This script creates an initial directory database for use by the phone/SMS App.
@author: Hunter Stiles
"""


import sqlite3
import pandas as pd
con = sqlite3.connect('directory.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS PhoneNumbers');
cur.execute('CREATE TABLE PhoneNumbers (name text, number text)')

numbers = [('Kean University', '9087375326'),
           ('Hunter Cell', '9084053344'),
           ('Dad Cell', '9085559946'),
           ('Hunter Home', '90865554827'),
           ('Kean Comp Sci Dept',  '9087374250')
           ]
cur.executemany('INSERT INTO PhoneNumbers VALUES (?,?)', numbers)
con.commit()
#print out the directory to be sure that it is there 
for row in cur.execute('SELECT * FROM PhoneNumbers ORDER BY name'):
        print(row)
        

df = pd.read_sql_query("SELECT name, number FROM PhoneNumbers ORDER BY name", con)
print(df)
print("--------------------------")
print(df['name'].tolist())
ind=df.index[(df['name'] == 'Hunter Cell')].tolist()
print (df.at[ind[0], 'number'])
cur.close()
con.close()