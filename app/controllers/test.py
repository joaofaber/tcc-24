import cv2
from app.models.tables import Pessoa
#import os

#ARQUIVO FEITO PARA TESTES

#dir_list = os.listdir("./img/")
#print(dir_list)
#for foto in dir_list:
#    print(foto)

def show_cam():
    vid = cv2.VideoCapture(1)
    if not (vid.isOpened()):
        print("não foi possível ler a camera")

    while (True):
        ret, frame = vid.read()
        cv2.imshow('preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #APERTE "q" PARA PARAR O VIDEO
            break
    vid.release()

def take_pic(cpf):
    nome = str(cpf) + '.jpg'
    vid = cv2.VideoCapture(1)
    if not (vid.isOpened()):
        print("não foi possível ler a camera")

    while(True):
        ret, frame = vid.read()
        cv2.imshow('Tirar Foto', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #APERTE "q" PARA PARAR O VIDEO
            cv2.imwrite('/home/tcc/Documentos/test/app/controllers/img/' + nome,frame)
            break
    vid.release()

def test_db(cpf):

    pessoa = Pessoa.query.filter_by(cpf=cpf).first()
    print(pessoa.cpf)


#show_cam()
#take_pic('teste_foto_cpf')
#test_db(54224332116)
