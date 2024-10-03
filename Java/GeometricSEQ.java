import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

      //defines a new scanner object
        Scanner scanner = new Scanner(System.in);

      //asks the user for the length of the sequence
        System.out.print("Length of sequence? (n>1) ");
        int n = scanner.nextInt();

        System.out.println("Checking sequence: the common ratio must be a positive integer.");

      //creates a new double array named sequence.
        double[] sequence = new double[n];


      //Uses a For loop to loop over the length of the sequence
        for (int i = 0; i < n; i++) {
            System.out.print("Enter number " + (i + 1) + " (positive integer): ");

          //collects each number input from the user
            int num = scanner.nextInt();

          //While i is more than 0 it calculates the ratio of the sequence and sets the ratio value for the entire sequence.  
            if (i > 0) {
                double ratio = (double) num / sequence[i - 1];

              //checks if the entered value is negative or not an integer. 
                if (ratio != (int) ratio || ratio <= 0) {
                    System.out.println("Error, ratio between last entered is " + ratio + ", which is not a positive integer.");
                    return;
                }
            }
            //adds numbers to the sequence
            sequence[i] = num;
        }

      //calcuates the finalratio and prints the ratio to the user.
        double FinalRatio = sequence[1] / sequence[0];
        System.out.println("The common ratio was: " + FinalRatio);
    }
}
//END PROGRAM.






   