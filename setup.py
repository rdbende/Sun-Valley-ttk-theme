import re
from pathlib import Path

from setuptools import setup


long_description = re.sub(
    r"(?s)<picture>.*</picture>",
    '<img alt="Cover image" src="https://raw.githubusercontent.com/rdbende/Sun-Valley-ttk-theme/master/assets/hero_light.png">',
    (Path(__file__).parent / "README.md").read_text(),
)


setup(
    name="sv_ttk",
    version="2.4.5",
    license="MIT",
    author="rdbende",
    author_email="rdbende@gmail.com",
    url="https://github.com/rdbende/Sun-Valley-ttk-theme",
    project_urls={
        "Source": "https://github.com/rdbende/Sun-Valley-ttk-theme",
        "Documentation": "https://github.com/rdbende/Sun-Valley-ttk-theme/wiki",
        "Tracker": "https://github.com/rdbende/Sun-Valley-ttk-theme/issues",
    },
    description="A gorgeous theme for Tkinter, based on Windows 11's UI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_packages=["sv_ttk"],
    package_data={"sv_ttk": ["sv.tcl", "theme/*"]},
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
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
        "dark-theme",
        "modern",
        "sun-valley",
        "tcl",
        "tcl/tk",
        "theme",
        "theme",
        "tile",
        "tk",
        "tkinter",
        "ttk",
        "windows-11",
        "winui",
    ],
)
