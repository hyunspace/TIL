package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.*;

public class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    @Test
    public void save() {
        Member member = new Member();
        member.setName("spring");

        repository.save(member);

        Member result = repository.findById(member.getId()).get(); // 저장한 것 꺼내기
        // 1번방법
        // System.out.println("result = " + (result == member));
        // 2번
        // Assertions.assertEquals(member, result); // (기대하는 것, 실제 결과 값) => 일치하면 초록불, 불일치하면 빨간불!
        // 3번
        assertThat(member).isEqualTo(result);
    }
}
