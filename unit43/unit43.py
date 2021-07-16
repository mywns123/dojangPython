import re

# print(re.search("^Hello", "Hello World!! haaaa,,,"))
#
# print(re.search("World!$", "Hello World!! haaaa,,,"))
# print(re.search("World!$", "Hello World!"))
#
# print(re.match("Hello|World", "Hello"))
# print(re.match("[0-9]", "11aaaa1235"))
# print(re.match("a*b", "b"))
# print(re.match("a+b", "b"))
# print(re.match("a*b", "aab"))
# print(re.match("a+b", "aab"))
# print(re.match("abc?d", "abd"))  # 'c'가 1 or 0개
# print(re.match("abc?d", "abccd"))
# print(re.match("ab[0-9]?c", "ab3c"))
# print(re.match("ab.d", "abㄱd"))
# print(re.match("h{3}", "hhhello"))
# print(re.match("(hello){3}", "hellohellohello"))
print(re.match("[0-9]{3}-[0-9]{4}-[0-9]{4}", "010-1234-5678"))


