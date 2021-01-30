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

    public VIPCustomer(int customerID, String customerName){
        this.customerID = customerID;
        this.customerName = customerName;
        customerGrade = "VIP";
        bonusRatio = 0.05;
    }

    public int getAgentID() {
        return agentID;
    }
}
