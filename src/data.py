import os
parent = "./src"
path = f"{parent}/data"
with open(f"{parent}/data.js", "w", encoding="utf8") as f:
    items = os.listdir(path)
    f.write("var imageUrls = [\n")
    for item in items:
        if item.endswith((".png", ".jpg", ".jpeg")):
            f.write(f'\t"{path}/{item}",\n')
    f.write("]\n")
    f.write("var textUrls = [\n")
    for item in items:
        if item.endswith(".txt"):
            f.write(f'\t"{path}/{item}",\n')
    f.write("]\n")
