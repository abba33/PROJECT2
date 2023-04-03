import PySimpleGUI as psg
import pyttsx3

voice = pyttsx3.init()
voice_type = voice.getProperty('voices')



layout = [[psg.Text('Select your type of voice:',text_color='white', background_color='maroon'),
           psg.Radio('Male', 'RADIO1', default=True, key='male',background_color='maroon',text_color = 'black'),
           psg.Radio('Female', 'RADIO1', key='female',background_color='maroon',text_color = 'black')],
          [psg.Text('Enter text to speak🔊:',text_color='white',background_color='maroon',)],
          [psg.InputText(key='input'),psg.Button('Speak', button_color='white')],]

window = psg.Window('My text to speech app❤️', layout,background_color='maroon')

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            voice.setProperty('voice', voice_type[0].id)
        elif values['female']:
           voice.setProperty('voice', voice_type[1].id) 
    
        voice.say(text)
        voice.runAndWait()

window.close()