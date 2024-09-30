class LabInit:
    def __init__(self) -> None:
        self.votos = {}
        self.votos[1] = 2

    def showVotos(self):
     print(self.votos[1])
    
    def registraVotos(self,numCamisa):
       
    #    self.votos[numCamisa] = self.votos[numCamisa] + 1 
       self.votos[numCamisa] = self.votos.get(numCamisa,0)+1
       print("Voto registrado para camisa ", numCamisa)
       self.votos[numCamisa] = self.votos.get(numCamisa,0)+1

       print("\n\n total de votos para ",numCamisa," é ",self.votos[numCamisa])

l = LabInit()
l.showVotos()
l.registraVotos(3)