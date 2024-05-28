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
        self._model.buildGrafo(self._view.ddyear.value, self._view.ddcountry.value)

        self._view.txtOut2.clean()
        if self._model.grafo is not None:
            self._view.txtOut2.controls.append(ft.Text("Grafo creato correttamente"))
        else:
            self._view.txtOut2.controls.append(ft.Text("Grafo vuoto"))

        self._view.update_page()



    def handle_volume(self, e):
        volumi = self._model.calcolaVolumi()  # volumi e' un tupla come (Retailer, peso)
        volumi.sort(key=lambda x: x[1], reverse=True)
        self._view.txtOut2.clean()
        self._view.txtOut2.controls.append(
            ft.Text(f"Il grafo creato ha {self._model.getNumNodi()} nodi e {len(self._model.grafo.edges)} archi"))
        for elem in volumi:
            self._view.txtOut2.controls.append(ft.Text(f"{elem[0]} --> {elem[1]} :"))
        self._view.update_page()

    def handle_path(self, e):
        path, pesoTot = self._model.inizializzazioneRicorsione(self._view.txtN.value):

