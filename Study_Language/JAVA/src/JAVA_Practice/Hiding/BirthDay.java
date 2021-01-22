package JAVA_Practice.Hiding;

class BirthDay {

    private int day;
    private int month;
    private int year;

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        if (month == 2){
            if (day < 1 || day > 28) {
                System.out.println("입력 오류 입니다.");
            }
        } else {
            this.month = month;
        }
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public void getInformation() {
        System.out.println(year+ ":" + month + ":"  + day);
    }
}

class BirthDayTest{
    public static void main(String[] args) {
        BirthDay day = new BirthDay();

        day.setMonth(2);
        day.setYear(2018);
        day.setDay(30);

        day.getInformation();
    }
}