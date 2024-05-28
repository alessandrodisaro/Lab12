import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}
        # roba ricrosione
        self.pesoParziale = 0
        self.bestPeso = 0
        self.bestPath = []



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
                    if edge[0][0] != edge[0][1]:
                        self.grafo.add_edge(v0, v1, peso=int(edge[0][2]))

            print(f"archi: {len(self.grafo.edges)}")




    def calcolaVolumi(self):
        results = []
        for v0 in self.grafo.nodes:
            volume = 0
            for v1 in self.grafo.neighbors(v0):
                volume += self.grafo[v0][v1]["peso"]


            results.append((v0, volume))

        return results

    def inizializzazioneRicorsione(self, limite):
        parziale = []
        parziale.append(self.idMap[self.grafo.nodes[0]])
        path = self.ricorsione(parziale, limite, self.pesoParziale)

        return path, self.pesoParziale


    def ricorsione(self, parziale, limite):
        # condizione terminale
        if len(parziale) == limite:
            pesoDaValutare = self.calcolaPeso(parziale)
            if(pesoDaValutare > self.bestPeso):
                self.bestPath = copy.deepcopy(parziale)
                self.bestPeso = pesoDaValutare

        # continuo
        else:
            for vicino in self.grafo.neighbors(parziale[-1]):
                parziale.append(vicino)
                pesoTmp = self.calcolaPeso(parziale)

                # QUI METTERE QUALCOSA DEL TIPO UN CHECK PER VEDERE SE RIESCO GIA ATAGLIARE LA RICERCA

                self.ricorsione(parziale, limite)
                parziale.pop()


    def calcolaPeso(self, parziale):
        peso = 0
        # da qui provo con u, v

        # v = parziale[0]
        # if parziale[-1] != v:
        #
        #     for u in parziale:
        #         peso += self.grafo[v][u]["peso"]

        ####### OPPURE FALLO CON INDICI (SOLUZIONE ALTERNATIVA)
        v = parziale[0]
        if parziale[-1] != v:
            for i in range(len(parziale)-1):  # CONTROLLA SE QUESTO INDICE NON SFORA
                v = parziale[i]
                u = parziale[i+1]
                peso += self.grafo[v][u]["peso"]
        else:
            return 0  # se ho un solo nodo NON HO ARCHI quindi il peso sara' zero

        # se non entra nell esle ritorna il peso
        return peso


            # DA CONTINUARE QUESTA PARTE








