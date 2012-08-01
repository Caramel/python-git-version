#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name="python-git-version",
	version="1.0",
	description="Provides helpers to annotate version numbers in git-controlled packages.",
	author="Michael Farrell",
	author_email="michael@uanywhere.com.au",
	url="http://www.uanywhere.com.au/",
	license="",
	requires=(
	),
	
	packages=find_packages(),
	
	entry_points = {
	},
	
	classifiers=[
		'Intended Audience :: Software Developers',
	],
	
)

