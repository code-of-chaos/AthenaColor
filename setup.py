# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import setuptools

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AthenaColor",
    version="2.0.0",
    author="Andreas Sas",
    author_email="",
    description="A little package which allows you to use ANSI codes to print color to the console.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DirectiveAthena/AthenaColor",
    project_urls={
        "Bug Tracker": "https://github.com/DirectiveAthena/AthenaColor/issues",
    },
    license="GPLv3",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7"
)