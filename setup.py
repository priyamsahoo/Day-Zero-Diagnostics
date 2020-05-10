from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='healthoslib',
    version='1.0.0',
    description='Welcome to HealthOS API!   HealthOS allows you to create world class healthcare applications, leveraging our data source of medicines (generics and branded), food items (with nutrition value), various excercises and physical activities, lab tests, diseases etc.  The API is organized around REST. All requests should be made over SSL. All request and response bodies, including errors, are encoded in JSON.',
    long_description=long_description,
    author='Shahid Khaliq',
    author_email='shahid.khaliq@apimatic.io',
    url='https://apimatic.io/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)