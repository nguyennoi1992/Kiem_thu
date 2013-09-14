package test_PTB2_junit;

public class GiaiPTB2 {

	public String giai1(double a, double b) {
		if(a == 0 && b == 0){
			return "Phuong trinh co vo so nghiem!";
		}
		
		if( a == 0 && b != 0){
			return "Phuong trinh vo nghiem!";
		}
		
		return "Phuong trinh co 1 nghiem la: x = " + -b/a; 
	}
	
	public String giai2(double a, double b, double c) {
		if(a == 0) {
			return giai1(b, c);
		}
		
		double delta;
		delta = b * b - 4 * a * c;
		
		if(delta < 0){
			return "Phuong trinh vo nghiem!";
		} else if(delta == 0){
			return "Phuong trinh co nghiem kep x1 = x2 = " + -b/(2*a);
		} else {
			double x1 = (-b - Math.sqrt(delta)) / (2 * a);
			double x2 = (-b + Math.sqrt(delta)) / (2 * a);
			
			return "Phuong trinh co 2 nghiem phan biet la: x1 = " + x1 + " x2 = " + x2;
		}
	}
	
//	public static void main(String[] args) {
//	
//		// a = b = 0: Mot nghiem don
//		System.out.println("" + giai2(0, 0, 1));
//		
//		// a = 0, b # 0: Mot nghiem don
//		System.out.println("" + giai2(0, 2, 1));
//		
//		//Vo nghiem
//		System.out.println("" + giai2(1, 4, 100));
//		
//		//Nghiem kep
//		System.out.println("" + giai2(1, -2, 1));
//		
//		//Hai nghiem phan biet
//		System.out.println("" + giai2(1, -7, 12));
//		
//	}
}
