from setuptools import setup, find_packages

with open('README.md') as f:
	readme = f.read()

setup_args = {
	'name': 'PyAutoWebAPI',
	'version': '0.0.1',
	'description': 'A simple way to call APIs from Python',
	'long_description_content_type': 'text/markdown',
	'long_description': readme,
	'license': 'MIT',
	'packages': find_packages(),
	'author': 'Nathan Dai',
	'author_email': 'nathandai2000@gmail.com',
	'keywords': ['API', 'PyAutoWebAPI', 'web API'],
	'url': 'https://github.com/NathanDai5287/PyAutoWebAPI',
	'download_url': 'https://pypi.org/project/pyautowebapi/',
}

install_requires = [
	'requests',
]

if __name__ == '__main__':
	setup(**setup_args, install_requires=install_requires)
