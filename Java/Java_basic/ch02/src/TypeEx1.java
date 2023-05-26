public class TypeEx1 {

    public static void main(String[] args) {

        // 문자열 3
        String str = "3";

        // 문자열 "3" → 문자 '3'
        System.out.println(str.charAt(0));
        // 문자 '3' → 숫자 3
        System.out.println(str.charAt(0) - '0');
        System.out.println('3' - '0' + 1); // 4
        // 문자열 "3" → 숫자 3
        System.out.println(Integer.parseInt("3") + 1); // 4
        // 문자열 + 숫자 1
        System.out.println("3" + 1); // 31 (문자열)
        // 숫자 3 + 문자 '0'
        System.out.println(3 + '0'); // '0'은 숫자로 48이다
        System.out.println((char)(3 + '0')); // '3'
    }
}
