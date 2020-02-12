import os
import shutil

shutil.copyfile()

print(os.name)
print(os.environ)
print(os.environ.get('PATH'))
print(os.path.abspath("."))
print(os.path.split(os.path.abspath(".")))
print(os.path.splitext("/aa/f/t.txt"))
