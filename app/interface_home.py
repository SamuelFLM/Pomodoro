import PySimpleGUI as sg


class Home:

    def __init__(self):
        self.background_color = sg.theme_background_color("#C6E59D")

    def front(self):

        head_imagem = [sg.Image(filename="dependency/img/logo_max.png", background_color=self.background_color,
                                pad=(0, (30, 0)))]

        main = [
            [sg.Input("0 min", key="input_usuario", pad=(30, (45, 0)), size=(7, 5), font="Inter 12 bold",
                      disabled=True, border_width=0, background_color=self.background_color,
                      disabled_readonly_background_color=self.background_color),

             sg.Image(filename="dependency//img//chevron-up-24.png", background_color=self.background_color,
                      pad=(30, (45, 0)), enable_events=True, key="aumenta_time"),

             sg.Image(filename="dependency//img//chevron-down-24.png", background_color=self.background_color,
                      pad=(0, (45, 0)), enable_events=True, key="diminui_time"),

             ],
            [sg.HSep(pad=(20, (5, 0)), color="black")],
        ]

        rodape = [
             sg.Image(filename="dependency//img//iniciar sessao (1).png", background_color=self.background_color,
                      pad=(0, (45, 0)), enable_events=True, key="iniciar_sessao_de_foco")]
        test = [sg.Button("test")]

        layout = [head_imagem, main, rodape, test]
        window = sg.Window("Sessão de foco", layout=layout, size=(272, 442), margins=(0, 0), grab_anywhere=True,
                           element_justification='c', icon="dependency//img//ico.ico")
        return  window


    def back(self, window):
        while True:

            event, values = window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                break

            if event == "iniciar_sessao_de_foco":
                print("1")

    def main(self):
        home = Home()
        home.back(home.front())

if __name__ == "__main__":
    home = Home()
    home.main()
