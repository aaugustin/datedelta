import os

import setuptools

# Avoid polluting the .tar.gz with ._* files under Mac OS X
os.putenv('COPYFILE_DISABLE', 'true')

# Prevent distutils from complaining that a standard file wasn't found
README = os.path.join(os.path.dirname(__file__), 'README')
if not os.path.exists(README):
    os.symlink(README + '.rst', README)

description = "Like datetime.timedelta, for date arithmetic."

with open(README) as f:
    long_description = '\n\n'.join(f.read().split('\n\n')[1:])

setuptools.setup(
    name='datedelta',
    version='1.1',
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    url='https://github.com/aaugustin/datedelta',
    description=description,
    long_description=long_description,
    download_url='http://pypi.python.org/pypi/datedelta',
    py_modules=['datedelta'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    platforms='all',
    license='BSD'
)
