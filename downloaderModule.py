import requests,zipfile,io
from os import walk,replace
from shutil import rmtree

def downloader():
    url = "https://ihmecovid19storage.blob.core.windows.net/latest/ihme-covid19.zip"
    tempFolder = "./Downloads"

    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(tempFolder)

    path, dirs, filenames = next(walk(tempFolder))
    print(filenames)
    print(dirs)
    print(path)

    dataFile="reference_hospitalization_all_locs.csv"
    fullPath = f'{path}/{dirs[0]}/{dataFile}'
    fullPath


    path2file = "./Data/datosCovid.csv"
    replace(fullPath, path2file)

    rmtree(f'{path}', ignore_errors=True)

