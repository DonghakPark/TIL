package JAVA_Practice.OOP_5;

public class GlodCustomer extends Customer{
    public GlodCustomer() {
        bonusRatio = 0.05;
    }

    public GlodCustomer(int customerID, String customerName) {
        super(customerID, customerName);
    }

    @Override
    public int calcPrice(int price) {
        return super.calcPrice(price);
    }

    @Override
    public String showCustomerInfo() {
        return super.showCustomerInfo();
    }

    @Override
    public int getCustomerID() {
        return super.getCustomerID();
    }

    @Override
    public void setCustomerID(int customerID) {
        super.setCustomerID(customerID);
    }

    @Override
    public String getCustomerName() {
        return super.getCustomerName();
    }

    @Override
    public void setCustomerName(String customerName) {
        super.setCustomerName(customerName);
    }

    @Override
    public String getCustomerGrade() {
        return super.getCustomerGrade();
    }

    @Override
    public void setCustomerGrade(String customerGrade) {
        super.setCustomerGrade(customerGrade);
    }

    @Override
    public int getBonusPoint() {
        return super.getBonusPoint();
    }

    @Override
    public void setBonusPoint(int bonusPoint) {
        super.setBonusPoint(bonusPoint);
    }

    @Override
    public double getBonusRatio() {
        return super.getBonusRatio();
    }

    @Override
    public void setBonusRatio(double bonusRatio) {
        super.setBonusRatio(bonusRatio);
    }
}
