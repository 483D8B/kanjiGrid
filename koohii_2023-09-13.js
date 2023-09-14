var csvData = 
`FrameNumber,Kanji,Keyword,LastReview,ExpireDate,LeitnerBox,FailCount,PassCount,Vocab
1,"一","one",2023-09-13 00:56:04,2023-09-19,2,0,1,""
2,"二","two",2023-09-13 00:56:04,2023-09-17,2,0,1,""
3,"三","three",2023-09-13 01:21:31,2023-09-17,2,0,1,""
4,"四","four",2023-09-13 01:21:31,2023-09-19,2,0,1,""
5,"五","five",2023-09-13 01:24:58,2023-09-17,2,0,1,""
6,"六","six",2023-09-13 01:24:58,2023-09-19,2,0,1,""
7,"七","seven",2023-09-13 01:24:58,2023-09-18,2,0,1,""
8,"八","eight",2023-09-13 01:24:58,2023-09-18,2,0,1,""
9,"九","nine",2023-09-13 01:24:58,2023-09-19,2,0,1,""
10,"十","ten",2023-09-13 01:24:58,2023-09-18,2,0,1,""
11,"口","mouth",2023-09-13 01:24:58,2023-09-18,2,0,1,""
12,"日","day",2023-09-13 01:24:58,2023-09-19,2,0,1,""
13,"月","month",2023-09-13 01:24:58,2023-09-19,2,0,1,""
14,"田","rice field",2023-09-13 01:24:58,2023-09-19,2,0,1,""
15,"目","eye",2023-09-13 01:24:58,2023-09-17,2,0,1,""
16,"古","old",2023-09-13 03:57:16,2023-09-17,2,0,1,""
17,"吾","I",2023-09-13 03:57:16,2023-09-14,2,0,1,""
18,"冒","risk",2023-09-13 04:03:37,2023-09-16,2,0,1,""
19,"朋","companion",2023-09-13 04:03:37,2023-09-15,2,0,1,""
20,"明","bright",2023-09-13 04:03:37,2023-09-14,2,0,1,""
21,"唱","chant",2023-09-13 04:07:54,2023-09-16,2,0,1,""
22,"晶","sparkle",2023-09-13 04:06:50,2023-09-15,2,0,1,""
23,"品","goods",2023-09-13 04:03:37,2023-09-17,2,0,1,""
24,"呂","spine",2023-09-13 04:06:50,2023-09-17,2,0,1,""
25,"昌","prosperous",2023-09-13 04:07:54,2023-09-16,2,0,1,""
26,"早","early",2023-09-13 04:07:54,2023-09-15,2,0,1,""
27,"旭","rising sun",2023-09-13 04:07:54,2023-09-15,2,0,1,""
28,"世","generation",2023-09-13 04:07:54,2023-09-15,2,0,1,""
29,"胃","stomach",2023-09-13 04:07:54,2023-09-17,2,0,1,""
30,"旦","nightbreak",2023-09-13 04:07:54,2023-09-16,2,0,1,""
31,"胆","gall bladder",2023-09-13 04:07:54,2023-09-17,2,0,1,""
32,"亘","span",2023-09-13 04:07:54,2023-09-16,2,0,1,""
33,"凹","concave",2023-09-13 04:07:54,2023-09-17,2,0,1,""
34,"凸","convex",2023-09-13 04:07:54,2023-09-15,2,0,1,""
35,"旧","olden times",2023-09-13 14:48:21,2023-09-14,2,0,1,""
36,"自","oneself",2023-09-13 14:48:21,2023-09-14,2,0,1,""
37,"白","white",2023-09-13 14:51:50,2023-09-16,2,0,1,""
38,"百","hundred",2023-09-13 14:51:50,2023-09-16,2,0,1,""
39,"中","in",2023-09-13 14:51:50,2023-09-14,2,0,1,""
40,"千","thousand",2023-09-13 14:51:50,2023-09-14,2,0,1,""
41,"舌","tongue",2023-09-13 14:51:50,2023-09-14,2,0,1,""
42,"升","measuring box",2023-09-13 14:54:21,2023-09-16,2,0,1,""
43,"昇","rise up",2023-09-13 14:54:21,2023-09-17,2,0,1,""
44,"丸","round",2023-09-13 14:55:36,2023-09-17,2,0,1,""
45,"寸","measurement",2023-09-13 14:55:36,2023-09-17,2,0,1,""
46,"肘","elbow",2023-09-13 14:55:36,2023-09-15,2,0,1,""
47,"専","specialty",2023-09-13 14:55:36,2023-09-17,2,0,1,""
48,"博","Dr.",2023-09-13 14:55:36,2023-09-17,2,0,1,""
49,"占","fortune-telling",2023-09-13 14:55:36,2023-09-17,2,0,1,""
50,"上","above",2023-09-13 14:54:21,2023-09-14,2,0,1,""
51,"下","below",2023-09-13 14:54:21,2023-09-14,2,0,1,""
52,"卓","eminent",2023-09-13 14:55:36,2023-09-15,2,0,1,""
53,"朝","morning",2023-09-13 14:55:36,2023-09-17,2,0,1,""
54,"嘲","derision",2023-09-13 14:55:36,2023-09-15,2,0,1,""
55,"只","only",2023-09-13 17:47:06,2023-09-16,2,0,1,""
56,"貝","shellfish",2023-09-13 17:47:06,2023-09-17,2,0,1,""
57,"唄","pop song",2023-09-13 17:50:14,2023-09-14,2,0,1,""
58,"貞","upright",2023-09-13 17:50:14,2023-09-14,2,0,1,""
59,"員","employee",2023-09-13 18:50:52,2023-09-14,2,0,1,""
60,"貼","post a bill(stick)",2023-09-13 20:38:26,2023-09-14,2,1,1,""
61,"見","see",2023-09-13 17:50:14,2023-09-15,2,0,1,""
62,"児","newborn babe",2023-09-13 17:50:14,2023-09-14,2,0,1,""
63,"元","beginning",2023-09-13 18:50:52,2023-09-14,2,0,1,""
64,"頁","page",2023-09-13 17:50:14,2023-09-14,2,0,1,""
65,"頑","stubborn",2023-09-13 18:53:41,2023-09-14,2,0,1,""
66,"凡","mediocre",2023-09-13 18:50:52,2023-09-14,2,0,1,""
67,"負","defeat",2023-09-13 18:53:41,2023-09-14,2,0,1,""
68,"万","ten thousand",2023-09-13 18:50:52,2023-09-14,2,0,1,""
69,"句","phrase",2023-09-13 18:50:52,2023-09-14,2,0,1,""
70,"肌","texture",2023-09-13 18:50:52,2023-09-14,2,0,1,""
71,"旬","decameron",2023-09-13 18:23:35,2023-09-15,2,0,1,""
72,"勺","ladle",2023-09-13 18:23:35,2023-09-14,2,0,1,""
73,"的","bull's eye",2023-09-13 18:52:42,2023-09-14,2,0,1,""
74,"首","neck",2023-09-13 18:23:35,2023-09-14,2,0,1,""
75,"乙","fish guts",2023-09-13 18:23:35,2023-09-15,2,0,1,""
76,"乱","riot",2023-09-13 18:52:42,2023-09-14,2,0,1,""
77,"直","straightaway",2023-09-13 18:52:42,2023-09-14,2,0,1,""
78,"具","tool",2023-09-13 18:52:42,2023-09-14,2,0,1,""
79,"真","true",2023-09-13 18:52:42,2023-09-14,2,0,1,""
80,"工","craft",2023-09-13 18:26:08,2023-09-16,2,0,1,""
81,"左","left",2023-09-13 18:52:42,2023-09-15,2,0,1,""
82,"右","right",2023-09-13 18:52:42,2023-09-16,2,0,1,""
83,"有","possess",2023-09-13 18:52:42,2023-09-16,2,0,1,""
84,"賄","bribe",2023-09-13 18:52:42,2023-09-14,2,0,1,""
85,"貢","tribute",2023-09-13 18:52:42,2023-09-14,2,0,1,""
86,"項","paragraph",2023-09-13 20:38:26,2023-09-14,2,1,1,""
87,"刀","sword",2023-09-13 18:26:08,2023-09-16,2,0,1,""
88,"刃","blade",2023-09-13 18:49:19,2023-09-16,2,0,1,""
89,"切","cut",2023-09-13 18:53:41,2023-09-17,2,0,1,""
90,"召","seduce",2023-09-13 18:53:41,2023-09-14,2,0,1,""
91,"昭","shining",2023-09-13 18:53:41,2023-09-14,2,0,1,""
92,"則","rule",2023-09-13 18:53:41,2023-09-14,2,0,1,""
93,"副","vice-",2023-09-13 18:53:41,2023-09-14,2,0,1,""
94,"別","separate",2023-09-13 18:53:41,2023-09-14,2,0,1,""
95,"丁","street",2023-09-13 18:49:19,2023-09-17,2,0,1,""
96,"町","village(small town)",2023-09-13 18:49:19,2023-09-14,2,0,1,""
97,"可","can",2023-09-13 18:53:41,2023-09-16,2,0,1,""
98,"頂","place on the head",2023-09-13 18:53:41,2023-09-14,2,0,1,""`;
