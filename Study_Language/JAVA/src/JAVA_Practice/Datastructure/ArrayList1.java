package JAVA_Practice.Datastructure;

public class ArrayList1 {

    public static void main(String[] args) {

        int num = 10;

        int[] numbers = new int[10];

        int[] numbers2 = new int[] {0,1,2};

        System.out.println(numbers2[0] + numbers2[1] + numbers2[2]);

        int[] numbers3 = new int[] {1,2,3};

        numbers[0] = 1;
        numbers3[0] = 1;
        numbers3[1] = 2;
        numbers3[2] = 3;

        for( int i =0; i < numbers3.length; i++){
            System.out.println(numbers3[i]);
        }

    }
}
