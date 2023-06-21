from setuptools import setup

setup(
    name='hello-world-python',
    version='1.0.0',
    url='https://github.com/yourusername/myprogram',
    author='Daniel Wärnelov',
    author_email='daniel.pean@gmail.com',
    py_modules=['helloworld'],
    entry_points={
        'console_scripts': [
            'helloworld=helloworld:main',
        ],
    },
    # packages=['helloworld']
)