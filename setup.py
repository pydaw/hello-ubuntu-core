from setuptools import setup

setup(
    name='helloworld',
    version='1.0.0',
    url='https://github.com/yourusername/myprogram',
    author='Daniel Wärnelöv',
    author_email='daniel.pean@gmail.com',
    packages=['src'],
    # include_package_data=True,
    entry_points={
        'console_scripts': [
            'helloworld=src.helloworld:main',
        ],
    },
)