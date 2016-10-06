/*
 * 
 * File:   PALINDR.cpp
 * Author: Andy Y.F. Huang
 * Created on Nov 24, 2013, 1:21:26 AM
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

namespace PALINDR {
struct Node {
  int cnt[10];
};
typedef long long ll;
const int mod = 1000000007;
ll fact[50111], ifact[50111];
Node tree[1 << 18];
char str[111000];
int PW;

void merge(Node& res, Node& a, Node& b) {
  for (int c = 0; c < 10; c++)
    res.cnt[c] = a.cnt[c] + b.cnt[c];
}

Node get(int l, int r) {
  static Node res;
  memset(res.cnt, 0, sizeof(res.cnt));
  for (l += PW, r += PW + 1; l < r; l >>= 1, r >>= 1) {
    if (l & 1)
      merge(res, res, tree[l++]);
    if (r & 1)
      merge(res, res, tree[--r]);
  }
  return res;
}

void update(int pos, char c) {
  int i = pos + PW;
  memset(tree[i].cnt, 0, sizeof(tree[i].cnt));
  tree[i].cnt[c - 'a'] = 1;
  for (; i > 0; i >>= 1)
    merge(tree[i], tree[i + i], tree[i + i + 1]);
}

void solve(int test_num) {
  int N, Q;
  scanf("%d %d %s", &N, &Q, str);
  for (PW = 1; PW < N;)
    PW <<= 1;
  memset(tree, 0, sizeof(tree));
  for (int i = 0; i < N; i++)
    tree[i + PW].cnt[str[i] - 'a'] = 1;
  for (int i = PW - 1; i > 0; i--)
    merge(tree[i], tree[i + i], tree[i + i + 1]);
  //plnarr(tree[1].cnt, tree[1].cnt + 10);
  while (Q--) {
    int ty, L, R;
    scanf("%d %d %d", &ty, &L, &R);
    L--, R--;
    if (ty == 1) { //reverse
      for (int i = L, j = R; i < j; i++, j--) {
        swap(str[i], str[j]);
        //update(i, str[i]);
        //update(j, str[j]);
      }
    } else {
      //Node res = get(L, R);
      //plnarr(res.cnt, res.cnt + 10);
      Node res;
      memset(res.cnt, 0, sizeof(res.cnt));
      for (int i = L; i <= R; i++)
        res.cnt[str[i] - 'a']++;
      ll ans = 1;
      int sum = 0, odd = 0;
      for (int c = 0; c < 10; c++) {
        odd += res.cnt[c] & 1;
        sum += res.cnt[c] >> 1;
        ans = ans * ifact[res.cnt[c] >> 1] % mod;
      }
      ans = ans * fact[sum] % mod;
      printf("%d\n", odd > 1 ? 0 : (int) ans);
    }
  }
}

ll fpow(ll b, int e) {
  ll res = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1)
      res = res * b % mod;
    b = b * b % mod;
  }
  return res;
}

void init() {
  fact[0] = ifact[0] = 1;
  for (int i = 1; i <= 50000; i++) {
    fact[i] = fact[i - 1] * i % mod;
    ifact[i] = fpow(fact[i], mod - 2);
  }
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  init();
  solve(1);
}
}

int main() {
  PALINDR::solve();
  return 0;
}
