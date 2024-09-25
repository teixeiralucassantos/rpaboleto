# Automação de Download e Processamento de Boletos

## Descrição

Este projeto automatiza o processo de login em uma conta de e-mail, busca e download do último boleto do mês, e extrai informações relevantes para facilitar o pagamento. Com esta ferramenta, você pode obter rapidamente todas as informações necessárias sobre o seu boleto, simplificando o processo de pagamento e economizando tempo.

## Funcionalidades

- **Login Automático**: Realiza o login na conta de e-mail utilizando Selenium e um perfil do Chrome.
- **Busca de Boletos**: Localiza o último boleto recebido na caixa de entrada.
- **Download de Boletos**: Faz o download do boleto e o salva na pasta designada.
- **Tratamento de PDFs**: Remove a proteção por senha do PDF do boleto e extrai seu conteúdo.
- **Extração de Informações**: Captura informações essenciais do boleto, como valor a pagar, data de vencimento, titular, código de barras e valor mínimo.
- **Relatório em CSV**: Gera um arquivo CSV com todas as informações do boleto para fácil consulta e organização.

## Tecnologias Utilizadas

- **Python**: A linguagem principal utilizada para a automação.
- **Selenium**: Biblioteca usada para automação de navegadores, facilitando o login e a busca no Gmail.
- **PyMuPDF (fitz)**: Utilizada para manipulação de arquivos PDF, permitindo a remoção de senhas e extração de texto.
- **Pandas**: Utilizada para manipulação de dados e geração de relatórios em formato CSV.

## Como Funciona

1. **Configuração**: Insira suas credenciais de e-mail em um arquivo JSON para que o script possa fazer login automaticamente.
2. **Execução**: Ao executar o script, ele faz login no Gmail, busca pelo último boleto do mês e faz o download.
3. **Processamento do PDF**: O PDF é tratado para remover a proteção por senha, e o texto é extraído.
4. **Geração de Relatório**: As informações extraídas são salvas em um arquivo CSV, que pode ser consultado a qualquer momento.

## Instalação

Para rodar este projeto, você precisará do Python instalado e das seguintes bibliotecas:

```bash
pip install selenium PyMuPDF pandas
