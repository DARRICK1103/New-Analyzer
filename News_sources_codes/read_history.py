import mysql.connector

def findLargestID():
    # Establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query to find the largest id value
    query = "SELECT MAX(HISTORY_ID) FROM read_history"
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
        new_id = "H{:09d}".format(new_numeric_part)
    else:
        new_id = "H000000001"

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return new_id

class History:
    def __init__(self, HISTORY_ID, USER_ID, NEWS_ID, DATE_TIME, STATUS):
        self.HISTORY_ID = HISTORY_ID
        self.USER_ID = USER_ID
        self.NEWS_ID = NEWS_ID
        self.DATE_TIME = DATE_TIME
        self.STATUS = STATUS


def insert(history):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Preparing SQL query to INSERT a record into the database.
        sql = ("INSERT INTO read_history (HISTORY_ID, USER_ID, NEWS_ID, DATE_TIME, STATUS)"
               "VALUES (%s, %s, %s, %s, %s)"
               )
        history.HISTORY_ID = findLargestID()
        data = (history.HISTORY_ID, history.USER_ID, history.NEWS_ID, history.DATE_TIME, history.STATUS)

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
        query = "SELECT * FROM read_history"
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Create a list to store the History objects
        history_list = []

        # Iterate over the results and create History objects
        for result in results:
            history_id, user_id, news_id, date_time, status = result
            history = History(history_id, user_id, news_id, date_time, status)
            if status == '1':
                history_list.append(history)

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        return history_list

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()

def get(user_id):
    try:
        # Establish the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Execute SQL query to fetch history records by category_id
        query = "SELECT * FROM read_history WHERE USER_ID = %s"
        cursor.execute(query, (user_id,))

        # Fetch all the results
        results = cursor.fetchall()

        news_ids = []
        for result in results:
            history_id, user_id, news_id, date_time, status = result
            if status == 1:
                history = History(history_id, user_id, news_id, date_time, status)
                news_ids.append(history.NEWS_ID)

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        return news_ids

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()

    return None


def delete_history(history_id):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Deleting the user
        query = "DELETE FROM read_history WHERE HISTORY_ID = %s"
        cursor.execute(query, (history_id,))

        # Commit your changes in the database
        connection.commit()

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        print("History deleted successfully.")

    except Exception as e:
        # Rolling back in case of error
        connection.rollback()

        print("Error occurred:", str(e))

        # Closing the connection
        connection.close()