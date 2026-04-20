# 1165B-Polycarp-Training

**Problem:** [1165B-Polycarp-Training](https://codeforces.com/problemset/problem/1165/B)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

Polycarp wants to train before another programming competition. During the first day of his training he should solve exactly 1 problem, during the second day — exactly 2 problems, during the third day — exactly 3 problems, and so on. During the k-th day he should solve k problems.

Polycarp has a list of n contests, the i-th contest consists of a_i problems. During each day Polycarp has to choose exactly one of the contests he didn't solve yet and solve it. He solves exactly k problems from this contest. Other problems are discarded from it. If there are no contests consisting of at least k problems that Polycarp didn't solve yet during the k-th day, then Polycarp stops his training.

How many days Polycarp can train if he chooses the contests optimally?


**Input**

The first line of the input contains one integer n (1 ≤ n ≤ 2 ⋅ 10⁵) — the number of contests.

The second line of the input contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 2 ⋅ 10⁵) — the number of problems in the i-th contest.


**Output**

Print one integer — the maximum number of days Polycarp can train if he chooses the contests optimally.


**Examples**

**Input**

```
4
3 1 4 1
```

**Output**

```
3
```

**Input**

```
3
1 1 1
```

**Output**

```
1
```

**Input**

```
5
1 1 1 2 2
```

**Output**

```
2
```
