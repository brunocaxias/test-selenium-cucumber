from selenium import webdriver

from time import sleep
from src.utils import click_btn, input_text

class TestCategoria():
    def __init__(self, nome_categoria):   
        self.nome_categoria = nome_categoria
        self.driver = webdriver.Chrome()
        
    def executar_teste(self):
        xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"
        xpath_botao_salvar =  "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
        xpath_input_categoria = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"

        try:
            self.driver.get("https://serra.budibase.app/app/serra-para-todos#/categoria")
            sleep(12)
            
            click_btn(self.driver, xpath_botao_novo, 10)
            input_text(self.driver, xpath_input_categoria, "Categoria Teste")
            click_btn(self.driver, xpath_botao_salvar)
            
            print(">> O TESTE PASSOU !")
        except:
            print(">> O TESTE FALHOU !")  
            
        self.driver.quit()