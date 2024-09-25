import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class EmailAutomationView:
    def __init__(self, driver_path, chrome_profile_path, json_file_path):
        self.chrome_service = Service(driver_path)
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--remote-debugging-port=9222")
        self.options.add_argument(f"--user-data-dir={chrome_profile_path}")
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.options)
        self.json_file_path = json_file_path

    def open_gmail(self):
        # Abrir Gmail
        self.driver.get('https://www.gmail.com/')
        print("Página aberta:", self.driver.title)

    def login(self):
        # Carregar credenciais do JSON
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
        
        # Inserir o username
        text_to_type = data.get("username", "")
        input_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
        input_element = self.driver.find_element(By.XPATH, input_xpath)
        input_element.click()
        input_element.send_keys(text_to_type)
        time.sleep(2)

        # Clicar no botão "Próximo"
        button_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span"
        button_element = self.driver.find_element(By.XPATH, button_xpath)
        button_element.click()
        time.sleep(2)

        # Inserir a senha
        password_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
        input_element2 = self.driver.find_element(By.XPATH, password_xpath)
        text_to_type2 = data.get("password", "")
        input_element2.click()
        input_element2.send_keys(text_to_type2)
        time.sleep(15)

    def search_email(self, email):
        # Procurar e-mail por endereço
        search_box_xpath = "/html/body/div[6]/div[3]/div/div[1]/div/div[2]/div[2]/header/div[2]/div[2]/div[2]/form/div/table/tbody/tr/td/table/tbody/tr/td/div/input[1]"
        input_element = self.driver.find_element(By.XPATH, search_box_xpath)
        input_element.click()
        input_element.send_keys(email)
        input_element.send_keys(Keys.RETURN)
        time.sleep(5)

    def open_latest_email(self):
        # Abrir o último e-mail na lista
        latest_email_xpath = "/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[7]/div[1]/div/table/tbody/tr[1]/td[6]/div[2]"
        try:
            email_element = self.driver.find_element(By.XPATH, latest_email_xpath)
            email_element.click()
        except NoSuchElementException:
            print("O último e-mail não foi encontrado.")
        time.sleep(5)

    def hover_over_email_body(self):
        # Posicionar o mouse sobre o corpo do e-mail
        email_body_xpath = "/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/center"
        try:
            email_body_element = self.driver.find_element(By.XPATH, email_body_xpath)
            actions = ActionChains(self.driver)
            actions.move_to_element(email_body_element).perform()
        except NoSuchElementException:
            print("Corpo do e-mail não encontrado.")
        time.sleep(5)

    def scroll_to_bottom(self):
        # Simular scroll até o fim da página
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

    def download_attachment(self):
        # Localizar e baixar o anexo
        attachment_xpath = "/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[4]/div[4]/span/a/div/div[3]/div[1]"
        try:
            attachment_element = self.driver.find_element(By.XPATH, attachment_xpath)
            attachment_element.click()
        except NoSuchElementException:
            print("O anexo não foi encontrado.")
        time.sleep(5)

    def close(self):
        # Fechar o navegador
        self.driver.quit()
