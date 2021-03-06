import PySimpleGUI as sg
import tkinter
from tkinter import *
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
        if int(values[7]) > int(values[6]):
            errors.append('El ancho debe ser mayor o igual a el ancho')

    for error in errors:
        sg.Popup(error,title='error', keep_on_top=True, any_key_closes=True)

    return len(errors)

def update(values,control,layout):
    if getErrors():
        print('exiting')
    else:
        control.updateTable((0,0,float(values[6]),float(values[7])),float(values[0]),float(values[1]),float(values[2]))
        control.setTableCapacity(int(values[5]))
        max=int(int(values[3])*(int(values[4])/100))
        control.setMaxCapacity(max)
        layout[8][1].Update(value=0)
        layout[9][1].Update(value=control.getMaxCapacity())
    return control.getTables()

def remap(value, oldLow, oldHigh, newLow, newHigh):
    return newLow + (newHigh - newLow)*((value -oldLow)/(oldHigh - oldLow ))

if __name__ == "__main__":

    sg.theme("DarkGrey")
    control=Control([],0,0)

    layout = [
            [sg.Text("Distancia entre Mesas: ",size = (30,1)),sg.InputText()],                          #0
            [sg.Text("Radio de Mesa: ",size = (30,1)),sg.InputText()],                                  #1
            [sg.Text("Espacio por Persona: ",size = (30,1)),sg.InputText()],                            #2
            [sg.Text("Capacidad Normal: ",size = (30,1)),sg.InputText()],                               #3
            [sg.Text("Porcentaje de Capacidad: ",size = (30,1)),sg.InputText()],                        #4
            [sg.Text("Capacidad por Mesa: ",size = (30,1)),sg.InputText()],                             #5
            [sg.Text("Ancho del Restaurante: ",size = (30,1)),sg.InputText()],                          #6
            [sg.Text("Largo del Restaurante: ",size = (30,1)),sg.InputText(),],                         #7
            [sg.Text("Gente Dentro: ",size=(30,1),text_color = "green"),sg.InputText(disabled=True, text_color='black')],                    #8
            [sg.Text("Cupo Limite: ",size=(30,1),text_color = "green"),sg.InputText(disabled=True,text_color='black')],                     #9
            [sg.Text("Sentar Grupo de tamaño: ",size=(30,1),text_color = "green"),sg.InputText()],      #10
            [sg.Text("Desalojar Mesa No: ",size=(30,1),text_color = "green"),sg.InputText()],           #11
            [sg.Button("Enviar", size = (30,1)), sg.Button("Dibujar", size = (30,1))],
            [sg.Button("Sentar", size = (30,1)), sg.Button("Desalojar", size = (30,1))],
            [sg.Graph(canvas_size=(475, 475),graph_bottom_left=(0,0), graph_top_right=(475, 475), background_color='white', key='graph',drag_submits = True)]
           ]

    window = sg.Window("CoSMaS",layout,finalize = True,icon = "restaurant.ico")
    window.Maximize()

    while True:
        event,values = window.read()
        if event=="Enviar":
            lsTable = update(values,control,layout)

        if event == "Dibujar" and lsTable:
            # dibujar mesas
            graph = window['graph']
            graph.TKCanvas.delete('all')

            h = int(values[7])/int(values[6])*450
            offset = (475 - h)/2

            for index, table in enumerate(control.getTables()):
                x,y = table.position
                x = remap(x,0,int(values[6]),25,450)
                y = remap(y,0,int(values[7]),25 + offset,h - 25 + offset)

                if table.capacity == 0:
                    fill_color = 'green'
                else:
                    fill_color = 'red'

                graph.DrawCircle((x,y), 10, fill_color,line_color='black')
                graph.DrawText(str(index), (x,y), color='white')
        if event=='Sentar' and values[10]:
            control.setMaxCapacity(int(values[9]))
            error=control.sentar_grupo(int(values[10]))
            if error:
                sg.Popup(error,title='error', keep_on_top=True, any_key_closes=True)
            else:
                print(control.getCapacity())
                layout[8][1].Update(value=control.getCapacity())
                for index, table in enumerate(control.getTables()):
                    x,y = table.position
                    x = remap(x,0,int(values[6]),25,450)
                    y = remap(y,0,int(values[7]),25 + offset,h - 25 + offset)

                    if table.capacity == 0:
                        fill_color = 'green'
                    else:
                        fill_color = 'red'
                    graph.DrawCircle((x,y), 10, fill_color,line_color='black')
                    graph.DrawText(str(index), (x,y), color='white')
        if event == 'Desalojar' and values[11]:
            control.vaciar_mesa(int(values[11]))
            for index, table in enumerate(control.getTables()):
                x,y = table.position
                x = remap(x,0,int(values[6]),25,450)
                y = remap(y,0,int(values[7]),25 + offset,h - 25 + offset)

                if table.capacity == 0:
                    fill_color = 'green'
                else:
                    fill_color = 'red'
                graph.DrawCircle((x,y), 10, fill_color,line_color='black')
                graph.DrawText(str(index), (x,y), color='white')
        if event == sg.WIN_CLOSED:
            break

    window.close()
