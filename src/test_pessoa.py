from selenium import webdriver
from time import sleep
from src.utils import click_btn, input_text

class TestPessoa():
    def __init__(self, nome, cpf, email, dataNascimento, contato, rg, rendaFamiliar, etnia, sexo, deficiencia):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.dataNascimento = dataNascimento
        self.contato = contato
        self.rg = rg
        self.rendaFamiliar = rendaFamiliar
        self.etnia = etnia
        self.sexo = sexo
        self.deficiencia = deficiencia
        self.driver = webdriver.Chrome()
        
    def executar_teste(self):
        xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/button"
        xpath_botao_salvar =  "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
        # xpath_input_deficiencia = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
        # xpath_categoria_select = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/button"
        # xpath_categoria = "/html/body/div[2]/div/div/div[1]/div/div[5]/div/div/div/ul/li[2]"
        xpath_nome = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
        xpath_cpf = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input"
        xpath_email = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/input"
        xpath_dataNascimento = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div/input"
        xpath_numeroIdentidade = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[5]/div/div/div/input"
        xpath_rendaFamiliar = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[15]/div/div/div/input"

        try:
            self.driver.get("https://serra.budibase.app/app/serra-para-todos#/pessoa")
            sleep(10)
            
            click_btn(self.driver, xpath_botao_novo, 10)
            input_text(self.driver, xpath_nome, "Joao")
            input_text(self.driver, xpath_cpf, "1234567890")
            input_text(self.driver, xpath_email, "test@gmail.com")
            input_text(self.driver, xpath_dataNascimento, "11/01/1999")
            input_text(self.driver, xpath_numeroIdentidade, "12453672")
            input_text(self.driver, xpath_rendaFamiliar, "1000")
            # click_btn(self.driver, xpath_categoria_select, 10)
            sleep(3)
            click_btn(self.driver, xpath_botao_salvar)
            
            print(">> O TESTE PASSOU !")
        except:
            print(">> O TESTE FALHOU !")  
        
        self.driver.quit()