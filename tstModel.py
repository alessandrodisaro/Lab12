from model.model import Model

model = Model()

grafo = model.buildGrafo(2015, str("France"))
print(f"{model.grafo.number_of_nodes() - model.grafo.number_of_edges()}")

path, peso = model.inizializzazioneRicorsione(5)
for nodo in path:
    print(nodo)
print(f"peso tot: {peso}")
