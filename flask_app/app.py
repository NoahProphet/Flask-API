from flask import Flask, request , jsonify
import psycopg2

# Create a Flask app
server = Flask(__name__)

# Connect to the database using psycopg2 library and the database credentials
conn = psycopg2.connect(
	host="db",
	database="test",
	user="test",
	password="test"
)

# Root route


@server.route('/', methods=['GET'])
def hello_world():
	return 'Hello, World!'


@server.route('/create', methods=['POST'])
def create():
    # Get the username and email from the request body
    username = request.form.get('username')
    email = request.form.get('email')

    # Validate input
    if not username or not email:
        return jsonify({"error": "Username and email are required!"}), 400

    try:
        # Insert the data into the database
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
        conn.commit()
        cur.close()

        return jsonify({"message": "User created successfully!"}), 201
    except psycopg2.Error as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

@server.route('/select', methods=['GET'])
def select():
    cur = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM users;"
    cur.execute(postgreSQL_select_Query) 
    users = cur.fetchall()
    if users:
        result = []
        for user in users:
            result.append({"ID": user[0], "UserName": user[1], "Email": user[2]})
        return jsonify(result)
    else:
        return jsonify({"error": f"Users not found."}), 404
        
    
    

    


