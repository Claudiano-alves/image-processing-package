from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
with open("README.md", "r") as f:
    requiremenets = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Claudiano",
    description="image Processing Packege using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)
    