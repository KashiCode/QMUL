import java.util.Scanner;

//Record to hold the key and value
class StringMapEntry {
    public String key;
    public String value;
}

public class Main {

    //
    private static final int MAX_ENTRIES = 100;
    private static StringMapEntry[] entries = new StringMapEntry[MAX_ENTRIES];
    private static int entryCount = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Boolean end = false;

        //Initialises a loop to ask users to enter the key and value mappings.
        while (!end) {
            System.out.print("Enter new map key or XXX to end: ");
            String key = scanner.nextLine();

            if ("XXX".equalsIgnoreCase(key)) {
                break;
            }

            if (!isValidKey(key)) {
                System.out.println("Invalid key. Keys must not be empty or start with a digit.");
                continue;
            }

            if (containsKey(key)) {
                System.out.println("The key \"" + key + "\" is already mapped to a value.");
                continue;
            }

            System.out.print("Enter map value for key " + key + ": ");
            String value = scanner.nextLine();
            putEntry(key, value);
        }

        printMapContents();
        scanner.close();
        end = true; 
    }

    private static boolean isValidKey(String key) {
        return key != null && !key.isEmpty() && !Character.isDigit(key.charAt(0));
    }

    private static boolean containsKey(String key) {
        for (int i = 0; i < entryCount; i++) {
            if (entries[i] != null && entries[i].key.equals(key)) {
                return true;
            }
        }
        return false;
    }

    private static void putEntry(String key, String value) {
        if (entryCount >= MAX_ENTRIES) {
            System.out.println("Cannot add more entries, the map is full.");
            return;
        }
        StringMapEntry entry = new StringMapEntry();
        entry.key = key;
        entry.value = value;
        entries[entryCount] = entry;
        entryCount++;
    }

    private static void printMapContents() {
        System.out.println("Map contents:");
        for (int i = 0; i < entryCount; i++) {
            if (entries[i] != null) { 
                System.out.println(entries[i].key + " -> " + entries[i].value);
            }
        }
    }
}