#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name="python-git-version",
	version="1.0",
	description="Provides helpers to annotate version numbers in git-controlled packages.",
	author="Caramel",
	url="http://www.caramel.com.au/",
	license="MIT",
	requires=(
	),
	
	packages=find_packages(),
	zip_safe=True,
	
	entry_points = {
	},
	
	classifiers=[
		'Intended Audience :: Software Developers',
	],
	
)

