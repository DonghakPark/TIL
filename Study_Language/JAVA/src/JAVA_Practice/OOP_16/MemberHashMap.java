package JAVA_Practice.OOP_16;

import JAVA_Practice.OOP_4.Member;

import java.util.HashMap;
import java.util.Iterator;

public class MemberHashMap {

    private HashMap<Integer, Member> hashMap;

    public MemberHashMap() {
        hashMap = new HashMap<Integer, Member>();
    }

    public void addMember(Member member) {
        hashMap.put(member.getMemberId(), member);
    }

    public boolean removeMember(int memberID) {
        if ( hashMap.containsKey(memberID) ) {
            hashMap.remove(memberID);
            return true;
        }

        System.out.println(memberID + " 가 존재하지 않습니다.");
        return false;
    }

    public void showAllMember() {
        Iterator<Integer> ir = hashMap.keySet().iterator();

        while(ir.hasNext()) {
            int key = ir.next();

            Member member = hashMap.get(key);
            System.out.println(member);
        }
    }
}
