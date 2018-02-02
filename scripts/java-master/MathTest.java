import java.util.Scanner;

public class MathTest {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        System.out.println(num + " + 1 = " + (num + 1));
        double num2 = scan.nextDouble();
        System.out.println(num2 + " * 2 = " + (num2 * 2));

        String str = scan.next();
        System.out.println("String: " + str);
    }
}