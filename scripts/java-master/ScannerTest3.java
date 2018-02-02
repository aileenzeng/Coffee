import java.util.Scanner;

public class ScannerTest3 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str1 = scan.nextLine();
        String str2 = scan.nextLine();
        System.out.println("This program takes in two strings");
        System.out.println("First string: " + str1);
        System.out.println("Second string: " + str2);
    }
}