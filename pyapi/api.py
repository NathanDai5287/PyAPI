import requests
import json

class Api:
	def __init__(self, base: str, **kwargs):
		self.base = base
		self.parameters = kwargs

	@property
	def url(self):
		url = self.base + '?'
		for key, value in self.parameters.items():
			url += str(key) + '=' + str(value) + '&'

		return url[:-1]

	def __getitem__(self, key):
		return self.parameters[key]

	def __setitem__(self, key, value):
		self.parameters[key] = value

	def call(self):
		response = requests.get(self.url).text

		return json.loads(response)
