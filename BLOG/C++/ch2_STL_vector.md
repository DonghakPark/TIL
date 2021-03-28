### Vecotr Container란 무엇인가 ?

- 자동으로 메모리가 할당되는 배열
- 다양한 자료형을 담을 수 있는 배열
- 아래와 같은 구조를 가지고 있다.

### Vector 사용법, 생성방법

```{.c++}
    #include <vector>
    using namespace std;

    int main(){
    // 비어있는 벡터 생성
    vector<int> v;

    // 기본값 0 으로 초기화된 10개의 원소를 가진 vector 생성
    vector<int> v(10);

    // 2로 초기화된 vector 생성
    vector<int> v(10,2);

    //vector 복사
    vector<int> v1(v2);

    return 0;
    }

```

### Vector 내장 함수

- V.assign(5,2)
  - 2의 값으로 5개의 원소 할당
- V.at(idx)
  - idx번째 원소를 참조
- V[idx]
  - idx번째 원소를 참조
- V.front()
  - 첫번 째 원소 참조
- V.back()
  - 마지막 원소 참조
- V.clear()
  - 모든 원소를 제거 (크기(capacity)는 유지)
- V.push_back()
  - 마지막 원소 뒤에 원소를 삽입
- V.pop_back()
  - 마지막 원소 pop
- V.begin()
  - 첫 번째 원소
- V.end()
  - 마지막의 다음 원소
- V.rbegin()
  - reverse begin
- V.rend()
  - reverse end
- V.reserve()
  - 저장할 위치 예약 : 미리 할당
- V.resize()
  - 크기를 변경
- V.size()
  - 원소의 갯수를 반환
- V.capacity()
  - 할당된 크기를 리턴
- V2.swap(V1)
  - 두 벡터를 교체해줌
- V.insert(2,3,4)
  - 2번째 위치에 3개의 4값을 삽입
- V.insert(2,3)
  - 2번째에 3의 값을 삽입
- V.erase(iter)
  - 원소 제거
- V.empty()
  - 비었으면 True (Size가 0인지)

#### References

1. https://blockdmask.tistory.com/70?category=249379
2. https://codingplus.tistory.com/16?category=704484
