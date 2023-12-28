import pyodbc
from connection_string import sandbox, live

#TODO : clean up insert functions
class SQL:
    SANDBOX_CONN_STRING = sandbox 
    LIVE_CONN_STRING = live 

    def __init__(self, use_live=False):
        self.conn_string = self.LIVE_CONN_STRING if use_live else self.SANDBOX_CONN_STRING        
        print(self.conn_string)

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.conn_string)
        except pyodbc.Error as e:
            print(f"Error connecting to the database {e}")
        finally:
            self.conn.close()

    def insert_multiple_values(self, insert_query, values):
        """opens a connection of its own - does not use the connect function"""
        try:
            with pyodbc.connect(self.conn_string) as conn:
                with conn.cursor() as cursor:
                    set_insert = "SET IDENTITY_INSERT Item ON;"
                    cursor.execute(set_insert)
                    conn.commit()
                    x = 0
                    for value in values:
                        cursor.execute(insert_query, value)
                        x += 1
                        print(f"Executed query number - {x}")
                conn.commit()

        except pyodbc.Error as e:
            print(f"Error - Rolling back changes {e}")
            conn.rollback()
        finally:  # we dont need this as with statement will close the connection automatically
            print(f"Total executions - {x}")

    def insert_item_inventory(self, data_dict):
        try:
            with pyodbc.connect(self.conn_string) as conn:
                with conn.cursor() as cursor:
                    set_insert = "SET IDENTITY_INSERT ItemInventory ON;"
                    cursor.execute(set_insert)
                    conn.commit()
                    x = 0
                    command = "INSERT INTO ItemInventory (ItemInventoryPK) VALUES (?)"
                    for entry in data_dict:
                        cursor.execute(command, entry[1])  # entry[1] is the fk in item table
                        conn.commit()
                        x += 1
                        print(f"Inventory table updated - count = {x}")
                    conn.execute("SET IDENTITY_INSERT ItemInventory OFF;")
        except pyodbc.Error as e:
            print(f"Error - {e}")
        finally:
            print(f"Connection Closed - Updates {x} values")
