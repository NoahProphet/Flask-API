from flask import Flask, request , jsonify
import models, serilizers
# Create a Flask app
server = Flask(__name__)



@server.route('/', methods=['GET'])
def hello_world():
	return 'Hello, World!'


@server.route('/create/', methods=['POST'])
def create():
	serilizer = serilizers.UserSerilizers(input=request.data)
	if serilizer.create():
		return 'User created successfully!', 201
	return 'Creation error!', 400

@server.route('/list-create/', methods=['POST'])
def list_create():
	serilizer = serilizers.UserSerilizers(input=request.data, many=True)
	if serilizer.create():
		return 'User created successfully!', 201
	return 'Creation error!', 400

@server.route('/list/', methods=['GET'])
def list():
	username = request.args.get('username')
	email = request.args.get('email')
	id = request.args.get('id')
	filters = {}
	if username:
		filters.update({"UserName":username})
	if email:
		filters.update({"Email":email})
	if id:
		filters.update({"ID":id})

	if email or username or id:
		users = models.User.filter(**filters)
	else:
		users = models.User.all()

	if users:
		serilizer = serilizers.UserSerilizers(input=users, many=True)
		return jsonify(serilizer.data), 200
	else:
		return jsonify({"error": f"Users not found."}), 404
    
    
@server.route('/detail/<user_id>/', methods=['GET'])
def detail(user_id):
	try:
		user = models.User.get(id=user_id)
		result = serilizers.UserSerilizers(input=user).data
		return jsonify(result), 200
	except:
		return jsonify({"error": f"Users not found."}), 404