import PySimpleGUI as sg
from random import randint

class Dado:
    
    def __init__(self):
        self.valor_dado = 0
        self.valor_min = 1
        self.valor_max = 6

    def Iniciar(self):
        sg.ChangeLookAndFeel('LightBrown5')
        layout=[
                [sg.Button('jogue o dado', button_color=('white','orange'))],
                ]
        window = sg.Window('Clique no botão', layout)  
        
        while True:
            event, values = window.read()
            if event in (None, 'Cancel'):	
                break
            
            if event == 'jogue o dado':
                window.close()
                self.CarregarDado()            
        window.close()

    def CarregarDado(self):
        sg.ChangeLookAndFeel('LightBrown5')
        g1 = r'imagens\dado.gif' 
        layout_dado=[
                [sg.Exit('Sair do dado', button_color=('white','orange')), 
                sg.Button('Sair da aplicação', button_color=('white','red'))],
                [sg.Text('O dado está girando!')],
                [sg.Image(key='-IMAGE-')],
                [sg.Button('Gerar Valor')],
                ]
        window = sg.Window('Esse é o dado', layout_dado)
        image =  window['-IMAGE-']
        
        while True:
            event, values = window.read(timeout=100)
            image.update_animation(g1)
            
            if event in (None, 'Cancel'):	
                break
            
            if event == 'Gerar Valor':
                self.GerarValor()
                sg.popup('O valor que caiu no dado foi:', self.valor_dado, 
                            no_titlebar=True,
                            background_color='grey')
                window.close()
                self.CarregarDado()
                
            if event == 'Sair do dado':                
                window.close()
                self.Iniciar()
            
            if event == 'Sair da aplicação':
                break      
                
    def GerarValor(self):       
        self.valor_dado = randint(self.valor_min, self.valor_max)


dado = Dado()
dado.Iniciar()