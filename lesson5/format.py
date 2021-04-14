x = (1, 2, 3, 4, 5)


header = "{:^15}|{:^15}|{:^15}|".format("x", "x^2", "x^3")
splitter = "=" * len(header)
body = ''
for num in x:
    line = "{:<15}|{:^15}|{:>15}|".format(num, num**2, num**3)
    body += line + "\n"
result = "\n".join([header, splitter, body])
print(result)