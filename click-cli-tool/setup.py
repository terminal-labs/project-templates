from setuptools import setup
setup (
  name = "click-cli",
  packages=['app'],
  install_requires=[
  'click',
  'requests',
  ],
  entry_points='''
      [console_scripts]
      click-cli=app.main:main
  '''
)
