public class java2 {
    public static void main(String[] args) {
        int n = 5; // height of pyramid

        for (int i = 1; i <= n; i++) {
            String spaces = " ".repeat(n - i);

            if (i == 1) {
                // first row
                System.out.println(spaces + "*");
            } else if (i == n) {
                // last row
                System.out.println("*".repeat(2 * n - 1));
            } else {
                // middle rows
                String innerSpaces = " ".repeat(2 * i - 3);
                System.out.println(spaces + "*" + innerSpaces + "*");
            }
        }
    }
}
