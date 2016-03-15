import unittest

from selenium import webdriver

class TestHomeNaoLogado(unittest.TestCase):

    def setUp(self):
        self.firefox = webdriver.Firefox()

    def tearDown(self):
        self.firefox.close()

    def test_pagina_home_deve_conter_no_titulo_nome_do_site(self):
        self.firefox.get('http://localhost:5000/')

        self.assertIn('Academic Forge', self.firefox.title)

    def test_deve_ter_botao_de_cadastrar_que_leva_para_pagina_de_cadastro(self):

        self.firefox.get('http://localhost:5000/')

        button = self.firefox.find_element_by_id('singup-btn-id')
        button.click()

        self.assertEqual(self.firefox.current_url, 'http://localhost:5000/cadastro', msg='Pagina não direcionada para cadastro')

class TestPaginaDeCadastro(unittest.TestCase):

    def setUp(self):
        self.firefox = webdriver.Firefox()

    def tearDown(self):
        self.firefox.close()

    def test_cadastrar_um_usuario_valido_e_ser_direcionado_para_pagina_de_confirmação_de_email(self):

        # Usuario clicou no botao cadastrar na home ou veio direto para pagina de cadastro
        self.firefox.get('http://localhost:5000/cadastro')

        # Usuario digita se nome no campo de nome
        elem = self.firefox.find_element_by_id('form-input-name-id')
        elem.send_keys('Fulano de Tal Silva')

        # Usuario digita seu email da faculdade valido
        elem = self.firefox.find_element_by_id('form-input-email-id')
        elem.send_keys('fulano@centropaulasouza.com.br')

        # Usuario digita uma senha segura
        elem = self.firefox.find_element_by_id('form-input-password-id')
        elem.send_keys('Pass@192!mmmmsfsk')

        # Usuario clica no botao de cadastrar
        elem = self.firefox.find_element_by_id('form-btn-submit-id')
        elem.click()

        self.assertEqual(self.firefox.current_url, 'http://localhost:500/confirma-email')
if __name__ == '__main__':
    unittest.main()