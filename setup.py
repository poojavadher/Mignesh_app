from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mignesh_custom/__init__.py
from mignesh_custom import __version__ as version

setup(
	name="mignesh_custom",
	version=version,
	description="Mignesh Petrochem",
	author="Sanskartechnolab",
	author_email="pooja@sanskartechnolab.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
