from setuptools import setup, find_packages

setup(
    name='Example',
    version='1.0',
    description='Python Example Project',
    author='Samuel Krieg',
    author_email='sikcd90@gmail.com',
    install_requires=['bar', 'greek'], #external packages as dependencies
    url='https://github.com/develmusa/PythonTemplateProject',
    license=license,
    packages=find_packages(exclude=('tests'))
)