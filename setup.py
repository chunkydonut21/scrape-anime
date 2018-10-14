import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrape_anime",
    version="1.0.0",
    author="Shivam Maheshwari",
    author_email="shivammahe21@gmail.com",
    description="Scrape Anime from Kissanime",
    long_description='Scrapes Anime Details and Anime episodes from Kissanime',
    long_description_content_type="text/markdown",
    url="https://github.com/chunkydonut21/scrape-anime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)