import tornado.web
from tornado.escape import json_encode
from database import db_session
from models import User
from helpers import facebook

# Person Handler
class Person(tornado.web.RequestHandler):
	def get(self, limit=None):
		# Check if has argument 'limit', else, set None
		limit = limit or self.get_argument('limit', None)
		# Init the result list
		results = []
		# Fetch data from database
		users = db_session.query(User).limit(limit).all()

		# If has results, append to results list
		if users:
			for i in users:
				results.append(i.to_json())

		self.write(json_encode(results))

	def post(self,facebook_id=None):
		# Get facebook ID
		facebook_id = facebook_id or self.get_argument('facebookId', None)

		# If not isset facebook ID
		if not facebook_id or not facebook_id > 0:
			raise tornado.web.HTTPError(500, "A Facebook ID is required.")

		# Check if ID exists in database
		check = db_session.query(User).get(facebook_id)
		# If this ID doesn't exist, add it
		if not check:
			# Instantiate the Facebook API helper passing the user ID
			fbAPI = facebook.FacebookAPI(int(facebook_id))
			# Get user data
			user_data = fbAPI.getUserData()

			if not user_data:
				raise tornado.web.HTTPError(500, "Error while inserting data.")

			# Create the User object
			user = User(id=user_data['id'], name=user_data['name'])
			# Add object to session
			db_session.add(user)

			try:
				# Try to commit changes
				db_session.commit()
			except Exception, e:
				raise tornado.web.HTTPError(500, "Error while inserting data.")

		self.set_status(201)

	def delete(self, facebook_id):
		# Get facebook ID
		facebook_id = facebook_id or self.get_argument('facebookId', None)

		# If not isset facebook ID
		if not facebook_id or not facebook_id > 0:
			raise tornado.web.HTTPError(500, "A Facebook ID is required.")
		
		# Check if ID exists in database
		get_user = db_session.query(User).get(facebook_id)

		# If this ID doesn't exist, add it
		if get_user:
			# Delete the user in session
			db_session.delete(get_user)

			try:
				# Try to commit changes
				db_session.commit()
			except Exception, e:
				raise tornado.web.HTTPError(500, "Error while inserting data.")

		self.set_status(204)

