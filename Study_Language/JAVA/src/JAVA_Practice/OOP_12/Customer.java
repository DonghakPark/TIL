package JAVA_Practice.OOP_12;

public class Customer implements Buy, Sell{
    @Override
    public void buy() {
        System.out.println("Buy");
    }

    @Override
    public void sell() {
        System.out.println("Sell");
    }
}
