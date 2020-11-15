import pathlib
from setuptools import setup
# from distutils.core import setup
from awsomdesktop import __version__
from awsomdesktop import __name__

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
  name = '__name__',
  packages = ['__name__'],
  version = __version__,
  license='MIT',
  description = 'A data structure which allows both object attributes and dictionary keys and values to be used simultaneously and interchangeably.',
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Peter Fison',
  author_email = 'peter@southwestlondon.tv',
  url = f'https://github.com/pfython/{__name__}',
  download_url = f'https://github.com/pfython/{__name__}/archive/v_0.1.tar.gz',
  keywords = [__name__, "search", "video", "audio", "media", "AWSOM", "TV", "content", "manage", "organise", "organize", "Premiere", "Adobe", "Pymiere", "YouTube", "metadata", "workflow", "automation", "Creative Cloud", "edit", "editor", "editing"],
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
# python setup.py sdist
# python -m twine upload --repository testpypi dist/*
# python -m twine upload --repository pypi dist/*
