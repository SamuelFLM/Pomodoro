import PySimpleGUI as sg
import pyautogui as bot


class InterfacePomodoro:

    def __init__(self):
        self.background_color = sg.theme_background_color("#C6E59D")

    def pomodoro(self):

        header = [sg.Image(filename="dependency/img/logo_min.png", background_color=self.background_color,
                           pad=(0, (20, 0)))]
        main = [sg.Text("30 min restantes", background_color=self.background_color, pad=(0, (10, 15)), key="time", font="Inter 11 bold", text_color="black")]
        menu = [
            [sg.Image(filename="dependency/img/voltar.png", background_color=self.background_color, visible=False),
                sg.Image(filename="dependency/img/stop.png", background_color=self.background_color),
             sg.Image(filename="dependency/img/recomecar.png", background_color=self.background_color)]
        ]

        layout = [header, main, menu]
        window = sg.Window("Pomodoro", layout=layout, size=(226, 274), margins=(0, 0), grab_anywhere=True,
                           element_justification='c', icon="dependency//img//ico.ico")
        while True:
            event, values = window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                break


if __name__ == "__main__":
    t = InterfacePomodoro()
    t.pomodoro()
