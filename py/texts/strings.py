# define a str
a = 'hello'
b = "world"
c = """verbose..."""

lines = """Content-type: text/html
<h1>Hello world</h1>
Click <a href='test.html'>this</a>
"""
print(lines)

# conversion
s1 = '123'
i1 = int(s1)
print(i1)

print(str(i1))
print(repr(i1))
print(format(i1, '4d'))
print(format(i1, '0.5f'))
