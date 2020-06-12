import math
def solution(monsters, bullets):
    answer =0
    b_grad = bullet[1] / bullet[0] if bullet[0] != 0 else 0
    m_grad = monster[1] / monster[0] if monster[0] != 0 else 0
    print(b_grad, m_grad)
    if b_grad == m_grad:
        if (bullet[0] > 0 and monster[0] > 0) and (bullet[1] > 0 and monster[0] > 0):
            answer += 1
            bullets.remove(bullet)
            monsters.remove(monster)
            break
        elif (bullet[0] > 0 and monster[0] > 0) and (bullet[1] < 0 and monster[0] < 0):
            answer += 1
            bullets.remove(bullet)
            monsters.remove(monster)
            break
        elif (bullet[0] < 0 and monster[0] < 0) and (bullet[1] > 0 and monster[0] > 0):
            answer += 1
            bullets.remove(bullet)
            monsters.remove(monster)
            break
        elif (bullet[0] < 0 and monster[0] < 0) and (bullet[1] < 0 and monster[0] < 0):
            answer += 1
            bullets.remove(bullet)
            monsters.remove(monster)
            break
    elif b_grad == 0 and m_grad == 0:
        # 축이 맞는 경우 (x == 0)
        if bullet[0] == 0 and monster[0] == 0:
            # 부호 체크
            if bullet[1] > 0 and monster[1] > 0:
                answer += 1
                bullets.remove(bullet)
                monsters.remove(monster)
                break
            elif bullet[1] < 0 and monster[1] < 0:
                answer += 1
                bullets.remove(bullet)
                monsters.remove(monster)
                break

        # 축이 맞는 경우 (y==0)
        elif bullet[1] == 0 and monster[1] == 0:
            # 부호 체크
            if bullet[0] > 0 and monster[0] > 0:
                answer += 1
                bullets.remove(bullet)
                monsters.remove(monster)
                break
            elif bullet[0] < 0 and monster[0] < 0:
                answer += 1
                bullets.remove(bullet)
                monsters.remove(monster)
                break

    return answer

if __name__=="__main__":
    monsters = [[-4,4],[-2,2],[6,2],[0,-2]]
    bullets = [[3,1],[-1,1],[-1,1],[0,-4],[2,-3]]
    print(solution(monsters,bullets))

