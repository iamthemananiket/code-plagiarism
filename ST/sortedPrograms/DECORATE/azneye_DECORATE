/* Solved
 * 2013 Codechef December Challenge
 * Lucy and the Flowers
 * File:   DECORATE.cpp
 * Author: Andy Y.F. Huang
 * Created on Dec 12, 2013, 10:34:58 PM
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

namespace DECORATE {
/*
 * From http://arxiv.org/pdf/1305.2540.pdf:
 * Each subpalindrome of a string is the maximal suffix-palindrome
 * of some prefix of this string.
 * So there are at most n distinct non-empty palindromes of a string of length n
 *
 * From "Counting distinct palindromes in a word in linear time"
 *    let lmp[i] be the longest maximal palindrome ending at i (i = N or cant extend to i+1)
 *    let lps[i] = longest palindromic suffix of S[1, i]
 *    lps[N] = lmp[N]
 *    lps[i] = max(lmp[i], lps[i+1]-2) for 1 <= i < N
 *
 * http://en.wikipedia.org/wiki/Bracelet_%28combinatorics%29
 * Then find number of N-ary braclets of length P where p is the number of distinct sub-palindromes
 */

template <size_t MAXLEN> class BigUInt {
  static const int BASE = 1000000000;
  int len, digits[MAXLEN];

  void normalize() {
    while (len > 1 && digits[len - 1] == 0)
      len--;
  }

public:

  BigUInt(long long num)
      : len(0) {
    if (num == 0)
      len = 1;
    memset(digits, 0, sizeof(digits));
    for (; num > 0; num /= BASE)
      digits[len++] = num % BASE;
  }

  BigUInt(int num)
      : len(0) {
    if (num == 0)
      len = 1;
    memset(digits, 0, sizeof(digits));
    for (; num > 0; num /= BASE)
      digits[len++] = num % BASE;
  }

  BigUInt()
      : len(1) {
    memset(digits, 0, sizeof(digits));
  }

  BigUInt operator+(const BigUInt& x) const {
    BigUInt res = *this;
    return res += x;
  }

  BigUInt& operator+=(const BigUInt& x) {
    if (x.len > len)
      len = x.len;
    for (int i = 0; i < len; i++) {
      digits[i] += x.digits[i];
      if (digits[i] >= BASE)
        digits[i] -= BASE, digits[i + 1]++;
    }
    if (digits[len] > 0)
      len++;
    return *this;
  }

  BigUInt& operator-(const BigUInt& x) const {
    BigUInt res = *this;
    return res -= x;
  }

  BigUInt& operator-=(const BigUInt& x) {
    if (x.len > len)
      len = x.len;
    for (int i = 0; i < len; i++)
      if ((digits[i] -= x.digits[i]) < 0)
        digits[i] += BASE, digits[i + 1]--;
    normalize();
    return *this;
  }

  BigUInt operator*(const BigUInt& x) const {
    BigUInt res = *this;
    return res *= x;
  }

  BigUInt& operator*=(const BigUInt& x) {
    static long long temp[MAXLEN];
    memset(temp, 0, sizeof(long long) * (len + x.len));
    for (int i = 0; i < len; i++) {
      for (int j = 0, m = i; j < x.len; j++, m++) {
        temp[m] += (long long) (digits[i]) * x.digits[j];
        temp[m + 1] += temp[m] / BASE;
        temp[m] %= BASE;
      }
    }
    len += x.len;
    for (int i = 0; i < len; i++)
      digits[i] = (int) temp[i];
    normalize();
    return *this;
  }

  BigUInt& operator<<=(int amount) {
    if (len == 1 && digits[0] == 0)
      return *this;
    memmove(digits + amount, digits, len << 2);
    memset(digits, 0, amount << 2);
    len += amount;
    return *this;
  }

  BigUInt operator/(const BigUInt& x) const {
    return divide_mod(*this, x).first;
  }

  BigUInt& operator/=(const BigUInt& x) {
    return *this = divide_mod(*this, x).first;
  }

  BigUInt operator%(const BigUInt& x) const {
    return divide_mod(*this, x).second;
  }

  BigUInt& operator%=(const BigUInt& x) {
    return *this = divide_mod(*this, x).second;
  }

  static pair<BigUInt, BigUInt> divide_mod(const BigUInt& a, const BigUInt& b) {
    if (a < b)
      return make_pair(BigUInt(), a);
    pair<BigUInt, BigUInt> ans;
    BigUInt &quot = ans.first, &rem = ans.second;
    for (int i = a.len - 1; i >= 0; i--) {
      rem <<= 1, rem.digits[0] = a.digits[i];
      for (int low = 0, high = BASE - 1, mid; low <= high;) {
        mid = (low + high) >> 1;
        if ((b * mid).compare(rem) <= 0)
          quot.digits[i] = mid, low = mid + 1;
        else
          high = mid - 1;
      }
      rem -= b * quot.digits[i];
    }
    quot.len = a.len, quot.normalize();
    return ans;
  }

  //comparison operators

  bool operator>(const BigUInt& x) const {
    return compare(x) > 0;
  }

  bool operator<(const BigUInt& x) const {
    return compare(x) < 0;
  }

  int compare(const BigUInt& x) const {
    if (len != x.len)
      return len - x.len;
    for (int i = len - 1; i >= 0; i--)
      if (digits[i] != x.digits[i])
        return digits[i] - x.digits[i];
    return 0;
  }

  friend ostream& operator<<(ostream& out, const BigUInt& num) {
    out << num.digits[num.len - 1];
    for (int i = num.len - 2; i >= 0; i--)
      out << setw(9) << setfill('0') << num.digits[i];
    return out;
  }

  int length() const {
    return len;
  }

  int operator[](int pos) const {
    return digits[pos];
  }

  void print() const {
    printf("%d", digits[len - 1]);
    for (int i = len - 2; i >= 0; i--)
      printf("%09d", digits[i]);
  }

  void debug() const {
    cerr << "Len: " << len << ": ";
    for (int i = len - 1; i >= 0; i--)
      cerr << digits[i] << ',';
    cerr << endl;
  }
};

typedef BigUInt<5555> Int;
typedef unsigned long long ll;

const ll BASE = 1000000007;
int phi[666];
char str[111000];
ll hash[111000], rhash[111000], pw[111000];
ll pals[111000];
int lmp[111000], lps[111000];

ll get_hash(int a, int b) {
  return hash[b] - hash[a - 1] * pw[b - a + 1];
}

ll get_rhash(int a, int b) {
  return rhash[a] - rhash[b + 1] * pw[b - a + 1];
}

bool ispalin(int a, int b) {
  return get_hash(a, b) == get_rhash(a, b);
}

ll fpow(ll b, int e) {
  ll res = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1)
      res = res * b;
    b = b * b;
  }
  return res;
}

Int fpow2(Int b, int e) {
  Int res = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1)
      res = res * b;
    b = b * b;
  }
  return res;
}

ll neck(int n, int k) {
  //number of necklaces of length n, k different beads
  ll res = 0;
  for (int d = 1; d <= n; d++)
    if (n % d == 0)
      res += phi[d] * fpow(k, n / d);
  res /= n;
  return res;
}

Int neck2(int n, int k) {
  Int res = 0;
  for (int d = 1; d <= n; d++)
    if (n % d == 0)
      res += fpow2(k, n / d) * phi[d];
  res /= n;
  return res;
}

ll brace(int n, int k) {
  ll res = neck(n, k) >> 1;
  if (n & 1)
    res += fpow(k, (n + 1) / 2) / 2;
  else
    res += fpow(k, n / 2) * (k + 1) / 4;
  return res;
}

Int brace2(int n, int k) {
  Int res = neck2(n, k);
  if (n & 1)
    res += fpow2(k, (n + 1) / 2);
  else
    res += fpow2(k, n / 2) * (k + 1) / 2;
  res /= 2;
  return res;
}

void solve(int test_num) {
  for (int i = 1; i <= 600; i++)
    for (int j = 1; j <= i; j++)
      phi[i] += __gcd(i, j) == 1;
  int N;
  scanf("%s %d", str + 1, &N);
  const int L = strlen(str + 1);
  //plnarr(phi,phi+20);
  pw[0] = 1;
  for (int i = 1; i <= L; i++)
    pw[i] = pw[i - 1] * BASE;
  hash[0] = rhash[L + 1] = 0;
  for (int i = 1; i <= L; i++)
    hash[i] = hash[i - 1] * BASE + str[i];
  for (int i = L; i > 0; i--)
    rhash[i] = rhash[i + 1] * BASE + str[i];
  memset(lmp, 0, sizeof(lmp));
  for (int i = 1; i <= L; i++) {
    //even palindromes S[i - d + 1, i + d]
    int d = 0;
    for (int low = 1, high = min(i, L - i); low <= high;) {
      const int mid = (low + high) >> 1;
      if (ispalin(i - mid + 1, i + mid)) {
        d = mid;
        low = mid + 1;
      } else
        high = mid - 1;
    }
    lmp[i + d] = max(lmp[i + d], 2 * d);
    //odd palindromes S[i-d,i+d]
    d = 0;
    for (int low = 1, high = min(i - 1, L - i); low <= high;) {
      const int mid = (low + high) >> 1;
      if (ispalin(i - mid, i + mid)) {
        d = mid;
        low = mid + 1;
      } else
        high = mid - 1;
    }
    lmp[i + d] = max(lmp[i + d], 2 * d + 1);
  }
  lps[L] = lmp[L];
  for (int i = L - 1; i > 0; i--)
    lps[i] = max(lmp[i], lps[i + 1] - 2);
  for (int i = 1; i <= L; i++)
    pals[i - 1] = get_hash(i - lps[i] + 1, i);
  sort(pals, pals + L);
  const int K = unique(pals, pals + L) - pals;

//  dbgarr("lmp", lmp + 1, lmp + L + 1);
//  dbgarr("lps", lps + 1, lps + L + 1);
//  pln("Unique palindromes:", K);
//  for (int n = 1; n <= 10; n++)
//    for (int k = 1; k <= 10; k++)
//      pln(brace(n, k), brace2(n, k));

  Int res = brace2(N, K);
  //assert(res.length() <= 500);
  //pln(res.length());
  res.print();
  puts("");
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
  DECORATE::solve();
  return 0;
}
