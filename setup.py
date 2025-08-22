from setuptools import setup, find_packages

setup(
    name="penwiz",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],  # add dependencies here
    entry_points={
        "console_scripts": [
            "penwiz=penwiz.main:main",
        ],
    },
)
