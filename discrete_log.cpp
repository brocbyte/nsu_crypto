#include <iostream>
#include <cmath>
#include <cassert>
#include <vector>
using namespace std;

struct Result {
    int32_t multCnt;
    int32_t val;
};

Result pow_mod(int32_t a, int32_t b, int32_t p) {
    int32_t multCnt = 0;

    int32_t r = 1;
    int32_t tmp = b;
    while (b >>= 1) ++r;
    b = tmp;
    vector<int32_t> row2(r), row3(r);
    row2[0] = a;
    for (int i = 0; i < r; ++i) {
        row3[i] = row2[i] % p;
        if (i + 1 < r) {
            row2[i + 1] = row3[i] * row3[i];
            ++multCnt;
        }
    }
    vector<int32_t> row4(r, 0);
    for (int i = 0; i < r; ++i)
        if ((1 << i) & b) row4[i] = 1;

    vector<int32_t> row5(r, -1), row6(r, -1);
    int32_t val = -1;
    for (int i = 0; i < r; ++i) {
        if (!row4[i]) continue;
        if (val == -1) {
            row5[i] = row3[i];
        } else {
            row5[i] = val * row3[i];
            ++multCnt;
        }
        row6[i] = row5[i] % p;
        val = row6[i];
    }

    return {multCnt, row6.back()};
}

Result fast(int32_t y, int32_t a, int32_t p) {
    Result res;
    res.multCnt = 0;

    int32_t m = (int32_t)sqrt(p) + 1;
    int32_t k = m;
    assert(m * k > p);

    vector<int32_t> ay(m);
    ay[0] = y;
    cout << ay[0] << " ";
    for (int i = 1; i < m; ++i) {
        ay[i] = (ay[i - 1] * a) % p;
        ++res.multCnt;
        cout << ay[i] << " ";
    }
    cout << "\n";
    vector<int32_t> akm(k);
    for (int i = 0; i < k; ++i) {
        Result powRes = pow_mod(a, (i + 1) * m, p);
        akm[i] = powRes.val;
        res.multCnt += powRes.multCnt;
        cout << akm[i] << " ";
        for (int j = 0; j < m; ++j) {
            if (ay[j] == akm[i]) {
                cout << "\ni = " << (i + 1) << ", j = " << j << "\n";
                res.val = (i + 1) * m - j;
                return res;
            }
        }
    }
    cout << "\n";
    return {-1, -1};
}

Result brute(int32_t y, int32_t a, int32_t p) {
    Result res;
    res.multCnt = 0;
    for (int x = 0; x < p; ++x) {
        Result powRes = pow_mod(a, x, p);
        res.multCnt += powRes.multCnt;
        if (powRes.val == y) {
            res.val = x;
            return res;
        }
    }
    return {-1, -1};
}



int main() {
    Result res;
    res = fast(122, 79, 263);
    cout << "fast(122, 79, 263) --> x = " << res.val << ", multiplications: " << res.multCnt << "\n";
    res = brute(122, 79, 263);
    cout << "brute(122, 79, 263) --> x = " << res.val << ", multiplications: " << res.multCnt << "\n";
    cout << "#################################\n";

    res = fast(9, 2, 23);
    cout << "fast(9, 2, 23) --> x = " << res.val << ", multiplications: " << res.multCnt << "\n";
    res = brute(9, 2, 23);
    cout << "brute(9, 2, 23) --> x = " << res.val << ", multiplications: " << res.multCnt << "\n";
}
