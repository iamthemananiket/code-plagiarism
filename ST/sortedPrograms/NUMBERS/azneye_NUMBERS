/*
 * 
 * File:   NUMBERS.cpp
 * Author: Andy Y.F. Huang
 * Created on Nov 24, 2013, 12:33:19 AM
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

namespace NUMBERS {
typedef pair<int, string> Per;
Per p[11111];

void solve(int test_num) {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++)
    cin >> p[i].second >> p[i].first;
  sort(p, p + N);
  for (int i = 0; i < N; i++) {
    if (i > 0 && p[i].first == p[i - 1].first)
      continue;
    if (i == N - 1 || p[i].first != p[i + 1].first) {
      cout << p[i].second << endl;
      return;
    }
  }
  cout << "Nobody wins." << endl;
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  int tests;
  cin >> tests;
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  NUMBERS::solve();
  return 0;
}
