/* Solved
 * 2013 Codechef December Challenge
 * Query on a tree VI
 * File:   QTREE6.cpp
 * Author: Andy Y.F. Huang
 * Created on Dec 12, 2013, 8:18:39 PM
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

namespace QTREE6 {
/*
 * Idea:
 * Root the tree arbitraily
 * At all times maintain the number of black and whites connected to all of a node's childen
 *    for all nodes let this number be F[x][2] (2 colors)
 * Then the answer for a query to node x is simply F[p][color[x]]
 *    where p is the highest ancestor that is connected to x
 *    use segment tree to find p in O(log(n))
 * To update a node, note only the path to p needs to have their F values updated
 *    we can use BIT/Segment Tree over a HLDOT to do the update
 *    If p is not the root then parent[p] also needs to be updated
 *
*/

const unsigned int buffer_size = 1 << 16;
char input_buffer[buffer_size];
unsigned int bytes_read = 0;
unsigned int input_index = 0;

inline char next_char() {
  if (input_index == bytes_read) {
    bytes_read = fread(input_buffer, sizeof(char), buffer_size, stdin);
    input_buffer[bytes_read] = '\0'; //sentinel
    input_index = 0;
  }
  return input_buffer[input_index++];
}

inline int next_int() {
  char c = 0;
  int ans = 0;
  while (c < '-')
    c = next_char();
  for (; c >= '0'; c = next_char())
    ans = (ans << 1) + (ans << 3) + c - '0';
  return ans;
}

char output_buffer[buffer_size];
unsigned int output_index = 0;

inline void write_flush() {
  fwrite(output_buffer, sizeof(char), output_index, stdout);
  output_index = 0;
}

inline void write_char(char c) {
  output_buffer[output_index++] = c;
  if (output_index == buffer_size)
    write_flush();
}

inline void write_int(int num) {
  if (num >= 10)
    write_int(num / 10);
  write_char(num % 10 + '0');
}

inline void println(int num) {
  write_int(num);
  write_char('\n');
}

#define WHITE 1
#define BLACK 0
typedef long long ll;
const int ROOT = 1;
const int MAX = 100111;
const int INF = 0x3F3F3F3F;

struct BIT {
  //0-indexed
  //add V to [Color][L, R]
  //get value of [x, x]
  ll bit[2][MAX];
  int N;

  void init(int N) {
    this->N = N;
    memset(bit, 0, sizeof(bit));
  }

  int get(int x, int col) const {
    ll res = 0;
    for (int i = x + 1; i > 0; i -= i & -i)
      res += bit[col][i];
    return (int) res;
  }

  void update(int l, int r, int col, int v) {
    //pln("BIT update:", l, r, col, v);
    for (int i = l + 1; i <= N; i += i & -i)
      bit[col][i] += v;
    for (int i = r + 2; i <= N; i += i & -i)
      bit[col][i] -= v;
  }
};

struct Seg_Tree {
  //0-indexed
  //flip color of [x, x]
  //find position min p in [L, R] s.t. [p, R] are all color c
  //    or -1 if no such position exists
  int tree[2][1 << 18];
  int PW;

  void init(int N) {
    for (PW = 1; PW < N;)
      PW <<= 1;
    memset(tree, -INF, sizeof(tree));
    for (int i = 0; i < N; i++)
      tree[BLACK][i + PW] = i;
    for (int i = PW - 1; i > 0; i--)
      tree[BLACK][i] = max(tree[BLACK][i + i], tree[BLACK][i + i + 1]);
  }

  int get(int ll, int rr, int c) const {
    //find last position of opposite color and add one
    c ^= 1;
    int res = -INF;
    for (int l = ll + PW, r = rr + PW + 1; l < r; l >>= 1, r >>= 1) {
      if (l & 1)
        res = max(res, tree[c][l++]);
      if (r & 1)
        res = max(res, tree[c][--r]);
    }
    if (res < 0)
      return ll;
    if (res == rr)
      return -1;
    return res + 1;
  }

  void update(int i) {
    i += PW;
    swap(tree[BLACK][i], tree[WHITE][i]);
    for (i >>= 1; i > 0; i >>= 1) {
      tree[BLACK][i] = max(tree[BLACK][i + i], tree[BLACK][i + i + 1]);
      tree[WHITE][i] = max(tree[WHITE][i + i], tree[WHITE][i + i + 1]);
    }
  }
};

int pos[MAX], par[MAX], size[MAX], top[MAX], inv[MAX];
vector<int> adj[MAX];
bool col[MAX];
BIT bit;  //number of same color nodes connected to subtree of x
Seg_Tree tree;

static int next_pos() {
  static int P = 0;
  return P++;
}

void dfs1(const int at) {
  size[at] = 1;
  for (const int& to : adj[at]) {
    if (to != par[at]) {
      par[to] = at;
      dfs1(to);
      size[at] += size[to];
    }
  }
}

void dfs2(const int at, const int ctop) {
  top[at] = ctop;
  pos[at] = next_pos();
  inv[pos[at]] = at;
  int heavy = -1;
  for (const int& to : adj[at])
    if (to != par[at] && (heavy == -1 || size[to] > size[heavy]))
      heavy = to;
  if (heavy == -1)
    return;
  dfs2(heavy, ctop);
  for (const int& to : adj[at])
    if (to != par[at] && to != heavy)
      dfs2(to, to);
}

int highest_par(const int v) {
  //find highest parent such that all nodes from v to p are same color as v
  int a = v, res;
  while (true) {
    const int nres = tree.get(pos[top[a]], pos[a], col[v]);
    if (nres < 0) {
      assert(~res);
      return res;
    }
    res = inv[nres];
    if (res != top[a] || res == ROOT)
      return res;
    a = par[top[a]];
  }
  assert(false);
  return -1;
}

void update(const int v) {
  //pln("Updating Node:", v);
  //flip color of v
  int p = par[highest_par(v)];
  const int del_val = bit.get(pos[v], col[v]);
  bit.update(pos[v], pos[v], col[v], -1);
  int a = v, b = p;
  if (b != v) {
    a = par[a];
    while (top[a] != top[b]) {
      bit.update(pos[top[a]], pos[a], col[v], -del_val);
      a = par[top[a]];
    }
    bit.update(pos[b], pos[a], col[v], -del_val);
  }

  col[v] ^= 1;
  //color changed now
  tree.update(pos[v]);
  p = par[highest_par(v)];
  a = v, b = p;
  bit.update(pos[v], pos[v], col[v], 1);
  const int add_val = bit.get(pos[v], col[v]);
  if (b != v) {
    a = par[a];
    //at least one v's parents are the new color
    while (top[a] != top[b]) {
      bit.update(pos[top[a]], pos[a], col[v], add_val);
      a = par[top[a]];
    }
    bit.update(pos[b], pos[a], col[v], add_val);
  }
//  for (int i = 1; i <= 5; i++)
//    pf('(', bit.get(pos[i], BLACK), bit.get(pos[i], WHITE), col[i]), pf(')');
//  pln();
}

void query(const int v) {
  //find number of nodes connected v with same color
  const int p = highest_par(v);
  //assert(col[p] == col[v]);
  const int res = bit.get(pos[p], col[p]);
  println(res);
}

void solve(int test_num) {
  const int V = next_int();
  for (int v = 1; v < V; v++) {
    const int a = next_int();
    const int b = next_int();
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  memset(col, BLACK, sizeof(col));
  par[ROOT] = ROOT;
  dfs1(ROOT);
  dfs2(ROOT, ROOT);
  bit.init(V);
  tree.init(V);
  for (int v = 1; v <= V; v++)
    bit.update(pos[v], pos[v], BLACK, size[v]);
  //pln(tree.get(2, V, WHITE));
  //pln(bit.get(pos[0], BLACK));
  //dbgarr("Top", top + 1, top + V + 1);
  //dbgarr("Par", par + 1, par + V + 1);
  //dbgarr("Pos", pos + 1, pos + V + 1);
  const int Q = next_int();
  for (int qq = 0; qq < Q; qq++) {
    const int t = next_int();
    const int v = next_int();
    if (t == 0)
      query(v);
    else
      update(v);
  }
  write_flush();
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
  QTREE6::solve();
  return 0;
}
