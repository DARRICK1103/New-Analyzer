import mysql.connector


def getID():
    # Establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query to find the largest id value
    query = "SELECT MAX(NEWS_ID) FROM news"
    cursor.execute(query)

    # Fetch the result and extract the largest id value
    result = cursor.fetchone()

    if result[0] is not None:
        largest_id = result[0]
    else:
        largest_id = "N000000001"
    
    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return largest_id

def findLargestID():
    # Establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query to find the largest id value
    query = "SELECT MAX(NEWS_ID) FROM news"
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
        new_id = "N{:09d}".format(new_numeric_part)
    else:
        new_id = "N000000001"

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return new_id

class News:
    def __init__(self, NEWS_ID, AUTHOR, DATE, CONTENT, SUMMARY, URL, CATEGORY_ID, STATUS, NEWS_PIC, TITTLE):
        self.NEWS_ID = NEWS_ID
        self.AUTHOR = AUTHOR
        self.DATE = DATE
        self.CONTENT = CONTENT
        self.SUMMARY = SUMMARY
        self.URL = URL
        self.CATEGORY_ID = CATEGORY_ID
        self.STATUS = STATUS
        self.NEWS_PIC = NEWS_PIC
        self.TITTLE = TITTLE

def insert(news):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Preparing SQL query to INSERT a record into the database
        sql = ("INSERT INTO news (NEWS_ID, AUTHOR, DATE, CONTENT, SUMMARY, URL, CATEGORY_ID, STATUS, NEWS_PIC, TITTLE) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        news.NEWS_ID = findLargestID()
        data = (news.NEWS_ID, news.AUTHOR, news.DATE, news.CONTENT, news.SUMMARY, news.URL, news.CATEGORY_ID, '1', news.NEWS_PIC, news.TITTLE)
        # print(data)  # Print the data tuple for debugging purposes

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
        query = "SELECT * FROM news"
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Create a list to store the History objects
        news_list = []

        # Iterate over the results and create History objects
        for result in results:
            news_id, author, date, content, summary, url, category_id, status, news_pic = result
            news = News(news_id, author, date, content, summary, url, category_id, status, news_pic)
            if status == '1':
                news_list.append(news)

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        return news_list

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()


def get(news_id):
    try:
        # Establish the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Execute SQL query to fetch news records by news_id
        query = "SELECT * FROM news WHERE NEWS_ID = %s"
        cursor.execute(query, (news_id,))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            news_id, author, date, content, summary, url, category_id, status, news_pic, tittle = result
            if status == 1:
                news = News(news_id, author, date, content, summary, url, category_id, status, news_pic, tittle)
                # Close the cursor and database connection
                cursor.close()
                connection.close()
                return news
            else:
                print("News with specified ID is not active.")
        else:
            print("No news found with the specified ID.")

        # Close the cursor and database connection
        cursor.close()
        connection.close()
        return None

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()
        return None


def delete_news(news_id):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Deleting the user
        query = "DELETE FROM news WHERE NEWS_ID = %s"
        cursor.execute(query, (news_id,))

        # Commit your changes in the database
        connection.commit()

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        print("News deleted successfully.")

    except Exception as e:
        # Rolling back in case of error
        connection.rollback()

        print("Error occurred:", str(e))

        # Closing the connection
        connection.close()

def getURL(user_id):
    try:
        # Establish the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()

        # Execute SQL query to fetch history records by category_id
        query = "SELECT DISTINCT n.URL FROM news n INNER JOIN read_history rh ON n.NEWS_ID = rh.NEWS_ID WHERE rh.user_id = %s"
        cursor.execute(query, (user_id,))

        # Fetch all the results
        result = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        # Process the result as needed
        urls = [row[0] for row in result]
        return urls

    except Exception as e:
        print("Error occurred:", str(e))

        # Close the connection
        connection.close()
