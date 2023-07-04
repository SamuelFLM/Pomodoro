import threading
import time
import PySimpleGUI as sg
import pyautogui as bot

class InterfacePomodoro:
    def __init__(self, home):
        self.background_color = sg.theme_background_color("#C6E59D")
        self.interface = home()
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()

    def countdown(self, minutes):
        seconds = minutes * 60
        for i in range(seconds, 0, -1):
            if self.stop_event.is_set():
                print("Contagem interrompida")
                break
            while self.pause_event.is_set():
                time.sleep(1)
            remaining_minutes, remaining_seconds = divmod(i, 60)
            self.window['time'].update(f"{remaining_minutes} min {remaining_seconds} seg restantes")
            time.sleep(1)
        else:
            self.window['time'].update("Tempo esgotado!")
            bot.confirm(title="Tempo esgotado!", text="Time Finalizado", buttons=["OK"])

    def pomodoro(self, minutos):
        header = [sg.Image(filename="dependency/img/logo_min.png", background_color=self.background_color,
                           pad=(0, (20, 0)))]
        main = [sg.Text("", background_color=self.background_color, pad=(0, (10, 15)), key="time", font="Inter 11 bold", text_color="black")]
        menu = [
            [sg.Image(filename="dependency/img/voltar.png", background_color=self.background_color, visible=False , enable_events=True, key="voltar"),
                sg.Image(filename="dependency/img/stop.png", background_color=self.background_color, enable_events=True, key="pause"),
             sg.Image(filename="dependency/img/recomecar.png", background_color=self.background_color, enable_events=True, key="recomecar")]
        ]

        layout = [header, main, menu]
        self.window = sg.Window("Pomodoro", layout=layout, size=(226, 274), margins=(0, 0), grab_anywhere=True,
                           element_justification='c', icon="dependency//img//ico.ico", finalize=True)

        t = threading.Thread(target=self.countdown, args=(minutos,))
        t.start()

        while True:
            event, values = self.window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                self.stop_event.set()
                break

            elif event == "pause":
                self.window["voltar"].update(visible=True)
                self.pause_event.set()

            elif event == "voltar":
                self.window.close()
                self.interface.home()
                self.stop_event.set()
                break

            elif event == "recomecar":
                self.window["voltar"].update(visible=False)
                self.pause_event.clear()


if __name__ == "__main__":
    t  = InterfacePomodoro()
    t.pomodoro()

