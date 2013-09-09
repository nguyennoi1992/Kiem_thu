public class test {


    static int giaiptb1(int a, int b){

        if(a==0){
            return  0;
        } else {
            return -b / a;
        }
    }

    static void test1(){
        int ketqua = giaiptb1(1, 1);

        if(ketqua == -1){
            System.out.println("test1 is success!");
        } else {
            System.out.println("test1 is fail!");
        }
    }

    static void test2(){
        int ketqua = giaiptb1(1, 1);

        if(ketqua == -1){
            System.out.println("test2 is success!");
        } else {
            System.out.println("test2 is fail!");
        }
    }

    public static void main(String[] args) {
        // test 1
        test1();

        // test 2
        test2();

    }
}
