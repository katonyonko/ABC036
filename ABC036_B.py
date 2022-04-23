import io
import sys

_INPUT = """\
6
4
ooxx
xoox
xxxx
xxxx
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=[input() for _ in range(N)]
  for i in range(N): print(*[S[~j][i] for j in range(N)],sep='')