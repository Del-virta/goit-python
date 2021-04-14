str_i = "i i c"
str_ua_i = "i і с"

symbol_map = {ord("і"): "cyrillic i", ord("с"): "cyrillic c"}
fixed_string = str_ua_i.translate(symbol_map)

print(str_ua_i == str_i)
print(fixed_string == str_i)
print(fixed_string)