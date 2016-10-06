/*
 * 
 * File:   AMIFIB.cpp
 * Author: Andy Y.F. Huang
 * Created on Nov 17, 2013, 11:18:57 AM
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

namespace AMIFIB {
template <size_t MAXLEN> class BigUInt {
  static const int BASE = 1000000000;
  int len, digits[MAXLEN];

  void normalize() {
    while (len > 1 && digits[len - 1] == 0)
      len--;
  }

public:

  //TODO: make string constructor
  //  BigUInt(const char* str, int _len) : len(0) {
  //    //memset(digits, 0, MAXLEN);
  //    for (int i = _len - 1; i >= 0; i--)
  //      digits[len++] = str[i] - '0';
  //    normalize();
  //  }

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
    memmove(digits + len, digits + len - amount, amount << 2);
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

  string tostring() {
    stringstream ss;
    ss << digits[len - 1];
    for (int i = len - 2; i >= 0; i--)
      ss << setw(9) << setfill('0') << digits[i];
    return ss.str();
  }

};

typedef BigUInt<120> Int;
Int fib[5000];
string res[5000];

void solve(int test_num) {
  fib[0] = 0;
  fib[1] = 0;
  fib[2] = 1;
  res[2] = "1";
  res[0] = res[1] = "0";
  for (int i = 3; i < 5000; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
    res[i] = fib[i].tostring();
  }
  sort(res, res + 5000);
  int T;
  cin >> T;
  while (T--) {
    string str;
    cin >> str;
    if (binary_search(res, res + 5000, str))
      cout << "YES";
    else
      cout << "NO";
    cout << endl;
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
  AMIFIB::solve();
  return 0;
}
