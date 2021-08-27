import numpy as np


def solve(y, x, x_pred):
    # x transpose
    x_dash = x.T
    # product of x_dash and x
    X = x_dash.dot(x)
    # inverse of X
    X_inv = np.linalg.inv(X)
    # producet of X_inv and x_dash
    X_final = X_inv.dot(x_dash)
    # product of X_final and y i.e B
    B = X_final.dot(y)
    # calculate the y_pred
    y_pred = x_pred.dot(B)
    return y_pred


def main():
    m, n = map(int, input().strip().split())
    y = []
    x = []
    x_pred = []
    for _ in range(n):
        *features, y_val = map(float, input().strip().split())
        x.append([1] + features)
        y.append(y_val)

    for _ in range(int(input())):
        features = list(map(float, input().strip().split()))
        x_pred.append([1] + features)

    y = np.array(y)
    x = np.array(x)
    x_pred = np.array(x_pred)
    answer = solve(y, x, x_pred)

    for num in answer:
        print(round(num, 2))


if __name__ == "__main__":
    main()
