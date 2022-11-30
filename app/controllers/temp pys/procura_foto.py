import os


def procura_foto_dir(cpf):
    basedir = os.path.abspath(os.path.dirname(__file__))
    imgfolder = 'img'
    imgdir = os.path.join(basedir, imgfolder)
    os.chdir(imgdir)
    directory = os.getcwd()
    foto = cpf+'.jpg'


    for relPath, dirs, files in os.walk(directory):
        if(foto in files):
            fotodir = os.path.join(directory,relPath,foto)
            print('3°'+fotodir)
            return fotodir
        else:
            return print('nada')

def fotos():
    dir_list = os.listdir("./img/")
    print(dir_list)
    for foto in dir_list:
        print(foto)