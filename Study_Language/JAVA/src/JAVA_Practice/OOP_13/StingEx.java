package JAVA_Practice.OOP_13;

public class StingEx {
    public static void main(String[] args) {

        String str1 = new String("abc");
        String str2 = new String("abc");
        System.out.println(str1 == str2);

        String str3 = "abc";
        String str4 = "abc";
        System.out.println(str3 == str4);

        String str5 = new String("abc");
        String str6 = new String("concantrate");

        str5 = str5.concat(str6);
        System.out.println(str5);

    }
}
