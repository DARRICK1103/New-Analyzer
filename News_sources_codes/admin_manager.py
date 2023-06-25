import mysql.connector

def findLargestID():

        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

        # execute a SQL query to find the largest id value
        query = "SELECT MAX(ADMIN_ID) FROM admin"
        cursor.execute(query)

        # fetch the result and extract the largest id value
        result = cursor.fetchone()

        try:
            max_id = result[0]
        except TypeError:
            # if no id value is found, assign a default value of "A0001"
            max_id = "A000000001"

        

        # close the cursor and database connection
        cursor.close()
        connection.close()

        return max_id

class Admin:
    def __init__(self, ADMIN_ID, NAME, GENDER, AGE, IC_NUMBER, CONTACT_NUMBER, EMAIL, STATUS):
        self.ADMIN_ID = ADMIN_ID
        self.NAME = NAME
        self.GENDER = GENDER
        self.AGE = AGE
        self.IC_NUMBER = IC_NUMBER
        self.CONTACT_NUMBER = CONTACT_NUMBER
        self.EMAIL = EMAIL
        self.status = STATUS

    

def insert(admin):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()
        # Preparing SQL query to INSERT a record into the database. 
        sql = ("INSERT INTO admin (ADMIN_ID, NAME, GENDER, AGE, IC_NUMBER, CONTACT_NUMBER, EMAIL, STATUS)" 
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        admin.ADMIN_ID = findLargestID()
        data = (admin.ADMIN_ID, admin.NAME, admin.GENDER, admin.AGE, admin.IC_NUMBER, admin.CONTACT_NUMBER, admin.EMAIL, admin.STATUS)


        # Executing the SQL command
        cursor.execute(sql, data)
        
        # Commit your changes in the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()


    except:
        # Rolling back in case of error
        connection.rollback()

        print("Data inserted")

        # Closing the connection
        connection.close()


def update(admin):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

        # execute a SQL query to update the admin object with the given adminID
        query = "UPDATE admin SET NAME = %s, GENDER = %s, AGE = %s, IC_NUMBER = %s, CONTACT_NUMBER = %s, EMAIL = %s, STATUS = %s, WHERE ADMIN_ID = %s"
        values = (admin.NAME, admin.GENDER, admin.AGE, admin.IC_NUMBER, admin.CONTACT_NUMBER, admin.EMAIL, admin.STATUS, admin.ADMIN_ID)

        cursor.execute(query, values)

        # commit the changes to the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print(f"Error: {error}")



def delete(admin):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

        # execute a SQL query to update the admin object with the given adminID
        query = "UPDATE admin SET STATUS = 0 WHERE ADMIN_ID = %s"
        values = (admin.adminID,)
        cursor.execute(query, values)


        # commit the changes to the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as error:
        print(f"Error: {error}")




def get(adminID):
    #establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # create a cursor object
    cursor = connection.cursor()

    # execute a SQL query to find the admin object with the given adminID
    query = "SELECT * FROM admin WHERE ADMIN_ID = %s"
    values = (ADMIN_ID,)
    cursor.execute(query, values)

    # fetch the result and create an Admin object
    result = cursor.fetchone()

    if result is None:
        return None

    ADMIN_ID, NAME, GENDER, AGE, IC_NUMBER, CONTACT_NUMBER, EMAIL, STATUS = result
    admin = Admin(ADMIN_ID, NAME, GENDER, AGE, IC_NUMBER, CONTACT_NUMBER, EMAIL, STATUS)

    # close the cursor and database connection
    cursor.close()
    connection.close()

    return admin

def view_admins():
    try:
    #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

        # execute a SQL query to retrieve all admin objects
        query = "SELECT * FROM admin"
        cursor.execute(query)

        # fetch all rows and create a list of admin objects
        admins = []
        for row in cursor:
            admin = Admin(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            admins.append(admin)
        # close the cursor and database connection
        cursor.close()
        connection.close()

        # return the list of admin objects
        return admins

    except mysql.connector.Error as error:
        print(f"Error: {error}")





