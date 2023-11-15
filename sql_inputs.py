import pyodbc

def upload_data_to_table(data):
    # TODO : Live server - comment out when code works
    # connection_string = "DRIVER={SQL Server};SERVER=ETZ-SQL;DATABASE=ETEZAZIMIETrakLive;Trusted_Connection=yes;"
    connection_string = "DRIVER={SQL Server};SERVER=ETZ-SQL;DATABASE=Sandbox;Trusted_Connection=yes;"

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the table name and column names for data insertion
        table_name = 'Item'
        column_names = ['PartName', 'Description', 'Revision', 'DrawingNumber', 'DrawingRevision']  # check if this is all we need

        # Insert the extracted information into the database table
        insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (
            data.get('Part Number', ''),
            data.get('Part Name', ''),
            data.get('Part Revision Level', ''),
            data.get('Drawing Number', ''),
            data.get('Drawing revision Level', '')
        ))
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        print("Data uploaded successfully.")

    except pyodbc.Error as ex:
        print('Error in pyodbc:', ex)