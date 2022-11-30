import face_recognition as fr
import os

def reconhece_face(fotovar):
    foto = fr.load_image_file(fotovar)
    rosto = fr.face_encodings(foto)
    if(len(rosto)>0):
        return True, rosto
    return False, []

def get_rostos(foto, rosto_desconhecido):
    imgdir = "/home/tcc/Documentos/test/app/controllers/img/"

    directory = os.getcwd()

    rosto_conhecido = []
    cpf_pessoa = []


    fotodir = (imgdir + foto)
    #face = reconhece_face(fotodir)
    if (face[0]):
        rosto_conhecido.append(face[1][0])
        cpf_pessoa.append(foto)

        comparacao = fr.compare_faces(rosto_conhecido, rosto_desconhecido)

    return rosto_conhecido, cpf_pessoa




from procura_foto import procura_foto_dir

cpf = 'joao2'
dir_list = os.listdir("/home/tcc/Documentos/test/app/controllers/img")

# fotovar = procura_foto_dir(cpf)
fotovar = "/home/tcc/Documentos/test/app/controllers/img/" + cpf + '.jpg'

desconhecido = reconhece_face(fotovar)

if (desconhecido[0]):

    rosto_desconhecido = desconhecido[1]
    for foto in dir_list:
        rosto_conhecido, cpf_pessoa = get_rostos(foto, rosto_desconhecido)

        comparacao = fr.compare_faces(rosto_conhecido, rosto_desconhecido)


else:
    print('não encontrou rostos')