import face_recognition as fr
from app.controllers.engine import reconhece_face, get_rostos
import os

def reconhecimento_facial():
    dir_list = os.listdir("/home/tcc/Documentos/test/app/controllers/img")


    desconhecido = reconhece_face("/home/tcc/Documentos/test/app/controllers/imgtemp/login.jpg")
    if(desconhecido[0]):
            rosto_desconhecido = desconhecido [1][0]
            for foto in dir_list:
                rosto_conhecidos, nome_pessoa = get_rostos(foto)
                comparacao = fr.compare_faces(rosto_desconhecido, rosto_conhecidos)
                for i in range(len(rosto_conhecidos)):
                    resultado = comparacao[i]
                if(resultado):
                    rosto_reconhecido = str(nome_pessoa[i])
                    cpf_pessoa = rosto_reconhecido.replace('.jpg','')
                    return cpf_pessoa

    else:
        cpf_pessoa = str(0000)
        return cpf_pessoa
