#test
#Gabriel Browning
#Emma Reiff
#Logan Cagle

import psycopg2
server = "aquaview-server.database.windows.net"
port = 1433
user = "AquaView"
password = "SoftwareEngineering2023"
database = "AquaViewDB"
# Connect to your postgres DB
conn = psycopg2.connect(host = server, user = "AquaView@aquaview-server", password = "SoftwareEngineering2023", sslmode = 'require', port = 1433)

# Open a cursor to perform database operations 
cur = conn.cursor()

# Execute a query
cur.execute("Select * from [dbo].[storage]")

# Retrieve query results
records = cur.fetchall()

print(records)