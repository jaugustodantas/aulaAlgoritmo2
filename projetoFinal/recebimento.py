class recebimento: 
    def __init__(self,pesoBruto,taraCarreta,saidaCampo,chegadaUbs,entradaUbs,saidaUbs,campo):
        self.pesoBruto = pesoBruto
        self.taraCarreta = taraCarreta
        self.saidaCampo = saidaCampo
        self.chegadaUbs = chegadaUbs
        self.entradaUbs = entradaUbs
        self.saidaUbs = saidaUbs
        self.campo = campo

    def calculoPesoLiquido(self, pesoBruto,taraCarreta):
        return pesoBruto - taraCarreta
