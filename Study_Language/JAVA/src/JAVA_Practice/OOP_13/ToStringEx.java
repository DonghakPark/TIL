package JAVA_Practice.OOP_13;

class Book {
    String title;
    String author;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    @Override
    public String toString() {
        return title + "," + author;
    }
}
public class ToStringEx {
    public static void main(String[] args) {
        Book book = new Book("ddddd", "dddssss");
        System.out.println(book);

    }
}
