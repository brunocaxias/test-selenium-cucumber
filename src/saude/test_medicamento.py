from selenium import webdriver
from time import sleep
from src.utils import click_btn, input_text

class TestMedicamento():
    def __init__(self, nome_medicamento, descricao_medicamento):
        self.nome_medicamento = nome_medicamento
        self.descricao_medicamento = descricao_medicamento
        self.driver = webdriver.Chrome()
    
    def executar_teste(self):
        xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"
        xpath_input_medicamento = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
        xpath_input_descricao = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input"
        xpath_botao_salvar = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
    
        try:   
            self.driver.get("https://serra.budibase.app/app/serra-para-todos#/medicamento")
            sleep(12)
            
            click_btn(self.driver, xpath_botao_novo, 10)
            input_text(self.driver, xpath_input_medicamento, "Medicamento de teste")
            input_text(self.driver, xpath_input_descricao, "Descrição do Medicamento de teste")
            input_text(self.driver, xpath_input_descricao, "Descrição do Medicamento de teste")
            click_btn(self.driver, xpath_botao_salvar)
            print(">> O TESTE PASSOU !")
        except:
            print(">> O TESTE FALHOU !")  
                
        self.driver.quit()