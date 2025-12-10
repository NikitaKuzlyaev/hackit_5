// Author: Kuzlyaev Nikita
// https://github.com/NikitaKuzlyaev


#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 5000;
bitset<MAXN> outside[MAXN];
bitset<MAXN> inside[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            char x;
            cin >> x;
            if (x == '1') {
                outside[i].set(j);
                inside[j].set(i);
            }
        }
    }

    for (int u = 0; u < n; u++) {
        for (int v = 0; v < n; v++) {
            if (v == u) continue;

            if (outside[u][v] && (inside[u] & outside[v]).any()) {
                cout << "YES\n";
                return 0;
            }
        }
    }

    cout << "NO\n";
    return 0;
}

