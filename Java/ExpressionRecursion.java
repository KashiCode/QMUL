import java.util.Scanner;

public class Main {

    // Method to parse the expression recursively
    private static int parseExpression(String expression) {
        if (expression.isEmpty()) {
            throw new IllegalArgumentException("Invalid input: Expression is empty.");
        }

        char firstChar = expression.charAt(0);
        if (Character.isDigit(firstChar)) {
            // Base case: single digit
            return Character.getNumericValue(firstChar);
        } else {
            int result;
            int nextExpressionIndex = 2; // By default, assume next expression starts after one operator and one digit

            switch (firstChar) {
                case '+':
                    // Recursively process the remaining string after the operator and the first digit
                    result = parseExpression(expression.substring(1)) + parseExpression(expression.substring(nextExpressionIndex));
                    break;
                case '-':
                    result = parseExpression(expression.substring(1)) - parseExpression(expression.substring(nextExpressionIndex));
                    break;
                case '&':
                    result = 0;
                    // Iterate through each character in the string and recursively sum the digits
                    for (int i = 1; i < expression.length(); i++) {
                        result += parseExpression(expression.substring(i, i + 1));
                    }
                    break;
                default:
                    throw new IllegalArgumentException("Invalid input: Expression contains invalid characters.");
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please input the expression ");
        String expression = scanner.nextLine().replaceAll("\\s+", ""); // Remove all whitespace

        try {
            int result = parseExpression(expression);
            System.out.println("The answer is " + result);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

        scanner.close();
    }
}