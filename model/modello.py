import copy
import time

from database.DAO import DAO

class Model:
    def __init__(self):
        self._solBest = None
        self._bestTotAff = 0
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()


    def worstCase(self, nerc, maxY, maxH):
        pos=0
        print("qui")
        eventi = self.loadEvents(nerc)
        self.ricorsione(eventi, [], maxY, maxH, pos)


    def is_ammissibile(self, parziale, maxY, maxH):
        if parziale == []:
            return True
        if (parziale[0]._date_event_began.year - parziale[-1]._date_event_began.year) > maxH:
            return False
        sumY = 0
        for e in parziale:
            delta = (e._date_event_finished - e._date_event_began).total_seconds()
            sumY += float((delta/60)/60)
            print(sumY)
        return sumY <= maxY

    def ricorsione(self, eventi, parziale, maxY, maxH, pos):
        if self.is_ammissibile(parziale, maxY, maxH) == False:
            print("stop")
            return
        else:
            totAff = 0
            for e in parziale:
                totAff += e._customers_affected
            if totAff > self._bestTotAff:
                self._solBest = copy.deepcopy(parziale)
                self._bestTotAff = totAff
            for i in range(pos, len(eventi)):
                parziale.append(eventi[i])
                self.ricorsione(eventi, parziale, maxY, maxH, i + 1)
                parziale.pop() #BACKTRACKING

    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)
        return self._listEvents

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc


if __name__ == "__main__":
    m = Model()
    tic = time.time()
    m.worstCase(m._listNerc[1], 200, 4)
    tac = time.time()
    print(f"Elapsed time: {tac-tic}")
    for e in m._solBest:
        print(e)
    print(m._bestTotAff)
    print(m._solBest)


