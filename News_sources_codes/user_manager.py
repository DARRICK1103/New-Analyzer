import mysql.connector


def findLargestID():
    # Establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query to find the largest id value
    query = "SELECT MAX(USER_ID) FROM users"
    cursor.execute(query)

    # Fetch the result and extract the largest id value
    result = cursor.fetchone()

    if result[0] is not None:
        largest_id = result[0]
        # Extract the numerical part of the ID
        numeric_part = int(largest_id[1:])

        # Increment the numeric part
        new_numeric_part = numeric_part + 1

        # Format the new numeric part back into the ID format with leading zeros
        new_id = "U{:09d}".format(new_numeric_part)
    else:
        new_id = "U000000001"

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return new_id


class User:
    def __init__(self, USER_ID, PIC, NAME, GENDER, BIRTHDAY, EMAIL, PASSWORD, STATUS):
        self.USER_ID = USER_ID
        self.PIC = PIC
        self.NAME = NAME
        self.GENDER = GENDER
        self.BIRTHDAY = BIRTHDAY
        self.EMAIL = EMAIL
        self.STATUS = STATUS
        self.PASSWORD = PASSWORD


def insert(user):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Read the image file
        with open(user.PIC, 'rb') as file:
            image_data = file.read()

        # Preparing SQL query to INSERT a record into the database.
        sql = ("INSERT INTO users (USER_ID, PIC, NAME, GENDER, BIRTHDAY, EMAIL, PASSWORD, STATUS)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
               )
        user.USER_ID = findLargestID()
        data = (user.USER_ID, image_data, user.NAME, user.GENDER, user.BIRTHDAY, user.EMAIL, user.PASSWORD, user.STATUS)

        # Executing the SQL command
        cursor.execute(sql, data)

        # Commit your changes in the database
        connection.commit()

        # Close the cursor and database connection
        cursor.close()
        connection.close()

    except Exception as e:
        # Rolling back in case of error
        connection.rollback()

        print("Error occurred:", str(e))

        # Closing the connection
        connection.close()


def update(user):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

          # Read the image file
        with open(user.PIC, 'rb') as file:
            image_data = file.read()

        # execute a SQL query to update the admin object with the given adminID
        query = "UPDATE users SET PIC = %s, NAME = %s, GENDER = %s, BIRTHDAY = %s, EMAIL = %s, PASSWORD = %s, STATUS = %s WHERE USER_ID = %s"
        values = (image_data, user.NAME, user.GENDER, user.BIRTHDAY, user.EMAIL, user.PASSWORD, user.STATUS, user.USER_ID)

        cursor.execute(query, values)

        # commit the changes to the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print(f"Error: {error}")


def delete(user_id):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

        # execute a SQL query to update the user object with the given userID
        query = "UPDATE users SET STATUS = 0 WHERE USER_ID = %s"
        values = (user_id,)
        cursor.execute(query, values)


        # commit the changes to the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as error:
        print(f"Error: {error}")

def delete_user(user_id):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Deleting the user
        query = "DELETE FROM users WHERE USER_ID = %s"
        cursor.execute(query, (user_id,))

        # Commit your changes in the database
        connection.commit()

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        print("User1 deleted successfully.")

    except Exception as e:
        # Rolling back in case of error
        connection.rollback()

        print("Error occurred:", str(e))

        # Closing the connection
        connection.close()


def getLogin(email, password):
    #establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # create a cursor object
    cursor = connection.cursor()

    # execute a SQL query to find the admin object with the given adminID
    query = "SELECT * FROM users WHERE EMAIL = %s AND PASSWORD = %s"
    values = (email, password)
    cursor.execute(query, values)

    # fetch the result and create an Admin object
    result = cursor.fetchone()

    if result is None:
        return None

    USER_ID, PIC, NAME, GENDER, BIRTHDAY, EMAIL, PASSWORD, STATUS = result
    user = User(USER_ID, PIC, NAME, GENDER, BIRTHDAY, EMAIL, PASSWORD, STATUS)

    # close the cursor and database connection
    cursor.close()
    connection.close()

    return user

def get(user_id):
    try:
        # Establish the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Execute SQL query to fetch history records by category_id
        query = "SELECT * FROM users WHERE USER_ID = %s"
        cursor.execute(query, (user_id,))

        # Fetch all the results
        result = cursor.fetchone()

        user_id, pic, name, gender, birthday, email, password, status = result
        if result is not None and status == 1:
            user = User(user_id, pic, name, gender, birthday, email, password, status)
        else:
            return None
        
        # Close the cursor and database connection
        cursor.close()
        connection.close()

        return user

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()


def check_email_duplicate(email):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Preparing SQL query to check for duplicate email
        sql = "SELECT COUNT(*) FROM users WHERE EMAIL = %s"
        cursor.execute(sql, (email,))

        # Fetch the result
        result = cursor.fetchone()
        count = result[0]

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        # Return False if email is repeated, True otherwise
        return count == 0

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()
        return False
    
