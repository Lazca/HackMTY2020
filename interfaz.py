import PySimpleGUI as sg
from control import *

def getErrors():
    errors=[]
    if float(values[0]) < 1.5:
        errors.append('La distancia entre mesas debe ser de al menos 1.5 m')
    if int(values[4]) <=10 or int(values[4]) >100:
        errors.append('Introduzca un valor de ocupacion por porcentaje entre 10 y 100')
    if int(values[6]) <= 0 or int(values[7]) <=0:
        errors.append('Introduzca medidas validas')
    if int(values[5]) <1:
        errors.append('La capacidad por mesa debe ser de al menos una persona')
    if float(values[1])<0.5:
        errors.append('el radio de la mesa debe ser de al menos 0.4 m')
    if int(values[3]) < 10:
        errors.append('la capacidad normal debe ser de al menos 10 personas')

    for error in errors:
        sg.Popup(error,title='error', keep_on_top=True, any_key_closes=True)

    return len(error)

def update(values,control):
    if getErrors():
        print('exiting')
        return

    control.updateTable((0,0,float(values[6]),float(values[7])),float(values[0]),float(values[1]),float(values[2]))
    control.setTableCapacity(int(values[5]))
    max=int(int(values[3])*(int(values[4])/100))
    control.setMaxCapacity(max)


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
