strings = input("Nhap vao sring: ")sorts = sorted([strings[i:i+1] for i in range(len(strings))])print("".join(sorts))