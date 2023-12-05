import pymssql

# Database connection parameters
server = "aquaview.database.windows.net"  # Your server
user = "hamm0074"  # Your username
password = "Bulldog102299"  # Your password
database = "aquaview"  # Your database name

# Create a connection to the database
try:
    connection = pymssql.connect(server, user, password, database)
    print("Connected to the database successfully")

    # Create a cursor object
    cursor = connection.cursor()

    # Example query
    query = "SELECT * FROM your_table_name"  # Replace with your actual query

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
