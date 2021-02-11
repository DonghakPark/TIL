package JAVA_Practice.OOP_5;

public class OverridingTest {

    public static void main(String[] args){
        Customer customerLee = new Customer(10001, "Lee");
        int price = customerLee.calcPrice(10000);
        System.out.println("지불 금액은 " + price + " 이고 " + customerLee.showCustomerInfo());

        VIPCustomer customerKim = new VIPCustomer(100011, "Kin", 100);
        price = customerKim.calcPrice(10000);
        System.out.println("지불 금액은 " + price + " 이고 " + customerKim.showCustomerInfo());


    }

}
