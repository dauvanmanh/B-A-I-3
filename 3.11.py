def benefit(t, n, k):
    for month in range(k):
        n = n + (n * t / 100)
    return n

# Nhập lãi suất, số vốn ban đầu, và số tháng gửi
t = float(input("Nhập lãi suất t (%/tháng): "))
n = float(input("Nhập số vốn ban đầu n: "))
k = int(input("Nhập số tháng gửi k: "))

# Tính và in số tiền nhận được sau k tháng
print("Số tiền nhận được sau", k, "tháng là:", benefit(t, n, k))
