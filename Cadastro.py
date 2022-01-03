#pegando a biblioteca PySimpleGui, caso naõ tenha, precisa instalar
import PySimpleGUI as sg

#Criando o Layout
sg.theme('LightBrown6')
layoutTela = [
    [sg.Text('Usuário:',size=(8,1)), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha:',size=(8,1)),sg.Input(key='pwd', size=(20,1), password_char='*')],
    [sg.Checkbox('Salvar o seu acesso?', key='salva')],
    [sg.Button('ENTRAR')]

]

#Operando as janelas
janela = sg.Window('Tela de Login', layoutTela)

#Ler os eventos
while True:
    #guarda as informações obtidas pela janela.read() em eventos e valores
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos ==  'ENTRAR' and (valores['usuario'] == "" or valores['pwd'] == ""):
        sg.popup('Informe seu Usuário e Senha')
    elif valores['usuario'] == 'amorim' and valores['pwd'] == '123456':
        sg.popup('Seja Bem Vindo!!!')
        break
    else:
        sg.popup('Digite um usuário válido')

