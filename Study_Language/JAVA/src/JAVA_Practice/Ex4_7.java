package JAVA_Practice;

public class Ex4_7 {
    public static void main(String args[]){
        int num = 0;

        for ( int i = 1; i <= 20; i ++)
        {
            System.out.println(Math.random());
        }
        for ( int i =0; i<=20; i++){
            System.out.println((int)(Math.random()*10+1));
        }
    }
}
