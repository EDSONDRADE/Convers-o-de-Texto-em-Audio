import PySimpleGUI as sg
import pyttsx3
sg.theme('DarkBrown4')  


layout = [
      [sg.Text(f'SELECIONE UM ARQUIVO TXT PARA CONVERTER!')],
      [sg.Text('Source for Files ', size=(15, 1)), sg.Input(key='-FILE-'), sg.FileBrowse('Arquivo')],
      [sg.Submit('PLAY'), sg.Button('Exit')]]

window = sg.Window('Rename Files or Folders', layout, enable_close_attempted_event=True)

janela = window
while True:
    eventos, valores = janela.read()
    if window == janela and eventos == sg.WIN_CLOSED:
        break
    if eventos =='PLAY':
        if valores['-FILE-'] != None:
            print(valores['-FILE-'])
            print(valores['Arquivo'])
            file = valores['Arquivo']
            if file.split(".")[-1] == 'txt':
                print(file.split(".")[-1])
                with open(file, 'r', encoding="utf8") as f:
                    texto = f.read()

                    speaker = pyttsx3.init() 
                    voices = speaker.getProperty('voices') 
             
                    speaker.setProperty("voice","Brazil") 
                    rate = speaker.getProperty('rate')
                    speaker.setProperty('rate', rate-25) 

                    print(texto) 
                    speaker.say(texto)
                    speaker.runAndWait() 
                    if (eventos == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or eventos == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':

                        f.close() 
                    
    elif (eventos == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or eventos == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
                                break   
window.close()


