import PySimpleGUI as sg
import pyautogui as bot
from interface_pomodoro import InterfacePomodoro


class InterfaceHome:

    def __init__(self):
        self.background_color = sg.theme_background_color("#C6E59D")

    def home(self):

        header_imagem = [sg.Image(filename="dependency/img/logo_max.png", background_color=self.background_color,
                                pad=(0, (30, 0)))]

        main = [
            [sg.Input(default_text="", key="input_usuario", pad=(30, (45, 0)), size=(7, 5), font="Inter 12 bold",
                        disabled=True,border_width=0, background_color=self.background_color,justification='c',
                      disabled_readonly_background_color=self.background_color),

            sg.Image(filename="dependency//img//chevron-up-24.png", background_color=self.background_color,
                     pad=(30, (45, 0)), enable_events=True, key="aumenta_time"),

            sg.Image(filename="dependency//img//chevron-down-24.png", background_color=self.background_color,
                     pad=(0, (45, 0)), enable_events=True, key="diminui_time"),],

            [sg.HSep(pad=(20, (5, 0)), color="black")],
        ]

        rodape = [
             sg.Image(filename="dependency//img//iniciar sessao (1).png", background_color=self.background_color,
                      pad=(0, (45, 0)), enable_events=True, key="iniciar_sessao_de_foco")]

        layout = [header_imagem, main, rodape]
        window = sg.Window("Sessão de foco", layout=layout, size=(272, 442), margins=(0, 0), grab_anywhere=True,
                           element_justification='c', icon="dependency//img//ico.ico", finalize=True)
        count = 30
        window["input_usuario"].update(f"30 min")
        while True:
            event, values = window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                break


            if event == "iniciar_sessao_de_foco" and int(count) == 0:
                bot.confirm(title="Aviso", text="Time nâo pode ser 0", buttons=["OK"])

            if event == "iniciar_sessao_de_foco" and int(count) >= 1:
                window.close()
                interface = InterfacePomodoro(InterfaceHome)
                interface.pomodoro(minutos=int(count))
                break

            if event == "aumenta_time":
                count += 1
                window["input_usuario"].update(f"{count} min")

            if event == "diminui_time":
                if count != 0:
                    count -= 1
                    window["input_usuario"].update(f"{count} min")

if __name__ == "__main__":
    home = InterfaceHome()
    home.home()
