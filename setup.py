import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyTAPI",
    version="0.0.6",
    author="Teddy Morduhovich",
    author_email="swizex@gmail.com",
    description="a general purpose/random stuff api i made for myself",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swizex/pyTAPI",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)