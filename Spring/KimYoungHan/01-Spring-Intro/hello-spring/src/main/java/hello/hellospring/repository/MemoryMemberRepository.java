package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberRepository {

    private static Map<Long, Member> store = new HashMap<>();
    private static long sequence = 0L;

    @Override
    public Member save(Member member) {
        member.setId(++sequence); // sequence 값 업데이트
        store.put(member.getId(), member); // 스토어에 추가
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id)); // null인 경우에 대비해서 optional 사용
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                // 파라미터로 넘어온 name과 member의 name 일치 여부 확인
                .filter(member -> member.getName().equals(name))
                .findAny(); // 찾으면 반환, 없으면 Optional에 null 반환
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values()); // 스토어의 values(members)를 반환
    }
}
