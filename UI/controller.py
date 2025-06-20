import flet as ft

from model.nerc import Nerc

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()

        self.years = None
        self.hours = None
        self.ner = None

    def handleWorstCase(self, e):
        self.read_years()
        self.read_hours()
        self.read_nerc()
        self._model.worstCase(self.ner, self.hours, self.years)
        self._view.load_output(self, self.ner, self.hours, self.years, self._model._bestTotAff,  self._model._solBest)

    def fillDD(self):
        nercList = self._model.listNerc
        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(key= n, text= n.__str__()))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v

    def read_years(self):
        self.years = self._view._txtYears.value
        print(self.years)

    def read_hours(self):
        self.hours = self._view._txtHours.value
        print(self.hours)

    def read_nerc(self):
        self.ner = self._view._ddNerc.value
        print(self.ner)
