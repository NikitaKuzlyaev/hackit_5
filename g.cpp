// Author: Mikhailov Gleb
// https://github.com/flexyw1be


#include <bits/stdc++.h>

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    int m;
    std::cin >> m;

    std::vector<int> queries(m);
    int max_n = 0;
    for (int i = 0; i < m; ++i) {
        std::cin >> queries[i];
        if (queries[i] > max_n) {
            max_n = queries[i];
        }
    }

    std::vector<bool> is_prime(max_n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (long long i = 2; i * i <= max_n; ++i) {
        if (is_prime[i]) {
            for (long long j = i * i; j <= max_n; j += i) {
                is_prime[j] = false;
            }
        }
    }

    for (int n : queries) {
        if (n == 2) {
            std::cout << "-1\n";
            continue;
        }
        bool found = false;
        for (int p = 2; p <= n / 2; ++p) {
            if (is_prime[p] && is_prime[n - p]) {
                std::cout << p << ' ' << (n - p) << '\n';
                found = true;
                break;
            }
        }
        if (!found) {
            std::cout << "-1\n";
        }
    }

    return 0;
}

