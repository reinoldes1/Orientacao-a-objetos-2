class Trofeus:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_trofeus(self):
        print('Muitos achievements')

class FinalFantasy(Trofeus):
    def mostrar_trofeus(self):
        print('Muitos achievements no Final Fantasy')

    def busca_trofeus(self, trofeu=None):
        print(f'Mostrando achievements - {trofeu}' if trofeu else 'Mostrando os achievements')

class GTA(Trofeus):
    def mostrar_trofeus(self):
        print('Muitos achievements no GTA')

    def busca_trofeus_nao_desbloqueados(self):
        print('Achievements não desbloqueados')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class SPFan(GTA):
    pass

class SPMPFan(FinalFantasy, GTA):
    pass

class MPFan(FinalFantasy, GTA, Hipster):
    pass

jose = SPFan('José')
jose.busca_trofeus_nao_desbloqueados()

luan = MPFan('Luan')
luan.busca_trofeus_nao_desbloqueados()
luan.busca_trofeus()

luan.mostrar_trofeus()

print(luan)