import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-structures",
    version="0.0.1",
    author="Daniel Ng See Cheong",
    author_email="None",
    description="A small package containing basic data structure implementations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ngseecheong/<todo>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    extras_require={
        'docs': [
            'sphinx>=3.2.1',
        ]
    }
)
