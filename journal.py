import os

def get_full_path(name):
    filename = os.path.join(".", "journals", f"{name}.jrn")
    return filename

def load(name):
    data = []
    filename = get_full_path(name)
    print(f"......loading from {filename}")
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(name, data):
    filename = get_full_path(name)
    print(f"......saving to {filename}")
    with open(filename, "w") as fout:
        for entry in data:
            fout.write(entry+"\n")

def add_entry(text, data):
    data.append(text)