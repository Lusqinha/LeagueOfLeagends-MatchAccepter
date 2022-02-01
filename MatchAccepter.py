from pyautogui import locateOnScreen, click, moveTo
from PySimpleGUI import Text, Button, Output, WIN_CLOSED, Window, theme



def accept(x, y):
    moveTo(x, y)
    click()
    pass

def send_notification():
    status = 'Partida aceita!'
    print (status)


def check_screen():
    locate = locateOnScreen('acceptButton.png', confidence=0.7)
    if locate != None:
        accept(locate.left, locate.top)
        return True
    return False

def main():
    print('Procurando partida...')
    while True:
        if check_screen():
            send_notification()
            break
    

theme('DarkBrown1')

layout = [
    [Text('Para o programa funcionar, o Client deve ser estar na tela principal.')],
    [Button('Iniciar')],
    [Output(size=(50,3))]
]

window = Window('AceitaLoL', layout)

while True:
    event, values = window.read()
    if event == WIN_CLOSED:
        break
    if event == 'Iniciar':
        main()
        
        
window.close()