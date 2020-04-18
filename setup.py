from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='MplRoundedRectangle',
    version='0.1',
    description='Rounded rectangle extention for Matplotlib rectangle pach.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    author='Alexander Marinsek',
    author_email='alexander.marinsek@gmail.com',
    zip_safe=False,
    packages=['MplRoundedRectangle'],
    install_requires=[
        'Matplotlib>=3.2.1'
    ],
    python_requires = '>=3.6'
)
