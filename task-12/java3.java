import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class java3 {
    public static void main(String[] args) {
        try {
            File file = new File("input.txt");
            Scanner sc = new Scanner(file);
            int n = sc.nextInt(); 
            sc.close();

            for (int i = 1; i <= n; i++) {
                String spaces = " ".repeat(n - i);

                if (i == 1) {
                    System.out.println(spaces + "*");
                } else if (i == n) {
                    System.out.println("*".repeat(2 * n - 1));
                } else {
                    String innerSpaces = " ".repeat(2 * i - 3);
                    System.out.println(spaces + "*" + innerSpaces + "*");
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        }
    }
}
