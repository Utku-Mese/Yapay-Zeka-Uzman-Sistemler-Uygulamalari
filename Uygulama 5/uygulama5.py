from experta import *


class DisAgrisı(Fact):
    """Diş ağrısı ile ilgili belirtileri temsil eden sınıf"""
    pass


class DisAgrisıUzmanSistemi(KnowledgeEngine):
    @Rule(DisAgrisı(dis_eti_kanamasi=True))
    def kural1(self):
        print("Diş hastalığı var, diş hekimine başvur.")

    @Rule(DisAgrisı(dis_eti_kanamasi=True, uzun_sureli_kanama=True))
    def kural2(self):
        print("Diş eti çekilmesi var, diş hekimine başvur.")

    @Rule(DisAgrisı(dis_eti_cekilmesi=True, dis_koku_gorunuyor=True))
    def kural3(self):
        print("Dolgu yaptır.")

    @Rule(DisAgrisı(renk_degisimi=True))
    def kural4(self):
        print("Dişleri temizle.")

    @Rule(DisAgrisı(yeni_dis_cikma=True, morarma=True))
    def kural5(self):
        print("Diş hekimine başvur.")

    @Rule(DisAgrisı(curuk_var=True, agri_yapmiyor=True))
    def kural6(self):
        print("Dolgu yaptır.")

    @Rule(DisAgrisı(curuk_ileri_derece=True))
    def kural7(self):
        print("Kanal tedavisi ve dolgu yaptır.")


# Uzman sistemin çalıştırılması
sistem = DisAgrisıUzmanSistemi()
sistem.reset()

# Örnek verilerle çalıştırma
sistem.declare(DisAgrisı(dis_eti_kanamasi=True, uzun_sureli_kanama=True))
sistem.run()
