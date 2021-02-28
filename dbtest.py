import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'Lc654321'
database = 'MyDatabase'


def doQuery( conn ):
    cur = conn.cursor()

    cur.execute( "SELECT \"Firstname\", \"Lastname\", \"Email\", \"City\" FROM public.\"Contacts\"" )

    for Firstname, Lastname, Email, City in cur.fetchall() :
        print (Firstname, Lastname, Email, City)

        print()

      #  cur.execute( "SELECT \"Name\", \"Age\", \"Salary\" FROM public.\"Practice\"" )

        cur.execute( "SELECT \"Name\", \"Age\", \"Salary\" FROM \"Practice\" WHERE \"Name\" = 'Joe' OR \"Age\" = '73';" )

    #    cur.execute("ALTER TABLE \"Practice\" DROP COLUMN \"Name\"")

    print()

    for Name, Age, Salary in cur.fetchall() :
        print (Name, Age, Salary)


    cur.execute( "INSERT INTO public.\"Contacts\" (\"Firstname\", \"Lastname\", \"Email\", \"City\") VALUES( 'Bill', 'Hader', 'BillHader@icloud.com', 'Los Santos')")


    cur.execute( "SELECT \"Firstname\", \"Lastname\", \"Email\", \"City\" FROM public.\"Contacts\"" )

    for Firstname, Lastname, Email, City in cur.fetchall() :
        print (Firstname, Lastname, Email, City)

    cur.execute( "SELECT o.\"Firstname\", o.\"Lastname\", o.\"Email\", o.\"City\", i.\"City\", i.\"State\", i.\"Mayor\", i.\"Inception\" FROM public.\"Contacts\" o INNER JOIN public.\"Cities\" i ON o.\"City\" = i.\"City\"")

    for Firstname, Lastname, Email, City, City, State, Mayor, Inception in cur.fetchall() :
        print (Firstname, Lastname, Email, City)


print ("Using psycopg2…")
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()