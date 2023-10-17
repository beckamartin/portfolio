import unittest
from solution import rot13


class TestRot13(unittest.TestCase):
    def test_rot_13_1(self):
        self.assertEqual(rot13("EBG13 rknzcyr."), "ROT13 example.")

    def test_rot_13_2(self):
        self.assertEqual(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."), "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
    
    def test_rot_13_3(self):
        self.assertEqual(rot13("123"), "123")
    
    def test_rot_13_4(self):
        self.assertEqual(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"), "This is actually the first kata I ever made. Thanks for finishing it! :)")
        
    def test_rot_13_5(self):
        self.assertEqual(rot13("@[`{"), "@[`{")   


if __name__ == "__main__":
    unittest.main()