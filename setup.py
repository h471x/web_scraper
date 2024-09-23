from setuptools import setup, find_packages

setup(
    name='pyscrap-tool',
    version='0.1',
    description='A CLI tool for web scraping',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hatix Ntsoa',
    author_email='hatixntsoa@gmail.com',
    url='https://github.com/h471x/web_scraper',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyscrap=pyscrap.app.main:main',
        ],
    },
)