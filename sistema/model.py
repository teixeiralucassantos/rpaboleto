class BoletoModel:
    def processar_boleto(self, boleto_data):
        if boleto_data["status"] == "sucesso":
            print("Boleto baixado e pronto para ser processado.")
        else:
            print("Erro ao baixar o boleto.")
