def all_variants(string):
    result = []
    length = 1
    while length <= len(string):
        for i in range(len(string)):
            if i+length <= len(string):
                result.append(string[i:i+length])
        length += 1
    yield result



a = all_variants("abc")
for i in a:
    print(i)