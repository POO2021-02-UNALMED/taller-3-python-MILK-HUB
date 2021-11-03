from televisores.tv import TV

class Control:
    def __init__(self):
        self._tv = "TV"
    
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

    def setCanal(self,canal):
        self._tv.setCanal(canal)

    def enlazar(self,televisor):
        self._tv = televisor
        televisor._control = self

    def getTv(self):
        return self._tv
    def setTv(self,televisor):
        self._tv = televisor

    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()