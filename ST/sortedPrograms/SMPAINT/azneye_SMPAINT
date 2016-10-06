/*
 * 2013 Codechef December Challenge
 * Art in Digital Age
 * File: SMPAINT.cpp
 * Author: Andy Y.F. Huang
 * Created on 2013-12-06, 7:17:27 PM
 */

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

using namespace std;

namespace SMPAINT {
struct Paint {
  int c, u, d, l, r;
};
const int dx[] = { 1, 0, -1, 0 };
const int dy[] = { 0, 1, 0, -1 };
typedef pair<int, int> Point;
int c[1111][1111];
bool vis[1111][1111];
int N;
vector<Paint> res;

void go(const int sr, const int sc) {
  const int color = c[sr][sc];
  vis[sr][sc] = true;
  queue<Point> q;
  vector<Point> pt;
  pt.push_back(Point(sr, sc));
  q.push(Point(sr, sc));
  for (; !q.empty(); q.pop()) {
    const int x = q.front().first;
    const int y = q.front().second;
    for (int d = 0; d < 4; d++) {
      const int nx = x + dx[d], ny = y + dy[d];
      if (!vis[nx][ny] && c[nx][ny] == color) {
        q.push(Point(nx, ny));
        vis[nx][ny] = true;
        pt.push_back(Point(nx, ny));
      }
    }
  }
  sort(pt.begin(), pt.end());
  vector<Paint> hort, nh;
  for (const Point& p : pt) {
    if (!hort.empty() && hort.back().u == p.first && hort.back().r + 1 == p.second)
      hort.back().r++;
    else
      hort.push_back(Paint { color, p.first, p.first, p.second, p.second });
  }
  for (const Paint& p : hort) {
    bool add = false;
    for (Paint& h : nh) {
      if (h.l == p.l && h.r == p.r && p.u == h.d + 1) {
        h.d++;
        add = true;
        break;
      }
    }
    if (!add)
      nh.push_back(p);
  }
  hort = nh;
    for (const Paint& p : hort)
      res.push_back(p);
}

void solve(int test_num) {
  memset(c, 0, sizeof(c));
  scanf("%d", &N);
  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++)
      scanf("%d", c[i] + j);
  memset(vis, false, sizeof(vis));
  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++)
      if (!vis[i][j] && c[i][j])
        go(i, j);
  printf("%d\n", res.size());
  for (const Paint& p : res)
    printf("%d %d %d %d %d\n", p.c, p.u, p.d, p.l, p.r);
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  solve(1);
}
}

int main() {
  SMPAINT::solve();
  return 0;
}
