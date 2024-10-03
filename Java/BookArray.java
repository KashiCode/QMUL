class Book {
    int yearPublished;
    String title;
}

class BookList {
    int numBooks;
    Book[] books;
}

public class Main {
    /* Book ADT: newBook, getBookYear, getBookTitle */

    public static Book newBook(int yearPublished, String title) {
        Book b = new Book();
        b.yearPublished = yearPublished;
        b.title = title;
        return b;
    }

    public static int getBookYear(Book b) {
        return b.yearPublished;
    }

    public static String getBookTitle(Book b) {
        return b.title;
    }

    /* BookList ADT: newBookList, addBook, printYearOfTitle, printAndCountBooksByYear */

    public static BookList newBookList() {
        BookList list = new BookList();
        list.numBooks = 0;
        list.books = new Book[1000];
        return list;
    }

    public static BookList addBook(BookList list, int yearPublished, String title) {
        if (list.numBooks >= list.books.length) {
            return list;
        }
        Book b = newBook(yearPublished, title);
        list.books[list.numBooks++] = b;
        return list;
    }

    public static void printYearOfTitle(BookList list, String title) {
        for (int i = 0; i < list.numBooks; i++) {
            Book b = list.books[i];
            if (getBookTitle(b).equals(title)) {
                System.out.println("The book \"" + title + "\" was published in " + getBookYear(b));
                return;
            }
        }
        System.out.println("Book " + title + " not found.");
    }

    public static void printAndCountBooksByYear(BookList list, int yearPublished) {
        int count = 0;
        for (int i = 0; i < list.numBooks; i++) {
            Book b = list.books[i];
            if (getBookYear(b) == yearPublished) {
                System.out.println("\"" + getBookTitle(b) + "\"");
                count++;
            }
        }
        if (count == 0) {
            System.out.println("No books found from the year " + yearPublished + ".");
        } else {
            System.out.println("Total number of books from the year " + yearPublished + " is " + count);
        }
    }

    public static void main(String[] args) {
        java.util.Scanner kb = new java.util.Scanner(System.in);
        BookList books = newBookList();
        menu(kb, books);
    }

    public static void menu(java.util.Scanner kb, BookList books) {
        System.out.println("(1) Add book (2) Search for title " +
                           "(3) List books by year (4) Exit");
        String opt = "";
        while (!opt.equals("4")) {
            opt = askString(kb, "Enter option [1-4]: ");
            if (opt.equals("1")) {
                int yearPublished = askInt(kb, "Year published? ");
                String title = askString(kb, "Title? ");
                addBook(books, yearPublished, title);
            } else if (opt.equals("2")) {
                String title = askString(kb, "Title to search for? ");
                printYearOfTitle(books, title);
            } else if (opt.equals("3")) {
                int yearPublished = askInt(kb, "Year to list books from? ");
                printAndCountBooksByYear(books, yearPublished);
            } else if (!opt.equals("4")) {
                System.out.println("Unknown option.");
            }
        }
    }

    public static int askInt(java.util.Scanner kb, String prompt) {
        System.out.print(prompt);
        return Integer.parseInt(kb.nextLine());
    }

    public static String askString(java.util.Scanner kb, String prompt) {
        System.out.print(prompt);
        return kb.nextLine();
    }
}

