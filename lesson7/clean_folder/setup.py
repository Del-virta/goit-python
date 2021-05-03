from setuptools import setup, find_packages

setup(
    name = "clean_folder",
    version = "1.0"
    entry_points = {
        'console_scripts': ['clean-folder=clean_folder.clean:main']
    }
    author='Delvirta',
    url='http://github.com/dummy_user/useful',
    author_email='delvirta@gmail.com',
    zip_safe = False
    packages = find_packages()
    include_package_data = True
    description = "Clean folder script"
    )