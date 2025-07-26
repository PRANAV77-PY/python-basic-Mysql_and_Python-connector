import mysql.connector  #mysqlconnection
mydb = mysql.connector.connect(
    host = "localhost",     #or your server host
    user = "root",          #your MySQL username
    password = "root",   #your MySQL password
    database = "pythonmysqlconnection"  #optional: the DB to use
)


print("connection sucessfull")


# Create a cursor object

mycursor = mydb.cursor()


#Execute a simple query
# mycursor.execute("SHOW DATABASES")


# Create a new table
'''mycursor.execute ("""
    CREATE TABLE IF NOT EXISTS students(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age int
    )
    """)
print("table created sucessfully")

                 '''


#INSERT MUTIPLE ROWS

'''sql = " INSERT INTO Students(Id,Name,Age)VALUES (%s,%s,%s)"
values = [
    (1,'Pranav',26),
    (2,'Jack',28),
    (3,'Vivek',29),
    (4,'Omkar',23),
    (5,'Gaurav',25)    
]

#
mycursor.executemany(sql,values)
mydb.commit()

print("record_inserted")'''

'''mycursor.execute("SELECT * FROM students")
result = mycursor.fetchall()
for row in result:
    print(row)'''

#UPDATE DATA
'''sql = 'UPDATE students SET age = %s WHERE name = %s'
val = (22,'Jack')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,'record(s)affected')'''


sql = 'UPDATE students SET age = %s  WHERE name = %s'
val = (22,'vivek')
mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount,'records affected')

#delete
sql = 'DELETE FROM students WHERE name = %s'
val = ('Gaurav',)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,'records deleted')

