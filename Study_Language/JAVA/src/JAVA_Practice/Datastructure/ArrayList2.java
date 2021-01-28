package JAVA_Practice.Datastructure;

import java.util.ArrayList;

public class ArrayList2 {
    public static void main(String[] args) {

        ArrayList<String> list = new ArrayList<String>();
        list.add("aaa");
        list.add("bbb");
        list.add("ccc");

        for(int i=0; i < list.size(); i++){
            String s = list.get(i);
            System.out.println(s);
        }
    }
}
