import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

requires = ["click"]
tests_requires = ["pytest", "pytest-cache", "pytest-cov"]
lint_requires = ["flake8", "black"]
dev_requires = requires + tests_requires + lint_requires


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="{{cookiecutter.repo_name}}",
    version="00.0.0.0",
    description="{{cookiecutter.description}}",
    long_description="\n\n".join([open("README.rst").read()]),
    license="MIT",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://{{cookiecutter.repo_name}}.readthedocs.org",
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "{{cookiecutter.cli_name}} = {{cookiecutter.package_name}}.cli:main"
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    extras_require={"test": tests_requires, "dev": dev_requires, "lint": lint_requires},
    cmdclass={"test": PyTest},
)
