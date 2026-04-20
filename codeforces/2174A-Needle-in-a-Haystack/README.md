# 2174A-Needle-in-a-Haystack

**Problem:** [2174A-Needle-in-a-Haystack](https://codeforces.com/problemset/problem/2174/A)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

You got lucky to know the answer to all important questions in the world. This time, the answer is the string s, consisting of lowercase English letters only. You want to hide this string.

You have another string t also consisting of lowercase English letters only. You need to shuffle the letters in t so that the string s appears at least once in t as a subsequence^{\text{∗}}. Among all possible reorderings of t containing s as a subsequence, find the lexicographically smallest^{\text{†}} one.

^{\text{∗}}A sequence a is a subsequence of a sequence b if a can be obtained from b by the deletion of several (possibly, zero or all) element from arbitrary positions. 

^{\text{†}}A string a is lexicographically smaller than string b if and only if one of the following holds: 

 
-  a is a prefix of b, but a ≠ b; or 
-  in the first position where a and b differ, the string a has a letter that appears earlier in the alphabet than the corresponding letter in b.


**Input**

Each test contains multiple test cases. The first line contains the number of test cases T (1 ≤ T ≤ 10⁴). The description of the test cases follows. 

The first line of each test case contains the string s (1 ≤ |s| ≤ 10⁵), where |s| is the length of the string s.

The second line of each test case contains the string t (|s| ≤ |t| ≤ 10⁵).

Both strings consist of lowercase English letters only.

The sum of |t| over all test cases does not exceed 10⁵.


**Output**

For each test case, print a single string: the lexicographically smallest reordering of letters in the string t that contains s as a subsequence. If no such string exists, print "Impossible" instead.


**Example**

**Input**

```
3
dcbe
bedbaecfc
babadab
abacabadabacaba
babaisyou
flagiswin
```

**Output**

```
abcdcbeef
aaaaabababccdab
Impossible
```


**Note**

In the first test case, \mathtt{abc}\,\mathtt{dcbe}\,\mathtt{ef} contains \mathtt{dcbe}.

In the second test case, \mathtt{aaaaa}\,\mathtt{baba}\,\mathtt{bcc}\,\mathtt{dab} also contains \mathtt{babadab}.

It can be proven that these are the lexicographically smallest strings satisfying the given condition.

In the third test case, no rearrangement of letters in t contains s.
