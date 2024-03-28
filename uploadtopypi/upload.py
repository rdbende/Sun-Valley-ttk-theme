import os
os.system("pip install twine")
os.system("twine check dist/*")
os.system("twine upload -r pypi dist/*")