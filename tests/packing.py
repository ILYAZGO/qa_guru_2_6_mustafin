import zipfile,os



def clear():
    if os.path.exists('all.zip'):
        os.remove('all.zip')
def packing():
    all = os.listdir('resources')
    os.chdir(os.getcwd()+'/resources/')
    with zipfile.ZipFile('all.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(all[0])
        zf.write(all[1])
        zf.write(all[2])
