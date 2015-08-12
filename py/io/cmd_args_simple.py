import sys

if len(sys.argv) != 3:
    sys.stderr.write('Usage: python %s num1 num2 \n' % sys.argv[0])
    raise SystemExit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
print(num1 + num2)

