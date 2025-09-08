''' `sys` → Sum from Command Line'''
import sys
if len(sys.argv) != 4:
    print("Usage: python add.py num1 num2 num3")
else:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
    total = n1 + n2 + n3
    print("Sum =", total)
