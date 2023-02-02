import PySimpleGUI as sg
import threading
import pathlib
import json
import os

dir = os.chdir('../')
sg.ChangeLookAndFeel('Dark')

def json_add(name, username, password):
    file = pathlib.Path("login_info.json")
    if file.exists():
        print ("File exist")

        with open('login_info.json', 'r') as f:
            data = json.load(f)
            with open('login_info.json', 'w') as fs:
                data[name] = [username, password]
                json_object = json.dumps(data, indent=4)
                fs.write(json_object)
                print(data)
    else:
        with open('login_info.json', 'x') as f:
            dictionary = {
                name: [username, password]
            }
            json_object = json.dumps(dictionary, indent=4)
            f.write(json_object)
            print(dictionary)
        


def GUI():
    layout = [
        [sg.Text('Enter what you would like to call this in the JSON file')],
        [sg.InputText(key='-NAME-')],
        [sg.Text('Enter email used for Microsoft Rewards')],
        [sg.InputText(key='-USERNAME-')],
        [sg.Text('Enter password for Microsoft Rewards')],
        [sg.InputText(key='-PASSW-')],
        [sg.Submit()],
        [sg.Cancel()],
    ]
    window = sg.Window('MS Rewards Setup', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        if event == 'Submit':
            t1 = threading.Thread(target = json_add, args =(str(values['-NAME-']), str(values['-USERNAME-']), str(values['-PASSW-'])))
            t1.start()
            break
    t1.join()
    print('thread killed')
    window.close()


def main():
    GUI()



if __name__ == '__main__':
    main()