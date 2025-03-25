import re
import setuptools
from pathlib import Path

# Read version dynamically from a _version.py file
version_file = Path(__file__).parent / "sv_ttk" / "_version.py"
version_globals = {}
exec(version_file.read_text(), version_globals)
version = version_globals["__version__"]

# Read and modify long description
long_description = re.sub(
    r"(?s)<picture>.*</picture>",
    '<img alt="Cover image" src="https://raw.githubusercontent.com/rdbende/Sun-Valley-ttk-theme/master/assets/hero_light.png">',
    (Path(__file__).parent / "README.md").read_text(),
)

setuptools.setup(
    name="sv_ttk",
    version=version,  # Dynamically retrieved version
    license="MIT",
    author="rdbende",
    author_email="rdbende@proton.me",
    url="https://github.com/rdbende/Sun-Valley-ttk-theme",
    project_urls={
        "Source": "https://github.com/rdbende/Sun-Valley-ttk-theme",
        "Documentation": "https://github.com/rdbende/Sun-Valley-ttk-theme/wiki",
        "Tracker": "https://github.com/rdbende/Sun-Valley-ttk-theme/issues",
    },
    description="A gorgeous theme for Tkinter, based on Windows 11's UI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=["sv_ttk", "sv_ttk.*"]),  # Dynamically include package data
    package_data={"sv_ttk": ["*.tcl", "theme/*", "py.typed"]},
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Tcl",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "sv-ttk",
        "tcl",
        "tcl/tk",
        "theme",
        "tile",
        "tk",
        "ttk",
        "tkinter",
        "modern",
        "fluent",
        "dark-theme",
        "sun-valley",
        "windows-11",
        "winui",
    ],
)
