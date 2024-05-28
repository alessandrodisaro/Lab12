from model.model import Model

model = Model()

grafo = model.buildGrafo(2015, str("France"))
print(grafo, sep=" \n")
