x, y, op=0,0,""

x=int(input("여행 기간 동안의 총 식비를 입력하세요.:"))
y=int(input("여행 기간 동안의 총 숙박비를 입력하세요.:"))
b=int(input("여행 기간 동안의 총 레저비비를 입력하세요.:"))
a=int(input("여행 기간 동안의 총 교통비를 입력하세요.:"))
z=int(input("여행 기간 동안의 기타 지출 내역을 입력하세요.:"))
op=input("계산할 연산자를 입력하세요.:")

if op=="+":
    print("%d + %d + %d + %d + %d = %d 입니다." %(x,y,b,a,z,x+y+b+a+z))

q=int(input("계산할 인원 수를 입력하세요.:"))
op=input("계산할 연산자를 입력하세요.:")
ssum=(x+y+b+a+z)

if op=="/":
    print("%d / %d = %f 입니다." %(ssum,q,ssum/q))

