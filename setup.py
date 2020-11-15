import pathlib
from setuptools import setup
from AWSOMdesktop import __version__

NAME = "AWSOMdesktop"
URL = f'https://github.com/pfython/{NAME}'
HERE = pathlib.Path(__file__).parent

setup(
  name = NAME,
  # packages = ['NAME'],
  version = __version__,
  license='MIT',
  description = 'Desktop automation tools for managing common tasks such as renaming media files and making backups, as well as interacting with Adobe Premiere Pro using the `Pymiere` library (Windows only).',
  long_description=(HERE / "README.md").read_text(),
  long_description_content_type="text/markdown",
  author = 'Peter Fison',
  author_email = 'peter@southwestlondon.tv',
  url = URL,
  download_url = f'{URL}/archive/v_{__version__}.tar.gz',
  keywords = [NAME, "search", "video", "audio", "media", "AWSOM", "TV", "content", "manage", "organise", "organize", "Premiere", "Adobe", "Pymiere", "YouTube", "metadata", "workflow", "automation", "Creative Cloud", "edit", "editor", "editing"],
  install_requires=['cleverdict'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Multimedia',
    'Topic :: Multimedia :: Video',
    'Topic :: Multimedia :: Video :: Non-Linear Editor',
  ],
)

# Run the following from the command prompt:

# python -m pip install setuptools wheel twine
# python setup.py sdist
# python -m twine upload --repository testpypi dist/*
# python -m twine upload --repository pypi dist/*
