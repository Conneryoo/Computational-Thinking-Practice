total_sum=0
std_count=0
print(f"종료하려면 음수를 입력하시오")

score=int(input("성적을 입력하시오 : "))
while score>=0:
    total_sum=total_sum+score
    std_count=std_count+1
    score=int(input("성적을 입력하시오 : "))


if std_count==0:
    print(f"성적의 평균은 0입니")
    
else:
    print(f"성적의 평균은 {total_sum/std_count}입니다.")
