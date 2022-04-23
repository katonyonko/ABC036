import io
import sys

_INPUT = """\
6
12 36
12 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=map(int,input().split())
  print((B-1)//A+1)