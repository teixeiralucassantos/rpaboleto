from sistema.controller import BoletoController
from sistema.controller import get_latest_pdf, unlock_pdf_and_save_as_text

def main():
    controller = BoletoController()
    controller.baixar_boleto()
    

    # Definir caminhos
    pdf_directory = r"C:\Users\User\Downloads"
    json_password_path = r"C:\Users\User\Documents\portfolio\web\senhapdf.json"
    output_text_path = r"C:\Users\User\Documents\portfolio\web\output_pdf_text.txt"

    # Pegar o PDF mais recente e converter para texto
    latest_pdf = get_latest_pdf(pdf_directory)
    unlock_pdf_and_save_as_text(latest_pdf, json_password_path, output_text_path)





if __name__ == "__main__":
    main()
