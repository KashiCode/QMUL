class Student4 {
    String name;
    int id;

    // Keeping track of the created instances
    private static final int MAX_STUDENTS = 30;
    private static Student4[] registeredStudents = new Student4[MAX_STUDENTS];
    private static int studentCount = 0;

    // Constructor is private to prevent direct instantiation
    private Student4(String name, int id) {
        this.name = name;
        this.id = id;
    }

    // Static method to register a student
    public static Student4 register(String name, int id) {
        // Check if the student is already registered
        for (int i = 0; i < studentCount; i++) {
            if (registeredStudents[i].name.equals(name) && registeredStudents[i].id == id) {
                return registeredStudents[i]; // Return the existing instance
            }
        }
        // If not already registered and array is not full, register new student
        if (studentCount < MAX_STUDENTS) {
            Student4 newStudent = new Student4(name, id);
            registeredStudents[studentCount++] = newStudent;
            return newStudent;
        }
        return null; // Array full or student already exists
    }

    // Added for access in Main4
    public static int getStudentCount() {
        return studentCount;
    }

    public static Student4 getRegisteredStudent(int index) {
        if (index >= 0 && index < studentCount) {
            return registeredStudents[index];
        }
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        Student4 student1 = Student4.register("John", 123);
        Student4 student2 = Student4.register("Jane", 456);
        Student4 student3 = Student4.register("John", 123);

        System.out.println(student1 == student3); // true
        System.out.println(student1 == student2); // false

        for (int i = 0; i < Student4.getStudentCount(); i++)
            System.out.println(Student4.getRegisteredStudent(i).name + " " + Student4.getRegisteredStudent(i).id);
    }
}
