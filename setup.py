import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
read_file = lambda filename: open(os.path.join(here, filename)).read()
read_requirements = lambda filename: read_file(filename).splitlines()

# Stops exit traceback on tests
try:
    import multiprocessing
except:
    pass

test_requirements = [
    'nose'
]

setup(
    name='Flask-MongoRest',
    version='0.1.1',
    url='http://github.com/elasticsales/flask-mongorest',
    license='BSD',
    author='Anthony Nemitz',
    author_email='anemitz@gmail.com',
    maintainer='Anthony Nemitz',
    maintainer_email='anemitz@gmail.com',
    description='Flask restful API framework for MongoDB/MongoEngine',
    long_description=read_file('README.md'),
    packages=[
        'flask_mongorest',
    ],
    package_data={
        'flask_mongorest': ['templates/mongorest/*']
    },
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=read_requirements('requirements.txt'),
    tests_require=test_requirements,
    extras_require={'test': test_requirements},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
