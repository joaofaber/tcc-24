from app import db

class Pessoa(db.Model):
	__tablename__ = 'pessoas'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50), nullable=False)
	cpf = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String)
	numero_cel = db.Column(db.Integer, nullable=False)
	datanascimento = db.Column(db.String)
	#dia_nascimento = db.Column(db.String)
	#mes_nascimento = db.Column(db.String)
	#ano_nascimento = db.Column(db.String)
	sexo = db.Column(db.String(1))
	cep = db.Column(db.Integer)
	rua = db.Column(db.String(255))
	numero = db.Column(db.Integer)
	bairro = db.Column(db.String(255))
	complemento = db.Column(db.String(255))
	estado = db.Column(db.String(255))
	cidade = db.Column(db.String(255))
	convenio = db.Column(db.String(255))
	numero_carteirinha = db.Column(db.String(255))
	aceitatermos = db.Column(db.String(1))
	pcd = db.Column(db.String(1))


	def __init__(self, nome='Anônimo', cpf='12345678911', email='anonimo@invalid.com', numero_cel='11946318493', datanascimento='90', sexo='M', cep='', rua='', numero='', bairro='', complemento='', estado='', cidade='', convenio='', numero_carteirinha='', aceitatermos='S', pcd='N'):
		self.nome = nome
		self.cpf = cpf
		self.email = email
		self.numero_cel = numero_cel
		self.datanascimento = datanascimento
		self.sexo = sexo
		self.cep = cep
		self.rua = rua
		self.numero = numero
		self.bairro = bairro
		self.complemento = complemento
		self.estado = estado
		self.cidade = cidade
		self.convenio = convenio
		self.numero_carteirinha = numero_carteirinha
		self.aceitatermos = aceitatermos
		self.pcd = pcd



	def __repr__(self):
		return '<Pessoa %r>' % self.nome
