#Definindo configuraçoes

#Importando modulos
import PySimpleGUI as sg
from random import randint

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('GERADOR DE CPF', size=(29, 1), font=("Helvetica", 20), justification='center', relief=sg.RELIEF_RIDGE, text_color='#000080')],
            [sg.Text('QUANTIDADE:'), sg.Slider(range=(0,100), default_value=1, size=(30,20), orientation='h', key='slider')],
            [sg.Button('GerarCPF', key='GerarCPF', size=(14,2), font=("Helvetica", 15), button_color=('white', 'green')), sg.Button('GerarRG', key='GerarRG', size=(15,2), font=("Helvetica",15), button_color=('white', 'blue'))],
            [sg.Output(size=(39,10), key='-OUTPUT-')],
            [sg.Button('CriarTXT', size=(19,2), font=("Helvetica", 15), key='CriarTXT')],
            [sg.Button('Sair', key='Sair', size=(19,2), font=("Helvetica", 15), button_color=('white', 'red'))]
        ]
        #Definindo Janela
        self.janela = sg.Window('Gerador de CPF', element_justification='c').layout(layout)
        self.cpf = []
        self.rg = []

    def iniciar(self): 
        #Extraindo Dados
        while True:
            self.Button, self.values = self.janela.Read()
            for i in range(int(self.values['slider'])):
                #Gerando CPFS
                if self.Button == 'GerarCPF':
                    print(f'CPF: {randint(-1,9)}{randint(0,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}')
                    self.cpf.append(f'CPF: {randint(-1,9)}{randint(0,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}')
                if self.Button == 'GerarRG':
                    print(f'RG: {randint(-1,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}')
                    self.rg.append(f'RG: {randint(-1,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}.{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}')
            if self.Button == 'CriarTXT':
                #Gerando TXT
                with open('CPF_GERADOS.txt', '+wt') as arquivo:
                    for i in self.cpf:
                        arquivo.write(f'{i}\n')
                with open('RG_GERADOS.txt', '+wt') as arquivo:
                    for i in self.rg:
                        arquivo.write(f'{i}\n')
            if self.Button == 'Sair':
                break

'''
    GERADOR DE DOCUMENTOS PYTHON
    By: GABRIEL VINICIUS
'''