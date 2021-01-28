package JAVA_Practice.Datastructure;

public class ObjectArray {

    public static void main(String[] args) {

        Book[] library = new Book[5];
        library[0] = new Book("test1", "박동학");
        library[1] = new Book("test2", "박동학");
        library[2] = new Book("test3", "박동학");
        library[3] = new Book("test4", "박동학");
        library[4] = new Book("test5", "박동학");

        for(int i =0; i<library.length; i++){
            System.out.println(library[i]);
            library[i].showBookInfo();
        }

    }
}
