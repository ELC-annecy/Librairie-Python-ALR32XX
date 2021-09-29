import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Library_ALR32XX",
    version="0.0.4",
    author="elc-construction-electronique",
    author_email="be@elc.fr",
    description="Ce module permet de commander via liaison série les alimentations programmables ALR32XX de ELC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX",
    project_urls={
        "Bug Tracker": "https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["ALR32XX"],
    python_requires=">=3.6",
)
