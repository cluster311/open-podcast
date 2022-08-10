# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# ? from openpodcast import __VERSION__


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "src/openpodcast/__init__.py"), encoding="utf-8") as f:
    init = f.read()
    for line in init.splitlines():
        if line.startswith("__VERSION__"):
            delim = '"' if '"' in line else "'"
            VERSION = line.split(delim)[1]


setup(
    name="""openpodcast""",
    version=VERSION,
    description="""A general open podcasts library""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cluster311/open-podcast",
    author="""Cluster 311""",
    author_email="""cluster311@gmail.com""",
    license="AGPL",
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="""podcast""",
    packages=find_packages("src", exclude=["tests", "docs"]),
    package_dir={"": "src"},
    install_requires=[],
)
