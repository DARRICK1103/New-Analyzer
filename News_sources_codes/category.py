import mysql.connector

def findLargestID():
    # Establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query to find the largest id value
    query = "SELECT MAX(CATEGORY_ID) FROM category"
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
        new_id = "C{:09d}".format(new_numeric_part)
    else:
        new_id = "C000000001"

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return new_id

class Category:
    def __init__(self, CATEGORY_ID, NAME, DESCRIPTION, STATUS):
        self.CATEGORY_ID = CATEGORY_ID
        self.NAME = NAME
        self.DESCRIPTION = DESCRIPTION
        self.STATUS = STATUS


def insert(category):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Preparing SQL query to INSERT a record into the database.
        sql = ("INSERT INTO category (CATEGORY_ID, NAME, DESCRIPTION, STATUS)"
               "VALUES (%s, %s, %s, %s)"
               )
        category.CATEGORY_ID = findLargestID()
        data = (category.CATEGORY_ID, category.NAME, category.DESCRIPTION, '1')

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


def get_all_history():
    try:
        # Establish the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Execute SQL query to fetch all history records
        query = "SELECT * FROM category"
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Create a list to store the History objects
        category_list = []

        # Iterate over the results and create History objects
        for result in results:
            category_id, name, description, status = result
            category = Category(category_id, name, description, status)
            if status == '1':
                category_list.append(category)

        # Close the cursor and database connection
        cursor.close()
        connection.close()
        return category_list

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()

def get(Name):
    try:
        # Establish the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Execute SQL query to fetch history records by category_id
        query = "SELECT * FROM category WHERE NAME = %s"
        cursor.execute(query, (Name,))

        # Fetch all the results
        result = cursor.fetchone()

        category_id, name, description, status = result
        if result is not None and status == 1:
            category = Category(category_id, name, description, status)
        else:
            return None
        
        # Close the cursor and database connection
        cursor.close()
        connection.close()

        return category

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()