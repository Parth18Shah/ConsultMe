import db_conn
con = db_conn.connect()

def insert_records(choice,form_values):
    if(choice== 'patient'):
        addquery = '''
                INSERT INTO users (username,u_name,gender,email_id,mobileno,dob,age,med_history,pswd,ispatient)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
    else:
        addquery = '''
                INSERT INTO users (username,u_name,gender,specialist,reg_no,year_reg,email_id,mobileno,pswd,ispatient)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
    try:
        mycursor = con.cursor()
        given_val = tuple(form_values)
        mycursor.execute(addquery, given_val)
        con.commit()
        return 1
        
    except Exception as ex:
        return ex

def fetch_details(username):
    try:
        mycursor = con.cursor()
        searchquery = '''
                    SELECT username,email_id,pswd 
                    FROM users 
                    WHERE username = %s
                    '''
        mycursor.execute(searchquery, (username,))
        records = mycursor.fetchone()
        return records
        
    except Exception as ex:
        return ex