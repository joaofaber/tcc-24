import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos(cpf):

    rosto_conhecidos = []
    nome_pessoa = []
    
    foto = reconhece_face("/home/tcc/Documentos/test/app/controllers/img/"+cpf)
    if(foto[0]):
        rosto_conhecidos.append(foto[1][0])
        nome_pessoa.append(cpf)

    return rosto_conhecidos, nome_pessoa