import PySimpleGUI as sg 

sg.theme("DarkBlack")


layout = [
        [sg.Text("Distancia entre Mesas: ",size = (30,1)),sg.InputText()],
        [sg.Text("Radio de Mesa: ",size = (30,1)),sg.InputText()],
        [sg.Text("Espacio por Persona: ",size = (30,1)),sg.InputText()],
        [sg.Text("Capacidad Normal: ",size = (30,1)),sg.InputText()],
        [sg.Text("Porcentaje de Capacidad: ",size = (30,1)),sg.InputText()],
        [sg.Text("Capacidad por Mesa: ",size = (30,1)),sg.InputText()],
        [sg.Text("Ancho del Restaurante: ",size = (30,1)),sg.InputText()],
        [sg.Text("Largo del Restaurante: ",size = (30,1)),sg.InputText()],
        [sg.Button("Enviar",auto_size_button = True)]]

window = sg.Window("test",layout,size = (800,600),resizable = True)



while True:
    event,values = window.read()
    print(values)
    if event == sg.WIN_CLOSED:
        break


window.close()
