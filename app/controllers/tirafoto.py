import cv2

def tirar_foto(cpf):
    nome = str(cpf) + '.jpg'
    vid = cv2.VideoCapture(1)
    if not (vid.isOpened()):
        print("não foi possível ler a camera")

    while (True):
        ret, frame = vid.read()
        cv2.imshow('Pressione "Q" para salvar a foto', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # APERTE "q" PARA PARAR O VIDEO
            cv2.imwrite('/home/tcc/Documentos/test/app/controllers/img/' + nome, frame)
            break
    vid.release()
    cv2.destroyAllWindows()
    return None


def tirar_foto_temp():
    nome = 'login.jpg'
    vid = cv2.VideoCapture(1)
    if not (vid.isOpened()):
        print("não foi possível ler a camera")

    while (True):
        ret, frame = vid.read()
        cv2.imshow('Pressione "Q" para salvar a foto', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # APERTE "q" PARA PARAR O VIDEO
            cv2.imwrite('/home/tcc/Documentos/test/app/controllers/imgtemp/' + nome, frame)
            break
    vid.release()
    cv2.destroyAllWindows()
    return None

#tirar_foto_temp()

