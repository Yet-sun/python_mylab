def fab(max):
    n, a, b = 0, 0, 1
    l = []
    while n < max:
        l.append(b)
        a, b = b, a + b
        n = n + 1
    return l


for num in fab(5):
    print(num)

# 改写后的 fab 函数通过返回 List 能满足复用性的要求
# 但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大而增大
# 如果要控制内存占用，最好不要用 List来保存中间结果，而是通过 iterable 对象来迭代
