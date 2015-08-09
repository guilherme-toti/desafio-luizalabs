import tornado.web
from tornado.httpclient import HTTPClient
import json

class FacebookAPI():
	def __init__(self, user_id):
		# User ID passed by parameter
		self.id = user_id
		# Access Token to use Facebook API
		self.access_token = "CAAIw5GTJv48BAEUrheMZAEP4ila8bc9vnlJ5wZAD4LGpLPy29GZCTash87ClHIUXnN1bJZCVQ9NCnd9HIZC28g6JzKILzrrRSMcx2VfxwqqaZCfwlo4Wh1rqCaLifJUkIoxLzSS8oLco6LfSjSzr0pr4JewC9m2KeGYsoJWOlmzba7I1QVorVXiL34cdFvy7gZD"
		# Mount request URL
		self.request_url = "https://graph.facebook.com/%d?fields=id,name&access_token=%s" % (self.id, self.access_token)

	def getUserData(self):
		# instantiate the HTTPClient
		client = HTTPClient()
		# Start data as None
		data = None

		# Try to get data from Facebook API
		try:
			# Fetch URL
			response = client.fetch(self.request_url)
			# Get data as JSON
			data = json.loads(response.body)
		except Exception, e:
			# If some error, redirect to 500
			raise tornado.web.HTTPError(500, "Error while getting Facebook information.")
		finally:
			# Close
			client.close()

		# Return JSON with data or None
		return data