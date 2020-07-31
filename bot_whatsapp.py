from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia! Tenha uma ótima semana."
        self.grupos_ou_contato = ["Contato1", "Contato2"]
        # Substituir pelo nome do contato da maneira como ele está escrito no WhatsApp.
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupos_ou_contato in self.grupos_ou_contato:
            campo_contato = self.driver.find_element_by_xpath(
                f"//span[@title='{grupos_ou_contato}']")
            time.sleep(3)
            campo_contato.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()