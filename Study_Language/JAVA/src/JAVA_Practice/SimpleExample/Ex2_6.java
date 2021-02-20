package JAVA_Practice.SimpleExample;

public class Ex2_6 {
    public static void main(String[] args){
        double pi = 3.141592;
        double shortPi = Math.round(pi * 1000) / 1000.0;
        System.out.println(shortPi);
        System.out.println(Math.round(pi));
    }
}
