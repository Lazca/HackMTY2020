import PySimpleGUI as sg
from control import *

def getErrors():
    errors=[]
    for i in range(0,8):
        if not values[i]:
            errors.append('No debe haber valores nulos')
            break
    if not len(errors):
        if float(values[0]) < 1.5:
            errors.append('La distancia entre mesas debe ser de al menos 1.5 m')
        if 10 > int(values[4]) or int(values[4])>100:
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

    return len(errors)

def update(values,control):
    if getErrors():
        print('exiting')
    else:
        control.updateTable((0,0,float(values[6]),float(values[7])),float(values[0]),float(values[1]),float(values[2]))
        control.setTableCapacity(int(values[5]))
        max=int(int(values[3])*(int(values[4])/100))
        control.setMaxCapacity(max)

    return control.getTables()


if __name__ == "__main__":

    sg.theme("DarkGrey")
    layoutTemp = [
            [sg.Text("Themes: "),sg.Combo(values = ("White","Black","Default"),key = "-Theme-")],
            [sg.Button("Confirm")]]
    windowTemp = sg.Window("Themes",layoutTemp, size = (200,200))

    event,values = windowTemp.read()

    if event == "Confirm" and values["-Theme-"] == "Black":
        print(True)
        theme = "DarkBlack"
    elif event == "Confirm" and values["-Theme-"] == "White":
        theme = "BrightColors"
    else:
        theme = "DarkGrey"

    windowTemp.close()

    sg.theme(theme)
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
            [sg.Button("Enviar", size = (30,2))],
            [sg.Button("Dibujar", size = (30,2))],
            [sg.Graph(canvas_size=(500, 400), graph_bottom_left=(0,0), graph_top_right=(500, 400), background_color='white', key='graph')]]

    window = sg.Window("test",layout,size = (500,600),resizable = True)

    while True:
        event,values = window.read()
        lsTable = update(values,control)

        if event == "Dibujar" and lsTable:
            graph = window['graph']

            for table in lsTable:
                circle = graph.DrawCircle(table.position, 10, fill_color='white',line_color='black')

        if event == sg.WIN_CLOSED:
            break

    window.close()
