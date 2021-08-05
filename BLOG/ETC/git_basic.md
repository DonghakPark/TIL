### Git 사용법 정리

아래 그림은 버전을 관리하는 것의 플로우를 보여주는 것이다.

![image](https://user-images.githubusercontent.com/44962038/128297211-321ed8d5-d8bc-4a18-bb0d-0b1ba57ea19d.png)

> 이미지 출처 : https://jrebel.com/rebellabs/git-commands-and-best-practices-cheat-sheet/

#### git 생성하기

- 로컬 저장소 생성하기
  - 자신이 작업하고 싶은 project name을 입력해 git 설정을 초기화 해줍니다.

```zsh
git init [project_name]
```

- 저장소 가져오기

  - Remote 저장소에 있는 source를 불러와 다운로드 합니다. 이때 url는 저장소 주소입니다.

```zsh
git clone [url]
```

#### git 상태 조회

- git 상태 ( 변경 사항 )
  - 작업중인 디렉토리에서의 변경사항을 볼 수 있습니다.

```zsh
git status
```

- 변경된 Staged 파일 확인
  - Stage가 변경되 파일을 확인합니다.

```zsh
git diff
```

- 로그 보기
  - 변경 이력을 볼 수 있습니다.

```zsh
git log
```

#### 브랜치(Branch) 작업하기

- 로컬 브랜치 보기

```zsh
git branch
```

- 로컬과 원격 브랜치 보기

```zsh
git branch -av
```

- 브랜치 변경

```zsh
git checkout <branch>
```

- 브랜치 생성

```zsh
git branch <new_branch>
```

- 브랜치 삭제

```zsh
git branch -d <branch>
```

- 원격 브랜치를 추적하는 새로운 브랜치 생성

```zsh
git checkout --track <remote/branch>
```

- 원격 브랜치 추적하기

```zsh
git branch -u <remote/branch>
```

- 현재 커밋에 태그 달기

```zsh
git tag <tag-name>
```

#### Git 변경하기

- 파일의 변경 사항을 다음 커밋에 반영하기

```zsh
git add [filename]
```

- 모든 변경 사항을 다음 커밋에 반영하기

```zsh
git add .
```

- 메세지와 함께 커밋

```zsh
git commit -m "write Commit Message HERE"
```

- 모든 변경 사항을 반영 + 커밋하기

```zsh
git commit -a
```

- 마지막 커밋 수정하기

```zsh
git commit --amend
```

#### Git 취소하기

- 작업 디렉토리에 모든 변경 사항 버리기

```zsh
git reset --hard HEAD
```

- 커밋 되돌리기

```zsh
git revert <commit>
```

#### 동기화하기

- 원격 저장소의 변경사항 가져오기

```zsh
git fetch <remote>
```

- 원격 저장소의 변경사항을 가져오고, 머지하기

```zsh
git pull <remote> <branch>
```

- 원격 저장소의 변경사항을 가져오고 리베이스하기

```zsh
git pull --rebase
```

- 원격 저장소에 변경사항 발행하기

```zsh
git push
```

- 원격 저장속에 태그 발행하기

```zsh
git push --tags
```

#### 병합, 리베이스

- 병합하기

```zsh
git merge <branch>
```

- 리베이스하기

```zsh
git rebase <branch>
```

#### 변경사항 저장하고 복원하기

- 임시로 변경사항 저장하기

```zsh
git stash
```

- 임시 변경사항 복원하기

```zsh
git stash pop
```

- 임시 변경사항 보기

```zsh
git stash list
```
