import java.util.Scanner;

public class Main {

    // Inner class Record acts as a data container
    private static class Record {
        private String name;
        private int score;
    }

    // RecordManager to handle Record objects
    private static class RecordManager {

        // Method to create and initialize a new Record instance
        public Record createRecord(String name, int score) {
            Record newRecord = new Record();
            newRecord.name = name;
            newRecord.score = score;
            return newRecord;
        }

        // Method to set the name of a Record
        public void setName(Record record, String name) {
            record.name = name;
        }

        // Method to set the score of a Record
        public void setScore(Record record, int score) {
            record.score = score;
        }

        // Method to get the name of a Record
        public String getName(Record record) {
            return record.name;
        }

        // Method to get the score of a Record
        public int getScore(Record record) {
            return record.score;
        }
    }

    public static void main(String[] args) {
        RecordManager manager = new RecordManager();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter name: ");
        String name = scanner.nextLine();

        System.out.print("Enter score: ");
        int score = scanner.nextInt();

        // Creating a new Record instance
        Record record = manager.createRecord(name, score);

        // Interacting with the record through get and set methods
        System.out.println("Initial Record: " + manager.getName(record) + ", " + manager.getScore(record));

        System.out.print("Enter new score: ");
        scanner.nextLine(); // Consume the newline left by nextInt()
        int newScore = Integer.parseInt(scanner.nextLine());
        manager.setScore(record, newScore);

        System.out.println("Updated Record: " + manager.getName(record) + ", " + manager.getScore(record));

        scanner.close();
    }
}