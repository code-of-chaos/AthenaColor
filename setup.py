# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import setuptools

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def readme_handler() -> str:
    with open("README.md", "r") as readme_file:
        return readme_file.read()

def version_handler() -> str:
    # ------------------------------------------------------------------------------------------------------------------
    version = 7,0,2 # <-- DEFINE THE VERSION IN A TUPLE FORMAT HERE
    # ------------------------------------------------------------------------------------------------------------------
    version_str = ".".join(str(i) for i in version)

    return version_str

# ----------------------------------------------------------------------------------------------------------------------
# - Actual Setup -
# ----------------------------------------------------------------------------------------------------------------------
setuptools.setup(
    name="AthenaColor",
    version=version_handler(),
    author="Andreas Sas",
    author_email="",
    description="Package to support full usage of RGB colors in the console",
    long_description=readme_handler(),
    long_description_content_type="text/markdown",
    url="https://github.com/DirectiveAthena/AthenaColor",
    project_urls={
        "Bug Tracker": "https://github.com/DirectiveAthena/AthenaColor/issues",
    },
    license="GPLv3",
    package_data={"": ["py.typed"]},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Terminals"
    ]
)
