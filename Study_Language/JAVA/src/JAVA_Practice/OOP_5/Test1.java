package JAVA_Practice.OOP_5;

public class Test1 {

    public static void main(String[] args) {

//        Customer customerLee = new Customer();
//        customerLee.setCustomerID(10100);
//        customerLee.setCustomerName("Lee");
//        System.out.println(customerLee.showCustomerInfo());


        VIPCustomer customerKim = new VIPCustomer();
        customerKim.setCustomerID(10101);
        customerKim.setCustomerName("Kim");
        customerKim.bonusPoint = 1000;
        System.out.println(customerKim.showCustomerInfo());
        // 하위 클래스 생성시 상위 클래서 선행 생성

    }

}