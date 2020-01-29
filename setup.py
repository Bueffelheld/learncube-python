import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="learncube",
    version="0.0.1",
    author="Fabian Riewe",
    author_email="f.riewe@bueffelehld.de",
    description="A Python wrapper for the Learncube API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bueffelheld/learncube-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
