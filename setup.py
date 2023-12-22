import os
from typing import List

from setuptools import find_packages, setup

_pkg: str = "amazon-sagemaker-tsp-deep-rl"
_version: str = "0.0.1"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Declare minimal set for installation
required_packages: List[str] = []

setup(
    name=_pkg,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version=_version,
    description="Solving the Travelling Salesperson Problem with deep reinforcement learning on Amazon SageMaker",
    long_description=read("README.md"),
    author="Amazon Web Services",
    url=f"https://github.com/aws-samples/{_pkg}/",
    project_urls={
        "Bug Tracker": f"https://github.com/aws-samples/{_pkg}/issues/",
        "Documentation": "https://aws.amazon.com/blogs/opensource/solving-the-traveling-salesperson-problem-with-deep-reinforcement-learning-on-amazon-sagemaker/",
        "Source Code": f"https://github.com/aws-samples/{_pkg}/",
    },
    license="MIT License",
    keywords="Reinforcement Learning",
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6.0",
    install_requires=required_packages,
)