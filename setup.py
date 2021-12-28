from distutils.core import setup
setup(
  name = 'drps',         # How you named your package folder (MyLib)
  packages = ['drps'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "A module that aim to make it faster to start your fullstack project with few inputs in short time.Also all neccessary modules are supplied within starting the project.",   # Give a short description about your library
  author = 'Ghazi',                   # Type in your name
  author_email = 'ghazi-z3balawi@putlook.com',      # Type in your E-Mail
  url = 'https://github.com/ghazigamer/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ghazigamer/Django-React-Project-Setup/archive/refs/tags/v_01.zip',    # I explain this later on
  keywords = ['Project', 'Setup', 'For',"Django","And","React"],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'django',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',
  ],
)