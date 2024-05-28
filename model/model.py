import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}


    def getAllNazioni(self):
        return DAO.getAllNazioni()

    def getAnni(self):
        return DAO.getAnni()

    def getNumNodi(self):
        return self.grafo.number_of_nodes()

    def getNumArchi(self):
        return self.grafo.number_of_edges()


    def buildGrafo(self, anno, nazione):
        nodi = DAO.getAllNodes(nazione)
        self.grafo.add_nodes_from(nodi)
        for nodo in nodi:
            self.idMap[nodo.Retailer_code] = nodo
        # CON LA QUERY CHE CONTA DIRETTAMENTE TUTTO
        # archi = DAO.getAllEdges(anno, nazione)

        # CALCOLANDO INTERNAMENTE DA PYTHON
        for v0 in nodi:
            for v1 in nodi:
                edge = DAO.getArco(v0, v1, anno)

                if edge[0][0] is not None and edge[0][1] is not None:
                    self.grafo.add_edge(edge[0][0], edge[0][1], weigth=edge[0][2])

        results = []
        for v0 in self.grafo.nodes:
            volume = 0
            for arco in self.grafo.neighbors(v0):
                volume += arco[1]

            results.append((v0, volume))

        return results


