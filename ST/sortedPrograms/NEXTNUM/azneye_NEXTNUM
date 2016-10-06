/*
 * 
 * File:   NEXTNUM.cpp
 * Author: Andy Y.F. Huang
 * Created on Nov 17, 2013, 11:53:10 AM
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

namespace NEXTNUM {
typedef long long ll;
int cnt[10];
ll fact[19];

ll calc() {
  ll res = fact[accumulate(cnt, cnt + 10, 0)];
  for (int d = 0; d < 10; d++)
    res /= fact[cnt[d]];
  return res;
}

void solve(int test_num) {
  string str;
  cin >> str;
  const int N = str.size();
  memset(cnt, 0, sizeof(cnt));
  for (int i = 0; i < N; i++)
    cnt[str[i] - '0']++;
  ll res = 0;
  for (int i = 0; i < N; i++) {
    for (int d = 0; d < str[i] - '0'; d++) {
      if (cnt[d] > 0) {
        cnt[d]--;
        res += calc();
        cnt[d]++;
      }
    }
    cnt[str[i] - '0']--;
  }
  res++;
  cout << res << endl;
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  fact[0] = 1;
  for (int i = 1; i < 19; i++)
    fact[i] = i * fact[i - 1];
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  NEXTNUM::solve();
  return 0;
}
