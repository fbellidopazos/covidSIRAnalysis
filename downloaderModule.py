import requests,zipfile,io
import os

from shutil import rmtree

def downloader():
    url = "https://ihmecovid19storage.blob.core.windows.net/latest/ihme-covid19.zip"
    tempFolder = "./Downloads"

    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(tempFolder)

    path, dirs, filenames = next(os.walk(tempFolder))
    print(filenames)
    print(dirs)
    print(path)

    #dataFile="reference_hospitalization_all_locs.csv"
    dataFile="worse_hospitalization_all_locs.csv"
    fullPath = f'{path}/{dirs[0]}/{dataFile}'
    fullPath
    
    if not os.path.exists('Data'):
        os.makedirs('Data')

    path2file = "./Data/datosCovid.csv"
    os.replace(fullPath, path2file)

    rmtree(f'{path}', ignore_errors=True)


