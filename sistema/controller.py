from sistema.view import EmailAutomationView
from sistema.model import BoletoModel
import os
import fitz  # PyMuPDF
import datetime
import pandas as pd

class BoletoController:
    def __init__(self):
        # Definir caminhos dos arquivos e do ChromeDriver
        driver_path = r"C:\Users\User\Documents\portfolio\web\chromedriver.exe"
        chrome_profile_path = r"C:\Users\User\Documents\portfolio\web\localhost"
        json_file_path = r"C:\Users\User\Documents\portfolio\web\login.json"
        self.email_view = EmailAutomationView(driver_path, chrome_profile_path, json_file_path)
        self.boleto_model = BoletoModel()

    def baixar_boleto(self):
        self.email_view.login_email()
        boleto_data = self.email_view.buscar_boleto()
        self.boleto_model.processar_boleto(boleto_data)

    def processar_pdf(self):
        # Define o caminho da pasta
        caminho = r"C:\Users\User\Downloads"

        # Obtém a lista de arquivos PDF na pasta e ordena por data
        pdfs = [f for f in os.listdir(caminho) if f.endswith('.pdf')]
        pdfs.sort(key=lambda x: os.path.getmtime(os.path.join(caminho, x)))

        # Pega o último PDF
        ultimo_pdf = os.path.join(caminho, pdfs[-1])

        # Define a senha
        senha = ""

        # Abre o PDF e remove a senha
        doc = fitz.open(ultimo_pdf)

        if doc.is_encrypted:
            if not doc.authenticate(senha):  # Tenta autenticar com a senha
                print("Senha incorreta. Não foi possível desbloquear o PDF.")
                exit(1)

        # Cria um novo documento para salvar o PDF sem a senha
        novo_doc = fitz.open()  # Novo documento vazio

        # Copia todas as páginas para o novo documento
        for page in doc:
            novo_doc.insert_pdf(doc, from_page=page.number, to_page=page.number)

        # Gera um nome de arquivo único com base na data e hora atual
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_sem_senha = os.path.join(caminho, f"pdf_sem_senha_{timestamp}.pdf")
        novo_doc.save(pdf_sem_senha)
        novo_doc.close()
        doc.close()

        # Agora, extrai o texto do PDF sem senha
        doc = fitz.open(pdf_sem_senha)
        texto_final = ""

        for page in doc:
            texto_final += page.get_text() + "\n"

        doc.close()

        # Salva o texto extraído em um arquivo .txt
        caminho_txt = os.path.join(caminho, "texto_extraido.txt")
        with open(caminho_txt, "w", encoding='utf-8') as f:
            f.write(texto_final)

        print(f"Texto extraído e salvo em: {caminho_txt}")

        # Lê o arquivo texto
        with open(caminho_txt, 'r', encoding='utf-8') as file:
            linhas = file.readlines()

        # Armazena os valores das linhas específicas em variáveis, removendo espaços em branco
        valorpagar = linhas[33].strip()  # Linha 34
        datavencimento = linhas[37].strip()  # Linha 38
        titular = linhas[46].strip()  # Linha 47
        codigobarras = linhas[53].replace("Banco Itaú S.A.", "").strip()  # Linha 54
        pagminimo = linhas[0].strip()  # Linha 1

        # Cria o DataFrame com as colunas especificadas
        dados = pd.DataFrame(columns=['valor', 'vencimento', 'titular', 'codigo', 'minimo'])

        # Cria um dicionário com os valores extraídos
        nova_linha = {
            'valor': valorpagar,
            'vencimento': datavencimento,
            'titular': titular,
            'codigo': codigobarras,
            'minimo': pagminimo
        }

        # Insere os valores extraídos no DataFrame usando pd.concat
        dados = pd.concat([dados, pd.DataFrame([nova_linha])], ignore_index=True)

        # Salva o DataFrame em um arquivo CSV
        caminho_csv = r"C:\Users\User\Downloads\dados.csv"
        dados.to_csv(caminho_csv, index=False)

        print(f"Dados salvos em: {caminho_csv}")
