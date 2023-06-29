import mysql.connector
from datetime import datetime

def insert_record(first_name,last_name,email,occupation,date):
    date_obj=datetime.strptime(date, "%Y-%m-%d")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="love2002",
        database="Python_Work"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO job_forms (first_name, last_name, email, occupation, date) VALUES (%s, %s, %s, %s, %s)"
    val = (first_name,last_name,email,occupation,date_obj)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")