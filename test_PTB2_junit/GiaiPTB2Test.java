package test_PTB2_junit;

import org.junit.Test;

import junit.framework.TestCase;

public class GiaiPTB2Test extends TestCase {

	GiaiPTB2 test = null;
	
	protected void setUp() throws Exception {
		super.setUp();
		test = new GiaiPTB2();
	}

	protected void tearDown() throws Exception {
		super.tearDown();
	}
	
	@Test
	public void testGiai1A() {
		assertEquals("Result", "Phuong trinh vo nghiem!" , test.giai1(0, 1));
	}
	@Test
	public void testGiai1B() {
		assertEquals("Result", "Phuong trinh co vo so nghiem!" , test.giai1(0, 0));
	}
	
	@Test
	public void testGiai1C() {
		assertEquals("Result", "Phuong trinh co 1 nghiem la: x = -1.0" , test.giai1(1, 1));
	}

	


}
