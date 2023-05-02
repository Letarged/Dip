from setuptools import setup, find_packages

setup(
    name='MasterThesis',
    version='0.1.0',
    author='Michal Rajecký',
    author_email='xrajec01@fit.vutbr.cz',
    packages=find_packages(),
    install_requires=[
        'docker_py==1.10.6',
        'firebase_admin==6.1.0'
        'netifaces==0.11.0',
        'termcolor==2.3.0',
        'xmltodict==0.12.0'
    ],
    entry_points={
        'console_scripts': [
            'diplomka=p:main'
        ]
    }
)
