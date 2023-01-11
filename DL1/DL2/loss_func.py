'''
    손실함수
    1. 딥러닝 학습
        1) 순전파(Forward Propagation)
            - 입력층에서 출력층 방향으로 연산이 진행되면서 최종 출력값(예측값)이 도출되는 과정
        2) 손실 함수(Loss Function)
            - 예측값과 실제값의 차이를 구하는 함수
                - 두 값의 차이가 클수록 손실함수의 값은 커짐
                - 두 값의 차이가 작을수록 손실함수의 값도 작아짐

            - MSE (Mean squared error)
                - 평균 제곱 오차
                - 예측갑과 실제값의 차이의 제곱을 구한 후, 그 값들의 평균을 구하는 것
                - MSE가 작을수록 예측값과 실제값의 차이가 적은 것을 의미함.
                - MSE = 1/n * ∑((predicted_value - actual_value)^2)

'''
import numpy as np

# target : 정답(실제 값) , y : 예측 값
def MSE(target, y):
    return np.mean((y - target) ** 2)

y= np.array([0.0,0.0,0.8,0.1,0.0,0.0,0.0,0.1,0.0,0.0])
target = np.array([0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0 ])
print(MSE(target,y))

print("---------------------------------------------------")

y= np.array([0.9,0.0,0.8,0.1,0.0,0.0,0.0,0.1,0.0,0.0])
target = np.array([0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0 ])
print(MSE(target,y))