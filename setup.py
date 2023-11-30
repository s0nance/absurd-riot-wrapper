import re
from setuptools import setup, find_packages
import os.path

source_folder = "absurdriotwrapper"
cwd = os.path.dirname(__file__)
long_description = os.path.join(cwd, "README.md")

with open(f"{source_folder}/__version__.py", "r") as version_file:
    version_content = version_file.read()

with open(long_description, encoding="utf8") as long_description_file:
    long_description = long_description_file.read()

version_match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", version_content)
if version_match:
    version = version_match.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {source_folder}/__version__.py")

setup(
    name='absurd-riot-wrapper',
    version=version,
    packages=find_packages(source_folder, exclude=["test"]),
    install_requires=["requests"],
    license='MIT License',
    author="AbsurdTeam",
    long_description_content_type='text/markdown',
    long_description=long_description,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.10',
    ],
)
