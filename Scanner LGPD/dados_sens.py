import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import docx
from PyPDF2 import PdfReader
import re
import plotly.express as px
import plotly.graph_objects as go
from patterns import patterns

def is_personal_data(text):
    return [name for pattern, name in patterns if re.search(pattern, text)]

def process_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.docx':
        doc = docx.Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
    elif file_extension == '.xlsx':
        df = pd.read_excel(file_path)
        text = ' '.join(df.iloc[:, :].astype(str).values.flatten())
    elif file_extension == '.pdf':
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            text = '\n'.join([page.extract_text() for page in pdf_reader.pages])
    elif file_extension == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        raise ValueError('Formato de arquivo não suportado')

    found_info = is_personal_data(text)
    return 'Contém Dados Pessoais' if found_info else 'Não contém Dados Pessoais', found_info

def classify_files(folder_path):
    results = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            classification, found_info = process_file(file_path)
            results.append((file_name, classification, found_info))
    return results

def display_results(results):
    personal_data_count = 0
    not_personal_data_count = 0
    personal_data_info = {}

    for file_name, classification, found_info in results:
        if classification == 'Contém Dados Pessoais':
            personal_data_count += 1
            for info in found_info:
                if file_name not in personal_data_info:
                    personal_data_info[file_name] = [info]
                else:
                    personal_data_info[file_name].append(info)
        else:
            not_personal_data_count += 1

    data = {'Arquivo': [], 'Tipos de Dados': []}
    for file_name, info_list in personal_data_info.items():
        for info in info_list:
            data['Arquivo'].append(file_name)
            data['Tipos de Dados'].append(info)

    df = pd.DataFrame(data)
    fig_icicle = px.icicle(df, path=['Arquivo', 'Tipos de Dados'], width=800, height=600)

    fig_bars = go.Figure()
    fig_bars.add_trace(go.Bar(x=['Contém Dados Pessoais', 'Não Contém Dados Pessoais'],
                              y=[personal_data_count, not_personal_data_count],
                              width=0.4,
                              marker_color=['rgb(255, 0, 0)', 'rgb(0, 255, 0)']))

    fig_bars.update_layout(title='Classificação Geral de Arquivos',
                           xaxis_title='Classificação',
                           yaxis_title='Quantidade')

    fig_icicle.show()
    fig_bars.show()

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        results = classify_files(folder_path)
        display_results(results)

root = tk.Tk()
root.title('Classificação de Arquivos')

def on_button_click():
    folder_path = filedialog.askdirectory()
    if folder_path:
        results = classify_files(folder_path)
        display_results(results)

image_label = tk.Label(root)
image_label.pack(pady=20)
black_lotus_image = tk.PhotoImage(file='black_lotus.png')
image_label.config(image=black_lotus_image)

browse_button = tk.Button(root, text='Selecionar Pasta', command=on_button_click)
browse_button.pack()

root.mainloop()
