import java.util.Scanner;

public class ScannerTest2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();
        System.out.println("Input string: " + str);
        System.out.println("Doubled: " + str + str);
        System.out.println("third line");
    }
}
