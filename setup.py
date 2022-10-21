from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'x_rand',
  packages = ['x_rand','x_rand2'],
  version = '0.12',
  license='MIT',
  description = 'Random Problem Creation for edX',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Connor Makowski',
  author_email = 'connor.m.makowski@gmail.com',
  url = 'https://github.com/connor-makowski/x_rand',
  download_url = 'https://github.com/connor-makowski/x_rand/blob/master/dist/x_rand-0.12.tar.gz',
  keywords = ['x_rand', 'edX', 'randomization', 'random', 'cheating', 'prevention', 'detection'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  install_requires=[
          'random2>=1',
      ],
)
