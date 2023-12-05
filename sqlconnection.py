import pymssql

# Database connection parameters
server = "aquaview.database.windows.net"  # Your server
suser = "hamm0074"  # Your username
spassword = "NotAnImportantPassword"  # Your password
database = "aquaview"  # Your database name
def verify_user(usernames, passwords):
    try:
        with pymssql.connect(server, suser, spassword, database) as conn:
            with conn.cursor() as cursor:
                # Check if user exists with the given username and password
                cursor.execute("SELECT * FROM USERS WHERE usernames = %s AND passwords = %s", (usernames, passwords))
                return cursor.fetchone() is not None
    except Exception as e:
        print(f"Error verifying user: {e}")
        return False

def add_user(username, password):
    try:
        with pymssql.connect(server, suser, spassword, database) as conn:
            with conn.cursor() as cursor:
                # Check if user already exists
                cursor.execute("SELECT * FROM USERS WHERE usernames = %s", (username,))
                if cursor.fetchone():
                    return False  # User already exists

                # Add new user
                insert_query = "INSERT INTO USERS (usernames, passwords) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, password))
                conn.commit()
                return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False

# Create a connection to the database
try:
    connection = pymssql.connect(server, suser, spassword, database)
    print("Connected to the database successfully")

    # Create a cursor object
    cursor = connection.cursor()

    # Example query
    query = "SELECT * FROM USERS"  # Replace with your actual query

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if connection:
        connection.close()
        print("Connection closed")

