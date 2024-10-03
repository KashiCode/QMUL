import java.util.Scanner;

public class Main {

    private static class Restaurant {
        private String name;
        private int stepFreeAccess;
        private int disabledToilets;
        private int disabledParking;

        public void setStepFreeAccessScore(int score) {
            this.stepFreeAccess = score;
        }

        public void setDisabledToiletsScore(int score) {
            this.disabledToilets = score;
        }

        public void setDisabledParkingScore(int score) {
            this.disabledParking = score;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getName() {
            return this.name;
        }

        public int getStepFreeAccess() {
            return this.stepFreeAccess;
        }

        public int getDisabledToilets() {
            return this.disabledToilets;
        }

        public int getDisabledParking() {
            return this.disabledParking;
        }

        public String disabilityScore() {
            int totalScore = getStepFreeAccess() + getDisabledToilets() + getDisabledParking();
            if (totalScore >= 9) {
                return "OUTSTANDING";
            } else if (totalScore > 5) {
                return "GOOD";
            } else {
                return "POOR";
            }
        }

        public static Restaurant createRestaurant(String name, int stepFreeAccess, int disabledToilets, int disabledParking) {
            Restaurant newRestaurant = new Restaurant();
            newRestaurant.setName(name);
            newRestaurant.setStepFreeAccessScore(stepFreeAccess);
            newRestaurant.setDisabledToiletsScore(disabledToilets);
            newRestaurant.setDisabledParkingScore(disabledParking);
            return newRestaurant;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = "y";

        while (input.equalsIgnoreCase("y")) {
            System.out.print("What is the name of the restaurant? ");
            String name = scanner.nextLine();

            int stepFreeAccessScore = getInput("What is the score for step-free access? ", scanner);
            int disabledToiletsScore = getInput("What is the score for disabled toilets? ", scanner);
            int disabledParkingScore = getInput("What is the score for disabled parking? ", scanner);

            Restaurant restaurant = Restaurant.createRestaurant(name, stepFreeAccessScore, disabledToiletsScore, disabledParkingScore);

            String disabilityScore = restaurant.disabilityScore();
            System.out.println(restaurant.getName() + " has a Disability Score of " + disabilityScore);

            System.out.print("Another (y/n)? ");
            input = scanner.nextLine();
        }

        scanner.close();
    }

    private static int getInput(String message, Scanner scanner) {
        while (true) {
            System.out.print(message);
            if (scanner.hasNextInt()) {
                int score = scanner.nextInt();
                scanner.nextLine(); // Consume the newline left-over
                return score;
            } else {
                System.out.println("Please enter a valid number.");
                scanner.nextLine(); // Consume the invalid input
            }
        }
    }
}