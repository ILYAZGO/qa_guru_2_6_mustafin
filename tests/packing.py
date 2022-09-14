import zipfile,os

def packing():

    all = os.listdir('resources')
    os.chdir(os.getcwd()+'/resources/')
    with zipfile.ZipFile('all.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(all[0])
        zf.write(all[1])
        zf.write(all[2])

def unpacking():
    archive = zipfile.ZipFile('all.zip','r')
    csv_data = archive.read('csv_example.csv').decode()
    return csv_data
