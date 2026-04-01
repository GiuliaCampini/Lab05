import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue = None


    def fillDDCorsi(self):

        for c in self._model.get_corsi():
            self._view.ddCorsi.options.append(ft.dropdown.Option(
                key=c.codins,
                data=c,
                text=c,
                on_click=self._choiceDDCodins
            ))

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)

    def handleCercaIscritti(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Nessun corso selezionato")
            return
        iscritti = self._model.get_studenti_iscritti(self._ddCodinsValue.codins)
        if not(iscritti):
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for i in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{i.__str__()}"
                                                              ))

        self._view.update_page()

    def handleCercaStudente(self, e):
        self._view.txt_result.controls.clear()
        if self._view.insMatricola.value.strip() == "":
            self._view.create_alert("Nessuna matricola inserita")
            return
        if not self._view.insMatricola.value.isdigit():
            self._view.create_alert("Matricola inserita errata")
            return
        matricola = int(self._view.insMatricola.value)
        studente = self._model.get_matricolaStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola inserita non esistente")
            return
        self._view.insNome.value = studente.nome
        self._view.insCognome.value = studente.cognome
        self._view.update_page()

    def handleCercaCorsi(self, e):
        self._view.txt_result.controls.clear()
        if self._view.insMatricola.value.strip() == "":
            self._view.create_alert("Nessuna matricola inserita")
            return
        if not self._view.insMatricola.value.isdigit():
            self._view.create_alert("Matricola inserita errata")
            return
        matricola = int(self._view.insMatricola.value)
        corsi = self._model.get_corsi_matricola(matricola)
        if len(corsi) == 0:
            self._view.create_alert("Matricola inserita non esistente")
            return

        self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
        for cor in corsi:
            self._view.txt_result.controls.append(ft.Text(f"{cor}"))
        self._view.update_page()


    def handleIscrivi(self, e):
        self._view.txt_result.controls.clear()
        if self._view.insMatricola.value.strip() == "":
            self._view.create_alert("Nessuna matricola inserita")
            return
        if not self._view.insMatricola.value.isdigit():
            self._view.create_alert("Matricola inserita errata")
            return
        if self._ddCodinsValue is None:
            self._view.create_alert("Nessun corso selezionato")
            return
        matricola = int(self._view.insMatricola.value)
        codins=self._ddCodinsValue.codins
        aggiungi = self._model.add_studCorso(matricola, codins)
        self._view.txt_result.controls.append(ft.Text(aggiungi))
        self._view.update_page()
