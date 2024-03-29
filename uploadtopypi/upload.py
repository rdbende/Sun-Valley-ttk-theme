import os
os.system("pip install twine")
os.system("pip install build")
os.system("python -m build")
os.system("cd ..")
os.system("twine check dist/*")
os.system("twine upload -r pypi dist/* --verbose")