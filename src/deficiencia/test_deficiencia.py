from selenium import webdriver
from time import sleep
from src.utils import click_btn, input_text

class TestDeficiencia():
    def __init__(self, nome_deficiencia, nome_categoria):
        self.nome_deficiencia = nome_deficiencia
        self.nome_categoria = nome_categoria
        self.driver = webdriver.Chrome()
        
    def executar_teste(self):
        xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"
        xpath_botao_salvar =  "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
        xpath_input_deficiencia = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
        xpath_categoria_select = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/button"
        xpath_categoria = "/html/body/div[2]/div/div/div[1]/div/div[5]/div/div/div/ul/li[2]"
            
        try:
            self.driver.get("https://serra.budibase.app/app/serra-para-todos#/deficiencia")
            sleep(12)
            
            click_btn(self.driver, xpath_botao_novo, 10)
            input_text(self.driver, xpath_input_deficiencia, "Deficiência Teste")
            click_btn(self.driver, xpath_categoria_select, 10)
            sleep(3)
            click_btn(self.driver, xpath_categoria)
            click_btn(self.driver, xpath_botao_salvar)
            
            print(">> O TESTE PASSOU !")
        except:
            print(">> O TESTE FALHOU !")  
        
        self.driver.quit()