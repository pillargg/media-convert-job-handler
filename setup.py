import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
setup(
    name = "mediaconvert-job-constructor",
    version = "0.0.1",
    author = "Chandler Lofland",
    author_email = "chandler@pillar.gg",
    description = ("A tool for constructing AWS MediaConvert jobs"),
    license = "AGPL-3.0",
    keywords = "aws mediaconvert media convert",
    url = "https://github.com/pillargg/media-convert-job-handler",
    packages=['mediaconvert_job_constructor'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Framework :: AWS CDK",
        "Operating System :: OS Independent"
    ],
)
