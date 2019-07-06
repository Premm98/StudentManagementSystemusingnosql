import sqlite3

connection = sqlite3.connect("management.db")
print("Database connection successful")

TABLE_NAME = "employee_details"
EMP_ID = "employee_id"
EMP_NAME = "employee_name"
EMP_ADDRESS = "employee_address"
EMP_PHONE = "employee_phone"

## Take table
create_table_query = " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + EMP_ID + \
                     " INTEGER PRIMARY KEY AUTOINCREMENT, " + EMP_NAME + " TEXT, " + \
                     EMP_ADDRESS + " TEXT, " + EMP_PHONE + " INTEGER );"

connection.execute(create_table_query)
print("Table created successfully.")

def save_record(name, address, phone):

    detail_query = "INSERT INTO " + TABLE_NAME + " ( " + EMP_NAME + ", " + EMP_ADDRESS +\
                   ", " + EMP_PHONE + " ) VALUES ( '" + name + "', '" + address + "', " + \
                   str(phone) + " );"

    connection.execute(detail_query)
    connection.commit()
    print("Values saved successfully.")

























