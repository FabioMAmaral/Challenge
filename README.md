# Challenge
Grupo Black Lotus: Scanner LGPD de Documentos

# Classificação de Arquivos Sensíveis

Scanner LGPD de Documentos

Um script Python que automatiza a identificação de dados pessoais sensíveis em arquivos de texto (.txt), planilhas Excel (.xlsx), PDFs (.pdf) e documentos do Word (.docx), baseando-se nos critérios da Lei Geral de Proteção de Dados (LGPD) brasileira. O script utiliza expressões regulares para detectar padrões comuns de dados pessoais, ajudando a garantir a conformidade com a legislação vigente.

Suporte a múltiplos formatos de arquivo: .txt, .xlsx, .pdf, .docx. Identificação de uma ampla gama de dados pessoais, incluindo, mas não limitado a, nome completo, RG, CPF, gênero, e-mail, entre outros. Classificação simples dos arquivos como contendo ou não dados pessoais.

## Como Usar

1. **Requisitos:**
   - Python 3.x instalado.

2. **Arquivos para realização de teste:**
   - Instale a pasta Teste documentos.zip contendo 17 arquivos com formatos: .txt, .xlsx, .pdf, .docx.

3. **Instruções:**
   - Clone o repositório para o seu computador.
     ```
      git clone https://github.com/FabioMAmaral/Challenge.git
     ```
   - Bibliotecas necessárias:
     - tkinter
     - pandas
     - docx
     - PyPDF2
     - plotly
   - O arquivo requirements.txt para instalar as bibliotecas necessárias utilizando o pip:
     ```
      pip install -r requirements.txt
     ```
   - Abra a pasta "Scanner LGPD"
   - Abra o CMD de dentro da pasta "Scanner LGPD"
   - `pyhton dados_sens.py`.
   - Selecione a pasta contendo os arquivos a serem classificados.
   - O programa exibirá um gráfico de classificação geral e um gráfico detalhado de tipos de dados pessoais encontrados nos arquivos.

## Arquivos e Pastas

- `dados_sens.py`: Código-fonte principal do programa.
- `patterns.py`: Arquivo contendo padrões de dados pessoais.
- `black_lotus.png`: Imagem utilizada na interface gráfica.

## Troubleshotting
Caso tenha problemas na instalação das biblotecas
      ```
      pip install –upgrade
      ```
