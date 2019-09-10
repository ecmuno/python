class Neuronio:
    def __init__(self, vetor):
        self.vetor=vetor
    def sigma(self):
        import numpy as np
        import random
        vect=np.array(self.vetor)
        dim=vect.size
        peso=np.random.random(dim)
        bias=np.random.random(1)
        r=0
        res=vect*peso.T
        for v in res:
          r+=v
        r+=bias[0]
        return r



lista1=[1,2,3,4,34,56,12,0.1,0.224]
c=Neuronio(lista1)

saida=c.sigma()
print saida
