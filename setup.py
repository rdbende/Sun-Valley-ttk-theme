from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="sv_ttk",
    version="2.3",
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
    packages=["sv_ttk"],
    package_data={"sv_ttk": ["sv.tcl", "theme/*"]},
    python_requires=">=3.4",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
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
