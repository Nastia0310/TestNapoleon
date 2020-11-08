s = input()
s1 = input()
begin = end = -1
count = i = 0
for i in range(len(s)):
    if s[i] == '[':
        count += 1
        begin = i
        break
    i += 1
i += 1
while i < len(s):
    if s[i] == '[':
        count += 1
    elif s[i] == ']':
        count -= 1
        if count == 0:
            end = i
            break
    i += 1
res = s.replace(s[begin:end+1], s1, 1)
print(res)