import os

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

this = os.path.dirname(os.path.realpath(__file__))

def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()
setup(
    name='hello-world',
    version='0.0.1',
    description='description',
    long_description=readme,
    author='Daniel Wärnelov',
    author_email='daniel.pean@gmail.com',
    url='https://github.com/gocarlos/python-ubuntu-snap-app-example',
    packages=['packages'],
    install_requires=read('requirements.txt'),
    include_package_data=True,
    zip_safe=True,
    licence='MIT',
    keywords='Simple example of python snap',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English'
    ],
    test_suite='tests',
    scripts=['src/hello-world']S
)