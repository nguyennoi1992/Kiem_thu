import math

def detect_triangle(x, y, z):
        try:
                a = float(x)
                b = float(y)
                c = float(z)
        except ValueError:
                print("------------------------")
                return -1
        
	atemp = a*a
	btemp = b*b
	ctemp = c*c
	e = 10**-9
	
	if (a <= 0 or a > 2**32 - 1) or (b <= 0 or b > 2**32 - 1) or (c <= 0 or c > 2**32 - 1):
		print("Canh cua tam giac phai lon hon 0 va nho hon 2^32 -1!")
        	return 0
	elif a + b <= c or a + c <= b or b + c <= a:
		print("Day khong la mot tam giac!")
	        return 1
	elif a == b == c:
		print("Day la tam giac deu!")
        	return 2
	elif a == b or b == c or a == c:
                if math.fabs(atemp + btemp - ctemp) <= e or math.fabs(btemp + ctemp - atemp) <= e or math.fabs(atemp + ctemp - btemp) <= e:
                        print("Day la tam giac vuong can!")
                        return 3
		print("Day la tam giac can!")
        	return 4
	elif math.fabs(atemp + btemp - ctemp) <= e or math.fabs(btemp + ctemp - atemp) <= e or math.fabs(atemp + ctemp - btemp) <= e:
		print("Day la tam giac vuong!")
        	return 5
	else:
        	print("Day la tam giac thuong!")
		return 6


print("Tam giac 1")
detect_triangle(4, 4, 4)

print("Tam giac 2")
detect_triangle(4, 4, 5)

print("Tam giac 3")
detect_triangle(4, 3, 5)

print("Tam giac 4")
detect_triangle(4, 0, 5)

print("Tam giac 5")
detect_triangle(-1, 6, 5)

print("Tam giac 6")
detect_triangle(1, math.sqrt(2),1)

print("Tam giac 7")
detect_triangle(1, 1, 2)

print("Tam giac 8")
detect_triangle(3, 4, 6)
