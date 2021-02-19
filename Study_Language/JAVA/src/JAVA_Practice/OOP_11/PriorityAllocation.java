package JAVA_Practice.OOP_11;

public class PriorityAllocation implements scheduler{
    @Override
    public void getNextCall() {
        System.out.println("고객의 등급이 높은 고객의 전화를 먼저 가져옵니다.");
    }

    @Override
    public void sendCalltoAgent() {
        System.out.println("업무 Skill이 가장 높은 상담원의 대기열에 앞에 우선 배분합니다.");
    }
}
