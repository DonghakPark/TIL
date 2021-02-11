package JAVA_Practice.OOP_5;

public class VIPCustomer extends Customer {

    private int agentID;
    private double saleRatio;

    public VIPCustomer()
    {
        customerGrade = "VIP";
        bonusRatio = 0.05;
        saleRatio = 0.1;
    }

    public VIPCustomer(int customerID, String customerName, int agentID){
        this.customerID = customerID;
        this.customerName = customerName;
        customerGrade = "VIP";
        bonusRatio = 0.05;
        this.agentID = getAgentID();
    }

    public int calcPrice(int price){
        bonusPoint += price * bonusRatio;
        return price - (int)(price * saleRatio);
    }

    public int getAgentID() {
        return agentID;
    }
}
