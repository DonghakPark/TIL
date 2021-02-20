package JAVA_Practice.OOP_5;

import java.util.ArrayList;

public class CustomerTest {
    public static void main(String[] args) {

        ArrayList<Customer> customerList = new ArrayList<Customer>();

        Customer customerLee = new Customer(10010, "이순신");
        Customer customerShin = new Customer(10011, "신사임당");
        GoldCustomer2 customerKim = new GoldCustomer2(10012, "홍길동");
        GoldCustomer2 customerPark = new GoldCustomer2(10013, "박동학");
        VIPCustomer customerLee2 = new VIPCustomer(10013, "이상민", 11 );


        customerList.add(customerShin);
        customerList.add(customerLee);
        customerList.add(customerKim);
        customerList.add(customerPark);
        customerList.add(customerLee2);

        System.out.println("===========고객정보 출력============");

        for(Customer customer : customerList) {
            System.out.println(customer.showCustomerInfo());
        }
    }
}
