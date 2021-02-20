package JAVA_Practice.OOP_11;

import java.io.IOException;

public class scheduleTest {
    public static void main(String[] args) throws IOException {
        System.out.println("전화 상담 배분방식을 선택하세요 (R,L,P) : ");

        int ch = System.in.read();
        scheduler scheduler = null;

        if (ch == 'R' || ch == 'r') {
            scheduler = new RoundRobin();
        } else if (ch == 'L' || ch == 'l') {
            scheduler = new LeastJob();
        } else if (ch == 'P' || ch == 'p') {
            scheduler = new PriorityAllocation();
        } else {
            System.out.println("잘못된 입력입니다.");
            return;
        }

        scheduler.getNextCall();
        scheduler.sendCalltoAgent();

    }
}
