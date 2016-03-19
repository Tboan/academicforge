import unittest
from run import app

class TestHomeNoaLogado(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_deve_estar_rodando_com_status_code_200(self):
        rv = self.app.get('/')

        self.assertEquals(rv.status, '200 OK')

class TestCadastro(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_pagina_cadastro_deve_estar_rodando_com_status_code_200(self):
        rv = self.app.get('/cadastro')

        self.assertEquals(rv.status, '200 OK')

        self.assertIn(b'Cadastrar Usuario', rv.data)

    def test_deve_cadastrar_usuario_no_sistema(self):
        rv = singup(self.app, 'test', 'test@centropaulasouza.com.br', 'ABS@nmsk!')

        self.assertIn(b'Confirmar Email', rv.data, msg='Não redicinou para pagina de confirmar o email')

    def test_deve_mostar_mensagem_de_erro_para_cadastro_sem_nome(self):
        rv = singup(self.app, '', 'test@centropaulasouza.com.br', 'ABS@nmsk!')

        self.assertIn(b'E necessario colocar o nome', rv.data, msg='Não mostrou mensagem de erro para nome faltando')

    def test_deve_mostar_mensagem_de_erro_para_cadastro_com_email_invalido(self):
        rv = singup(self.app, 'test', 'test@gmail.com', 'ABS@nmsk!')

        self.assertIn(b'Email deve ser um valido do centropaulasouza', rv.data, msg='Não mostrou mensagem emails não validos')

    def test_deve_mostar_mensagem_de_erro_para_cadastro_sem_senha(self):
        rv = singup(self.app, 'test', 'test@centropaulasouza.com.br', '')

        self.assertIn(b'Deve adicionar uma senha', rv.data, msg='Não mostrou mensagem de erro para senha faltando')


class TestConfirmaEmail(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_pagina_confirma_email_deve_estar_rodando_com_status_code_200(self):
        rv = self.app.get('/confirma-email')

        self.assertEquals(rv.status, '200 OK')

        self.assertIn(b'Confirmar email', rv.data)

def singup(app, name='', email='', password=''):

    return app.post('/cadastro', data = {
        'name': name,
        'email': email,
        'password': password
    }, follow_redirects=True)