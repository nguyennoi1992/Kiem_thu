import math
import unittest
from triangle import detect_triangle

class Test_Triangle(unittest.TestCase):

    def setUp(self):
        pass
	
	#Kiem tra xau nhap vao khong la so
    def test_Input_Xau_1(self):
        self.assertEqual(detect_triangle("abds", 45.0, 6.0),-1)

    def test_Input_Xau_2(self):
        self.assertEqual(detect_triangle("abds", "def", "ghi"),-1)
	
	#Gia tri nhap vao phai duong
    def test_Canh_Min_1(self):
        self.assertEqual(detect_triangle(4.0, 0.0, 5.0),0)

    def test_Canh_Lon_Min_2(self):
        self.assertEqual(detect_triangle(-1.0, 6.0, 5.0),0)
	
	#Gia tri nhap vao phai nho hon 2**32
    def test_Canh_Max_1(self):
        self.assertEqual(detect_triangle(4.0, 0.0, 2**32),0)

    def test_Canh_Max_2(self):
        self.assertEqual(detect_triangle(-1.0, 6.0, 2**32),0)
	
	#Ba canh tao thanh duong thang
    def test_Duong_Thang_1(self):
        self.assertEqual(detect_triangle(1.0, 1.0, 2.0),1)

    def test_Duong_Thang_2(self):
        self.assertEqual(detect_triangle(10**-9, 1.0, 1+10**-9),1)
	
	#Tam giac deu
    def test_Tam_Giac_Deu_1(self):
        self.assertEqual(detect_triangle(1.0, 1.0, 1.0),2)

    def test_Tam_Giac_Deu_2(self):
		self.assertEqual(detect_triangle('1.0', '1.0', '1.0'),2)

    def test_Tam_Giac_Deu_3(self):
		self.assertEqual(detect_triangle('1.0', 1.0, 1.0),2)

    def test_Tam_Giac_Deu_4(self):
		self.assertEqual(detect_triangle(1.0, '1.0', 1.0), 2)

    def test_Tam_Giac_Deu_5(self):
		self.assertEqual(detect_triangle(1.0, 1.0, '1.0'), 2)

    def test_Tam_Giac_Deu_6(self):
		self.assertEqual(detect_triangle('1.0', '1.0', 1.0),2)

    def test_Tam_Giac_Deu_7(self):
		self.assertEqual(detect_triangle(1.0, '1.0', '1.0'),2)

    def test_Tam_Giac_Deu_8(self):
		self.assertEqual(detect_triangle('1.0', 1.0, '1.0'),2)
	
	#Tam giac vuong can
    def test_Tam_Giac_Vuong_Can_1(self):
        self.assertEqual(detect_triangle(math.sqrt(2), 1.0, 1.0),3)

    def test_Tam_Giac_Vuong_Can_2(self):
        self.assertEqual(detect_triangle(math.sqrt(2)*10**-9, 10**-9, 10**-9),3)

    def test_Tam_Giac_Vuong_Can_3(self):
        self.assertEqual(detect_triangle(math.sqrt(2), 1.0, 1.0),3)

    def test_Tam_Giac_Vuong_Can_4(self):
        self.assertEqual(detect_triangle(1.0, math.sqrt(2), 1.0),3)

    def test_Tam_Giac_Vuong_Can_5(self):
        self.assertEqual(detect_triangle(1.0, 1.0, math.sqrt(2)),3)

    def test_Tam_Giac_Vuong_Can_6(self):
        self.assertEqual(detect_triangle(math.sqrt(2), '1.0', 1.0),3)

    def test_Tam_Giac_Vuong_Can_7(self):
        self.assertEqual(detect_triangle(math.sqrt(2), 1.0, '1.0'),3)

    def test_Tam_Giac_Vuong_Can_8(self):
        self.assertEqual(detect_triangle(math.sqrt(2), '1.0', '1.0'),3)

    def test_Tam_Giac_Vuong_Can_9(self):
        self.assertEqual(detect_triangle('1.0', math.sqrt(2), 1.0),3)

    def test_Tam_Giac_Vuong_Can_10(self):
        self.assertEqual(detect_triangle('1.0', math.sqrt(2), '1.0'),3)

    def test_Tam_Giac_Vuong_Can_11(self):
        self.assertEqual(detect_triangle(1.0, math.sqrt(2), '1.0'),3)

    def test_Tam_Giac_Vuong_Can_12(self):
        self.assertEqual(detect_triangle('1.0', 1.0, math.sqrt(2)),3)

    def test_Tam_Giac_Vuong_Can_13(self):
        self.assertEqual(detect_triangle(1.0, '1.0', math.sqrt(2)),3)

    def test_Tam_Giac_Vuong_Can_14(self):
        self.assertEqual(detect_triangle('1.0', '1.0', math.sqrt(2)),3)
	
	#Tam giac can
    def test_Tam_Giac_Can_1(self):
        self.assertEqual(detect_triangle(4.0, 4.0, 5.0),4)

    def test_Tam_Giac_Can_2(self):
		self.assertEqual(detect_triangle('4.0', 4.0, 5.0),4)

    def test_Tam_Giac_Can_3(self):
		self.assertEqual(detect_triangle('4.0', '4.0', 5.0),4)

    def test_Tam_Giac_Can_4(self):
		self.assertEqual(detect_triangle('4.0', '4.0', '5.0'),4)

    def test_Tam_Giac_Can_5(self):
		self.assertEqual(detect_triangle(4.0, '4.0', 5.0),4)

    def test_Tam_Giac_Can_6(self):
		self.assertEqual(detect_triangle(4.0, '4.0', '5.0'),4)

    def test_Tam_Giac_Can_7(self):
		self.assertEqual(detect_triangle(4.0, 4.0, '5.0'),4)

    def test_Tam_Giac_Can_8(self):
		self.assertEqual(detect_triangle('4.0', 4.0, '5.0'),4)

	#Tam giac can
    def test_Tam_Giac_Vuong_1(self):
        self.assertEqual(detect_triangle(3.0, 4.0, 5.0),5)

    def test_Tam_Giac_Vuong_2(self):
        self.assertEqual(detect_triangle('3.0', 4.0, 5.0),5)

    def test_Tam_Giac_Vuong_3(self):
        self.assertEqual(detect_triangle(3.0, '4.0', 5.0),5)

    def test_Tam_Giac_Vuong_4(self):
        self.assertEqual(detect_triangle(3.0, 4.0, '5.0'),5)

    def test_Tam_Giac_Vuong_5(self):
        self.assertEqual(detect_triangle('3.0', '4.0', 5.0),5)

    def test_Tam_Giac_Vuong_6(self):
        self.assertEqual(detect_triangle(3.0, '4.0', '5.0'),5)

    def test_Tam_Giac_Vuong_7(self):
        self.assertEqual(detect_triangle('3.0', 4.0, '5.0'),5)

    def test_Tam_Giac_Vuong_8(self):
        self.assertEqual(detect_triangle('3.0', '4.0', '5.0'),5)

    def test_Tam_Giac_Vuong_9(self):
        self.assertEqual(detect_triangle(4.0, 3.0, 5.0),5)

    def test_Tam_Giac_Vuong_10(self):
        self.assertEqual(detect_triangle(3.0, 5.0, 4.0),5)

    def test_Tam_Giac_Vuong_11(self):
        self.assertEqual(detect_triangle(5.0, 4.0, 3.0),5)

    def test_Tam_Giac_Vuong_12(self):
        self.assertEqual(detect_triangle(5.0, 10.0, math.sqrt(125)),5)

    def test_Tam_Giac_Vuong_13(self):
        self.assertEqual(detect_triangle(5.0, math.sqrt(125), 10.0),5)

    def test_Tam_Giac_Vuong_14(self):
        self.assertEqual(detect_triangle(10.0, math.sqrt(125), 5.0),5)

    def test_Tam_Giac_Vuong_15(self):
        self.assertEqual(detect_triangle(10.0, 5.0, math.sqrt(125)),5)

    def test_Tam_Giac_Vuong_16(self):
        self.assertEqual(detect_triangle('5.0', 10.0, math.sqrt(125)),5)

    def test_Tam_Giac_Vuong_17(self):
        self.assertEqual(detect_triangle(5.0, '10.0', math.sqrt(125)),5)

    def test_Tam_Giac_Vuong_18(self):
        self.assertEqual(detect_triangle('5.0', '10.0', math.sqrt(125)),5)
        
	#Tam giac thuong
    def test_Tam_Giac_Thuong_1(self):
        self.assertEqual(detect_triangle(3.0, 4.0, 6.0),6)

    def test_Tam_Giac_Thuong_2(self):
        self.assertEqual(detect_triangle(3.0, 2.0, math.sqrt(3)),6)

if __name__ == '__main__':
    unittest.main()
