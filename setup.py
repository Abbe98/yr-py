from distutils.core import setup
setup(
  name = 'yr',
  packages = ['yr'], # this must be the same as the name above
  install_requires=['lxml'],
  version = '0.4',
  description = 'Wrapper for the YR.no API, for near time weather prediction.',
  author = 'Albin Larsson',
  author_email = 'albin.post@gmail.com',
  url = 'https://github.com/Abbe98/yr-py', # use the URL to the github repo
  download_url = 'https://github.com/Abbe98/yr-py/tarball/0.4', # I'll explain this in a second
  keywords = ['weather', 'yr', 'yr.no'], # arbitrary keywords
  classifiers = [],
)