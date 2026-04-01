import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCorsi = None
        self.btnCercaIscritti= None
        self.insMatricola = None
        self.insNome = None
        self.insCognome = None
        self.btnCercaStudente = None
        self.btnCercaCorsi = None
        self.btnIscrivi = None
        self.txt_result= None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #Row1
        self.ddCorsi=ft.Dropdown(label = "corso", width=500)
        self._controller.fillDDCorsi()
        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                  on_click=self._controller.handleCercaIscritti,
                                                  width=200)
        self.row1 = ft.Row([self.ddCorsi, self.btnCercaIscritti],
                           alignment=ft.MainAxisAlignment.CENTER)


        #Row2
        self.insMatricola = ft.TextField(label="Matricola",
                                         width=200,
                                         hint_text="Inserisci la tua matricola"
                                         )
        self.insNome = ft.TextField(label="Nome",
                                    width=400,
                                    read_only=True
                                    )
        self.insCognome = ft.TextField(label="Cognome",
                                    width=400,
                                    read_only=True,
                                    )
        self.row2 = ft.Row([self.insMatricola, self.insNome, self.insCognome],
                           alignment=ft.MainAxisAlignment.CENTER)

        #row 3
        self.btnCercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                  on_click=self._controller.handleCercaStudente,
                                                  width=200,
                                                  tooltip="Verificia se c'è uno studente")
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi",
                                               on_click=self._controller.handleCercaCorsi,
                                               width=200)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi",
                                            on_click=self._controller.handleIscrivi,
                                            width=200)
        self.row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi, self.btnIscrivi],
                           alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(self.row1,self.row2, self.row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        #self._page.add(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
