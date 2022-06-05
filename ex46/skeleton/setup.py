try:
	from setuptools import setup
except ImportError:
	from distutils import setup

config = {
	'name' : 'Project Name',
	'description' : 'My Project',
	'author' : 'Ratul Sharker',
	'url' : 'Url to get it at',
	'download_url' : 'Where to download it.',
	'author_email' : 'sharker.ratul.08@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : []
}

setup(**config)