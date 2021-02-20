package JAVA_Practice.OOP_12;

public class InterTest {
    public static void main(String[] args) {
        Customer customer = new Customer();

        Buy buyer = customer;
        buyer.buy();

        Sell seller = customer;
        seller.sell();

        customer.buy();
        customer.sell();

        seller.sell();
        buyer.buy();

    }
}
