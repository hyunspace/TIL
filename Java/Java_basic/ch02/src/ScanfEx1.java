import java.util.Scanner;

public class ScanfEx1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // system.i => 화면에서 입력

//        int num = scanner.nextInt(); // => 정수 하나는 num에 입력
//        int num2 = scanner.nextInt(); // 두 개 연속으로 받기
//        System.out.println(num);
//        System.out.println(num2);

        // 행 단위로 입력 받기
        String input = scanner.nextLine();
        int num3 = Integer.parseInt(input);

        System.out.println(num3);
    }
}
