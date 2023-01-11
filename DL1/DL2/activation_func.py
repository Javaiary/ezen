'''
    1. 딥러닝(Deep Learning)
        1) 여러 층(특히 은닉층이 여러 개) 을 가진 인공신경망을 사용하여 머신 러닝을 수행하는 것
            - 입력층 : 학습하고자 하는 데이터를 입력받음
            - 은닉층 : 모든 입력 노드로부터 입력값을 받아 가중합을 계산하고,
                      이 값을 활성화 함수에 적용하여 출력층에 전달
            - 출력층 : 최종 결과 출력
            - 가중치 : 입력 신호가 출력에 미치는 영향을 조절하는 매개변수로, 입력값의 중요도를 결정 (기울기)
            - 편향 : 가중합에 더하는 상수로, 하나의 뉴런에서 활성화 함수를 거쳐 최종적으로 출력되는 값을 조절 (절편)

        2) 다층 퍼셉트론(MLP, multilayer perceptron)
            - 입력층과 출력층 사이에 은닉층(hidden layer)을 가지고 있는 퍼셉트론

        3) 활성화 함수 (activation function)
            - 입력 신호가 출력 결과에 미치는 영향도를 조절하는 매개변수
            - 활성화 함수를 사용하는 이유
                - 출력값을 0~1 (-1~1) 사이의 값으로 변환해야 하는 경우에 사용
                - 비선형(Non-linear)을 위해 사용
                    - 직선이 아닌, 그래프에서 곡선 모양을 취하는 것
                - 종류
                    - 시그모이드(Sigmoid) 함수
                        - x 값의 변화에 따라 0에서 1까지의 값을 출력하는 S자형 함수
                        - 로지스틱 함수라고도 부름
                    - 하이퍼볼릭 탄젠트(Hyperbolic Tangent) 함수
                        - 시그모이드 함수와 유사
                        - -1 ~ 1의 값을 가지면서 데이터 평균이 0이라는 점이 다름
                    - 렐루 (ReLu)함수
                        - x가 음의 값을 가지면 0을 출력하고, 양의 값을 가지면 x를 그대로 출력
                            - 입력이 0을 넘으면 그대로 출력하고, 입력이 0보다 적으면 출력은 0이 됨
                        - max(0, x)
'''
import numpy as np  # 머신러닝은 넘파이 배열을 사용
import matplotlib.pyplot as plt

def step(x):
    result = x > 0.0000001      # 부동소수점 오차 방지, True/False
    return result.astype(int)   # 정수로 변환

x = np.arange(-10.0, 10.0, 0.1)
y = step(x)
plt.plot(x,y)
#plt.show()

print("==============================================")

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

x = np.arange(-10.0, 10.0, 0.1)     # -10 부터 10까지 0.1 간격으로
y= sigmoid(x)
plt.plot(x,y)
#plt.show()

print("==============================================")

x = np.linspace(-np.pi, np.pi, 60)
#print(x)
y = np.tanh(x)
plt.plot(x,y)
#plt.show()

print("==============================================")
def relu(x):
    return np.maximum(x,0)

x = np.arange(-10.0, 10.0, 0.1)
#print(x)
y = relu(x)
plt.plot(x,y)
plt.show()

















