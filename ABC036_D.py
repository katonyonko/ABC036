import io
import sys

_INPUT = """\
6
5
2 5
1 5
2 4
3 2
10
7 9
8 1
9 6
10 8
8 6
10 3
5 8
4 8
2 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(1000000)
  def dfs(G,r=0):
    used=[False]*len(G)
    parent=[-1]*len(G)
    st=[]
    st.append(r)
    while st:
        x=st.pop()
        if used[x]==True:
            continue
        used[x]=True
        for v in G[x]:
            if v==parent[x]:
                continue
            parent[v]=x
            st.append(v)
    return parent
  mod=10**9+7
  N=int(input())
  G=[[] for _ in range(N)]
  for i in range(N-1):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].append(b)
    G[b].append(a)
  ans=[[1]*2 for _ in range(N)]
  looked=[False]*N
  parent=dfs(G)
  def rec(k):
    if looked[k]==True: return ans[k][0],ans[k][1]
    for i in G[k]:
      if parent[k]==i: continue
      looked[k]=True
      a,b=rec(i)
      ans[k][0]=(ans[k][0]*b)%mod
      ans[k][1]=(ans[k][1]*(a+b))%mod
    return ans[k][0],ans[k][1]
  rec(0)
  print(sum(ans[0])%mod)