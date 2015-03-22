#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import os
import sys
import codecs


try:
	from setuptools.core import setup, find_packages
except ImportError:
	from setuptools import setup, find_packages

from setuptools.command.test import test as TestCommand


if sys.version_info < (2, 7):
	raise SystemExit("Python 2.7 or later is required.")
elif sys.version_info > (3, 0) and sys.version_info < (3, 3):
	raise SystemExit("Python 3.3 or later is required.")

exec(open(os.path.join("web", "blueprint", "release.py")).read())


class PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		
		self.test_args = []
		self.test_suite = True
	
	def run_tests(self):
		import pytest
		sys.exit(pytest.main(self.test_args))


here = os.path.abspath(os.path.dirname(__file__))

tests_require = [
		'pytest',  # test collector and extensible runner
		'pytest-cov',  # coverage reporting
		'pytest-flakes',  # syntax validation
		'pytest-cagoule',  # intelligent test execution
		'pytest-spec',  # output formatting
	]


setup(
	name = "WebCore",
	version = version,
	
	description = description,
	long_description = codecs.open(os.path.join(here, 'README.rst'), 'r', 'utf8').read(),
	url = url,
	download_url = 'http://s.webcore.io/aIly',
	
	author = author.name,
	author_email = author.email,
	
	license = 'MIT',
	keywords = '',
	classifiers = [
			"Development Status :: 5 - Production/Stable",
			"Environment :: Console",
			"Environment :: Web Environment",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python",
			"Programming Language :: Python :: 2",
			"Programming Language :: Python :: 2.6",
			"Programming Language :: Python :: 2.7",
			"Programming Language :: Python :: 3",
			"Programming Language :: Python :: 3.2",
			"Programming Language :: Python :: 3.3",
			"Programming Language :: Python :: 3.4",
			"Programming Language :: Python :: Implementation :: CPython",
			"Programming Language :: Python :: Implementation :: PyPy",
			"Topic :: Internet :: WWW/HTTP :: WSGI",
			"Topic :: Software Development :: Libraries :: Python Modules",
		],
	
	packages = find_packages(exclude=['bench', 'docs', 'example', 'test']),
	include_package_data = True,
	namespace_packages = [
			'web',  # primary namespace
			'web.blueprint',  # quick-start templates
		],
	
	entry_points = {
			'marrow.blueprint': [
					# Core
					'webcore.small = web.blueprint.small:SmallBlueprint',  # small collection of files
					'webcore.medium = web.blueprint.medium:MediumBlueprint',  # lightly structured application
					'webcore.large = web.blueprint.large:LargeBlueprint',  # full MVC separation and structure
					
					# Contentment
					# single deployable application, fully dynamic; development and small sites
					'contentment.solo = web.blueprint.contentment.solo:SoloBlueprint',
					# local write, static read application; blogs and GitHub Pages
					'contentment.static = web.blueprint.contentment.static:StaticBlueprint',
					# dynamic write, static read application; high-availability, large-scale applications
					'contentment.hybrid = web.blueprint.contentment.hybrid:HybridBlueprint',
				],
		},
	
	install_requires = [
			'web.template<3.0.0',  # extensible template engine support
			'marrow.package<2.0',  # dynamic execution and plugin management
			'pyyaml',  # rich data interchange format; used for configuration
		],
	
	extras_require = dict(
			development = tests_require,
		),
	
	tests_require = tests_require,
	
	dependency_links = [],
	
	zip_safe = True,
	cmdclass = dict(
			test = PyTest,
		)
)
