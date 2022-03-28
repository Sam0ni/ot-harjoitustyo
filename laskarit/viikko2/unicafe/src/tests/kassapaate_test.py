import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class Testkassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()

    def test_oikea_summa_aluksi(self):
        self.assertEqual(self.paate.kassassa_rahaa / 100, 1000)

    def test_aluksi_edullisia_nolla(self):
        self.assertEqual(self.paate.edulliset, 0)

    def test_aluksi_maukkaita_nolla(self):
        self.assertEqual(self.paate.maukkaat, 0)

    def test_kateismaksu_riittava_ed(self):
        self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)

    def test_kateismaksu_riittava_ed_p(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(500), 260)

    def test_kateismaksu_riittava_ed_l(self):
        self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.edulliset, 1)

    def test_kateismaksu_riittava_ma(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)

    def test_kateismaksu_riittava_ma_p(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(500), 100)

    def test_kateismaksu_riittava_ma_l(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_kateismaksu_ei_riittava_ed(self):
        self.paate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kateismaksu_ei_riittava_ed_p(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(100), 100)

    def test_kateismaksu_ei_riittava_ed_l(self):
        self.paate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.paate.edulliset, 0)

    def test_kateismaksu_ei_riittava_ma(self):
        self.paate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kateismaksu_ei_riittava_ma_p(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(300), 300)

    def test_kateismaksu_ei_riittava_ma_l(self):
        self.paate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.paate.edulliset, 0)

    def test_korttimaksu_riittava_ed(self):
        kortti = Maksukortti(500)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 260)

    def test_korttimaksu_riittava_ed_p(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(kortti), True)

    def test_korttimaksu_riittava_ed_l(self):
        kortti = Maksukortti(500)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.paate.edulliset, 1)

    def test_korttimaksu_riittava_ma(self):
        kortti = Maksukortti(500)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_korttimaksu_riittava_ma_p(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(kortti), True)

    def test_korttimaksu_riittava_ma_l(self):
        kortti = Maksukortti(500)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_korttimaksu_ei_riittava_ed(self):
        kortti = Maksukortti(100)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_korttimaksu_ei_riittava_ed_p(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(kortti), False)

    def test_korttimaksu_ei_riittava_ed_l(self):
        kortti = Maksukortti(100)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.paate.edulliset, 0)

    def test_korttimaksu_ei_riittava_ma(self):
        kortti = Maksukortti(100)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_korttimaksu_ei_riittava_ma_p(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(kortti), False)

    def test_korttimaksu_ei_riittava_ma_l(self):
        kortti = Maksukortti(100)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_korttimaksu_riittava_ed_kassa(self):
        kortti = Maksukortti(500)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_korttimaksu_riittava_ma_kassa(self):
        kortti = Maksukortti(500)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataaminen(self):
        kortti = Maksukortti(500)
        self.paate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo, 1000)

    def test_kortille_rahan_lataaminen_kassa(self):
        kortti = Maksukortti(500)
        self.paate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(self.paate.kassassa_rahaa, 100500)

    def test_kortille_rahan_lataaminen_negatiivinen_summa_kassa(self):
        kortti = Maksukortti(500)
        self.paate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataaminen(self):
        kortti = Maksukortti(500)
        self.paate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(kortti.saldo, 500)