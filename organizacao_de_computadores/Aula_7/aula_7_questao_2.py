class MemRAM:
    def __init__(self):
        self.memoria = list()
        for c in range(0, 1024):
            self.memoria.append(0)
        
    def LerMem(self, endereco):
        return self.memoria[endereco - 1]

    def EscreverMem(self, endereco, dado):
        self.memoria[endereco - 1] = dado
    def print_RAM(self):
        print(self.memoria)

# Programa Principal
minhaRAM = MemRAM()
minhaRAM.EscreverMem(4, 245)
minhaRAM.EscreverMem(11, 25)
minhaRAM.EscreverMem(2, 45)
minhaRAM.EscreverMem(31, 52)
minhaRAM.EscreverMem(7, 10)
print(minhaRAM.LerMem(31))
for c in range(0, 10):
    print(minhaRAM.LerMem(c))