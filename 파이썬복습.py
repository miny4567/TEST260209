# 변수명 = 값

a = 5
b = 6
c = 7 
# ; 만나면 줄이 끝났다고 인식
# 그래서 여러줄을 한줄로 기재 가능
a = 5; b = 6; c = 7

#자료형: 숫자형(float, int, complex), 
#문자형, 논리형
#객체구조
#   리스트 : []
#   튜플 : ()
#   딕셔너리: {"키":"값", "키":"값"}
#   셋: {"값"}

# 조건문
"""
if 조건:
    조건을 만족했을 때 처리
elif 조건:
    if 문을 만족하지 않고 
    다른 조건을 주고 싶을 때:  
else: 
    조건을 만족하지 않았을 때 처리
finally:
    조건을 만족하든 안하든 어떠한 처리
"""
# 반복문
"""
for문은 반복될 목록을 알고 있을 때 사용
while문은 반복될 조건을 알고 있을 때 사용
for 변수명 in 목록명:
    변수명에 따른 반복된 처리
while 조건:
    조건을 만족할 때 반복된 처리
"""

# 현재 폴더 혹은 패키지가 있는 경로에서
# .py파일이나 폴더를 가지고 올 때 import
# 사용 가능
import my_math

# import 하고 나면 그 파일 안에 있는
# 함수나 클레스 혹은 객체 사용이 가능
my_math.add_number(3, 4)

# 너무 길면 from 통해서 짧게 사용 가능
from my_math import add_number
add_number(3, 4)

# 쌍 따옴표 홑따옴표 사용 가능
a = "one way writing a string"
# 특정 패턴의 개수 확인 가능
a.count('ing')
# 인덱싱: 특정 위치의 값
# 슬라이싱: 어디서부터 어디까지 범위로 값
a[0] # 인덱싱
a[4:7] # 슬라이싱
# 텍스트 안에 값을 치환 가능
a.replace('one', 'two')

# 역슬레쉬는 특정한 용도로 미리 정해진
# 내용을 사용할 때 사용
print('aaa\naaa')
# \n 줄바꿈 \t 텝 이런식으로 미리 정해진 의미가
# 존재합니다.

# \가 미리 정해진 의미가 없다 그냥 문자다라고
# 인지하게 하려면 \\ 2개 붙여야 그냥 문자로 인식
# 주석 단축키는 Ctrl + 1
print('aaa\\naaa')

# \는 특수한 의미가 있다고 인지하므로
# 파일이나 폴더의 경로를 가지고 왔을 때도
# \ 라고 표현되어 있는 부분이 특수한 의미가
# 있다고 인식하므로
# 하나씩 \\로 변경해주거나 /로 변경해주어야 함
# 귀찮으므로 문자열 바깥 맨 앞에 r 을 붙여주면
# 경로로 인식하게 됨
rf"E:\2506~260106"

amount = 10 
rate = 88.46
currency = "Pesos"
f"{amount} {currency} is worth US$ {amount/rate:0.3f}"

import datetime

dt = datetime.datetime(2011, 10, 29, 20, 30, 21)
type(dt)
dt.year
dt.month
dt.minute

datetime.date
datetime.time

dt.date()
dt.time()

# datetime 을 원하는 문자열 형태로 변경하고 싶을 때 
# strftime 사용 가능
dt.strftime("%Y/%m/%d %H:%M:%S")

# 문자열 -> datetime 만들어주는 함수
datetime.datetime.strptime("20190901", "%Y%m%d")
datetime.datetime.strptime("2019-09-01", "%Y-%m-%d")

# 현재 시간 출력하는 함수
datetime.datetime.now()
# 코드가 실행되는 시간 같으거 확인 할 때 자주 사용
start = datetime.datetime.now()

end = datetime.datetime.now() - start

# open 함수 통해서 생성이 가능
f = open(
    "./test.txt", 
    mode = "w", 
    encoding="utf-8")
f.write("aaaa")
f.close()

# close 문 대신에 with 구문 사용
# with 구문으로 작성하면 
with open("./test2.txt", mode = 'w') as f:
    f.write("aaaa")
# with 에서 파일을 test2.txt라고 
# 열고 이름을 f 라 부르겠다
# with 구문이 끝나면 알아서 닫겠다

# with 구문이 끝나게 되면 알아서 close


# 속도가 느려서 계산을 조금 빠르게 처리할 수 있게
# 만들어진 패키지가 numpy

import numpy
# pip install 패키지명 통해서 pypi 저장소에서 
# 패키지 설치 가능
# pip install numpy[추천]
# conda install numpy 
# 개인 패키지들은 pip 로 등록하게 되어있음
# 혼용이 가능한데 일반적으로 하지말아달라 conda 측에서
# 부탁함

import numpy as np
# 배열: 같은 자료형을 가지는 수열을 의미
np.array([1,2,3])
np.array(["a","b","c"])
np.array([True, False])

range(1,4,0.1)
np.arange(1, 4,0.1) # range 함수의 numpy 버전
# 간격을 소숫점 단위로 가능

arr = np.array([1,2,3])
arr.dtype
arr.shape

arr = np.array([[1,2,3],[1,2,3]])
arr.shape

# 0값으로 가득찬 특정 크기의 numpy 객체
# 0으로 가득찬 2,3 형태의 numpy 객체 
# np.zeros(크기): 크기에 맞는 0값으로 차있는 
# numpy 객체 생성
# dtype을 통해서 타입 변경 가능
np.zeros((2, 3), dtype=int)
# 객체에 크기만큼 0값을 반환하고 싶을 때
arr.shape # (2,3)
np.zeros_like(arr) # arr 크기인 (2,3) 만큼 
# 0으로 가득차있는 numpy 객체 생성
np.ones((2, 3), dtype=int)
np.ones_like(arr)

np.full((2,3), 4)
# 단위행렬
np.eye(3)

np.int8
np.int16
np.float32
arr.dtype # dtype을 통해서 타입 조회 가능
arr.astype(np.int8) # astype을 통해서 타입 변경 가능
# 199번째 줄 arr.astype(np.int8)  화면에 출력만하고
# 이를 저장하지 않으므로 202번째 줄
# arr = arr.astype(np.int8)처럼 덮어쓰기 해줘야함
arr = arr.astype(np.int8)
arr.dtype

# 배열은 타입을 1개만 가질수 있어서
# 문자열이랑 숫자랑 혼용하면 자동으로 문자열로 바꿔준다
np.array([1,'a'])

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr + 1
arr + 2
arr * 2
arr / 2

arr * arr # 필드 자기 자신끼리 곱하기가 진행됨
arr.shape
arr * [1,2,3] # 곱하기 가능

# 행렬곱도 가능
arr.shape
arr2 = np.array([[4, 5],[6,7],[8,9]])
np.dot(arr,arr2)
# (n * m) * (m * k)  = (n * k)

arr. shape

arr[0,:] # 0번째 행 가져와라
arr[0] # 생략해서 사용이 가능
arr[:,0] # 0번째 열 가져와라

arr[0,1:] # 0번째 행 중에서 첫번째 열부터 끝까지

arr3 = np.arange(0, 27,1).reshape((3,3,3))
# 3개 공간에서 데이터 추출
arr3[:,:,:]
arr3[0,:,:]
arr3[1,:,:]
arr3[2,:,:]
arr3[0] # 생략 가능
arr3[0,1] # 생략 가능
arr3[0,1,:]

arr2 = np.array([[4, 5],[6,7],[8,9]])
# 인덱싱 후 값 변경하기
# 모든 행에 첫번째 값 변경하기 
arr2[:,0] = 30
arr2

arr2d = np.arange(1, 10,1).reshape((3,3))
arr2d[2]
arr2d[0,2]
arr2d[0][2]


arr1d = np.arange(1,10,1)
arr_bool = arr1d%2==0
arr1d[arr_bool] # True 값을 가진 애들만 추출이 가능
arr1d[~arr_bool] # ~ 통해서 부호를 반대로 변경이 가능

# 데이터 추출: 인덱싱 + 슬라이싱 + 논리값으로 가능
arr2d
arr2d.T # 전치 행렬

# p160 함수 목록 정리
np.sin(90 * np.pi/180) # sin 동작
np.fabs(-3)
np.sqrt(4)
np.square(10)
np.exp(2)
np.log(4)
np.ceil(3.14)
np.floor(3.14)
np.rint(3.14)
np.modf(3.14)
np.isnan(123)
np.isfinite(11)


# 정규분포: 종모양의 데이터의 분포
# 표준 정규분포: 평균 0, 분산1인 정규분포
np.random.standard_normal(size=3)
np.random.RandomState(42).standard_normal(size=3)

# RandomState(42): 난수 고정
# 돌릴때 마다 같은 랜덤값을 추출할 수 있게 
# 해주는 함수

# replace: 같은 번호가 나올지 안나올지 유무
# np.random.choice(범위, 개수)
np.random.choice(range(1,46), 5, replace=False)

np.random.choice(range(1,4), 1, p=[0.8,0.1,0.1])

img = np.zeros((200,300,3))

img_list = list()
for i in range(32):
    img = np.zeros((200,300,3))
    img_list.append(img)
len(img_list)
img_list[0].shape
imgs = np.array(img_list)
