"""


"""

__all__ = [
	'get',
	'get_git_version'
]

from subprocess import Popen, PIPE
from os.path import join

def pep386_adapt(version):
	"""
	Adapt git-describe version to be in line with PEP 386.
	By ilogue: https://gist.github.com/2567778

	"""
	if version != None and '-' in version:
		parts = version.split('-')
		parts[-2] = 'post'+parts[-2]
		version = '.'.join(parts[:-1])

	return version


def git_describe():
	try:
		p = Popen(['git', 'describe'], stdout=PIPE, stderr=PIPE)
		p.stderr.close()
		
		return p.stdout.readline().strip()
	except:
		return None


def get_release_identifier(package):
	"""
	Reads the release identifier from the package/version.py file.
	
	"""
	
	version = None
	
	try:
		pkg = __import__('%s.version' % package)
		version = pkg.version.VERSION
	except:
		pass
	
	return version


def set_release_identifier(package, version):
	"""
	Writes the release identifier file.
	
	"""
	with open(join(package, 'version.py'), 'wb') as f:
		f.write("""#!/usr/bin/env python
# THIS FILE IS GENERATED AUTOMATICALLY BY PYTHON-GIT-VERSION.
# ALL CHANGES TO THIS FILE WILL BE OVERWRITTEN BY A TOOL.

VERSION = %r
""" % version)


def get_git_version(package):
	"""
	Gets the release version from git and version.py, overwriting
	.release_version if there is better information in it.
	
	"""
	release_identifier = get_release_identifier(package)
	version = pep386_adapt(git_describe())
	
	if version == None:
		version = release_identifier
	
	if version == None:
		raise ValueError("No version number from git or version.py!")
	
	if release_identifier != version:
		set_release_identifier(package, version)
	
	return version

get = get_git_version

