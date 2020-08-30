import PySimpleGUI as sg
from control import *

def update(values,control):
    control.updateTable((0,0,float(values[6]),float(values[7])),float(values[0]),float(values[1]),float(values[2]))
    control.setTableCapacity(int(values[5]))
    max=int(int(values[3])*(int(values[4])/100))
    control.setMaxCapacity(max)
    print(max)

if __name__ == "__main__":

    sg.theme("DarkBlack")
    control=Control([],0,0)

    layout = [
            [sg.Text("Distancia entre Mesas: ",size = (30,1)),sg.InputText()],  #0
            [sg.Text("Radio de Mesa: ",size = (30,1)),sg.InputText()],          #1
            [sg.Text("Espacio por Persona: ",size = (30,1)),sg.InputText()],    #2
            [sg.Text("Capacidad Normal: ",size = (30,1)),sg.InputText()],       #3
            [sg.Text("Porcentaje de Capacidad: ",size = (30,1)),sg.InputText()],#4
            [sg.Text("Capacidad por Mesa: ",size = (30,1)),sg.InputText()],     #5
            [sg.Text("Ancho del Restaurante: ",size = (30,1)),sg.InputText()],  #6
            [sg.Text("Largo del Restaurante: ",size = (30,1)),sg.InputText()],  #7
            [sg.Button("Enviar",auto_size_button = True)]]

    window = sg.Window("test",layout,size = (800,600),resizable = True)

    while True:
        event,values = window.read()
        update(values,control)
        if event == sg.WIN_CLOSED:
            break

            window.close()
