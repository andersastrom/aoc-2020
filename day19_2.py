import itertools


class Day19_2:
    input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

    input = """120: "b"
117: 120 51 | 2 10
37: 120 96 | 2 94
19: 110 2 | 52 120
26: 120 102 | 2 79
2: "a"
32: 120 57 | 2 55
22: 64 2 | 12 120
3: 120 18 | 2 82
5: 2 81 | 120 34
1: 2 120 | 120 131
63: 2 120
71: 120 78 | 2 45
128: 120 46 | 2 62
9: 118 2 | 91 120
36: 82 2 | 63 120
64: 50 2 | 38 120
16: 69 120 | 80 2
92: 96 2 | 50 120
113: 131 18
38: 120 120 | 120 2
6: 2 112 | 120 15
24: 2 1 | 120 18
111: 120 70 | 2 115
34: 2 119 | 120 96
104: 50 120 | 91 2
85: 117 2 | 74 120
12: 2 82 | 120 118
79: 100 2 | 56 120
78: 120 118 | 2 119
116: 2 75 | 120 22
55: 89 2 | 107 120
82: 2 2
119: 2 120 | 2 2
100: 2 23 | 120 68
0: 8 11
50: 131 131
102: 39 2 | 6 120
95: 120 38 | 2 94
21: 119 2 | 63 120
69: 124 120 | 32 2
10: 84 120 | 104 2
49: 96 120 | 94 2
88: 2 82 | 120 63
72: 120 2 | 2 2
76: 77 120 | 106 2
51: 120 9 | 2 35
122: 91 120 | 96 2
109: 2 119 | 120 28
101: 88 2 | 70 120
57: 81 2 | 99 120
83: 98 120 | 30 2
61: 119 2
68: 120 3 | 2 92
86: 2 54 | 120 77
18: 120 120 | 131 2
80: 120 123 | 2 90
74: 2 86 | 120 101
118: 2 131 | 120 120
91: 2 120 | 120 2
131: 2 | 120
121: 63 2 | 82 120
43: 120 50 | 2 60
99: 60 120 | 91 2
20: 66 2 | 99 120
73: 29 120 | 37 2
129: 49 2 | 21 120
13: 120 120
29: 131 94
87: 2 13
107: 2 28 | 120 13
66: 50 131
115: 120 60
65: 2 38 | 120 119
70: 2 63 | 120 18
47: 2 108 | 120 19
108: 17 120 | 116 2
62: 120 63 | 2 18
125: 120 93 | 2 12
105: 113 120 | 114 2
46: 60 2 | 119 120
54: 120 91 | 2 118
94: 120 120 | 2 2
4: 120 53 | 2 95
23: 103 120 | 43 2
75: 70 120 | 127 2
39: 27 120 | 5 2
90: 128 120 | 59 2
59: 65 120 | 36 2
48: 2 118 | 120 63
81: 2 82 | 120 96
130: 2 61 | 120 48
45: 120 72 | 2 96
93: 131 28
35: 120 28 | 2 63
40: 2 118 | 120 119
7: 87 120 | 9 2
106: 2 60 | 120 63
41: 120 9 | 2 65
77: 119 2 | 38 120
58: 54 2 | 61 120
33: 2 29 | 120 109
17: 2 111 | 120 58
8: 42
123: 25 2 | 105 120
11: 42 31
84: 82 120 | 91 2
96: 120 2
56: 33 120 | 73 2
15: 62 120 | 24 2
114: 63 120 | 91 2
112: 122 120 | 44 2
127: 119 120 | 91 2
53: 18 131
124: 4 2 | 20 120
30: 14 120 | 130 2
25: 121 2 | 40 120
97: 120 28
52: 2 71 | 120 7
110: 2 129 | 120 125
60: 120 120 | 2 120
42: 120 16 | 2 126
27: 37 2 | 104 120
28: 2 131 | 120 2
126: 2 83 | 120 85
44: 60 2 | 94 120
31: 2 26 | 120 47
98: 41 2 | 76 120
89: 2 28 | 120 91
67: 120 13 | 2 119
14: 120 97 | 2 67
103: 120 28 | 2 38

abbaabbbababaaaabbababbbbbbaabbaaabaabbb
ababaaabbbaababbbabaabaabaaabaaaaabaaabb
babaabbaaababbabaaaababa
aabbbbbbbaabbbaababbbaab
babaabbbbbabaaaaabababaabbbbaaba
baaaabbbbbababbaabbbbbbbbaababbbbbbaababbbbbbabaaaaabbbbabaabbbabaaaabba
bbbbabbaaababbbbababaaaabbabbbaa
aaaabaaabababbaaabbbbbbbababbbbbbbbbaabbabbbbaaaaaabbaba
aabbbbbbbabaabaabaaaabba
aabbbaabbbabababbabbaaaa
aababbbbabaabbababbbaaba
baabbabbabaaabbabbbaabbbaaabaaababbbbbab
bbababbbbaaababaabaaabbbabbabbbb
babbbbabbbabaabaaaaabbaa
bbbaababaabaaaabaaabbbbb
babbaaababaabbababbbaaba
bbbaabbbabbbaaaaababaabb
babbbabaaaabababbbaaabaaabbbbbbbbbaababbababbbbaabbbbaaaabbbbaaaaaaaabaa
bbababbbbabbabbbbbbabbab
aabbbaabbbbaaababaabaabb
babaabaabbaaaabbbbabbaab
baaaabbbbababbaaaabbabbb
bababbaabababbaaabaaabbababaabaaabbbbaab
bbaaabaabababaaaaababaaaabaaaaabbbaaaabaababaababaababaaababbaabbabbaababbbaaaab
abaaaaabaabbabbabbbbaabbbaaabbbaaababaabbbbababa
baaabbabaababbaaabbbbbba
baaabaabaababaabaabbbabb
bbbbabbaabbaabbbbaaabaaa
abababaaabbababaaabbabababbaaaabbabbbabbbbaaabab
bbbabbbaaaabbbabbaaabbaaabababaabaaaababbbabbbaabbbbabbbaabbbbab
babbbbbbbbabaaaaabbbabaaaaabbaaa
abbbbbaaaabbbbbbbbbbbaab
aabaaaabaabbababaaabbaab
bbbbbbbaababababbbabbaab
babababaaabbaabaabaababbaabbabbaabbabaab
abaaabaaaaaababbbbbbbbbbabbaaaabbabbababbbbbbaba
bbbabbaabaaaaaabbbaabbba
bbbbbbbbaabbbbbbbbbabaab
babaabaabbaaabbababbabbbabaaaaaaaabaaaba
bbbaabbabbaababbbaabbaba
aabaabaaaababbabaaabbbbaaaabbbbbbbabbbbb
abaabababbbababbabbaaaabbababababbabbbabababaabb
baaabbbaaabbbababaabbbaabbbaabbabbbbabbbbbabbaaa
aababaababbabababbaabaaabbbabbaaabaabaaabaaabbbbbaabbbbb
abbbaabbaaaaabbaaabbbbaa
babbaabbbbabbbbaabbababaabbabaabaaaaabab
baabaaabaaaaaabaaaabbbaa
bbbaaabaaababbaaabaaaabb
aabaabaaabaabbabbbbbaabbbbbbbbaababbbbaa
abaaaabbbbbbabbbbbabbbbb
babababaabbbbabaaaabaaba
aaababbbbbaaabaaabbbababaabbaaaa
aabbbabaabababbabbbbaaaabaabbbbbaaabaabbaaaaabababbabbbaaaabaaab
bbbbabbbababaaabbbbabbba
babbbabbababaabaaaaaabbbbbbbaaabbbbabaabbabbabbabbbababa
aaaaabbbbabaabbbbbaaabbaaabaaaabbbbabbbb
abbbbabbabaaabaabababbbbbbababbbbbabaabb
aabbababbbbabbaababaaaba
aaaaabbbabbbaaaabbbbaabbbbabaaab
aaabbabbbaababbbabaaaaabababaabaaaabaabaabbaabab
aaaabaababbaaaaabababbbaabbababbaaabaababbbaaabababaaabbaabaaaab
abaababaabaaaaabbaabbaaababaabbbbbaaaaaababbaaaa
bbbbabbbabbaaaabbabbabbbbaabbabbbabbabab
bbabbbaaaabaabaaaababbababaaaabbaaaaaaab
bbbaabbbbbaabaaaaaaabbaa
baaaaabbaababbaaaaabbbbaababbbaaaababbabbbbbbbabbbaaaaaa
bbbaababaabbabababaaabab
baaaaaaababbbbbbbbababbaaabbabbabbaaaabaabbabbbb
abababaabbbbaaababbbababbaaabababbabbbbababbbabaaaabaabb
bbaabbaabbabaababbbaabaabaabaabbaaababaa
bbbababbabbbabaabaaabbbb
babaabbababbbbbbaabaabbb
aababbaababaabbbbbabbabb
bababbaaaabaaaabbbaaaaaa
abbaaaabaaaabbabaabbbbbbbbbbbaaaaabbaabb
bbbbbbabbaaabbabbaaaaababbaaaabbbababbaaaabaaabb
baaaaaaabaabbaaabaabbaaabbabbabb
bbaababbabaaaabbabbaabbbbbabaababbbbababbbbbbbaa
abbbabababbaaaabaabbabbabaaaaabababaaababbaaaaba
baabaabababaaabaaaababaabbbaaabababaabaaaababbbaaaabaaaa
baabababbbabbbaaababbbaabbaabbbbaabbabbb
bbaababbaabbbaabbbbababbaaaababbbabbaaba
aaabababbaabbbaaabbabaab
bbbbbabbbbaabbaabaabbabaaabababaababaaaabbbabbbabbaaabaabaaaaaabbaaaabaa
aaaaaaaababbaabbbaababbbaaaaaaaabbaaababbaaabaaa
bbabbbababaaabaababbbaaa
bababbbaaabbababbbaabbbbababaaabababbbab
bbbababbbbbbaabbababbbaabaababaaabbbabababbaaabb
bbaabaaaabbbbbaaabbbaaaabbabaabbbabababb
baabbbabbbaaababbaaabaaaaababaabbbaababaababbbaaaaaabbabbbaaaaaaabaaabaa
bbababbaabbbabbaabaaaabbbbababbbbaabaaba
aabbbbbababaaababbbbbbbaaaaabaaaaabababbabaaabbbaaaaaabbbbabbbbb
babaabaaabaabbaabaabaaabaaabaaba
bbbbabbbbbbaabbbbbababaaaabaaaabbabbbaababbaaaaaabbaababaaabaaab
abaababbbbbaabaaabbbbbab
aaaababbaabababbaabbabaababbbaaaaabbabbb
aaababbbbbbabbaaabaaabaaaabaaabb
bbbbaabbbbaabbbbabbababaaabbabaabbaabbaaabaabbba
baababbbaababaabbaaaaabbaaaaaabaaabaaaabbabaabbbbaabbbbb
babbaaabbaaaabbbbaaaaabbbbabbabbbabbabba
bbabbbabbbaaaaabbbaabbaabbababaa
aabbbaabbaabbabbaaabbaaa
abbaaaabbbbbabbbaabababa
bbaabbaaaabbbabaaaaabbba
baaabaabbaaabbabbbbabaab
bbabaabababaabbbbaabbbbb
aabaaaabababbbbbaaaaabab
abbbaabbabaaabbaabbbbabbbbabaabbabababba
bbbaaababaaabbbaaaababba
bbaabbaaaabbabaabbbabbab
baaaaaabbbaababbbbbbabab
babaabbabbaaabaabbababbabbbbabbbaaaaabbbbabbabab
aabaaaaaaaabbbbabbbabaaa
aaaaabbbabbaabbbabaabbba
baaaaabbbbbbbabbaababbabababbaaa
abaaabbababbbabbbbbbbbbbbbbbababaabbaabb
bbbabbaaabaabbbbababaaabbabbbbbb
bbaaabbbaababbaabbaabaab
bbabbabaabaabbababbaaababbabbabb
bbbababbabbaaabaaaaababbaaaabbaababababb
bbbbbababaabbbbababbabbaababaabbabbabbbababbbaaa
bbababbaabbaabbbbbbabaab
bbabbaaaaaabbbbbabaaaabbbabbbbaaabbabbaaababaababbbabbabbabaabbb
abaaabbaabbabbaabbbaaabababaaaba
bbaabababaabbbbbabbbbaaaaaabbaaaabbbaaba
baaaaaaaabbbbbbbbbabaabb
aababaaaabbbbbbbbabababababbaaabbababbaaababbaaaabbaaaba
bbbbabbbaaababbbaabbabbb
aababaabbbabbbbabbaaaabbaabbababbaabaabb
aaabbabbbbbbabbbbabaabab
aaaabbabbabbaabbbbbabbbb
aaaaabbaabaaaabbaabaabaaaabbbbbababbbbaabaaaabbbabbabaaaaabbbbab
abababababaaaaabbbaabbaabababbbababbabaa
baaaaaaababaabaabbaaaabbbababaabaaabbabbaabaabbb
abaaaaabbbbabbaaaaabbbbabbaabbaaabbabbaaabaaaaaabbaababa
abbbabbabababaababbbbaab
bbbbbbbbbbbbbbabbababaaa
baabaaabaaaababbbabaaaab
abbbbbaabababbbbaaababbbaaaaabaa
bbaabbaaabbbbbbbbbabaabb
baabbaaaaabbabaabaabbaaababaabaaababbabaaaaaaabb
babababaaaaababbaababaabaabaaaaabaaabbaabbbbbaba
ababbbaabaaaaabbaaaaabbbaababbababaaaaabbbbbaaaa
babbbabbbbbaaababababbbabbbbabbaabaaabab
baaababababababaabbbbaab
abaaabbaabbbaabbabaaabaa
bbaabbaaaaaaaaaaababbbab
baabbaaababaabbabaabbbbb
aabbabaabaaaaaaaabbabbab
bbababbaabbbbbbbaabbbaaa
abbbbabababbbabbbabaabab
babbbabaabbbababbbaabaaabbababbbaabaabaaaabbbaabaaaaaabb
baaaaaababaaaabbbabababb
bbbbaaabababbaabaabbbbbaabbabbababbbaaab
abbbabaaaabaaaaaabaaaabbabaaaaabbbbabaaa
bbbababbbaaabaabaabbaabb
abbaabbbbbaabbaaaabaaababaabbbabbaabbaba
aabababbbaaabbabbababaab
bbabaaaabbaaabaaaaabaaabbbbababbabaaabaabaaabbbbabbababb
bbabaaaaaaaababbbbabbbabaabbabbb
abbbaabbababaaaabaabbbab
aaabbbbaaabababbabbbabaaababbabbaaaabaabbbbbbaaa
aaaaaaaaababbbaabbbabbbb
abbbbaaabbaaaabbabbbaabaabaabbbbaaaabbbbabbabbaaaabababaaaaaabbabaaaabbbbbbbbbaabbabbbba
babaabaabbabbbbaabbbbbab
aababbaaabaaabbbababbaaa
bababbaabaabbaaaaababbaaaaabbbab
bbabaaaabbabbbaabbaababbababababbabbaaaa
baaaaabbbbaabbbbbbababababaababaababbbbaabbaabaa
bbaabaaabbabababaaababbbbbaabbab
babbbbabbaaaababaabbaaab
ababbbbbbbaaabbaabbaabaa
aabbaababbabbabababbabba
babaababbbbaaaaaaaabaabb
bbbbbbabaabbbaababbbaaaabbbaaaaaaaabbababaabbbabaaabbaab
aabbbaabababaaabaabaabab
babbbbabbbabbbabbabaabbaaabbbbaa
aababbbbababbbaabbaabaaaaabaaaabaaaaabaabbbbbaba
ababbbaaabaabaaababaabaabbabaabbaabaaabb
bbbaabbaaabaaaaabaaaababaaaaaaaaabbababb
bbaabbaaaaabaaababbbbabbaabbbababbaaabaaaaaaabababaaabab
abaabaaaaabbababbabababb
abbabababbbaaabaabaabbba
baababaaabbaabbbbaabbbab
abbbbbaabaaaaaabbbaaaaabaaabbaabbaaabaaa
bababbbbabaaabaabaaaaaaababbaaabbbbbabbaaabbbbbaabbabaab
aaaaabbabaaaaababaaaaaaabbaabaab
bbbaabbbbbbbbbbaabbbbbaaababaaabababababbaaabbbb
abbabaaaabbbbabbbababbab
bbababbbbabbaabbbbaaabab
bbabaaaabaaaabbbaabbabaabbbaabaabaaababaaaaabbbbaabaaabaabbabbba
abababaaaabaaaaaababaabb
baaaababbbbaabbbabbbabbaaaaabbaa
bbbaabaababbabbbaabbaabaabbabbbb
aaabababaaabababbbabbbbaabbbbbababbabbba
bbaaabbaababaaaabbabbabaabbbabbaaaaaabbbbbaaabab
ababaababbbaabbaabbaaaababbbababaaababbbaabaabbaabbabbbb
abaabbabaaaabaabbbbbabbbaaaabaaaababaababbbbbabbbbaaabab
bbaabbbbaabaaaabaaaabbbb
bbaabaaaabbabbaaabaaaabbbaaaababaabaaabbabbabbba
aaaabaabaabbbabababbbabbaaaababa
bbaabbbbbbbabbaababbaaaa
abbbabaaaaabbabbbbaaaaba
bbbaabbabbbaabaabbbaaaab
bababbbaabbaaaabaaaabaaa
abbbaaaaaabbbbbbbbabaaaabbaabbba
abaababbbbbababbbabaaabb
abaaabaabbabbbabbbbabaaa
aaabaaabbaabaaabaaaabbabbbbaaabbbbbaaaababaaababbabaabbbbbaababbbbababaabbaababaaabaaabb
baabbbaaabababaabbabaaab
abbaaababbbaaabaabbaaaabbbbbaaaa
abaaabbbaaabbbbaaabbbaaabbababaaaaabaababababbbbbbaaaabababaababaaaabaab
baaabababbaaaaabbbaaaaabbbbbbbabaaababaabbbabbbb
aabbbbbbaabbababababbabb
abababaaaaababababbababaababbbbbaaabbbaaaaaabbbb
bbabaaaaabaababbaaaabbba
bbbaabbbbbabbbabbaabaaaa
bbaaabbabbbbbbabbbabaaaaaabbbbba
bbabaabbabbbabbbbabaabbaabbaabbbaabaaababbababba
aabbabbaabbabaaabbaabbaabbbaabaaababaaabbbbbabab
aabaaaaaaababbaabaaaaabaaaaabaabbaaababaaabbbbab
babbaabbabbbababbaaaaabbaaaabaabbabbaaba
abaababbbaaababababbabba
aabbababababaaababababba
baaaababaaaaabbababaabab
aababbaaabbbbabaaabaaabb
ababbbbbaaabbbbaaabbaaab
baababaabbabaabaaabaaaaababbaaabbabbaaaabbabaabbabbabaab
ababbabbbbbaaabbbbabaaaaaabbaaba
aaabaaababaabababbbaaabababbbbbbabbaabaababbbaab
abbaaaabbaaaabababaabbaabbbaabbbabbaabba
abbabababbaabbaababbbabaabbbaaaabababaabbabaabbabbaabababaaababb
baaaaaaaabaabbabbababaabbbaababababbabab
aabbbbbbaaaababbabbbaabbbbbbbabbaaaaaaab
abbaabbbbaaaaaabbabbbbbbbaaaaabbabaaabbbabbabbbb
babbbbbbbaaababaaaabbaba
bbbbabbbbaaaaaaaabaababaaaabbbab
aaabaaababaababbbbbababbbbaaaaba
abbbbbbbbbbabbaaababaaabbaaaaabbbabaaaab
aabaaaababbbababbabbaaabbbbaaaabaabaaaba
abbbbbaaababaaabababaaabaaaabaabbaaabbbabbbabbbaababbbab
abaabbbbabababaabbaaabaababbabbbbbaaabaaaaaababbaabaaaab
bbaaaaabbaababbaaaaaaababbaaabbaaaaaabab
babbbbbbabaabbaaaabaaaaaabaaabbbbaababbabaabaaaa
aaaaabbabbbbbbbbaaaabbabbaababbabbbbbaab
babbaaababbaabbbbaaabababbabaaaaaabbaaaa
aabbabbababbaaababaaaaaa
bbaaaabbaaaababbaaabbaabbbbabababaaababbbbbbababbaabbaaababaababbbbaababaaaaabbaaaababbababbbbaa
babababbaabbabaabbbbabababbbbbaaabaaabbaabbbaaabbbabbbba
aabbbabaabbbabbaabbabbba
abbaaaababbaababbaaaabababaababbbbbaaaab
aabbabbaaaaaaabaabaabaaabbaabaaabbbbbabbaaababbbbbababaa
abbaaaabbabbaaabbbababaa
abaaabaabaababaabaaaababbabbaaba
bababbbbaaabababbbabbbbb
bbabbababaababbbbbbabbbb
bbbaaababaaabbbabbababbaabaaabba
baaaabababaababaabaaaaababababaaaaabbabbbaabbbab
baaaabbbbbaabbaabbbaabaaaabbaaab
baabbabbbbaaabbbaaabbbaa
bababbbabbbaababbbbababa
bbabbbababaaaaabbbaabaab
babbaaabbbabbbabaabbaabb
bbaaabaabbbbbbbaaaabbbbb
bbbaabbbbabbbbabaaaaabab
baaaabaabbbabbbabbbbbbaabaabababbaabbbbbbaaaaabbbbabaabbabbbabaa
bbbbbbbbbbabbabababbbaab
babaabababbbaaaaabbbaabbaaabaaabbabaabbaabbaaabababbbabaabbbbbbbaaabbbaa
aaaaaabaabbbaaaaabbbbbba
bbbaabaabbaaaaababaabaab
babbaababbbbbbbaaabbbbbbbbbabbbbbabaaaaabbababaabaabaaabbabaabbaabbbbbbabaababba
aababbaabaaaabbbbbbbbbaa
bbaaabaaaabbbabaababbabbaabbbbbbbabbabbbbbaabbbbabbabaabaababaaabbaaaaaa
aabababbbabbbabbbbbbbbaa
baaabbbabaabbbaaaaaabbbb
abaaabaaaababbaaaabaaaba
abababbbaaabbbaabbaaaabbaabbababaabbbabbbbbbbbbaabbbbaabbabaabbb
abaaabbabababaabaabaabab
aabbaabaabbbabaabbabbabaaabaaaaaaabbbabaaabbababbabbaaaa
bbbaabbabaaaabbbabbbbaaa
aaabababaabbbbbbbaababbbaabaaabbbaaaabaaabbababb
baaaabbbaaaabaabbaaaababaaaababa
abaaabbbababaaababbaabbbaabbbbbbbbabbababbaaabbbabbababb
bbabbabaabbbbabaaaaabbababbbbaaa
baabbabbbbbbbbabaaabaaababbaaaaa
bbaaabbabaababbaaabaaaaaaabaabaaabbaabab
bbaaabbababbabbbaababaabbbaabbaaabbbaaba
bbababbbbbbaaabbaaabbbbaababaaababaabaaaaaabbaabbaabbaab
ababababbbabbbaaababbbaabbabbabaabaaaaaa
bbbbbabbabbaaabaaaabbaaa
baaabbabbbaaabaabbaaabaabbaaabbabbabbabababababb
aaabbbbaaabbabbabbbbaaba
baaabaababaaabbbbbbababa
bbbbbbbbbbabaababbbbabab
baaabbbaaaaabbabaaabababaaabbbbabababbab
abbbaaaaababbabbbbbbaabbaabbabbababbbabbbbaaaabbbbbbbbaa
bbababbbaaabbbbabaaababb
aabbbbbbabbbaaaaabbbbbaabbbbbbabbabbabaa
bbabbbabbabbbabbaabbabaabbabaaaabbbabbbb
aaababbbaabaaaabbbabbaab
babbabbbbbabbbaaababababbabbaaababbbbbaabbabbbbbbbbabaab
baaaababaabbababbaaabaaa
abaaabbbaaaaaabaaaababbbbbbbbbaa
babbaabbabaaabaaaaaababa
baaabababbaabbbabbabbabbbbababbaaaaababbbbbbaabbbbbabbaaaaabbbbbabbbabba
abbbbababaaaabbbbbbbbaaa
babababaaabbbbbbbbaabaab
bbbaababaabbbbbbbbbabbab
bbabbabaaaaababbbbaabaab
baaaaababaabbabbbabbbbaa
bababbbbbbbaabaabaaababababaaabb
bbbbbaaabbbbabbabaaabbabaaaaababbaaababbbbbaabbabbaaaaaaaaaaabaabbaaaaabbbabaaaa
bbababbbbbaaaaabaababbbbbaabaaaa
bbaaabbaabbabaaabaabbabbbbbbaaba
baabaabaabbaababbbbaaababbbbbbabaabaaaaaabbbbbabababaaaabbaaaaba
baabbabbabbbaaaabbbbbaaa
bababbbaaaabbabbaaababba
aabababbabbbaaaaabaabaab
bbaaabaaababbbbbabaaabbbbbababaa
bbbaaabbababbbbbbbbbaaba
aabababbbabbbbbbabbbabbb
aabababbaabbaabaaaaaabbbbbabaaab
aabbbbbbabaaabbbabbaaaaa
aababaabbbaabaaaabbbaaaaabbaabaa
babbbbbbbabaabbababbbaaa
bbbbaaabbabbaabbbbbbbbbbbbaaabbbaabaabba
babbbababbbbbbbbbbbbbaab
babaabaaaaaababbaaabababbbabaaaaabbaabbbaaaaaabbabbaabab
ababaaaabbababbbabaaaaaa
baaaababbbababbbabbababb
aabbabbabaaaababbaababbbbaabbbabaabaabbaabaabbaaaabbaabaaaabbbab
abaababbbababbbbbbbbbaab
babaabbabaababababbbabbaabaabbabbbaababbabbabbbb
ababaabababbaabbaabbaabb
aaaabaaaababaabaabbbbbab
abaaabbbaaababbbababaabb
bbbaababaabaabaabaababbaabaaabaabbbbabbabbbabbbaababbbbaaabbbaaa
bababaabbaababbabbbbabbbaaaabbbb
abbbbbbaabbbbbaabbbababbabaaaabbabbbbbbbabbbabaaaaaaaabb
aabaabbbaaaabbaabbabbaaaabababbabbabaabb
aaababbbbbbaabaaaabaabaabbbabaab
baaaababaabbabbabbaababa
abbabababbababbabaaabbababbbabbb
babbabbbaabababbbabbaaba
bbabaabababbbbababbababb
abbbaabbabaabababbaaabbbbaabbaaabbbbaabbaabbbbba
babbbbabbbabbabaabbbabaaabbabababababbbbaabaababbbaababa
bababbbaaaaabaaaabababbb
babbaaababaaabbabababbbabbbbabaa
babaabbabbbaabbbabbaabbbaabbabbb
bbbaababaabaaaaaabaaabaabaababababaabbaaaaabbaabaaaabbbaaaabbaab
babbbaabaabbbabbabaaaaab
abbbbaababbaabaaaaaabbbbaaaabaabaabaaaba
bbbababbbaaabbbabbbbabaa
bababbaaaaabbabbbbabbbabbbbaaaaa
abaaaaabbbaaabbaaaabbbbaabaababbaabaabbb
abbbaabbabbbaaaabbaaaaaa
babaabbbbabababaaabaaaaaaabaabab
bbaaabbbaabbbbbbaababaaa
abbbbabaaabbbbbbabbbaaab
aabbabbaababaabaabbababaababaabb
aaaaaaaabbabaabaabaabaab
abbabaaaabbbbbbbabbaaabb
bbabaababaababbbbbaababbbaaabbbabaaaaaaabbbbbabbbbabbbbb
abbaaaabbbaabbbbabbbbbbbabbaabbbbbaabbbaabbaabba
abbaaababaaaaabaabaaabbabbaaabbaaababbbbabbaabaaabbababbabbbbaaa
aaababbbbbabbbaabbababaa
baaaaabaaabbababbabaababaaaaaabb
babbaabbaaaaaababbaababa
aaaabbabbabbabbbabbaaabababbaaaabbabaaab
abbbaaaababaabbbbbabababbbbbabaa
baabbabbababbabbaabbbabaabbabababaabababaaaabbbababbaaba
baababaabaaaaababbababaa
bbabbbaaaabaaaabbaaabbaa
bbbbbbbabbbaababaabaabbb
baaaabbbbaaabaabbaaabbbb
aaaabaaabaaaababaabaabaaabaabababaabbbbbaaababba
bbabbbbaaaabbabbbabaabaabababaaababbbbba
abaaabbbbabbbbbbbababbbaabbbabbabbbaaaaa
aabbbbbbbbbaaabbabbabbab
aaabbabbaaaabaababbabbbb
baaaabbbaabaaaaaaabbabbb
bbbbaaababaaabbabababaabbbabbaaa
aaaaaabababaabbbababaaabbababbbabbbaaaaaaabbbaaa
aabbabababaabaaabbababaa
abaabaaabbabbbbaabaaabbaaaaaaabb
bbbaaaaaaaaaabaabbaaaaaabbabbaaabaaabbbbabbbbaab
bbaaaabbaabbabaabaabbaaaabaaababbabaabab
baaabbbaabaaabbbbbbbbbabaaaaabababbabbab
bbbbbbbabbababbaabbabaab
baababbbbabababaaaaababbaababbabaaaaabab
bbaaaabbaaaaabbaababbaaa
bababbaabbababbbaabbbaababaaabaaaaabababbbbaabaabbbabbbbaaabbaaa
bbaaaabbabbabaaaabaaaaaa
babbbabbbbabaaaabaaabbbabbaabbab
abbbbbbbabbbbabaaaababbbabbbaaabaaabbaabaabaabbb
aabbbbbbbabbabbbabaaaaabaabbbbbbbabbabbbaababababababaaa
abaabaaaaabbabaaaabababa
babbbbbbaaabaaabaaabaaaa
abbaabaabababbbbabbbbaababbbaaaaabaaaabbbbbababbabbaaaba
abaabaaaaabaaaabbbbaabbbbbbababbbbbbabaaabbababb
abababaabaaabababbababbbbbbbaaaababbabba
bbbaabbaabaabbaaaaaaabaa
babaabaaabbbababbbababbaaaabbaba
bababbaabbaaaabbbbbaababaaaababbaaaabbabbaabbbabbababbab
bbabbbaaaabbbaabaaaabaabaabbbabb
babababaababbbaabbbbbbbaaabaabaababbaaabbaaaabbabbbabbba
bbbaabaaabbabbaabaaaaabaaaabaaba
baaabbbaabbabbaaaabbababbbabbabbaabaabbb
babaabbababbabbbaaabbaaa
baabababbbbaaabbbbbababa
abbbbbbbbaababaaaaabaaababbbabbabbbaaabaabbbabbb
aaaabaababbabaaabaaaaabaaaababaa
abaabbaaabbbbbbbbaaabbbabbababbbbbabaabb
bbababababbaaabaaabaabbb
babbabbbbbbababbbaaabbbb
bbbbaabbaababbaaaaaababa
ababaaabbaaaaababbabbbbb
aababbbbbabaabbbabbbabaaaaaaabab
baababbbabaaabaababaabaabbaababa
abaababbbabbbbbbabababaababaaabb
baaaaaabaabaaaabbbbbbaba
aaaaababbbaaaabaaaaaaaabaabbababbbbabbbbbbbaabababbbbbbabaabaababbaaaabbaabbabbbbabaaaabbaaaabba
babaabbaaaabababaaaaaabb
babbbababbabbbababbaaabb
bbabbbbabbaaabbabaaabbbaabbbbaaaaababbba
bababaababbbbabababaabab
baaabbbaaababbaabbaaaabb
bbbababbaaababbbbaababbbbabbbaaaaabbabbaaabbbbaabaabaababababbabbbbbabaabbaabbab
aabaabaaabaaabaaabbbaaaaababababababbbba
aaaabaaabbabbbabbaabbbaabaabbbbbbabaaaba
abbbaaabaabaaababaababaaabbababbaaaabbabaabbabaaaabbaabbaaaaaabaaaaababbbbbababb
abaaaabbbababbbabbbabbbb
aababbaaabbbbabbbbaabbaaaabbabbbabbaabba
bababaabbbabbabaaabaabbb
aabaabbabbaaaabaabbbbaaa
babbbabaabaabbaaaaaaabaa
aababbaaaaabbbbaabbbabaababbbaabaabbaaaa
babaabbaabbbbabbaabaabab
bbbaababababaaaabbbaaabbbaaaaabbbbbbbaaabbbbabaa
bbbabbaabaaaabbbaaabbbab
baaaabbbaaaababbaabaabaabaaaaaabaabbbbaa
bbaaabbbbaabbbaabbaabaaaaabbaaab
aaaabaabbbbaabbbabbabbba
bbabaaaabbbbbabbbbbaababbabbaaabbbaaabbbbabbbbbbbaabbabaabbbabbbbaaaabbabaabbaba
aaaabbabbbbbabbbbaabbbaabbaababbaaabaaabbbaaabab"""

    rules = dict()

    def __init__(self):
        rules_raw, messages_raw = self.input.split('\n\n')

        for r in rules_raw.split('\n'):
            nr = int(r.split(':')[0])
            rule = r.split(':')[1][1::]
            self.rules[nr] = rule

        comb1 = set(self.recur(42))
        comb2 = set(self.recur(31))
        sub_len = len(list(comb1)[0])
        sum = 0
        for message in messages_raw.split('\n'):
            if len(message) % sub_len != 0:
                continue

            comb1_matches = []
            for i in range(0, len(message), sub_len):
                comb1_matches.append(message[i:i + sub_len] in comb1)
            comb2_matches = []
            for i in range(0, len(message), sub_len):
                comb2_matches.append(message[i:i + sub_len] in comb2)
            for i in range(len(comb1_matches)):
                if all(comb1_matches[:i]) and all(comb2_matches[i:]) and i > (len(comb1_matches) - i):
                    sum += 1
        print(sum)

    def recur(self, i):
        combinations = []
        rule = self.rules[i]
        if "\"" in rule:
            combinations.append(self.rules[i][1:-1])
        else:
            options = rule.split(' | ')
            for option in options:
                values = []
                for key in option.split(' '):
                    values.append(self.recur(int(key)))
                for c in itertools.product(*values):
                    combinations.append("".join(c))
        return combinations


Day19_2()