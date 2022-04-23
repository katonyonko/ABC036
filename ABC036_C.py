import io
import sys

_INPUT = """\
6
5
3
3
1
6
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=[int(input()) for _ in range(N)]
  B=sorted(list(set(A)))
  d={B[i]:i for i in range(len(B))}
  for i in range(N): print(d[A[i]])