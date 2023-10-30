def gradient(x):
    return 2.0 * x - 4


def gradient_descent():
    x = 0.0
    num = 1000
    alpha = 0.01
    for i in range(0, num):
        print(f"iterate num = {i}, x = {x:1f}, gradient = {gradient(x):1f}")
        x = x - alpha * gradient(x)
    return x

if __name__ == '__main__':
    print(gradient_descent())
