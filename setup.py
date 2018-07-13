from setuptools import setup

setup(
  name = 'bimap',
  packages = ['bimap'],
  version = '0.1.1',
  description = 'Container similar to boost bimap',
  author = 'Sushobhit',
  author_email = 'sushobhitsolanki@gmail.com',
  url = 'https://github.com/sushobhit27/bimap',
  download_url = 'https://github.com/sushobhit27/bimap/archive/0.1.tar.gz',
  keywords = ['container', 'bimap', 'bidict', 'boost'], # arbitrary keywords
  classifiers = [
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: Implementation :: CPython',
      'Operating System :: Microsoft',
      'Operating System :: Microsoft :: Windows :: Windows 7',
      'Operating System :: Unix',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Utilities',
      'Intended Audience :: Developers',
      ],
  install_requires = [
      'multiindex >= 0.2.0',
      ]
)
