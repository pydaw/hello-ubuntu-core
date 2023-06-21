from setuptools import setup

setup(
    name='helloworld',
    version='1.0.0',
    url='https://github.com/yourusername/myprogram',
    author='Daniel Wärnelov',
    author_email='daniel.pean@gmail.com',
    py_modules=['hello-world'],
    entry_points={
        'console_scripts': [
            'helloworld=helloworld:main',
        ],
    },
    # packages=['helloworld']
)