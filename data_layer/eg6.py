from hr import DBConnection,DataLayerException
try:
    dbConnection=DBConnection.getConnection()
    print("Connected to database")
except DataLayerException as dle:
    print(dle.message)
    print(dle.exceptions)
finally:
    try:
        if dbConnection.is_connected(): dbConnection.close()
    except:  
        pass