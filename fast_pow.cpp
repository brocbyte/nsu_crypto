#include <iostream>
#include <vector>
#include <iomanip>
#include <cassert>
using namespace std;

int32_t bitsset(int32_t a) {
    int32_t r = 0;
    while (a) {
        r += a & 1;
        a >>= 1;
    }
    return r;
}

int32_t pow_mod(int32_t a, int32_t b, int32_t p) {
    int32_t multCnt = 0;

    int32_t r = 1;
    int32_t tmp = b;
    while (b >>= 1) ++r;
    b = tmp;
    for (int i = 0; i < r; ++i)
        cout << setw(7) << "a^" + to_string(1 << i); cout << "\n";
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


    for (int i = 0; i < r; ++i) cout << setw(7) << row2[i]; cout << "\n";
    for (int i = 0; i < r; ++i) cout << setw(7) << row3[i]; cout << "\n";
    for (int i = 0; i < r; ++i) cout << setw(7) << row4[i]; cout << "\n";
    for (int i = 0; i < r; ++i)
        if (row5[i] == -1) cout << setw(7) << "-";
        else cout << setw(7) <<  row5[i];
    cout << "\n";
    for (int i = 0; i < r; ++i)
        if (row6[i] == -1) cout << setw(7) << "-";
        else cout << setw(7) << row6[i];
    cout << "\n";
    cout << a << " -> " << bitsset(a) << "\n";
    cout << b << " -> " << bitsset(b) << "\n";
    cout << "multiplications: " << multCnt << "\n";
    return row6.back();
}

int main() {
    assert(pow_mod(5, 701, 11) == 5);
    assert(pow_mod(3, 100, 7) == 4);
    assert(pow_mod(3, 800, 13) == 9);
    assert(pow_mod(7, 8999, 45) == 13);
}
