import face_recognition as fr
import os
from engine import reconhece_face, get_rostos
#from procura_foto import procura_foto_dir

cpf = 'joao2'
dir_list = os.listdir("/home/tcc/Documentos/test/app/controllers/img")


#fotovar = procura_foto_dir(cpf)
fotovar = "/home/tcc/Documentos/test/app/controllers/img/"+cpf+'.jpg'

desconhecido = reconhece_face(fotovar)


if(desconhecido[0]):


    rosto_desconhecido = desconhecido[1]
    for foto in dir_list:

        rosto_conhecido, cpf_pessoa = get_rostos(foto, rosto_desconhecido)


        comparacao = fr.compare_faces(rosto_conhecido, rosto_desconhecido)


else:
    print('não encontrou rostos')