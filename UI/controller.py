import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        year = int(self._view.dd_anno.value)
        self._model.build_graph(year)


    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO
        team_sel_id = int(self._view.dd_squadra.value)

        vicini = self._model.get_neighbors(team_sel_id)

        self._view.txt_risultato.controls.clear()
        for t, peso in vicini:
            self._view.txt_risultato.controls.append(ft.Text(f"{self._model.teams[t].name}: {peso}"))
        self._view.txt_risultato.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO
        team_sel_id = int(self._view.dd_squadra.value)
        cammino, peso =self._model.compute_best_path(team_sel_id)

        self._view.txt_risultato.controls.clear()
        self._view.txt_risultato.controls.append(ft.Text(f"peso totale: {peso}"))
        for t  in cammino:
            self._view.txt_risultato.controls.append(ft.Text(f"{self._model.teams[t].name}"))
        self._view.txt_risultato.update()



    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO
    def popola_dd_anno(self):
        return [ft.dropdown.Option(str(y)) for y in self._model.get_year()]

    def popola_squadre(self,e):
        year = int(self._view.dd_anno.value)
        self.team_for_year = self._model.get_team_for_year(year)

        self._view.txt_out_squadre.controls.clear()
        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero squadre: {len(self.team_for_year)}"))
        for t in self.team_for_year:
            self._view.txt_out_squadre.controls.append(ft.Text(f'{t}'))
        self._view.txt_out_squadre.update()

        # Popolo dropdown con chiave/id
        self._view.dd_squadra.options = [
            ft.dropdown.Option(text=str(t), key=str(t.id)) for t in self.team_for_year
        ]
        self._view.dd_squadra.value = None
        self._view.dd_squadra.update()

