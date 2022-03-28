import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")
    
    def test_ei_voi_ladata_negatiivista_summaa(self):
        self.kortti.lataa_rahaa(-2)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_voi_ostaa_kun_vain_tasaraha(self):
        kortti = Maksukortti(2.5)
        kortti.syo_edullisesti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.0 euroa")

    def test_syo_maukkaasti_voi_ostaa_kun_vain_tasaraha(self):
        kortti = Maksukortti(4)
        kortti.syo_maukkaasti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 0 euroa")