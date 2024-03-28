import os
os.system("pip install twine")
os.system("cd ..")
os.system("twine check dist/*")
os.system("twine upload -r pypi dist/*")