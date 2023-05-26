public class PrintfEx1 {

    public static void main(String[] args) {
//        System.out.println(10 / 3);
//        System.out.println(10.0/3);
//        System.out.printf("age:%d year:%x\n", 14, 2017);
//        System.out.printf("%s\n", Integer.toBinaryString(15));
//
//        System.out.printf("%o\n", 15);
//        System.out.printf("%x\n", 15);
//        System.out.printf("%#o\n", 15);
//        System.out.printf("%#x\n", 15);

        System.out.printf("%5d\n", 15);
        System.out.printf("%o\n", 15);
        System.out.printf("%x\n", 15);
        System.out.printf("%s", Integer.toBinaryString(15));
        System.out.println("---------");
        double f = 123.456789;
        System.out.printf("%f%n", f);
        System.out.printf("%e%n", f);
        System.out.printf("%g%n", f);
    }
}
