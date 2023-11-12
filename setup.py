from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pos_advance/__init__.py
from pos_advance import __version__ as version

setup(
	name="pos_advance",
	version=version,
	description="POS APP",
	author="beshoyatef31@gmail.com",
	author_email="beshoyatef31@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
