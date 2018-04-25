import java.util.Scanner;

public class Problem1Demo1Runner {
    public static void main(String[] args) {
        // TODO: fix this so that it can be extended for all Problem1 type files
        Scanner s = new Scanner(System.in);
        int param1 = Integer.parseInt(s.nextLine());
            int param2 = Integer.parseInt(s.nextLine());
            int param3 = Integer.parseInt(s.nextLine());
            Problem1Demo1.printNums(param1, param2, param3);

        // String s = args[0];
        // System.out.println("First arg: " + s);
        //int a = Integer.parseInt(args[0]);
        //int b = Integer.parseInt(args[1]);
        //int c = Integer.parseInt(args[2]);

    }
}