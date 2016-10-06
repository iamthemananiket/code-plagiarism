/*
 * 
 * File:   TRSUBTR.cpp
 * Author: Andy Y.F. Huang
 * Created on Nov 17, 2013, 12:07:01 PM
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

namespace TRSUBTR {
typedef long long ll;
const ll BASE = 1000000007;
int age[222000];
int lch[222000], rch[222000];
bool inner[222000];
ll ha[222000], te[222000];

int read_tree() {
  int N;
  scanf("%d", &N);
  for (int i = 1; i <= N; i++) {
    scanf("%d", age + i);
    lch[i] = rch[i] = -1;
    inner[i] = false;
  }
  for (int i = 1, a, p; i < N; i++) {
    char type;
    scanf("%d %d %c", &p, &a, &type);
    inner[a] = true;
    if (type == 'M')
      lch[p] = a;
    else
      rch[p] = a;
  }
  return N;
}

ll go(int at) {
  if (at == -1)
    return 0;
  return ha[at] = age[at] + BASE * go(lch[at]) + BASE * BASE * go(rch[at]);
}

void solve(int test_num) {
  memset(lch, 0, sizeof(lch));
  memset(rch, 0, sizeof(rch));
  const int N = read_tree();
  for (int i = 1; i <= N; i++)
    if (!inner[i])
      go(i);
  for (int i = 1; i <= N; i++)
    te[i] = ha[i];
  //plnarr(te + 1, te + N + 1);
  sort(te + 1, te + N + 1);
  int Q;
  scanf("%d", &Q);
  while (Q--) {
    int M = read_tree();
    for (int i = 1; i <= M; i++)
      if (!inner[i]) {
        go(i);
        //plnarr(ha + 1, ha + M + 1);
        if (binary_search(te + 1, te + N + 1, ha[i]))
          puts("YES");
        else
          puts("NO");
      }
  }
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
  TRSUBTR::solve();
  return 0;
}
