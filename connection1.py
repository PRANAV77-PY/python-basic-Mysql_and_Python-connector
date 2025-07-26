import mysql.connector      #mysqlconnection

mydb = mysql.connector.connect(
        host = 'LocalHost' ,    #or ypur server host
        username = 'root',          #username my sql
        password = 'root',          #password
        database = 'PYSQL1'
)

print('ESTABLISHED')     #CONNECTION INTEGRATE


#CREATE CURSOR OBJECT
mycursor = mydb.cursor()

#CREATE A NEW TABLE
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee(
            emp_id INT,
            emp_Name VARCHAR(255),
            Salary INT
                )
                 """)

print('Table Created')

#insert multiple rows
sql = "INSERT INTO Employee (Emp_id,Emp_name,salary)Values (%s,%s,%s)"
values =[
    (4,'Vivek',40000.00),
    (5,'Omkar',50000.00),
    (6,'Pranav',90000.00),
    (7,'Vaibhav',45000.00),
    (8,'Ajit',60000)
]

mycursor.executemany(sql,values)
mydb.commit()

print('inserted')