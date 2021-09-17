import PySimpleGUI as sg

layout = [
    [sg.Text("Thank you for ordering from us!")],
    [sg.Button("Pizzas")],
    [sg.Button("Your Orders")]
]

window = sg.Window("Dino's Pizzeria", layout)



pizzaLayout = [
    [sg.Text("Choose your pizza,")],
    [sg.Button("Margherita")]
 ]

pizzaWindow = sg.Window("Menu", pizzaLayout)

while True:
    event, values = window.read()
    if event == "Your Orders" or event == sg.WIN_CLOSED:
        break
    if event == "Pizzas":
        window.hide()
        event, values = pizzaWindow.read()
        if event == "Margherita" or event == sg.WIN_CLOSED():
            window.un_hide()
            pizzaWindow.close()
window.close()