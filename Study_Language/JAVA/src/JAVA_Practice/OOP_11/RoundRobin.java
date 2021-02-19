package JAVA_Practice.OOP_11;

public class RoundRobin implements scheduler{

    @Override
    public void getNextCall() {
        System.out.println("상담 전화를 순서대로 대기열에서 가져옵니다.");
    }

    @Override
    public void sendCalltoAgent() {
        System.out.println("다음 순서 상담원에게 배분합니다.");
    }
}
