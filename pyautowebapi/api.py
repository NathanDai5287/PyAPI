import requests
import json

class Api:
	def __init__(self, base: str, form: str='json', **kwargs):
		"""generates a url for the api given the base url and the parameters

		Args:
				base (str): base url without trailing slash or question mark
				form (str): format of the response (json or text). Defaults to json
		"""

		self.base = base.rstrip('?').rstrip('/')
		self.parameters = kwargs

		assert form in ['json', 'text'], 'Invalid form.Must be json or text'

		self.form = form

	@property
	def url(self):
		url = self.base + '?'
		for key, value in self.parameters.items():
			url += str(key) + '=' + str(value) + '&'

		return url[:-1]

	def __repr__(self) -> str:
		return self.url

	def __getitem__(self, key):
		return self.parameters[key]

	def __setitem__(self, key, value):
		self.parameters[key] = value

	def call(self):
		response = requests.get(self.url).text

		if self.form == 'json':
			try:
				return json.loads(response)
			except json.decoder.JSONDecodeError:
				print('Invalid JSON, defaulting to text response.')
				return response

		elif self.form == 'text':
			return response
