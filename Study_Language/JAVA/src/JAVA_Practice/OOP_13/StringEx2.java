package JAVA_Practice.OOP_13;

public class StringEx2 {
    public static void main(String[] args) {

        String Str1 = new String("Java");

        System.out.println(System.identityHashCode(Str1));
        StringBuilder buffer = new StringBuilder(Str1);
        System.out.println(System.identityHashCode(buffer));

        buffer.append(" and");
        buffer.append(" android");
        System.out.println(System.identityHashCode(buffer));

        String str2 = buffer.toString();
        System.out.println(str2);

    }
}
