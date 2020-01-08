from distutils.core import setup
setup(
  name = 'x_rand',
  packages = ['x_rand'],
  version = '0.1',
  license='MIT',
  description = 'Random Problem Creation for edX',
  author = 'Connor Makowski',
  author_email = 'connor.m.makowski@gmail.com',
  url = 'https://github.com/connor-makowski/x_rand',
  download_url = 'https://github.com/connor-makowski/x_rand/archive/v_01.tar.gz',
  keywords = ['x_rand', 'edX', 'randomization', 'random', 'cheating', 'prevention', 'detection'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
  ],
)
