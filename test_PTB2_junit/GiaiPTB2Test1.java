package test_PTB2_junit;

import org.junit.Test;

import junit.framework.TestCase;

public class GiaiPTB2Test1 extends TestCase {

	GiaiPTB2 test = null;
	
	protected void setUp() throws Exception {
		super.setUp();
		test = new GiaiPTB2();
	}

	protected void tearDown() throws Exception {
		super.tearDown();
	}

	
	@Test
	public void testGiai2A(){
		assertEquals("Result","Phuong trinh vo nghiem!",test.giai2(0, 0, 1));
	}
	
	@Test
	public void testGiai2B(){
		assertEquals("Result","Phuong trinh co vo so nghiem!",test.giai2(0, 0, 0));
	}

	@Test
	public void testGiai2C(){
		assertEquals("Result","Phuong trinh co 1 nghiem la: x = -1.0",test.giai2(0, 1, 1));
	}
	
	@Test
	public void testGiai2D(){
		assertEquals("Result","Phuong trinh vo nghiem!",test.giai2(1, 4, 100));
	}

	@Test
	public void testGiai2E(){
		assertEquals("Result","Phuong trinh co nghiem kep x1 = x2 = 1.0",test.giai2(1, -2, 1));
	}

	@Test
	public void testGiai2f(){
		assertEquals("Result","Phuong trinh co 2 nghiem phan biet la: x1 = 3.0 x2 = 4.0",test.giai2(1, -7, 12));
	}

}
