from nbformat import v3, v4

with open("pi.py") as fpin:
    text = fpin.read()

nbook = v3.reads_py(text)
nbook = v4.upgrade(nbook)  # Upgrade v3 to v4

jsonform = v4.writes(nbook) + "\n"
with open("pi.ipynb", "w") as fpout:
    fpout.write(jsonform)