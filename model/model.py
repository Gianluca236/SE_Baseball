from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.teams=DAO.get_team()
        self.K = 3

    def build_graph(self,year):
        self.G = nx.Graph()

        team_for_year=self.get_team_for_year(year)

        self.G.add_nodes_from(t.id for t in team_for_year)

        for i,u in enumerate(team_for_year):
            for v in team_for_year[i+1:]:
                self.G.add_edge(u.id,v.id,weight=u.salari+v.salari)


    def get_year(self):

        years=[]

        for i in self.teams.values():
            if i.year not in years:
                years.append(i.year)

        return years

    def get_team_for_year(self, year):
        team_for_year=[]
        for team in self.teams.values():
            if team.year == year:
                team_for_year.append(team)

        return team_for_year

    def get_neighbors(self, team):
        vicini = []
        for n in self.G.neighbors(team):
            w = self.G[team][n]["weight"]
            vicini.append((n, w))
        return sorted(vicini, key=lambda x: x[1], reverse=True)

    def compute_best_path(self, start):
        """Calcola percorso di peso massimo con archi strettamente decrescenti"""
        self.best_path = []
        self.best_weight = 0
        self._ricorsione([start], 0, float("inf"))
        return self.best_path, self.best_weight

    def _ricorsione(self, path, weight, last_edge_weight):
        last = path[-1]
        if weight > self.best_weight:
            self.best_weight = weight
            self.best_path = path.copy()

        vicini = self.get_neighbors(last)
        neighbors = []
        counter = 0
        for node, edge_w in vicini:
            if node in path:
                continue
            if edge_w <= last_edge_weight:
                neighbors.append((node, edge_w))
                counter += 1
                if counter == self.K:
                    break

        for node, edge_w in neighbors:
            path.append(node)
            self._ricorsione(path, weight + edge_w, edge_w)
            path.pop()


