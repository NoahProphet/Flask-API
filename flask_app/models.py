import psycopg2
conn = psycopg2.connect(
	host="db",
	database="test",
	user="test",
	password="test"
)

class User():

    def __init__(self, data):
        self.ID = data[0]
        self.UserName =  data[1]
        self.Email = data[2]
        
    def serilizer(self):
        return({"ID": self.ID, "UserName": self.UserName, "Email": self.Email})
    
    
    def create(username, email):
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
            conn.commit()
            return True
        except:
            return False
        
    def all():
        try:
            cur = conn.cursor()
            postgreSQL_select_Query = "SELECT * FROM users;"
            cur.execute(postgreSQL_select_Query) 
            users = cur.fetchall()
            return users
        except:
            return []
        
    def get(id: int):
        try:
            cur = conn.cursor()
            postgreSQL_select_Query = f"SELECT * FROM users WHERE ID={id};"
            cur.execute(postgreSQL_select_Query) 
            users = cur.fetchall()
            return users[0]
        except:
            raise ValueError()
        
    def filter(ID=None, UserName=None, Email=None):
        try:
            
            where = ""
            if ID:
                where += "ID="+str(ID)
            if UserName:
                where += " , " if len(where)>0 else ""
                where += "UserName="+str(UserName)
            if Email:
                where += " , " if len(where)>0 else ""
                where += "Email="+str(Email)
            
            cur = conn.cursor()
            postgreSQL_select_Query = f"SELECT * FROM users WHERE {where};"
            cur.execute(postgreSQL_select_Query) 
            users = cur.fetchall()
            return users[0]
        except:
            raise ValueError()