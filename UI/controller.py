import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        nazioni = self._model.getAllNazioni()
        anni = self._model.getAnni()
        for nazione in nazioni:
            self._view.ddcountry.options.append(ft.dropdown.Option(nazione))
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))
        self._view.update_page()



    def handle_graph(self, e):
        nodi, archi = self._model.buildGrafo(self._view.ddyear.value, self._view.ddcountry.value)
        if nodi is None or archi is None:
            self._view.txtOut2.clean()
            self._view.txtOut2.controls.append(ft.Text(f"Il grafo e' vuoto"))
            return
        self._view.txtOut2.clean()
        self._view.txtOut2.controls.append(ft.Text(f"Il grafo creato ha {self._model.getNumNodi()} nodi e {self._model.getNumArchi} archi"))
        for arco in archi:
            self._view.txtOut2.controls.append(ft.Text(f"{self._model.idMap[arco[0]]} :"))


        self._view.update_page()



    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
