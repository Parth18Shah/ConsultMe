import mysql.connector as mysql

def connect():
	try:
		con = mysql.connect(user='root', password="root", host='127.0.0.1', port='3307', database='consultme')
		status = str(con.is_connected())
		# mycursor = con.cursor()
        # query = """
        # CREATE TABLE users (
        # username varchar(20) unique not null,
        # u_name varchar(20),
        # pswd varchar(20),
        # mobileno varchar(10) not null,
        # email_id varchar(50) not null,
        # gender varchar(10),
        # specialist varchar(50),
        # reg_no varchar(50),
        # year_reg date,
        # dob date,
        # age INT,
        # med_history VARCHAR(255),
        # ispatient BIT not null
        # );
        # """
        # mycursor.execute(query)
        # con.commit()
		if status == "True":
			return con
		
	except Exception as e:
		print("Connection Error : ", e)
		exit()

