---
title: 音階
date: 2026-01-22 12:00:00
updated: 2026-01-21 12:00:00
tags:
  - 音階 Scales
  - 調 Keys
  - 音程 Interval
  - 三和弦 Triads
categories:
  - [音高 Pitch, 音階 Scales]
cover: /img/cpp_cover.png
mathjax: true
---

# 【C++】競程筆記（背包問題）

題目範例參考：NTUCPC Guide，此筆記僅為個人學習用途。

最後更新時間：

## 什麼是背包問題

背包問題（Knapsack Problem）是一種組合最佳化的 NP-Complete 問題，擁有多種變形，其中最基礎的是「0/1 背包問題」。

在 DP 裡面，背包問題是最經典且常見的題型之一。

### 01 背包問題

Problem Source：https://oj.ntucpc.org/problems/801

所謂 0 1 就是物品可拿或不拿。

題目描述：

有 $N$ 個物品編號 $1 \sim N$ ，第 $i$ 個物品的重量和價值分別是 $w_i$ 和 $v_i$。學姊打算從 $N$ 個物品選其中一些帶走，但她只有大小為 $W$ 的背包，也就是說她選擇的物品總重不能超過 $W$。請問背包能容納的物品的總價值最大是多少？

---

如果直接定義 $dp[i]$ 是前 $i$ 個物品的最大總價值，是不實際的，因為需要考慮到 $W$ 重量的因素。

因此用到二維 DP 概念，$dp[i][j]$ 為前 $i$ 個物品且背包當前容重量限制為 $j$ 時，能獲得的最大價值。

對於第 $i$ 個物品（重量 $w[i]$，價值 $v[i]$），當考慮是否要放入背包（當前容量 $j$）時，只有兩種選擇：

1. 不拿第 $i$ 個物品，最大價值 = 前 $i-1$ 個物品且容量為 $j$ 的最大總價值。
$$dp[i][j] = dp[i-1][j]$$

2. 拿第 $i$ 個物品，前提是背包要夠裝（$j \geq w[i]$），如果拿了，會得到 $v[i]$ 的價值，但背包容量會減少 $w[i]$。剩下的容量 $j - w[i]$ 就要去查詢「前 $i-1$ 個物品」能湊出的最大價值。
$$dp[i][j] = dp[i-1][j-w[i]] + v[i]$$

由於要求最大價值，因此
$$dp[i][j] = max(dp[i-1][j], \quad dp[i-1][j-w[i]] + v[i])$$

最後在 base case 定義上，設定為全部都是 0。

範例程式碼：

```cpp
#include <bits/stdc++.h>

using namespace std;

const int MAXN = 105;
const int MAXW = 100005;
const int INF = -1e9;

long long dp[MAXN][MAXW];

int w[MAXN], v[MAXN];

int main(){
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int n, wmax;
    cin >> n >> wmax;

    for (int i = 1; i <= n; ++i) cin >> w[i] >> v[i];

    for (int i = 1; i <= n; ++i){
        for (int j = 0; j <= wmax; ++j){
            if (j < w[i]){
                dp[i][j] = dp[i - 1][j];
            }
            else{
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]);
            }
        }
    }
    cout << dp[n][wmax] << '\n';
}
```

### 0/1 背包問題變形：鐵棒問題

此為經典的子集和加總問題（Subset Sum Problem），屬於 0/1 背包問題的變形。

Problem Source：https://oj.ntucpc.org/problems/802

1. 定義狀態： $dp[i][j]$ 是一個布林值，其意義為從前 $i$ 條鐵棒中選出若干條，使其長度總和恰好為 $j$，則為 true，否則為 false。
2. 定義轉移式：

對於第 $i$ 條鐵棒（其長度為 $l_i$），有兩種選擇：

- 不選這條鐵棒：如果前 $i-1$ 條鐵棒能湊出長度 $j$，那前 $i$ 條當然也能。
$$dp[i-1][j]$$

- 選這條鐵棒：前提是目標長度 $j$ 必須大於等於鐵棒長度 $l_i$，如果選了，問題就變成「前 $i-1$ 條鐵棒能否湊出長度 $j - l_i$」。
$$dp[i-1][j-l_i] \text{ }, (j \geq l_i)$$

完整轉移式：
$$dp[i][j] = dp[i-1][j] \lor dp[i-1][j-l_i]$$

其中 $\lor$ 表示 OR，其中一個可以湊出長度 $j$ 就行。

3. 定義初始狀態：沒鐵棒時（$i = 0$），
   - 湊出長度為 0 是可能的（一條都不選）：$dp[0][0] = true$
   - 湊出任何大於 0 的長度是不可能的：$dp[0][j] = false$ （for $j > 0$）

範例程式碼：

```cpp
#include <iostream>

using namespace std;

const int MAXN = 35;
const int MAXL = 1005;

bool dp[MAXN][MAXL];

int l[MAXL];

int main(){
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int L, N;
        cin >> L >> N;
        for (int i = 1; i <= N; ++i) cin >> l[i];

        dp[0][0] = true;

        for (int i = 1; i <= N; ++i){
            for (int j = 0; j <= L; ++j){
                bool not_pick = dp[i - 1][j];

                bool pick = false;
                if (j >= l[i]) pick = dp[i - 1][j - l[i]];

                dp[i][j] = not_pick || pick;
            }
        }

        cout << (dp[N][L] ? "TAK\n" : "NO\n");
    }
}
```

### 0/1 背包問題變形：高棕櫚農場

Problem Source：https://tioj.sprout.tw/problems/143

為什麼是背包問題？

在時間的飽足感當容量（ $M$ ）限制下，選擇若干個高棕櫚（物品），使得總滿足感（價值）最大化。

1. 定義狀態：令 $dp[j]$ 表示當飽足感上限為 $j$ 時，能夠獲得的最大滿足感。（本問題可用二維 dp 做，但會超時，因此在這裡對狀態壓縮成一維）
2. 定義轉移式：

對於每個高棕櫚 $i$（其飽足感為 $A_i$，滿足感為 $B_i$），有兩種選擇：

- 不吃：最大滿足感保持不變，即 $dp[j]$。
- 吃：選後背包剩餘可裝重量為 $j - A_i$。此時的價值就是「容量為 $j - A_i$ 時的最大價值」加上「當前高棕櫚的滿足感 $B_i$」，即 $dp[j - A_i] + B_i$。

取兩種選擇的最大值即為轉移式：
$$dp[j] = max(dp[j], \quad dp[j - A_i] + B_i)$$

3. 定義初始狀態：滿足感全 0（$dp[0 \cdots M] = 0$）。

範例程式碼：

由於每個物品只能選一次，在用一維 dp 計算時，內層迴圈順序由大到小（從 $M$ 遞減到 $A_i$）遍歷，這樣可確保計算 $dp[j]$ 時所參考的 $dp[j - A_i]$ 是來自「上一個物品」的狀態，而不是「當前物品」已經被選過之後的狀態。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N, M;

        cin >> N >> M;

        vector<int> A(N), B(N);

        for (int i = 0; i < N; ++i) cin >> A[i] >> B[i];

        vector<int> dp(M + 1, 0);

        for (int i = 0; i < N; ++i) {
            int w = A[i];
            int v = B[i];

            for (int j = M; j >= w; --j)
                dp[j] = max(dp[j], dp[j - w] + v);
        }

        cout << dp[M] << '\n';
    }
    return 0;
}
```

### 0/1 背包問題變形：高棕櫚農場2

Problem Source：https://tioj.sprout.tw/problems/144

在原本的條件上，這題還給你加一個限制： $K$ （取幾高棕櫚的上限）。

解題邏輯跟上題差不多，不管物品 $i$ 的維度，只需忙 $M, K$ 的維度即可，此為滾動 DP 優化空間的做法。

1. 定義狀態：令 $dp[j][k]$ 為當前飽足感為 $j$，且吃了 $k$ 個高棕櫚時，所能獲得的最大滿足感。
2. 定義轉移式：

對於每個高棕櫚 $i$（其飽足感為 $A_i$，滿足感為 $B_i$），有兩種選擇：

- 不吃：狀態維持不變，即
$$dp[j][k]$$

- 吃：前提是當前飽足感 $j \geq A_i$ 且數量 $k \geq 1$。此時滿足感為由「飽足感 $j - A_i$ 且數量 $k - 1$」的狀態加上當前的滿足感 $B_i$，即
$$dp[j - A_i][k - 1] + B_i$$

完整轉移式：
$$dp[j][k] = max(dp[j][k], \quad dp[j-w][k-1] + v)$$

3. 定義初始狀態：跟上題一樣，dp 全 0。

範例程式碼：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--){
        int N, M, K;
        cin >> N >> M >> K;

        vector <vector <int>> dp(M + 1, vector<int>(K + 1, 0));

        vector<int> A(N), B(N);

        for (int i = 0; i < N; ++i) cin >> A[i] >> B[i];

        for (int i = 0; i < N; ++i){
            int w = A[i];
            int v = B[i];

            for (int j = M; j >= w; --j){
                for (int k = K; k >= 1; --k){
                    dp[j][k] = max(dp[j][k], dp[j - w][k - 1] + v);
                }
            }
        }

        cout << dp[M][K] << '\n';
    }
}
```

### 背包問題的另種形式：無限背包問題（Unbounded Knapsack Problem）

無限背包問題又稱為完全背包問題，與 0/1 背包問題不同的是，完全背包問題的每種物品的數量是無限的，只要背包裝得下，同一種物品可選 1 個、2 個，甚至無限個。

接下來講個問題。

Problem Source：https://oj.ntucpc.org/problems/825

**Description**

現在有 $N$ 個物品，第 $i$ 個物品的重量為 $w_i$ ，價值為 $v_i$ 。每個物品都有無限多個。你有一個重量限制為 $W$ 的背包，你希望可以在不超過這個背包重量限制的前提下，盡可能塞入價值總和最高的物品。請問你可以塞入最高的物品總價值是多少？

1. 定義狀態： $dp[j]$ 為當背包重量總和為 j 時所能裝入物品的最大價值總和。所求解為 $dp[W]$ （背包最大重量限制）。
2. 定義轉移式：
   - 不選：價值不變，仍為 $dp[j]$。
   - 選：選後背包剩餘可裝重量為 $j - w_i$。此時的價值就是「容量為 $j - w_i$ 時的最大價值」加上「當前物品的價值 $v_i$」。

最終得到完整轉移式：
$$dp[j] = max(dp[j], \quad dp[j-w_i] + v_i)$$

3. 定義初始狀態：全都是 0。

範例程式碼：

可發現在 0/1 背包問題中，內層迴圈往往是以「逆序」遍歷，也就是 $W \to w_i$ 的走訪。

但到了無限背包問題，就會相反過來變成「正序」遍歷（ $w_i \to W$ ）

差別在於 0/1 背包問題每個物品都只能取一次，而無限背包可以無限取，也就是每件物品可以重複取的情況，因而需要對無限背包改成正序遍歷。

- 正序（無限背包）：計算 $dp[j]$ 時， $dp[j - w_i]$ 是新的狀態，可能已包含當前物品。
- 逆序（0/1 背包）：計算 $dp[j]$ 時， $dp[j - w_i]$ 是舊的狀態，不包含當前物品。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N, W;
    cin >> N >> W;

    vector <int> w(N), v(N);
    for (int i = 0; i < N; ++i) cin >> w[i];
    for (int i = 0; i < N; ++i) cin >> v[i];

    vector <long long> dp(W + 1, 0);
    for (int i = 0; i < N; ++i)
        for (int j = w[i]; j <= W; ++j)
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);

    cout << dp[W] << '\n';
}
```
