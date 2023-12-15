from selenium import webdriver
from time import sleep
from src.utils import click_btn, input_text

class TestProcedimento():
    def __init__(self, procedimento, numero_procedimento, descricao_procedimento):
        self.procedimento = procedimento
        self.numero_procedimento = numero_procedimento
        self.descricao_procedimento = descricao_procedimento
        self.driver = webdriver.Chrome()
    
    def executar_teste(self):
        xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[3]/button"
        xpath_input_procedimento = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
        xpath_input_numero = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input"
        xpath_input_descricao = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/input"
        xpath_botao_salvar = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
        
        try:
            self.driver.get("https://serra.budibase.app/app/serra-para-todos#/procedimento")
            sleep(12)
            
            click_btn(self.driver, xpath_botao_novo, 10)
            input_text(self.driver, xpath_input_procedimento, "Procedimento Teste")
            input_text(self.driver, xpath_input_numero, "PROC-000")
            input_text(self.driver, xpath_input_descricao, "Descrição do Procedimento Teste")
            click_btn(self.driver, xpath_botao_salvar)
            print(">> O TESTE PASSOU !")
        except:
            print(">> O TESTE FALHOU !")  
                
        self.driver.quit()