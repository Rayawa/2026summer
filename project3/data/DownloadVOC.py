import os
import urllib.request
import tarfile

urls = {
    "voc2007": "http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar",
    "voc2012": "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar"
}

def download(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename} ...")
        urllib.request.urlretrieve(url, filename)
    else:
        print(f"{filename} already exists")

def extract(file):
    print(f"Extracting {file} ...")
    with tarfile.open(file) as tar:
        tar.extractall()

def main():
    for name, url in urls.items():
        file = f"{name}.tar"
        download(url, file)
        extract(file)

    print("VOC dataset ready!")

if __name__ == "__main__":
    main()