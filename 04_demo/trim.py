def trim(text):
    start = 0
    for char in text[:]:
        if not char == ' ':
            break;
        start += 1
    end = len(text)
    for char in text[::-1]:
        if not char == ' ':
            break;
        end -= 1
    return text[start:end]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
