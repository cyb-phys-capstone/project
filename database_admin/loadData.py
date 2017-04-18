import psycopg2

#connect to CYB_PHYS_CAPSTONE_DB 
connection = "host='localhost' dbname='CYB_PHYS_CAPSTONE_DB' user='admin' password='abc123'"

print "Attempting to connect to Postgres DB : %s" %(connection)
print
try:
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    print "Connected to Postgres DB"
    fileName = input("Enter the name of the file to read : ")
    file = open(fileName,'r')
    for line in file:
        #need to check for table name
        dataArray = line.split() #splits each line using whitespace by default
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")

        #collection.insert_one(
        #     {"operation":str(dataArray[0]),
        #     "grade":literal_eval(dataArray[1]),
        #    "difficulty":literal_eval(dataArray[2]),
        #    "operands":literal_eval(dataArray[3]),
        #     "incorrect":literal_eval(dataArray[4]),
        #     "solution":int(dataArray[5])
        #    }            
        #)
        file.close()

except psycopg2.DatabaseError, error:
    print "Failed to connect!"
    print "Postgres DB error : %s" % error



