import os.path

import setuptools

root_dir = os.path.abspath(os.path.dirname(__file__))

description = "Like datetime.timedelta, for date arithmetic."

with open(os.path.join(root_dir, 'README.rst')) as f:
    long_description = f.read()

setuptools.setup(
    name='datedelta',
    version='1.2',
    description=description,
    long_description=long_description,
    url='https://github.com/aaugustin/datedelta',
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    py_modules=[
        'datedelta',
    ],
)
