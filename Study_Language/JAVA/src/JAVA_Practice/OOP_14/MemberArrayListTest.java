package JAVA_Practice.OOP_14;

public class MemberArrayListTest {
    public static void main(String[] args) {
        MemberArrayList memberArrayList = new MemberArrayList();

        Member memberLee = new Member(101, "이순신");
        Member memberKim = new Member(102, "김동현");
        Member memberPark = new Member(103, "박동학");

        memberArrayList.addMember(memberLee);
        memberArrayList.addMember(memberKim);
        memberArrayList.addMember(memberPark);

        memberArrayList.showAll();

        memberArrayList.removeMember(memberKim.getMemberId());

        memberArrayList.showAll();

    }
}
