import time

from flask import render_template, request, Response
from app import app, db
from app.models.tables import Pessoa
from app.controllers.tirafoto import tirar_foto, tirar_foto_temp
from app.controllers.foto import reconhecimento_facial
from app.controllers.envioWhatsapp import enviar_senha_whatsapp
from app.controllers.envioSMS import envio_SMS
import os
import cv2

picFolder = os.path.join('static','pics')
camera = cv2.VideoCapture(0)

app.config['UPLOAD_FOLDER'] = picFolder

def generate_frames(cond):
    while cond:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    print('desativou')



@app.route('/')
@app.route('/listagem')
def listagem():
    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/foto', methods=['POST'])
def face():
    Id = int(request.form.get('id'))
    cpf = int(request.form.get('CPF'))
    #generate_frames(cond=False)
    tirar_foto(cpf)
    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')
    #return render_template('face.html', pessoas=pessoas)

@app.route('/foto_reconhecimento')
def foto_reconhecimento():
    return render_template('reconhecimento.html')

@app.route('/impressao_whatsapp/<int:cpf>')
def impressao_whatsapp(cpf=0):
    enviar_senha_whatsapp(cpf)
    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/impressao/<tipo>')
def impressao(tipo=''):
    envio_SMS(tipo)
    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/reconhecimento')
def reconhecimento():
    tirar_foto_temp()
    cpf = int(reconhecimento_facial())
    if cpf == 0000:
        return render_template('Erro_rosto.html')
    pessoa = Pessoa.query.filter_by(cpf=cpf).first()
    return render_template('impressaosenha.html', pessoa=pessoa)

@app.route('/repasse_recepcao')
def repasse_recepcao():
    return render_template("repasse_recepcao.html")

@app.route('/selecao/<int:id>')
def selecao(id=0):
    pessoas = Pessoa.query.filter_by(id=id).all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/ordenacao/<campo>/<ordem_anterior>')
def ordenacao(campo='id', ordem_anterior=''):
    if campo == 'id':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.id.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.id).all()
    elif campo == 'nome':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.nome.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.nome).all()
    elif campo == 'cpf':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.cpf.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.cpf).all()
    elif campo == 'email':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.email.desc()).all()
        else:
            pessoas = Pessoa.query.order_by(Pessoa.email).all()
    else:
        pessoas = Pessoa.query.order_by(Pessoa.id).all()

    return render_template('listagem.html', pessoas=pessoas, ordem=campo)

@app.route('/consulta', methods=['POST'])
def consulta():
    consulta = '%'+request.form.get('consulta')+'%'
    campo = request.form.get('campo')

    if campo == 'id':
        pessoas = Pessoa.query.filter(Pessoa.id.like(consulta)).all()
    elif campo == 'nome':
        pessoas = Pessoa.query.filter(Pessoa.nome.like(consulta)).all()
    elif campo == 'cpf':
        pessoas = Pessoa.query.filter(Pessoa.cpf.like(consulta)).all()
    elif campo == 'email':
        pessoas = Pessoa.query.filter(Pessoa.email.like(consulta)).all()
    else:
       pessoas = Pessoa.query.all()

    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/insercao')
def insercao():
    return render_template('insercao.html')

@app.route('/salvar_insercao', methods=['POST'])
def salvar_insercao():
    Nome = request.form.get('nome')
    CPF = int(request.form.get('cpf'))
    Email = request.form.get('email')
    Numero_Cel = int(request.form.get('numero_cel'))
    DataNascimento = request.form.get('datanascimento')
    Sexo = request.form.get('sexo')
    Cep = int(request.form.get('cep'))
    Rua = request.form.get('rua')
    Numero = int(request.form.get('numero'))
    Bairro = request.form.get('bairro')
    Complemento = request.form.get('complemento')
    Estado = request.form.get('estado')
    Cidade = request.form.get('cidade')
    Convenio = request.form.get('convenio')
    Numero_carteirinha = request.form.get('numero_carteirinha')
    AceitaTermos = request.form.get('aceitatermos')
    PCD = request.form.get('pcd')

    pessoa = Pessoa(Nome, CPF, Email, Numero_Cel, DataNascimento, Sexo, Cep, Rua, Numero, Bairro, Complemento, Estado, Cidade, Convenio, Numero_carteirinha, AceitaTermos, PCD)

    db.session.add(pessoa)
    db.session.commit()

    print('aqui foi insercao')
    pessoa_atual = Pessoa.query.filter_by(cpf=CPF).first()
    pessoas = Pessoa.query.all()

    return render_template('face.html', pessoas=pessoas, user_atual=pessoa_atual, cpf=CPF)

@app.route('/edicao/<int:id>')
def edicao(id=0):
    pessoa = Pessoa.query.filter_by(id=id).first()
    return render_template('edicao.html', pessoa=pessoa)

@app.route('/salvar_edicao', methods=['POST'])
def salvar_edicao():
    Id = int(request.form.get('id'))
    Nome = request.form.get('nome')
    CPF = int(request.form.get('cpf'))
    Email = request.form.get('email')
    Numero_Cel = int(request.form.get('numero_cel'))
    DataNascimento = request.form.get('datanascimento')
    Sexo = request.form.get('sexo')
    Cep = int(request.form.get('cep'))
    Rua = request.form.get('rua')
    Numero = int(request.form.get('numero'))
    Bairro = request.form.get('bairro')
    Complemento = request.form.get('complemento')
    Estado = request.form.get('estado')
    Cidade = request.form.get('cidade')
    Convenio = request.form.get('convenio')
    Numero_carteirinha = request.form.get('numero_carteirinha')
    AceitaTermos = request.form.get('aceitatermos')
    PCD = request.form.get('pcd')

    pessoa = Pessoa.query.filter_by(id=Id).first()

    pessoa.nome = Nome
    pessoa.cpf = CPF
    pessoa.email = Email
    pessoa.numero_cel = Numero_Cel
    pessoa.datanascimento = DataNascimento
    pessoa.sexo = Sexo
    pessoa.cep = Cep
    pessoa.rua = Rua
    pessoa.numero = Numero
    pessoa.bairro = Bairro
    pessoa.complemento = Complemento
    pessoa.estado = Estado
    pessoa.cidade = Cidade
    pessoa.convenio = Convenio
    pessoa.numero_carteirinha = Numero_carteirinha
    pessoa.aceitatermos = AceitaTermos
    pessoa.pcd = PCD

    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/delecao/<int:id>')
def delecao (id=0):
    pessoa=Pessoa.query.filter_by(id=id).first()
    return render_template('delecao.html', pessoa=pessoa)

@app.route('/salvar_delecao', methods=['POST'])
def salvar_delecao():
    Id = int(request.form.get('id'))

    pessoa = Pessoa.query.filter_by(id=Id).first()

    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route("/video")
def video():
    return Response(generate_frames(cond=True), mimetype='multipart/x-mixed-replace; boundary=frame')
