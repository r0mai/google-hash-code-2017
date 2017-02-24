#!/usr/bin/env python3

import subprocess

data = {
 "id": "5856783499264000",
 "round": {
  "id": "5293824016384000",
  "name": "Online Qualification Round",
  "problemBlobKey": "blob/AMIfv96DUQ98S642Eh6Q8n_JJ8mkWH0U_Ywh2wrWzYJldBdT8I6b_cME7dgTCOT6fbYg-23xeI0UsYahApI-lKK12HH1vDCQfnYqzuaRGQHT65tPrrsD6wIuez-rigwG_imUOQmxSy5bA_Fj_gq9arGbCyJgA-mA4Fx30-4t5pEuyP-_6yncAzV9w3n7lu_POia1y1BAjMZJW6tyjeHQ4-dDySQQZRtBhKnWrdG7YvLgFsyiaB7a_YVFgxHdmOWvmeQ1rKkcjyIxS7uMjrjgBC4sNOWgblf5pT9QAYarMVQM0kfHGEE25g2zO0TW4sMlEZjT_DZSSDjJ6t7uCGuCK0AQDoSn5L_9I3pRu7d-6QBUT2qgwaNyq-7HnEKhOLUwsLhCcYzzUbXY",
  "scorerLabel": "stream",
  "visualization": "stream",
  "hideScoreboard": False,
  "adminOnly": False,
  "start": "2017-02-23T17:45:00.000Z",
  "end": "2017-02-23T21:30:00.000Z",
  "freezeStart": "2017-02-23T20:30:00.000Z",
  "freezeEnd": "2017-02-23T21:40:00.000Z",
  "clarifications": "On page 3, the comment for the sixth line of the example input file (\"1 300\") should read: \"The latency (of endpoint 0) to cache 1 is **300ms**.\"",
  "dataSets": [
   {
    "id": "4881867933220864",
    "name": "Kittens",
    "inputBlobKey": "blob/AMIfv960aAmoeUIuOuiyVio2SD9lWIbIi2cUgztsWT7Hut7s01ijrUa2eaMf23V24rxodzLywW1w4unMQH-JZoJNYkSUxFK0N3V6PFMQXeEQnCurWllquX2-lpwkugFcZK0uxMVijqoqIFDFgm-tvXyIRnRRlUJDPnaTS0dK6zt-YF0_QUZFjQdPUiiVsioPR1UMvOOCL4hX9fhsg4kjvYWrCjXdByX9S6BPHrBQfmlngtU_bQxZQAi0pzHMspXip2S5qARWt-NZv0UeeRFl2TknumerdPcnv9TCAWsJNGzIO9NfbC9ACCjDE9MCo-7i5etgdanMSIV2h9wYuJ4wS3qz18UfKqjUO_FHtO2c_Zo4spfTWlJZ_tu-vZO-qL4T1UmGMD2JRnHi"
   },
   {
    "id": "5570727000408064",
    "name": "Me at the zoo",
    "inputBlobKey": "blob/AMIfv97gjia08wBirDRDPkceNYWx49Yqyd6niI9EpSszsxrRlqBMfVqlnfKLkC0WSPXMjE7atqqnYRWP9OoGwgbUr5QE1JFbtgKdF1BT7KzxUIYBtUYxG-gXVQcFhNJGrwKaAwCr0NI4FYY1ptmHe8mKJwyLxPl7RvhLP4NjpPzrBhRM7AQ_CwdgT3j69uKRzBndWmATmvamHSi7s3CY3LQWST1whQYDh8fVfCsKMrwwxrfboRoaes1DhZnEta6ebf-Iq3ECOvpeM547xR2L7-kzIsMrAF8EOnNbY4J1Dt1TBCgNQkeKpf-178kd-No_RPmQJ0Pnc1XPTXxhITxmrcdMvw_4gczF_86RQ7EBIHWJ9QNxsw9SjhCD1zHwENMsJylIGtrw5u9g"
   },
   {
    "id": "4919276561498112",
    "name": "Trending today",
    "inputBlobKey": "blob/AMIfv97hm6b9UYSrIz6pq2xMwgWRrVxik7VHz0GvKIrKR566ctvWTFNDGGO_LJrcH4laVdYcwTitbr8AANjfteMJvt0lWqpw3wLNGqXE4D5ZtwxZVAx-j-aAWPKTeLAO0xm0k-cUZP_MZlWNSoMw4uOxQdzzt5wZwawl09GHYV-gd1rEGX2dmzlm8p1umuVidWv59GL_6i2-q98_Xg4Wo-lZHSlzGcCUgxm1mLE14Ag6KQBSVcZgsuCeDboI1QxUvLnG3kkdhWDFStm7VqkkRi6aHgTNxMgyFyLlNlPxAJpGDmsoLZXZFZ243C7_ftfElp1lXposOgPZO7ql77w33IRTuO47UgXq-bbQ0Cqd-5jONbRSe17hvjWTjdv5b3UhZj3cTBDu3ffC"
   },
   {
    "id": "6412425163177984",
    "name": "Videos worth spreading",
    "inputBlobKey": "blob/AMIfv97hRTjWV6LZ2oahTzGf3wjval4E6W4PtlEh7ODDKw7S85pVYQMoopXMB11nclcNb5ceXKATKvOBmNFB-ttAOj-pGbyzZ11HSEKMxZQ1P-tASnM7F252OH0_cRExHjPVICZoxE5vT3Cgkey5-aKem2XDN5I-xV_bzVFqKnla1D5C2xSNOT8qtRZ8jVd82FssHE5VXL9q21PBHCGBE6w_js4XQEUxy-VZAqSy2srI53m12gO_0v0P4Hf__5fcvsAmHhTSznH4fVLXl51cEVbcO2KAM8vyhUZDTzd7TQCV0Ruo8AHiCPomYAP5y0W9or1G_9oe1CB3_9jsdGsJ3zRnxYFpeRGPmnTxQiRAhKsllykbJP8RYZfwgoIeukR1aEq47JXmhKpc"
   }
  ]
 },
 "time": "2017-02-24T10:27:12.813Z",
 "entries": [
  {
   "teamName": "Ababahalamaha",
   "teamId": "6377364808269824",
   "score": "2651999",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "All In",
   "teamId": "6303231793692672",
   "score": "2650005",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Switzerland",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Past Glory",
   "teamId": "5511276331532288",
   "score": "2649544",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "H(K XOR opad, H(K XOR ipad, text))",
   "teamId": "6642699096555520",
   "score": "2646990",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "NIN Team",
   "teamId": "6314053567774720",
   "score": "2646341",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "<(OvO)>",
   "teamId": "6368407653974016",
   "score": "2645237",
   "hubId": "6156894674616320",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Qualified Quad",
   "teamId": "5365209392742400",
   "score": "2644948",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Ukraine",
    "Russia"
   ]
  },
  {
   "teamName": "Bathers",
   "teamId": "5768125844815872",
   "score": "2644019",
   "hubId": "0",
   "countries": [
    "Russia",
    "Ukraine",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Bibeleskaes",
   "teamId": "4849655477174272",
   "score": "2642844",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "LessCaparos",
   "teamId": "5938621618061312",
   "score": "2641955",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Scorpions",
   "teamId": "6134964370276352",
   "score": "2641125",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Omogen Heap",
   "teamId": "6429925879840768",
   "score": "2641021",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "abacabadabacaba",
   "teamId": "6492573011017728",
   "score": "2640554",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Dasha hochet v Paris",
   "teamId": "6447424583237632",
   "score": "2640476",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "ENS5minutes",
   "teamId": "4786261961211904",
   "score": "2640301",
   "hubId": "5199323260256256",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Stealth Phoenix",
   "teamId": "4873405304143872",
   "score": "2639308",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Rashko",
   "teamId": "4568998423298048",
   "score": "2638862",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "AIM Tech",
   "teamId": "4851739341619200",
   "score": "2638613",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "BozziBoys",
   "teamId": "6407089068965888",
   "score": "2638601",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "qoloe",
   "teamId": "5050254810415104",
   "score": "2638033",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Switzerland"
   ]
  },
  {
   "teamName": "Warsaw Tigers and Tigress",
   "teamId": "5203136184582144",
   "score": "2637842",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Messi",
   "teamId": "5146142706761728",
   "score": "2637829",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "; DROP TABLE teams;--",
   "teamId": "5037475537879040",
   "score": "2637814",
   "hubId": "5173732637147136",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "void*",
   "teamId": "5121027818389504",
   "score": "2637310",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Broders",
   "teamId": "4773288542732288",
   "score": "2636013",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "tratata",
   "teamId": "5276618444505088",
   "score": "2632701",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Morituri",
   "teamId": "5750643717308416",
   "score": "2632267",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Jinotega",
   "teamId": "6324704281362432",
   "score": "2629225",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "unusual.og",
   "teamId": "5610129902796800",
   "score": "2628586",
   "hubId": "0",
   "countries": [
    "Latvia",
    "Latvia",
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "TUMbleweed",
   "teamId": "6042508555452416",
   "score": "2628109",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Bouncy Crocodile Rainstorm",
   "teamId": "6579914660642816",
   "score": "2627501",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Greece",
    "Latvia"
   ]
  },
  {
   "teamName": "Shaky",
   "teamId": "5748875264524288",
   "score": "2625970",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "2young2simple",
   "teamId": "5000069258412032",
   "score": "2625294",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "Ancelistas",
   "teamId": "5729392286236672",
   "score": "2624840",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Bella Domanda",
   "teamId": "6020445576888320",
   "score": "2620094",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "UCL WAC-WAC",
   "teamId": "6402035637288960",
   "score": "2620067",
   "hubId": "5944419287040000",
   "countries": [
    "United Kingdom",
    "Romania",
    "Poland"
   ]
  },
  {
   "teamName": "The Bit-les",
   "teamId": "5878530663514112",
   "score": "2618848",
   "hubId": "4747890253627392",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Isteric Salmon",
   "teamId": "5124090734051328",
   "score": "2615393",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "InterPython",
   "teamId": "5723118614085632",
   "score": "2613952",
   "hubId": "0",
   "countries": [
    "Poland",
    "Morocco",
    "Belarus",
    "Netherlands"
   ]
  },
  {
   "teamName": "SickTear",
   "teamId": "5164320283426816",
   "score": "2613263",
   "hubId": "0",
   "countries": [
    "Armenia",
    "Armenia",
    "Armenia",
    "Armenia"
   ]
  },
  {
   "teamName": "Collect monatki",
   "teamId": "4791629059719168",
   "score": "2610393",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "AIM Tech Funny Behavior",
   "teamId": "5191353881329664",
   "score": "2606788",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Warriors of ETH",
   "teamId": "5587382078275584",
   "score": "2605493",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "FaëriX",
   "teamId": "5754980359208960",
   "score": "2602771",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "YMTeam",
   "teamId": "6396436073676800",
   "score": "2599781",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "#Octothorp Code",
   "teamId": "6550243952820224",
   "score": "2594772",
   "hubId": "4735593493823488",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Blue Vision Labs",
   "teamId": "5996322557526016",
   "score": "2590812",
   "hubId": "0",
   "countries": [
    "Czech Republic",
    "Italy",
    "Croatia",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Shadow Team",
   "teamId": "6044948902182912",
   "score": "2588996",
   "hubId": "0",
   "countries": [
    "France"
   ]
  },
  {
   "teamName": "Game of Nolife",
   "teamId": "4791405721419776",
   "score": "2588795",
   "hubId": "0",
   "countries": [
    "Finland",
    "Finland",
    "Finland",
    "Finland"
   ]
  },
  {
   "teamName": "AG Global Opt",
   "teamId": "5190466500820992",
   "score": "2586837",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Depression Cherry",
   "teamId": "5700680429862912",
   "score": "2581722",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "SPbAU Droplets",
   "teamId": "5104251139260416",
   "score": "2579532",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "МЕТАШСА",
   "teamId": "5557533934616576",
   "score": "2578848",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "MIPT The Skblt",
   "teamId": "6542696353103872",
   "score": "2578050",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "KTU #NaN",
   "teamId": "6666496705036288",
   "score": "2575299",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Net",
   "teamId": "6144563890618368",
   "score": "2573611",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Visa required",
   "teamId": "5873527362158592",
   "score": "2572333",
   "hubId": "6478634030202880",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "what",
   "teamId": "5105622374678528",
   "score": "2571530",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "MIPT Amethysts",
   "teamId": "5742701853016064",
   "score": "2567244",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "BigRik",
   "teamId": "6433448289894400",
   "score": "2567079",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "493a32",
   "teamId": "5815493764055040",
   "score": "2566966",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Indigenous",
   "teamId": "6127772514648064",
   "score": "2566363",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Aibohphobia",
   "teamId": "6405667300573184",
   "score": "2565775",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Paris Saclay des liENS",
   "teamId": "6406355837517824",
   "score": "2564997",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Dvorkins",
   "teamId": "5314766008483840",
   "score": "2564208",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "FourtySim",
   "teamId": "5117292069257216",
   "score": "2562761",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "︻芫══----",
   "teamId": "5159962300907520",
   "score": "2562565",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Unagi",
   "teamId": "5215352011096064",
   "score": "2560859",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Cykličtí mamuti",
   "teamId": "6402217099657216",
   "score": "2559230",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "ENS Ulm 1",
   "teamId": "5730569375711232",
   "score": "2558153",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Tamarisk",
   "teamId": "5201564427878400",
   "score": "2555796",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "team BMWs",
   "teamId": "5684157959110656",
   "score": "2555259",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "VOVA",
   "teamId": "6622922852532224",
   "score": "2554470",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Balloons Tower Defenders",
   "teamId": "6650683709194240",
   "score": "2553983",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Тoматный джус",
   "teamId": "5669053565763584",
   "score": "2553560",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Bat.BC",
   "teamId": "5762865315184640",
   "score": "2552840",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Master Exploder",
   "teamId": "5266396623667200",
   "score": "2552775",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Red Alert",
   "teamId": "5775352194400256",
   "score": "2551210",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Constructors",
   "teamId": "4855255309221888",
   "score": "2549095",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "The Hypnotoad",
   "teamId": "5515041205911552",
   "score": "2547523",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Gummy bears",
   "teamId": "4764186634616832",
   "score": "2547237",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "AMPop",
   "teamId": "6163375444721664",
   "score": "2546114",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Vision of Doom",
   "teamId": "5158735014002688",
   "score": "2542475",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "#include<wraio_prama.h>",
   "teamId": "5149475802710016",
   "score": "2542366",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "kodırs",
   "teamId": "6189706748362752",
   "score": "2540938",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "NotEnoughBeerException",
   "teamId": "5780246309634048",
   "score": "2539898",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "ლ( ◕ 益 ◕ ) ლ Gib code ლ( ◕ 益 ◕ ) ლ",
   "teamId": "6448668580249600",
   "score": "2539047",
   "hubId": "5131865698598912",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "keypresser",
   "teamId": "4860365447888896",
   "score": "2535355",
   "hubId": "6711077593153536",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "wewewew",
   "teamId": "4521534672601088",
   "score": "2535163",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "B.Smart",
   "teamId": "4552150810099712",
   "score": "2534443",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "HashCoderZ",
   "teamId": "5641978091929600",
   "score": "2533925",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "NULL\"); DR0P T4BLE teams -- <5cript>$.ajax({data:document.cookie",
   "teamId": "5739309567049728",
   "score": "2533422",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "VirtualCoders",
   "teamId": "5036289791361024",
   "score": "2532589",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Team Floe",
   "teamId": "5563048739733504",
   "score": "2532570",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Matryoshka",
   "teamId": "5705925323128832",
   "score": "2532249",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "One Logic",
   "teamId": "5633056907984896",
   "score": "2531482",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "UWr Smurfs",
   "teamId": "6427848994717696",
   "score": "2531218",
   "hubId": "4594856005468160",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "ENS Ulm ☭",
   "teamId": "5687498571251712",
   "score": "2531059",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "schnitzel",
   "teamId": "5663163823423488",
   "score": "2530886",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "The Shawatinas",
   "teamId": "6659234989080576",
   "score": "2529177",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "TU_Dudes",
   "teamId": "5062752628375552",
   "score": "2526950",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Austria"
   ]
  },
  {
   "teamName": "malum criceta",
   "teamId": "5158043859812352",
   "score": "2523144",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Joga Bonito",
   "teamId": "5123680229130240",
   "score": "2522574",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "ETNA",
   "teamId": "5769928657338368",
   "score": "2522306",
   "hubId": "0",
   "countries": [
    "Italy",
    "Spain",
    "Namibia",
    "Togo"
   ]
  },
  {
   "teamName": "The Mathemagicians",
   "teamId": "4574042862387200",
   "score": "2518636",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Germany"
   ]
  },
  {
   "teamName": "FourSlovaks",
   "teamId": "5060132966760448",
   "score": "2515269",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Slovakia",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Lokomotiv Sanglier",
   "teamId": "6218367333564416",
   "score": "2513752",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Hekate",
   "teamId": "5844886305636352",
   "score": "2513473",
   "hubId": "6711077593153536",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Chrząszczyżewoszyce powiat Łękołody",
   "teamId": "4963736989204480",
   "score": "2511770",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "The Mentalists",
   "teamId": "6650790278070272",
   "score": "2509585",
   "hubId": "5659826029854720",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Cache Flow",
   "teamId": "6000082600067072",
   "score": "2505695",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Vandam Plastic",
   "teamId": "5002882394882048",
   "score": "2501760",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "PomuPomuNo",
   "teamId": "5472096029245440",
   "score": "2501192",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "UCUlele",
   "teamId": "6449185050066944",
   "score": "2499203",
   "hubId": "4735593493823488",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Old boy",
   "teamId": "5050883217817600",
   "score": "2499166",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Alien Contagion",
   "teamId": "6389466683932672",
   "score": "2498169",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Ca$hcode",
   "teamId": "5390062153891840",
   "score": "2497590",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "raclette",
   "teamId": "6198613369683968",
   "score": "2493044",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Standard deviation",
   "teamId": "6452829531144192",
   "score": "2491745",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "ex1t",
   "teamId": "6330962048712704",
   "score": "2491683",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "AO(1)",
   "teamId": "4725235374882816",
   "score": "2490890",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "UW.Belarus",
   "teamId": "6213208742297600",
   "score": "2490442",
   "hubId": "0",
   "countries": [
    "Poland",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Digital Hammer",
   "teamId": "6358956041568256",
   "score": "2488352",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Finifugal fudgel(s) ¯\\_(ツ)_/¯",
   "teamId": "6643551915999232",
   "score": "2484348",
   "hubId": "0",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "IllegalNumbers",
   "teamId": "6475806331109376",
   "score": "2481418",
   "hubId": "0",
   "countries": [
    "Germany",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "<script>window.open('www.bing.com');</script>",
   "teamId": "4853870517813248",
   "score": "2477128",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Time Limit Exceeded",
   "teamId": "5446041683886080",
   "score": "2475391",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Humdrum Lobsters",
   "teamId": "4742786758737920",
   "score": "2471618",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Floating Points",
   "teamId": "5391752223522816",
   "score": "2467396",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Hash TAG",
   "teamId": "6406483679903744",
   "score": "2463928",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Curious Coding",
   "teamId": "5897513076785152",
   "score": "2463855",
   "hubId": "0",
   "countries": [
    "Romania",
    "United Kingdom",
    "Netherlands"
   ]
  },
  {
   "teamName": "Rzarzsquad",
   "teamId": "4767446514794496",
   "score": "2462752",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "FIIT",
   "teamId": "5262081389494272",
   "score": "2462364",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "HashCollision",
   "teamId": "5184403080740864",
   "score": "2459877",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "insomnia",
   "teamId": "5597115279474688",
   "score": "2457890",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "AlleTeam",
   "teamId": "6617808620224512",
   "score": "2457504",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "matroid",
   "teamId": "6394224433954816",
   "score": "2456622",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "iziwin",
   "teamId": "6370930477498368",
   "score": "2455801",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "mubaRock",
   "teamId": "6625401317097472",
   "score": "2455462",
   "hubId": "4842390003122176",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Unsigned Long Long",
   "teamId": "6572377865453568",
   "score": "2454273",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Glorious guys",
   "teamId": "5386199636115456",
   "score": "2451470",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Ne Svarshchiki!",
   "teamId": "6174468808376320",
   "score": "2450983",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Belarus"
   ]
  },
  {
   "teamName": "Last Minute",
   "teamId": "5406299546189824",
   "score": "2449213",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Looptribe",
   "teamId": "6247614450237440",
   "score": "2449142",
   "hubId": "4954063850438656",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "O' abuzurile",
   "teamId": "5272296633663488",
   "score": "2447686",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "ETH Mobile Agents",
   "teamId": "5243452103065600",
   "score": "2447587",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "theDegenerateCase",
   "teamId": "5560832469499904",
   "score": "2447500",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "M$ BOYZ",
   "teamId": "5332046339637248",
   "score": "2445723",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "France",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ENSlip",
   "teamId": "5546983951433728",
   "score": "2444759",
   "hubId": "5199323260256256",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "LameName",
   "teamId": "4598440960983040",
   "score": "2440460",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Slovakia",
    "Romania",
    "United Kingdom"
   ]
  },
  {
   "teamName": "FourTuple",
   "teamId": "6628182576857088",
   "score": "2439106",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "SweetCake",
   "teamId": "6029228986335232",
   "score": "2436017",
   "hubId": "6156894674616320",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "LeftAsAnExercise",
   "teamId": "6664174537015296",
   "score": "2434271",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Aristokratska Metamorfna Mafija",
   "teamId": "5692470599876608",
   "score": "2434241",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "GYM",
   "teamId": "4855184106717184",
   "score": "2433442",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "BlahBlahTeam",
   "teamId": "4875371795185664",
   "score": "2428037",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "exact",
   "teamId": "4536784759291904",
   "score": "2427547",
   "hubId": "5199323260256256",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Paul Nerd0s",
   "teamId": "5094371170975744",
   "score": "2424857",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "102",
   "teamId": "5099131269808128",
   "score": "2424299",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "🍝",
   "teamId": "5380487329611776",
   "score": "2423180",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Beyond Ballmer's Peak",
   "teamId": "5573148623765504",
   "score": "2421914",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "Ravi",
   "teamId": "4708179187335168",
   "score": "2421151",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Lineage",
   "teamId": "5625127660158976",
   "score": "2417823",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "'\"><script>alert()</script>",
   "teamId": "5391416477876224",
   "score": "2416068",
   "hubId": "4552345895567360",
   "countries": [
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Raving Devs",
   "teamId": "6324282099499008",
   "score": "2414601",
   "hubId": "6504443965079552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "from get import rekt",
   "teamId": "4622975357681664",
   "score": "2414469",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "StacksOutForHarambe",
   "teamId": "5429691078934528",
   "score": "2413610",
   "hubId": "5690886025379840",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Das Hash-Gestirn",
   "teamId": "4527266306457600",
   "score": "2412153",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "CPUMons",
   "teamId": "5603644233744384",
   "score": "2411575",
   "hubId": "5547296812957696",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Veni Vidi Vsync",
   "teamId": "4572265819668480",
   "score": "2411558",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "wedontcare",
   "teamId": "6518478508916736",
   "score": "2410614",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "SAT",
   "teamId": "5590331378630656",
   "score": "2410078",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Schale",
   "teamId": "5804605753524224",
   "score": "2409412",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Attack of the Semicolons",
   "teamId": "4615167644008448",
   "score": "2408471",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Minor Thing",
   "teamId": "5505111241523200",
   "score": "2407787",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Platypus",
   "teamId": "6616660857323520",
   "score": "2407406",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "HashAgent",
   "teamId": "5113031730135040",
   "score": "2406321",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Geographix",
   "teamId": "6575363605921792",
   "score": "2405371",
   "hubId": "6508589212499968",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Gentlecat",
   "teamId": "6363078404866048",
   "score": "2404222",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Blatracking",
   "teamId": "5367275741773824",
   "score": "2403311",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Parse Attacks!",
   "teamId": "6564061735026688",
   "score": "2402587",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "bounty",
   "teamId": "6751027567001600",
   "score": "2401654",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "CTU FIT Ducklings",
   "teamId": "4606889966960640",
   "score": "2401179",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Slovakia",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "goggl_pls",
   "teamId": "5427961012420608",
   "score": "2400363",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "UWr Orange",
   "teamId": "5206250102980608",
   "score": "2397939",
   "hubId": "4594856005468160",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "ThiYo",
   "teamId": "5167734581100544",
   "score": "2396997",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Black cats",
   "teamId": "4520692590575616",
   "score": "2396296",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "NU #0",
   "teamId": "5339690240573440",
   "score": "2395950",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "Unhandled Exception",
   "teamId": "6574064378314752",
   "score": "2394904",
   "hubId": "4643428797251584",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "colorcode",
   "teamId": "5579632883531776",
   "score": "2394351",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "RЯRA",
   "teamId": "5996672664469504",
   "score": "2393529",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Chronos",
   "teamId": "5982012598910976",
   "score": "2391725",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "rETHink again",
   "teamId": "4821799393034240",
   "score": "2390578",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Our Team",
   "teamId": "4618042654851072",
   "score": "2389278",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Netherlands"
   ]
  },
  {
   "teamName": "DashCode",
   "teamId": "5387873935163392",
   "score": "2383696",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Switzerland",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "GARB",
   "teamId": "6035860952711168",
   "score": "2382946",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Les Coulommiers",
   "teamId": "4642517190443008",
   "score": "2382932",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Jacquies",
   "teamId": "5402342002262016",
   "score": "2382813",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "teamNPcompete",
   "teamId": "4726671504572416",
   "score": "2379780",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Skimbux",
   "teamId": "4968659357270016",
   "score": "2377425",
   "hubId": "6068492302286848",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "PizzaBoy's",
   "teamId": "6351520111001600",
   "score": "2377425",
   "hubId": "6068492302286848",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "KTU United",
   "teamId": "6071480525783040",
   "score": "2376962",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Lithuania",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ajonegro",
   "teamId": "6091010748710912",
   "score": "2376701",
   "hubId": "5381469333618688",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "BingIsBetter",
   "teamId": "6731698939101184",
   "score": "2376683",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "2SZ",
   "teamId": "5627317019738112",
   "score": "2372748",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "RAF",
   "teamId": "5008661877358592",
   "score": "2370620",
   "hubId": "0",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "Jagiellonian Ducks Quack",
   "teamId": "5979603659128832",
   "score": "2370179",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "侘寂",
   "teamId": "5847742056235008",
   "score": "2369652",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Victorious Secret",
   "teamId": "5449809980817408",
   "score": "2369562",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Lithuania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "SVL",
   "teamId": "5897335640948736",
   "score": "2368352",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "PITOT",
   "teamId": "4958820392501248",
   "score": "2368197",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "elseta",
   "teamId": "6379726570520576",
   "score": "2367902",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Germany",
    "United Kingdom"
   ]
  },
  {
   "teamName": "akatsuki",
   "teamId": "5673371215855616",
   "score": "2366842",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Brute Force",
   "teamId": "6197422053130240",
   "score": "2366756",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Solyanka",
   "teamId": "5952859971518464",
   "score": "2365572",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Nugget",
   "teamId": "4796217158533120",
   "score": "2365293",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "pony7",
   "teamId": "6330138488733696",
   "score": "2365264",
   "hubId": "5842748150120448",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "#nachvorn",
   "teamId": "5561818567147520",
   "score": "2365087",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "AtAvratKod",
   "teamId": "6520062479433728",
   "score": "2364038",
   "hubId": "4842390003122176",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "ACtiO(n)",
   "teamId": "5636806749978624",
   "score": "2363021",
   "hubId": "6125008703193088",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "TreeSum",
   "teamId": "5629366725771264",
   "score": "2361620",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "general Idea",
   "teamId": "4740287557533696",
   "score": "2361497",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Kyiv Algo Club",
   "teamId": "6579169215381504",
   "score": "2361401",
   "hubId": "6640431018278912",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Marc",
   "teamId": "5316248644616192",
   "score": "2360463",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "Boun0",
   "teamId": "6366444585484288",
   "score": "2359399",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Suicide squad",
   "teamId": "5445872099786752",
   "score": "2358988",
   "hubId": "4954063850438656",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Balooli",
   "teamId": "5132676038131712",
   "score": "2356944",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "A2Team",
   "teamId": "4869813302198272",
   "score": "2356217",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Vermon Lardero",
   "teamId": "6073673844785152",
   "score": "2355908",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TW#1",
   "teamId": "4992664936120320",
   "score": "2355819",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "GDG Beograd",
   "teamId": "5187081999482880",
   "score": "2355742",
   "hubId": "6409247491358720",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "SF[Ξ]IR-Lille",
   "teamId": "5987065023954944",
   "score": "2354119",
   "hubId": "6689384787083264",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Axxes' Dropouts",
   "teamId": "6061358562934784",
   "score": "2354009",
   "hubId": "5117366962749440",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "DCBrn",
   "teamId": "5960047062417408",
   "score": "2353634",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Frankly Incredible",
   "teamId": "4530949308022784",
   "score": "2353303",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "AuTUMatic",
   "teamId": "6226003986743296",
   "score": "2349040",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "GetInTheVan",
   "teamId": "5210838000467968",
   "score": "2348530",
   "hubId": "5803282098290688",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "NSU NET",
   "teamId": "6577700605001728",
   "score": "2348333",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Pitoni++",
   "teamId": "5361094008766464",
   "score": "2347685",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "long long int int",
   "teamId": "5093366148628480",
   "score": "2346406",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rösti 🥔",
   "teamId": "6036455335919616",
   "score": "2345041",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Flaming Lamborghini",
   "teamId": "5316065034764288",
   "score": "2343677",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "imagouille",
   "teamId": "6477149313695744",
   "score": "2342946",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "EPFLers",
   "teamId": "5756836925931520",
   "score": "2341739",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "HUE",
   "teamId": "5920360692187136",
   "score": "2339134",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "4FriendsAtAFooBar",
   "teamId": "5639834634813440",
   "score": "2338482",
   "hubId": "5745582165458944",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "WasIstDasFür1Team",
   "teamId": "5650483536461824",
   "score": "2335858",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Theta(1)",
   "teamId": "5780212151222272",
   "score": "2333284",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "BroDoYouEvenPraise",
   "teamId": "5808643291217920",
   "score": "2331446",
   "hubId": "0",
   "countries": [
    "Germany",
    "France"
   ]
  },
  {
   "teamName": "P is for Proxy",
   "teamId": "4742417861312512",
   "score": "2327918",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "huge jazz lovers",
   "teamId": "4649585632870400",
   "score": "2325844",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Red Geckos",
   "teamId": "5660329950314496",
   "score": "2325294",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Ready For Mom's Spaghetti",
   "teamId": "5062250922508288",
   "score": "2324653",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Germany",
    "Ukraine"
   ]
  },
  {
   "teamName": "BounLabs",
   "teamId": "5430613960032256",
   "score": "2322658",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "jkl;",
   "teamId": "6452181393735680",
   "score": "2317970",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Gausspunkterna",
   "teamId": "4530081724628992",
   "score": "2317423",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "assist-msm",
   "teamId": "4662002651758592",
   "score": "2317181",
   "hubId": "5613648487645184",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "unibg-seclab",
   "teamId": "4687423824986112",
   "score": "2316290",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Chaotic United",
   "teamId": "6216021207678976",
   "score": "2314411",
   "hubId": "5766567912538112",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Ze Daw",
   "teamId": "5076920181981184",
   "score": "2313173",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Post Quantum Rocket",
   "teamId": "6632142536704000",
   "score": "2310129",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "France",
    "Switzerland"
   ]
  },
  {
   "teamName": "TrePe Team",
   "teamId": "6265505337835520",
   "score": "2309666",
   "hubId": "0",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "Pozdro Dariusz",
   "teamId": "6117808928718848",
   "score": "2307461",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Kassos",
   "teamId": "5055642310017024",
   "score": "2307371",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Mr.Robot",
   "teamId": "4699505836425216",
   "score": "2306427",
   "hubId": "5419392015794176",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "MyNotary",
   "teamId": "4603558750060544",
   "score": "2305472",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Chocolateam",
   "teamId": "5255028449214464",
   "score": "2303656",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "404 - Team not found",
   "teamId": "4720780352946176",
   "score": "2303062",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "ZGlja2J1dHQK",
   "teamId": "5729137540988928",
   "score": "2301675",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Hash Bros Melee",
   "teamId": "4998665072541696",
   "score": "2297673",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Pizza",
   "teamId": "5680797616963584",
   "score": "2296546",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "OverGow",
   "teamId": "5962809263259648",
   "score": "2295638",
   "hubId": "4715704574017536",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Part Time Humans",
   "teamId": "5710311357153280",
   "score": "2294735",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Stekkerdozen",
   "teamId": "5717676957630464",
   "score": "2294606",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Lamp life is ending",
   "teamId": "5613183624544256",
   "score": "2293820",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Bikeshedding",
   "teamId": "5975732618526720",
   "score": "2291126",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "MOBster",
   "teamId": "5843533726482432",
   "score": "2287394",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "the R-Team",
   "teamId": "6728124318351360",
   "score": "2285484",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "‎We are trying to have a longer team name than other teams here,",
   "teamId": "6624671239766016",
   "score": "2284875",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "0xdeffbeef",
   "teamId": "6349967278997504",
   "score": "2282791",
   "hubId": "5112178910691328",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Les Orades",
   "teamId": "5779230482759680",
   "score": "2281479",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Dadanko",
   "teamId": "5583342997078016",
   "score": "2278395",
   "hubId": "0",
   "countries": [
    "Slovakia",
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "SloveniaTeam",
   "teamId": "6309872148676608",
   "score": "2277992",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Wankers",
   "teamId": "6701807241789440",
   "score": "2276533",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "No frontiers",
   "teamId": "5384022356131840",
   "score": "2276157",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Otakay",
   "teamId": "5126509069074432",
   "score": "2274779",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "New Folder",
   "teamId": "4794524404547584",
   "score": "2273913",
   "hubId": "4735593493823488",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "MontyPython",
   "teamId": "5802679997562880",
   "score": "2272886",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "(｡◕ ∀ ◕｡)",
   "teamId": "6587379917783040",
   "score": "2271999",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "Oppa",
   "teamId": "4864667730051072",
   "score": "2267009",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Panic! in the Kernel",
   "teamId": "5075934486986752",
   "score": "2266323",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "MAL",
   "teamId": "5795348689715200",
   "score": "2265367",
   "hubId": "5112178910691328",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "exit(0)",
   "teamId": "6300431810560000",
   "score": "2263712",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "team42",
   "teamId": "5268985952075776",
   "score": "2263496",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Tiltayen",
   "teamId": "4519080635662336",
   "score": "2261976",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "LNE",
   "teamId": "5688554126573568",
   "score": "2261070",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Stack Explosion",
   "teamId": "6009889084145664",
   "score": "2259808",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Omikron Berlin",
   "teamId": "6460344113299456",
   "score": "2258975",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Unable to create team as the name is already in use.",
   "teamId": "5539409977933824",
   "score": "2258809",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Criteo SORT",
   "teamId": "4735337406398464",
   "score": "2257078",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rabid Rabbits",
   "teamId": "4642740260306944",
   "score": "2255386",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "BsMind",
   "teamId": "5693310467309568",
   "score": "2249507",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Germany",
    "Italy"
   ]
  },
  {
   "teamName": "Winnie",
   "teamId": "5033811393904640",
   "score": "2249286",
   "hubId": "4747890253627392",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": ":)",
   "teamId": "4778942263197696",
   "score": "2248661",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "0xFF",
   "teamId": "4854533150736384",
   "score": "2246758",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Busy Beaver",
   "teamId": "4678123341742080",
   "score": "2245682",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Asfinges de corral",
   "teamId": "6355188549943296",
   "score": "2244578",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "The Blind Robin-Euler Correlations",
   "teamId": "5129600371785728",
   "score": "2244353",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "MyrStacken",
   "teamId": "6489665116831744",
   "score": "2244286",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "MMD",
   "teamId": "6546518404235264",
   "score": "2244198",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "#todo:",
   "teamId": "4706220682248192",
   "score": "2241232",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Podorozhnik",
   "teamId": "4853386931339264",
   "score": "2240607",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Grhugada",
   "teamId": "6602825693921280",
   "score": "2238839",
   "hubId": "5983641666584576",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "bored again",
   "teamId": "6612902425395200",
   "score": "2238519",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "IhateUML",
   "teamId": "5096365042434048",
   "score": "2238430",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "YouPiEf",
   "teamId": "6481913975930880",
   "score": "2237305",
   "hubId": "4610782683725824",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "(っ◔◡◔)っ ♥ surykatki ♥",
   "teamId": "5682527415042048",
   "score": "2236630",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "SegfaultTamers",
   "teamId": "5289843722551296",
   "score": "2233155",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "The vEBs",
   "teamId": "6322280309194752",
   "score": "2231963",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "KnowYourArchitecture",
   "teamId": "4867184245342208",
   "score": "2230781",
   "hubId": "5292985222692864",
   "countries": [
    "Finland",
    "Finland",
    "Finland"
   ]
  },
  {
   "teamName": "Dark Cobra",
   "teamId": "4655597312016384",
   "score": "2228297",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Ledas",
   "teamId": "6401379648143360",
   "score": "2226069",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "UPB_TeamName",
   "teamId": "5142855379058688",
   "score": "2225708",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Cyber Defence",
   "teamId": "5572183799627776",
   "score": "2224029",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Hash Code",
   "teamId": "5755444953874432",
   "score": "2220618",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "DeadCodePool",
   "teamId": "4850314150674432",
   "score": "2218582",
   "hubId": "5440298305978368",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "wildCats",
   "teamId": "6386333303963648",
   "score": "2217847",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "2.5p team",
   "teamId": "6283579969503232",
   "score": "2217459",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "The Pick-code Artists",
   "teamId": "5031210656989184",
   "score": "2213051",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team Fisher Price",
   "teamId": "6650544860954624",
   "score": "2212571",
   "hubId": "6029454941880320",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "PogChamp coding",
   "teamId": "4996378203783168",
   "score": "2212296",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Odlikaši",
   "teamId": "6241230182678528",
   "score": "2210960",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Meme",
   "teamId": "4858056634531840",
   "score": "2210581",
   "hubId": "4815401099722752",
   "countries": [
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "John Cena",
   "teamId": "5112473317277696",
   "score": "2209929",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "RollingRelease",
   "teamId": "6218430415896576",
   "score": "2207983",
   "hubId": "6125008703193088",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "Hash mouth - All Star",
   "teamId": "6728117406138368",
   "score": "2207368",
   "hubId": "5661462143959040",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Impect",
   "teamId": "6274354849513472",
   "score": "2206677",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Las Salsitas",
   "teamId": "6269883050360832",
   "score": "2205967",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "The Team",
   "teamId": "5851737382453248",
   "score": "2204925",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "RRHPC",
   "teamId": "4746248502378496",
   "score": "2204327",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "LNU VVT",
   "teamId": "5496670557044736",
   "score": "2202072",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "UpPeRcAmElCaSe",
   "teamId": "4933953605599232",
   "score": "2200286",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland",
    "Switzerland"
   ]
  },
  {
   "teamName": "X++",
   "teamId": "4826174890967040",
   "score": "2197907",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "France",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Three Eyed Games",
   "teamId": "6234252739870720",
   "score": "2194811",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Dogs",
   "teamId": "5654314982834176",
   "score": "2193622",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "lambda",
   "teamId": "5700812231671808",
   "score": "2192547",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Designated Drinkers 2.0",
   "teamId": "5363841579876352",
   "score": "2191660",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "sudo make sandwich",
   "teamId": "4784422171705344",
   "score": "2191455",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Smiley Pharos",
   "teamId": "4951700209139712",
   "score": "2190858",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Germany",
    "Egypt"
   ]
  },
  {
   "teamName": "meduza",
   "teamId": "4541471776571392",
   "score": "2189316",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "JBG",
   "teamId": "6531110410387456",
   "score": "2187520",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "apt-get moo",
   "teamId": "6659696161193984",
   "score": "2184583",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Qui(d) VR?",
   "teamId": "4805058952691712",
   "score": "2183958",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Ocamper",
   "teamId": "5014769857724416",
   "score": "2179425",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Matthieu suce des pneus",
   "teamId": "4585673633824768",
   "score": "2178970",
   "hubId": "5199323260256256",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Codee Latte",
   "teamId": "6205502497226752",
   "score": "2178739",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "JEIAG",
   "teamId": "6592099818405888",
   "score": "2177653",
   "hubId": "6358233077776384",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Yoshi",
   "teamId": "4625803123884032",
   "score": "2175853",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "λambda",
   "teamId": "5695700750827520",
   "score": "2175477",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "TheCodingDogs",
   "teamId": "5276840172191744",
   "score": "2175068",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Nexedi",
   "teamId": "5629572884201472",
   "score": "2174151",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Fatture in Cloud",
   "teamId": "5213010717048832",
   "score": "2171258",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "NavySol",
   "teamId": "6633995278221312",
   "score": "2170850",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "The Deditors",
   "teamId": "6290093018972160",
   "score": "2169107",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Macedonia's Elite",
   "teamId": "5479857169367040",
   "score": "2167733",
   "hubId": "4815401099722752",
   "countries": [
    "Netherlands",
    "Macedonia",
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "Inversion of control",
   "teamId": "4550810780303360",
   "score": "2167391",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Mosasaurus",
   "teamId": "5288185328304128",
   "score": "2167276",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Humble Bumbles",
   "teamId": "5162772954349568",
   "score": "2167153",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "#code.ml",
   "teamId": "6470127511928832",
   "score": "2166615",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Gauss",
   "teamId": "6094803741704192",
   "score": "2166347",
   "hubId": "0",
   "countries": [
    "Italy",
    "Germany"
   ]
  },
  {
   "teamName": "if((Pizzas||cofe)==0) Team = leave;",
   "teamId": "4810992450011136",
   "score": "2166045",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Tiuj Sen Kreivo",
   "teamId": "5361587124699136",
   "score": "2163153",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "L'Ciborg",
   "teamId": "4900901953208320",
   "score": "2161264",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Sword of Zeus",
   "teamId": "5824572519612416",
   "score": "2161189",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Pizza Party",
   "teamId": "5717711787130880",
   "score": "2159948",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "mind-PATT-ern",
   "teamId": "5304849801412608",
   "score": "2158816",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Muffins",
   "teamId": "4704448202932224",
   "score": "2158621",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "TheBookOfMozilla",
   "teamId": "5400492750405632",
   "score": "2158025",
   "hubId": "5807719806140416",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Super Jarvis",
   "teamId": "6176335441428480",
   "score": "2157885",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Malbolge",
   "teamId": "4600554017783808",
   "score": "2155858",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "verywow",
   "teamId": "4631635890798592",
   "score": "2155519",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "yaks perdus",
   "teamId": "6235167635013632",
   "score": "2155485",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "Germany"
   ]
  },
  {
   "teamName": "Fibonacci's soup",
   "teamId": "4655393770831872",
   "score": "2155438",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Uvivu",
   "teamId": "6711882631086080",
   "score": "2155037",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Germany",
    "Germany",
    "Ukraine"
   ]
  },
  {
   "teamName": "LGBS",
   "teamId": "6538934028861440",
   "score": "2152050",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Les artistes",
   "teamId": "5609768051802112",
   "score": "2151473",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "VJ",
   "teamId": "6544664253431808",
   "score": "2150859",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "JayZ Crew",
   "teamId": "5985530713997312",
   "score": "2150535",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "The Komodo Dragons",
   "teamId": "5857889587560448",
   "score": "2149595",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Problem = No Problem",
   "teamId": "4775099139883008",
   "score": "2149158",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "WillCodeForPizza",
   "teamId": "6099260374253568",
   "score": "2148645",
   "hubId": "5659826029854720",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Shawarma Djej Toum Zyede",
   "teamId": "5841417918218240",
   "score": "2147743",
   "hubId": "4917250343567360",
   "countries": [
    "Lebanon",
    "Lebanon",
    "Lebanon"
   ]
  },
  {
   "teamName": "UP!",
   "teamId": "4787935119409152",
   "score": "2147330",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Atomia",
   "teamId": "6360966623133696",
   "score": "2147266",
   "hubId": "5452279385686016",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "'; DROP TABLE",
   "teamId": "6147582178885632",
   "score": "2147061",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "BLZD",
   "teamId": "6718215090601984",
   "score": "2146838",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Blub",
   "teamId": "4709501231955968",
   "score": "2146678",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Catalysts",
   "teamId": "6435943800111104",
   "score": "2146615",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Stamina",
   "teamId": "5820085889400832",
   "score": "2145241",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "International Crew",
   "teamId": "5788514926985216",
   "score": "2145034",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Slovakia",
    "Switzerland"
   ]
  },
  {
   "teamName": "Spring",
   "teamId": "5391200320225280",
   "score": "2144825",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Code wars: the OS awakens",
   "teamId": "6617033647063040",
   "score": "2144755",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "blotter",
   "teamId": "5561958287802368",
   "score": "2143035",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "suboptimal",
   "teamId": "4720621774700544",
   "score": "2142499",
   "hubId": "5131865698598912",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "C2D Elite",
   "teamId": "6027356716138496",
   "score": "2141751",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "BiauBiau Boys",
   "teamId": "4934515105464320",
   "score": "2141643",
   "hubId": "4762512469786624",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "WindowsSucks",
   "teamId": "6311563292049408",
   "score": "2141243",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "RAZ to vyhra[me]",
   "teamId": "6234335417991168",
   "score": "2141117",
   "hubId": "5173732637147136",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "MnB",
   "teamId": "4784942936489984",
   "score": "2141074",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "United Kingdom",
    "France"
   ]
  },
  {
   "teamName": "Mendo",
   "teamId": "4592411028226048",
   "score": "2140632",
   "hubId": "4815401099722752",
   "countries": [
    "Macedonia",
    "Macedonia",
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "CardanOS",
   "teamId": "6432363542216704",
   "score": "2140485",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "DistributedSleepyAlgorithms",
   "teamId": "4914887373357056",
   "score": "2140262",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Kekathoners",
   "teamId": "4522766657126400",
   "score": "2140082",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "AltaBots",
   "teamId": "6320203692507136",
   "score": "2140038",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Expat Experts",
   "teamId": "5900899926933504",
   "score": "2138449",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "ProgCats",
   "teamId": "5757713300586496",
   "score": "2138121",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Les Tres",
   "teamId": "4629229165608960",
   "score": "2136824",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Algae",
   "teamId": "5739895830085632",
   "score": "2136806",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "1KB RAM",
   "teamId": "5176510205919232",
   "score": "2136665",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Dreikäsehoch",
   "teamId": "6642709229993984",
   "score": "2136657",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Blue Moon",
   "teamId": "5179845315133440",
   "score": "2136289",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "4S",
   "teamId": "6245150481186816",
   "score": "2136146",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Aless klarer",
   "teamId": "5088093203857408",
   "score": "2135426",
   "hubId": "5173732637147136",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "RudeMonkeys",
   "teamId": "5880681099952128",
   "score": "2134532",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "JA",
   "teamId": "5783834016612352",
   "score": "2134305",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "BoomTown",
   "teamId": "5383645070098432",
   "score": "2133910",
   "hubId": "4852035560144896",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Tianshi",
   "teamId": "5660689184063488",
   "score": "2133202",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "pranKIT",
   "teamId": "5759868099100672",
   "score": "2132317",
   "hubId": "6478634030202880",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "gassa & naagi",
   "teamId": "6454934132228096",
   "score": "2131750",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Blue Cord",
   "teamId": "6550383874801664",
   "score": "2128416",
   "hubId": "5547296812957696",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "People's Front of Judea",
   "teamId": "5254770684067840",
   "score": "2124924",
   "hubId": "4669383217512448",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "MMV",
   "teamId": "4791165270360064",
   "score": "2124115",
   "hubId": "4916204116377600",
   "countries": [
    "United Kingdom",
    "Croatia",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "MDSS",
   "teamId": "6656547413295104",
   "score": "2122653",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Les lézards du code",
   "teamId": "5902642073042944",
   "score": "2122532",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Deadly Ferrets",
   "teamId": "5145179224801280",
   "score": "2122099",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Fluffy Unicorns",
   "teamId": "6392496850468864",
   "score": "2121290",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Sudo Bashers",
   "teamId": "5254084361715712",
   "score": "2120919",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "stronglyeventualconsistency",
   "teamId": "5106398958452736",
   "score": "2120332",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Peaky Blinders",
   "teamId": "4719821031735296",
   "score": "2120301",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "MIRCH",
   "teamId": "5413034122018816",
   "score": "2120123",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "SWERC FOREVER",
   "teamId": "5137261184155648",
   "score": "2119794",
   "hubId": "4805185117356032",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "VIV",
   "teamId": "6102349261045760",
   "score": "2119557",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "ntua67p",
   "teamId": "6582432920764416",
   "score": "2118817",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "👉🏿👉🏽👉🏼 Unicode 👈🏼👈🏽👈🏿",
   "teamId": "5992786792808448",
   "score": "2118600",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Belgium",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "TJJJ",
   "teamId": "6254335537184768",
   "score": "2117831",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "DeltaPi²",
   "teamId": "5630742793027584",
   "score": "2117573",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "SCalaCS",
   "teamId": "6703321419087872",
   "score": "2116487",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Swaziland"
   ]
  },
  {
   "teamName": "Error31: Treiber konnte nicht geladen werden",
   "teamId": "5507336772780032",
   "score": "2116487",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Dead Stormtroopers",
   "teamId": "4810843669659648",
   "score": "2116487",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "OptimizeThis!",
   "teamId": "6719695445032960",
   "score": "2116286",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Futurama",
   "teamId": "4818183299006464",
   "score": "2116043",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "7ebra",
   "teamId": "5251615493718016",
   "score": "2113819",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Unicorn Ranch",
   "teamId": "6445963354832896",
   "score": "2111362",
   "hubId": "6249764886675456",
   "countries": [
    "Malta",
    "Malta",
    "Malta",
    "Malta"
   ]
  },
  {
   "teamName": "Marmots",
   "teamId": "6626303058903040",
   "score": "2111006",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy",
    "Poland",
    "Italy"
   ]
  },
  {
   "teamName": "Fallitur visus",
   "teamId": "5185469507698688",
   "score": "2110742",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Monty",
   "teamId": "4574965206614016",
   "score": "2110599",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "LuccaNantes",
   "teamId": "6261782742040576",
   "score": "2109779",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Pytong",
   "teamId": "5118510497792000",
   "score": "2106535",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "del /S C:\\",
   "teamId": "6437831773782016",
   "score": "2106342",
   "hubId": "6711077593153536",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Tigers",
   "teamId": "6013850855931904",
   "score": "2105735",
   "hubId": "5659826029854720",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Core",
   "teamId": "5727708323512320",
   "score": "2104812",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hipopotomonstrosesquipedaliofobicos",
   "teamId": "5851060857995264",
   "score": "2103659",
   "hubId": "4610782683725824",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "O(42)",
   "teamId": "6450037869510656",
   "score": "2101567",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "no",
   "teamId": "5476354489319424",
   "score": "2101475",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "ForTheGlory",
   "teamId": "5079028138508288",
   "score": "2101060",
   "hubId": "6126305246445568",
   "countries": [
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "KfcLovers",
   "teamId": "6364339850182656",
   "score": "2099939",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "DeepThreat",
   "teamId": "5100031401000960",
   "score": "2099812",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Bratishki",
   "teamId": "6219763936133120",
   "score": "2099412",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Lev Balkanski",
   "teamId": "4779963458781184",
   "score": "2098723",
   "hubId": "0",
   "countries": [
    "France",
    "Austria"
   ]
  },
  {
   "teamName": "Swanky Tiger",
   "teamId": "4555603762479104",
   "score": "2097484",
   "hubId": "4766541551763456",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Wizards of C++",
   "teamId": "6708508732948480",
   "score": "2095566",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "getTeamName()",
   "teamId": "4832481513570304",
   "score": "2095083",
   "hubId": "0",
   "countries": [
    "Germany",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "CodeMarines",
   "teamId": "6751991250288640",
   "score": "2094952",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Random Kittens",
   "teamId": "4768462610104320",
   "score": "2094057",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "2KPT",
   "teamId": "6393483015225344",
   "score": "2093608",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "KB",
   "teamId": "6719906703736832",
   "score": "2093203",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Th_",
   "teamId": "5402098531303424",
   "score": "2093145",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "dream team",
   "teamId": "5433500916252672",
   "score": "2091855",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "PandaCode",
   "teamId": "5024546545467392",
   "score": "2091652",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Felsformation",
   "teamId": "6168217617694720",
   "score": "2091451",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "QWERTYtriFISH",
   "teamId": "5101698049638400",
   "score": "2090125",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "Germany",
    "United Kingdom"
   ]
  },
  {
   "teamName": "IFT",
   "teamId": "4795445540814848",
   "score": "2089993",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Janusze Algebry",
   "teamId": "5020474111164416",
   "score": "2089704",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Roboy",
   "teamId": "4777107775291392",
   "score": "2089241",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Thomas",
   "teamId": "6085376288489472",
   "score": "2088913",
   "hubId": "0"
  },
  {
   "teamName": "O(3)",
   "teamId": "5795346810667008",
   "score": "2088874",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Trilobyte",
   "teamId": "4937582248984576",
   "score": "2088596",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "United Kingdom"
   ]
  },
  {
   "teamName": "NU team",
   "teamId": "4695112554643456",
   "score": "2088131",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "figyelő-zokni",
   "teamId": "6368714207264768",
   "score": "2087787",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "++j+++j",
   "teamId": "6304278155100160",
   "score": "2087491",
   "hubId": "6602827975622656",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Astro boys",
   "teamId": "4766702143275008",
   "score": "2087186",
   "hubId": "4852035560144896",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "DASHA",
   "teamId": "5136785516527616",
   "score": "2087177",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Wheel Inventors",
   "teamId": "4859297678753792",
   "score": "2085035",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "SPLit",
   "teamId": "5063808183697408",
   "score": "2084941",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Cimo",
   "teamId": "5149217567801344",
   "score": "2084574",
   "hubId": "0",
   "countries": [
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "beezzz",
   "teamId": "5795795164987392",
   "score": "2084560",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x",
   "teamId": "6040397847461888",
   "score": "2084414",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "France",
    "France"
   ]
  },
  {
   "teamName": "greadyFram",
   "teamId": "5612277118009344",
   "score": "2082864",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Can't hack it",
   "teamId": "5882853816532992",
   "score": "2081901",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ameN meaT",
   "teamId": "6476279247273984",
   "score": "2080453",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "The Musketeers",
   "teamId": "6139265578696704",
   "score": "2080133",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "KappaPride",
   "teamId": "4610711682547712",
   "score": "2079875",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Cheesy binome",
   "teamId": "5912216628887552",
   "score": "2079815",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "MARKJEKAVADIM",
   "teamId": "6202820424368128",
   "score": "2079655",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Eurecom-JVN",
   "teamId": "6710345569665024",
   "score": "2077736",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Slotije",
   "teamId": "4948996996988928",
   "score": "2076701",
   "hubId": "5766567912538112",
   "countries": [
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Inbarogre",
   "teamId": "6263630383284224",
   "score": "2075738",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Yenoty",
   "teamId": "5689998779088896",
   "score": "2074016",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "C'est phashorcier",
   "teamId": "5860790837968896",
   "score": "2073968",
   "hubId": "5199323260256256",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "De Hel van Schel",
   "teamId": "4977588325842944",
   "score": "2073613",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "cautious-chainsaw",
   "teamId": "6241291654397952",
   "score": "2073460",
   "hubId": "0",
   "countries": [
    "Albania",
    "Czech Republic"
   ]
  },
  {
   "teamName": "ROMB",
   "teamId": "5445740499304448",
   "score": "2073348",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "KrimTim2",
   "teamId": "4800748617465856",
   "score": "2072985",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "ubb_bence_arnold",
   "teamId": "4910907683504128",
   "score": "2072422",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Technodrones Remastered",
   "teamId": "6689891660333056",
   "score": "2072117",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "meowsome team",
   "teamId": "5660794410762240",
   "score": "2070729",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "BigBugTheory",
   "teamId": "4859796968701952",
   "score": "2070353",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Kota Gdziuka nocne gonitwy myśli",
   "teamId": "5870067497566208",
   "score": "2070253",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "The Fine Saucisson Team",
   "teamId": "5674406168756224",
   "score": "2068741",
   "hubId": "6308495074787328",
   "countries": [
    "France",
    "Denmark",
    "Denmark",
    "France"
   ]
  },
  {
   "teamName": "#Menschᴵᵀ",
   "teamId": "5693263491104768",
   "score": "2068681",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "YATN",
   "teamId": "6000894885756928",
   "score": "2067838",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "cockroach",
   "teamId": "5544640711229440",
   "score": "2067454",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Evercompliant1",
   "teamId": "6729970080546816",
   "score": "2067283",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "CULLUK",
   "teamId": "4581876882735104",
   "score": "2067277",
   "hubId": "0",
   "countries": [
    "Turkey",
    "France"
   ]
  },
  {
   "teamName": "Seixurra",
   "teamId": "6100720864460800",
   "score": "2066329",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Lambda",
   "teamId": "6307760098508800",
   "score": "2065720",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Only Fools and Pythons",
   "teamId": "5561696361906176",
   "score": "2065681",
   "hubId": "0",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Salade Tomate Oignon",
   "teamId": "6483571028000768",
   "score": "2065381",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Fluidité",
   "teamId": "6698268926935040",
   "score": "2065100",
   "hubId": "6448591136620544",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "kod to tamo peva",
   "teamId": "6057769044017152",
   "score": "2065075",
   "hubId": "0",
   "countries": [
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "Ja chce po polsku",
   "teamId": "5141807407038464",
   "score": "2064610",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Happy Idle Midnight Pirates",
   "teamId": "5544619773263872",
   "score": "2064421",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "StackOverFlower",
   "teamId": "4751923227918336",
   "score": "2064018",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "In honor of Karim Varkinosyan",
   "teamId": "6489340578365440",
   "score": "2064017",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Belarus"
   ]
  },
  {
   "teamName": "ngiNEUs",
   "teamId": "5990672326721536",
   "score": "2063511",
   "hubId": "5099990598811648",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Turkey"
   ]
  },
  {
   "teamName": "Smiling Alpacas",
   "teamId": "5821311028822016",
   "score": "2063415",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Hawaii mit Ei",
   "teamId": "5303508899201024",
   "score": "2063259",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Reem and the Three Bears",
   "teamId": "5743229530013696",
   "score": "2063136",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Sinapsis",
   "teamId": "6205818177323008",
   "score": "2062189",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Peace my pants",
   "teamId": "6491702474833920",
   "score": "2062055",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Ragnarok",
   "teamId": "4901925497602048",
   "score": "2062009",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "andola",
   "teamId": "5880841892790272",
   "score": "2061843",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Team Se\\/eN",
   "teamId": "4733167038627840",
   "score": "2060946",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "We byte",
   "teamId": "6308927725633536",
   "score": "2060946",
   "hubId": "6113594290733056",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "MAlchoholics",
   "teamId": "5740551081033728",
   "score": "2060946",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Bulgaria"
   ]
  },
  {
   "teamName": "Grapefruit",
   "teamId": "6271361525743616",
   "score": "2060946",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "The Pin Pals",
   "teamId": "4707169870020608",
   "score": "2060946",
   "hubId": "4560691285458944",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "treefiddy",
   "teamId": "5508838467829760",
   "score": "2060847",
   "hubId": "5841827282288640",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Dying Philosophers",
   "teamId": "5636053989851136",
   "score": "2060653",
   "hubId": "6128413739843584",
   "countries": [
    "Romania",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Gigsterous",
   "teamId": "4581032049246208",
   "score": "2059572",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Czech Republic"
   ]
  },
  {
   "teamName": "Section Antarctica",
   "teamId": "4711879100334080",
   "score": "2058913",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "3psa si Mardel",
   "teamId": "4812854251225088",
   "score": "2058813",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Aldebaran",
   "teamId": "5367616990347264",
   "score": "2058597",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "pythoneers",
   "teamId": "5380427736940544",
   "score": "2058589",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "cotuwpisac",
   "teamId": "4725658362052608",
   "score": "2058404",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "The Faggianos",
   "teamId": "5752207420948480",
   "score": "2057892",
   "hubId": "5165170082971648",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Shpetz",
   "teamId": "5585333378875392",
   "score": "2057815",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Capgenious",
   "teamId": "4558768348069888",
   "score": "2057670",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Det kommutativa laget",
   "teamId": "6435699926499328",
   "score": "2056891",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Lepsza niż żadna :)",
   "teamId": "5644791832379392",
   "score": "2055931",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "CJ Fans",
   "teamId": "6016312677498880",
   "score": "2055389",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "NASAFRVR",
   "teamId": "5836380391342080",
   "score": "2055326",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Die Milden Kerle",
   "teamId": "5876488675000320",
   "score": "2055068",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "dankmemes4u.biz",
   "teamId": "5285916713156608",
   "score": "2055052",
   "hubId": "6407743179063296",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Hacking Hares",
   "teamId": "5466056231485440",
   "score": "2053680",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Galal3laEsm5alto",
   "teamId": "6372039585693696",
   "score": "2052795",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "WixTigers",
   "teamId": "5140752791240704",
   "score": "2052789",
   "hubId": "0",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Kreygasm",
   "teamId": "4960086267002880",
   "score": "2052265",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "SaKaDoSh",
   "teamId": "6191469564002304",
   "score": "2052261",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "STC",
   "teamId": "5837559628300288",
   "score": "2051932",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "std::pizza",
   "teamId": "5646536662843392",
   "score": "2050440",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Macedonian Phalanx",
   "teamId": "6183246043807744",
   "score": "2050249",
   "hubId": "4815401099722752",
   "countries": [
    "Macedonia",
    "Macedonia",
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "kitcat",
   "teamId": "5271612324577280",
   "score": "2049727",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Mighty ETs of RWTH",
   "teamId": "4508606149951488",
   "score": "2049455",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Jap!",
   "teamId": "6031656716599296",
   "score": "2048546",
   "hubId": "6295925584560128",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "AICE AICE Baby",
   "teamId": "4724352423559168",
   "score": "2048016",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Pseudoprimi",
   "teamId": "5546607068053504",
   "score": "2047637",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Rostad kod",
   "teamId": "4890701070336000",
   "score": "2045488",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "gob-lätt",
   "teamId": "6270355765198848",
   "score": "2044039",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "🍺 Hit me baby one more time 🍺",
   "teamId": "6156876622331904",
   "score": "2043003",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Coding Slavs in Tracksuits",
   "teamId": "4613846136258560",
   "score": "2042932",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ClassB",
   "teamId": "5159354831470592",
   "score": "2042110",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Spanish Inquisition",
   "teamId": "6545537876623360",
   "score": "2041763",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Romania",
    "United Kingdom",
    "Serbia"
   ]
  },
  {
   "teamName": "Les inGEOnieurs",
   "teamId": "6398142517870592",
   "score": "2040526",
   "hubId": "5720755912310784",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Google",
   "teamId": "6109179601223680",
   "score": "2040377",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Two Beer Consumers",
   "teamId": "5022014058266624",
   "score": "2039838",
   "hubId": "5931430634848256",
   "countries": [
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "štiriglav",
   "teamId": "4571724452462592",
   "score": "2039263",
   "hubId": "0",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Streamline",
   "teamId": "5036658554568704",
   "score": "2038126",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Too Simplex",
   "teamId": "5301165256343552",
   "score": "2037756",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Hash Club",
   "teamId": "6074802615877632",
   "score": "2037439",
   "hubId": "5690886025379840",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "14",
   "teamId": "6214354491932672",
   "score": "2036908",
   "hubId": "5165170082971648",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "NOStress",
   "teamId": "5659195005206528",
   "score": "2036907",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Steel Raven",
   "teamId": "5372301658816512",
   "score": "2036436",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "XoXot",
   "teamId": "6608105282469888",
   "score": "2036264",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NetceteraOne",
   "teamId": "6086116096606208",
   "score": "2035851",
   "hubId": "4815401099722752",
   "countries": [
    "Macedonia",
    "Macedonia",
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "Blank",
   "teamId": "4734223869018112",
   "score": "2035654",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Apptozee",
   "teamId": "6427609281855488",
   "score": "2034283",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Romania"
   ]
  },
  {
   "teamName": "Anziani",
   "teamId": "6413926656901120",
   "score": "2034200",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Uni Freiburg",
   "teamId": "4691820730646528",
   "score": "2033900",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "HaiAfaraLaZapada",
   "teamId": "6314669023166464",
   "score": "2033388",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "AKO",
   "teamId": "4633625333071872",
   "score": "2032900",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "SPark",
   "teamId": "4726224291102720",
   "score": "2032179",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "MDP",
   "teamId": "6695485788127232",
   "score": "2030763",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Cebula",
   "teamId": "6012413652500480",
   "score": "2030379",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Above",
   "teamId": "5741328201678848",
   "score": "2030038",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "GICI",
   "teamId": "6475111821475840",
   "score": "2029813",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "SharkByte",
   "teamId": "5634023812497408",
   "score": "2025668",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Lalala",
   "teamId": "6267853074333696",
   "score": "2025419",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "Monaco"
   ]
  },
  {
   "teamName": "We just lost the game",
   "teamId": "4805466907475968",
   "score": "2025206",
   "hubId": "4936954646888448",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "TrollPick",
   "teamId": "5226123923292160",
   "score": "2023440",
   "hubId": "0",
   "countries": [
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Artistanbul",
   "teamId": "6164541125689344",
   "score": "2021961",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "TP*",
   "teamId": "5760443222065152",
   "score": "2020890",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "One Bug Man",
   "teamId": "6248328153006080",
   "score": "2020873",
   "hubId": "5607049471721472",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Rocha Nova",
   "teamId": "6697840503947264",
   "score": "2019897",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Les Crocos",
   "teamId": "6539164010938368",
   "score": "2019831",
   "hubId": "5720755912310784",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team Brute Force 👊🏻",
   "teamId": "5756775588429824",
   "score": "2018737",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "No Logic Programming",
   "teamId": "6479376254238720",
   "score": "2018393",
   "hubId": "6602827975622656",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "pony7 --reload",
   "teamId": "5762702576189440",
   "score": "2018040",
   "hubId": "5842748150120448",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "ibnSinaBros",
   "teamId": "5485713558601728",
   "score": "2017082",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "PontHu",
   "teamId": "6377741020561408",
   "score": "2016373",
   "hubId": "0",
   "countries": [
    "Germany",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "LargestCollectionOfRedBricksInOxford",
   "teamId": "5960824115953664",
   "score": "2016320",
   "hubId": "5107179300323328",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "kekius",
   "teamId": "4519618982969344",
   "score": "2016247",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Spain"
   ]
  },
  {
   "teamName": "MIPT Nonsense",
   "teamId": "5299507868729344",
   "score": "2013631",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Kohnplete-Sham Ansatz",
   "teamId": "5544528840753152",
   "score": "2013274",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Lala",
   "teamId": "6440773826379776",
   "score": "2012858",
   "hubId": "0",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "Kugini",
   "teamId": "6156356797071360",
   "score": "2012659",
   "hubId": "0",
   "countries": [
    "Malta",
    "Malta",
    "Malta"
   ]
  },
  {
   "teamName": "ICDSS Team A",
   "teamId": "4933877034385408",
   "score": "2012593",
   "hubId": "4629206549921792",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "OnePageCRM",
   "teamId": "5535040922451968",
   "score": "2012232",
   "hubId": "5732975631138816",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "zhu zhu zhu pyu pyu pyu",
   "teamId": "6135133753049088",
   "score": "2012110",
   "hubId": "0",
   "countries": [
    "Russia",
    "Sweden",
    "Russia"
   ]
  },
  {
   "teamName": "NDG",
   "teamId": "5774823376551936",
   "score": "2011989",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Extra Trio",
   "teamId": "5503425399750656",
   "score": "2011484",
   "hubId": "0",
   "countries": [
    "Montenegro",
    "Montenegro",
    "Montenegro"
   ]
  },
  {
   "teamName": ".pyVerts",
   "teamId": "6464666259685376",
   "score": "2011047",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Just Read The Instructions",
   "teamId": "5616598391980032",
   "score": "2010902",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "mlworks",
   "teamId": "4848099021291520",
   "score": "2010828",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "I Love Programming",
   "teamId": "4775506088034304",
   "score": "2009752",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "w0rms",
   "teamId": "5245879900438528",
   "score": "2008980",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Patatas Bravas",
   "teamId": "6354730599055360",
   "score": "2007506",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Meulemen",
   "teamId": "6685940021985280",
   "score": "2007158",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Blackforest Labs",
   "teamId": "4748852863172608",
   "score": "2006467",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Karlsruhe Data Scientists",
   "teamId": "4618224385654784",
   "score": "2006116",
   "hubId": "6478634030202880",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "π-ton",
   "teamId": "4589947394719744",
   "score": "2005914",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "eSchmetterlinge",
   "teamId": "5775931142569984",
   "score": "2005487",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Estonia"
   ]
  },
  {
   "teamName": "The Resistance",
   "teamId": "6095880771862528",
   "score": "2005317",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Flying Dinos",
   "teamId": "6316463782625280",
   "score": "2003416",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "RandomRockets",
   "teamId": "6681514796384256",
   "score": "2003144",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "The ReTARDIS",
   "teamId": "5497983944622080",
   "score": "2002108",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rational Unicorns of natural integrated Complexity",
   "teamId": "5680316916170752",
   "score": "2001999",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "AYO-Team",
   "teamId": "6024176829726720",
   "score": "2001854",
   "hubId": "5842748150120448",
   "countries": [
    "Morocco",
    "Morocco",
    "Morocco",
    "France"
   ]
  },
  {
   "teamName": "Pomaranchi",
   "teamId": "4859427534405632",
   "score": "2001728",
   "hubId": "5916923376173056",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "GoldieLab",
   "teamId": "4839510160441344",
   "score": "2001574",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "cyclops",
   "teamId": "4914552902778880",
   "score": "2000449",
   "hubId": "5112178910691328",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Los Hermanos",
   "teamId": "6445517617758208",
   "score": "2000330",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Team 134",
   "teamId": "5077345920614400",
   "score": "2000254",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Baku EU 1",
   "teamId": "5773097537896448",
   "score": "2000218",
   "hubId": "5414985513566208",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "import antigravity",
   "teamId": "5980363331469312",
   "score": "1999874",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "NinjaCats",
   "teamId": "5700705662795776",
   "score": "1999243",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "BytePigeon",
   "teamId": "6619523654352896",
   "score": "1999136",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Estonia",
    "Estonia",
    "Estonia"
   ]
  },
  {
   "teamName": "Beat Soy",
   "teamId": "6522931450478592",
   "score": "1998995",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "BingFanclub",
   "teamId": "4564192354893824",
   "score": "1998651",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Copy in the Past",
   "teamId": "5078426843086848",
   "score": "1998463",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "KG_knights_Seniors",
   "teamId": "5555275385798656",
   "score": "1998245",
   "hubId": "0",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "Platypuses",
   "teamId": "5363316117471232",
   "score": "1998245",
   "hubId": "6640431018278912",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "MAMOHT B OKEAHE",
   "teamId": "5444247931060224",
   "score": "1997775",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Ukraine",
    "Ukraine",
    "Netherlands"
   ]
  },
  {
   "teamName": "PleaseFillOutThisField.",
   "teamId": "5613827064332288",
   "score": "1997694",
   "hubId": "6448591136620544",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Pink Unicorns",
   "teamId": "5392041328508928",
   "score": "1997675",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "!superlemon",
   "teamId": "5919057505157120",
   "score": "1997675",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "ADNAKLASSNIKE_GIRMIYECEM",
   "teamId": "6395773306535936",
   "score": "1997675",
   "hubId": "5042625404993536",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "Becky appreciation club",
   "teamId": "5248804437622784",
   "score": "1997390",
   "hubId": "4679001863880704",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "great team name",
   "teamId": "5587552065028096",
   "score": "1996824",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "ElSacontala",
   "teamId": "5591832469700608",
   "score": "1996404",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Random",
   "teamId": "5675636408451072",
   "score": "1996360",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Diablo",
   "teamId": "6520721756913664",
   "score": "1996349",
   "hubId": "6291708597764096",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "WhatElse",
   "teamId": "4711189959409664",
   "score": "1996242",
   "hubId": "4852035560144896",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Los que van de propio",
   "teamId": "5143664711958528",
   "score": "1996157",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "The magnificent AA",
   "teamId": "5397505332215808",
   "score": "1995966",
   "hubId": "5751703970250752",
   "countries": [
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "Not Arazim(NotArazimIsn'tTheUnionOfAllTheSubsetsOfTheSetArazim",
   "teamId": "5198983890731008",
   "score": "1995532",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Connect's Four",
   "teamId": "5528060795289600",
   "score": "1995391",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "SantiAbascode",
   "teamId": "6302410112761856",
   "score": "1994935",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Tike Myson",
   "teamId": "5986204218556416",
   "score": "1994736",
   "hubId": "5659826029854720",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Ekipa",
   "teamId": "6687476882079744",
   "score": "1994702",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Kappa Pride",
   "teamId": "5511538861408256",
   "score": "1994031",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "C214",
   "teamId": "6177303486791680",
   "score": "1993880",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "familia_mocstro",
   "teamId": "4998980953964544",
   "score": "1993183",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "🦄🦄🔥哑挪嘘🔥🦄🦄",
   "teamId": "6544962552332288",
   "score": "1992782",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "DROP TABLE teams;",
   "teamId": "5770125420527616",
   "score": "1992497",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "dreamcode",
   "teamId": "5032347749580800",
   "score": "1992410",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "💩",
   "teamId": "4505898038853632",
   "score": "1991858",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Sea Systems",
   "teamId": "4981435005927424",
   "score": "1989972",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Awesomenauts",
   "teamId": "5483709419487232",
   "score": "1989420",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Hopfen & Malz",
   "teamId": "4919395478405120",
   "score": "1988811",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Muffin Miners",
   "teamId": "5430034407882752",
   "score": "1988802",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "eworx",
   "teamId": "5895717847564288",
   "score": "1987325",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Angle",
   "teamId": "5323794566610944",
   "score": "1986062",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Fast and Fourier",
   "teamId": "6018956833849344",
   "score": "1984865",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "MyLittleAdventure",
   "teamId": "4857927584186368",
   "score": "1983706",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NicidecumSoimiiMascati",
   "teamId": "5481613676773376",
   "score": "1981403",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Kinder",
   "teamId": "5050435534585856",
   "score": "1981062",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Gulf Glorkwimp",
   "teamId": "5209516022956032",
   "score": "1980028",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "EasyBit",
   "teamId": "4751923966115840",
   "score": "1979557",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "♚",
   "teamId": "5430098563956736",
   "score": "1979516",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Mavericks",
   "teamId": "6216445872570368",
   "score": "1979462",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "NASA",
   "teamId": "5853974456434688",
   "score": "1979275",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Fire Tigers",
   "teamId": "5781989730811904",
   "score": "1979259",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "GDG Fribourg",
   "teamId": "5897791712788480",
   "score": "1978959",
   "hubId": "6144857559007232",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Skills 404",
   "teamId": "5780375359979520",
   "score": "1977084",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Smart Sleeping Students",
   "teamId": "6189708090540032",
   "score": "1976671",
   "hubId": "6565180842442752",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Perfectly Intact Underarm",
   "teamId": "5267553110720512",
   "score": "1976025",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "{code}",
   "teamId": "5139745822736384",
   "score": "1975779",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "C(++)Laget",
   "teamId": "5660827361214464",
   "score": "1975459",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Team Foreign",
   "teamId": "4856184297226240",
   "score": "1974390",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TDBetterThanYourTeam",
   "teamId": "5212945218797568",
   "score": "1974321",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "4lg0n00bs",
   "teamId": "6301559977672704",
   "score": "1973116",
   "hubId": "0",
   "countries": [
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "Les Jean Mi",
   "teamId": "5697643351113728",
   "score": "1973092",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Bayes & Co.",
   "teamId": "4592739593224192",
   "score": "1972240",
   "hubId": "5436096754221056",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Lynxous",
   "teamId": "6490704767352832",
   "score": "1971398",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "1066",
   "teamId": "5583786653777920",
   "score": "1971197",
   "hubId": "6604327590297600",
   "countries": [
    "France",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Kernels",
   "teamId": "5194403844980736",
   "score": "1970433",
   "hubId": "6158895055634432",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "nevermind",
   "teamId": "5948881959387136",
   "score": "1969634",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "United Kingdom",
    "Poland"
   ]
  },
  {
   "teamName": "root-beer",
   "teamId": "5950112199081984",
   "score": "1967270",
   "hubId": "0",
   "countries": [
    "Austria",
    "United Kingdom",
    "Luxembourg",
    "Finland"
   ]
  },
  {
   "teamName": "The Heidis and the Taco",
   "teamId": "6241962071949312",
   "score": "1966917",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Insert name here",
   "teamId": "5403968184254464",
   "score": "1966306",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Mañocoders",
   "teamId": "4568609191886848",
   "score": "1964476",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "rational_shadows",
   "teamId": "6225558182559744",
   "score": "1964346",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Hoppers of the World",
   "teamId": "6504135935393792",
   "score": "1963176",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Germany",
    "United Kingdom",
    "Italy"
   ]
  },
  {
   "teamName": "Blue Whale",
   "teamId": "5808954743455744",
   "score": "1962497",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Coding Dori",
   "teamId": "6301954040922112",
   "score": "1962237",
   "hubId": "6144857559007232",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Synapse",
   "teamId": "5634791001030656",
   "score": "1962214",
   "hubId": "5493471611715584",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "qwerty123",
   "teamId": "6464593178132480",
   "score": "1962161",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Team Zebu",
   "teamId": "4667975072219136",
   "score": "1962101",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "YouTubeToMp3Converter",
   "teamId": "5283730306367488",
   "score": "1960735",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Dırınırınırınııı",
   "teamId": "6356695076831232",
   "score": "1959438",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Four of a kind",
   "teamId": "5507204702535680",
   "score": "1959161",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "InterEuro",
   "teamId": "5163503971205120",
   "score": "1958536",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Germany"
   ]
  },
  {
   "teamName": "Les 4 mousquetaires",
   "teamId": "5578835697336320",
   "score": "1956253",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "'TassoTeam",
   "teamId": "5614466477588480",
   "score": "1955948",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Big Brother",
   "teamId": "5626453395767296",
   "score": "1955729",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Melon Party",
   "teamId": "5757253739085824",
   "score": "1954981",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "crashcode.withnoodles.party",
   "teamId": "6396019730284544",
   "score": "1954429",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "¬False",
   "teamId": "5630676690796544",
   "score": "1954117",
   "hubId": "4936954646888448",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Kaffeeklatsch",
   "teamId": "5873714461671424",
   "score": "1953895",
   "hubId": "4842166262169600",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Slow Loris",
   "teamId": "4935196998631424",
   "score": "1953366",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland",
    "Egypt",
    "Ireland"
   ]
  },
  {
   "teamName": "calculated",
   "teamId": "6475626143809536",
   "score": "1953109",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "HashCodshiki",
   "teamId": "5907177558507520",
   "score": "1952891",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "ViaIsAwesome",
   "teamId": "6332733387177984",
   "score": "1952020",
   "hubId": "4805185117356032",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NU",
   "teamId": "6126772257030144",
   "score": "1948816",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "CCTeam",
   "teamId": "5401499651801088",
   "score": "1948744",
   "hubId": "0",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "Programatorji",
   "teamId": "6365381379751936",
   "score": "1948290",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Freeways",
   "teamId": "6232897946124288",
   "score": "1948073",
   "hubId": "0",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Insan Wa Alat",
   "teamId": "4770713105858560",
   "score": "1947449",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "diht guys",
   "teamId": "6222340916510720",
   "score": "1947283",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "PrzestrzenHausdorffa",
   "teamId": "4962293880193024",
   "score": "1947137",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Hi-Tek",
   "teamId": "5325139428245504",
   "score": "1946852",
   "hubId": "0",
   "countries": [
    "Macedonia",
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "Beslutsångest",
   "teamId": "6665138622955520",
   "score": "1946506",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Newbies",
   "teamId": "6733323980242944",
   "score": "1945108",
   "hubId": "0",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Germany",
    "Tunisia"
   ]
  },
  {
   "teamName": "Team 180°",
   "teamId": "6710436569284608",
   "score": "1944495",
   "hubId": "4842166262169600",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Ardoq",
   "teamId": "5368135808974848",
   "score": "1941738",
   "hubId": "5074919532527616",
   "countries": [
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "TimeWarrior",
   "teamId": "5942007998447616",
   "score": "1940682",
   "hubId": "5739578472267776",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "SSS",
   "teamId": "6096423279919104",
   "score": "1940640",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Commmedia Team",
   "teamId": "4938255283781632",
   "score": "1940585",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "vadtrevligt",
   "teamId": "4806947329015808",
   "score": "1939799",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Team.tmp",
   "teamId": "6112026090799104",
   "score": "1939694",
   "hubId": "6440138506764288",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Württemberg Wombats",
   "teamId": "5233398993911808",
   "score": "1938122",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "sa krompirom",
   "teamId": "5318596582440960",
   "score": "1937071",
   "hubId": "0",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "SoC Staff",
   "teamId": "5547906496987136",
   "score": "1936088",
   "hubId": "5123864979832832",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Unknown team",
   "teamId": "5636091906359296",
   "score": "1934703",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Wow so imperative",
   "teamId": "5364075521376256",
   "score": "1933929",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "fun team",
   "teamId": "5385765106221056",
   "score": "1931588",
   "hubId": "5983641666584576",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "LiisIasiRomania",
   "teamId": "4809413177114624",
   "score": "1931064",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "eawopf;rwaospfhj",
   "teamId": "6725402651262976",
   "score": "1929973",
   "hubId": "5157805958889472",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Nothing",
   "teamId": "6573754939342848",
   "score": "1929109",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Cabxolotl",
   "teamId": "6359298900754432",
   "score": "1928916",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Just in Case",
   "teamId": "6207355909832704",
   "score": "1927937",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Wizards",
   "teamId": "4957139919437824",
   "score": "1927537",
   "hubId": "0",
   "countries": [
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "Happy Trolls",
   "teamId": "4712026739834880",
   "score": "1925068",
   "hubId": "5645240186699776",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "0x2A",
   "teamId": "6163181030342656",
   "score": "1923657",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "the Argonauts",
   "teamId": "5490160460365824",
   "score": "1920925",
   "hubId": "6508589212499968",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Team0",
   "teamId": "6565676307185664",
   "score": "1919551",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "UCooL",
   "teamId": "4976102200049664",
   "score": "1919067",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Havana Blues",
   "teamId": "5663703982669824",
   "score": "1916476",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "404 Name not found",
   "teamId": "4641657995657216",
   "score": "1916466",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France",
    "Italy"
   ]
  },
  {
   "teamName": "The Unbrothers",
   "teamId": "5914055680196608",
   "score": "1916371",
   "hubId": "6407743179063296",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "dmg aalto",
   "teamId": "6069673955164160",
   "score": "1916335",
   "hubId": "5292985222692864",
   "countries": [
    "Finland",
    "Finland",
    "Finland",
    "Finland"
   ]
  },
  {
   "teamName": "X",
   "teamId": "5614520634441728",
   "score": "1916277",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "+1 2.0",
   "teamId": "6086153946005504",
   "score": "1915340",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "France"
   ]
  },
  {
   "teamName": "SAPO",
   "teamId": "4694850897182720",
   "score": "1915270",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "B.awesome",
   "teamId": "4616894019534848",
   "score": "1914421",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "vente-privee",
   "teamId": "6630975647776768",
   "score": "1914314",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "pew",
   "teamId": "5306463635374080",
   "score": "1913338",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Tordello",
   "teamId": "6666218538795008",
   "score": "1913012",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Hakatonci",
   "teamId": "5650238387781632",
   "score": "1912296",
   "hubId": "6409247491358720",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "Bargrizoon",
   "teamId": "4672264402370560",
   "score": "1911365",
   "hubId": "0",
   "countries": [
    "Iran",
    "Iran"
   ]
  },
  {
   "teamName": "The Prime",
   "teamId": "5414361803784192",
   "score": "1911343",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "l'API ne fait pas le moine",
   "teamId": "6091303880228864",
   "score": "1911083",
   "hubId": "0",
   "countries": [
    "France",
    "Gabon"
   ]
  },
  {
   "teamName": "Gases Nobles",
   "teamId": "6007825352359936",
   "score": "1911037",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "No For, No While",
   "teamId": "5895972592812032",
   "score": "1911015",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "EnigmaTeam",
   "teamId": "5666762469146624",
   "score": "1910996",
   "hubId": "0",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Try Again",
   "teamId": "4520656620224512",
   "score": "1910977",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "YotaFive",
   "teamId": "5627740006907904",
   "score": "1910736",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "UnworkableRiver",
   "teamId": "4880553136357376",
   "score": "1910709",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "SHS",
   "teamId": "6596455653441536",
   "score": "1910679",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "1P2L",
   "teamId": "6669613509115904",
   "score": "1910613",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "preventDefault()",
   "teamId": "6270289730076672",
   "score": "1910567",
   "hubId": "5117366962749440",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "TriggerAlert",
   "teamId": "4597936033890304",
   "score": "1910359",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Papayena",
   "teamId": "6423482288046080",
   "score": "1909811",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "UDP joke, got it?",
   "teamId": "6522997015838720",
   "score": "1909761",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "FIL",
   "teamId": "4557951029215232",
   "score": "1909724",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Your Team",
   "teamId": "6184261870682112",
   "score": "1909496",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Frunza",
   "teamId": "4681480932425728",
   "score": "1909299",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Titanic Swimteam",
   "teamId": "5748419461120000",
   "score": "1909240",
   "hubId": "5074919532527616",
   "countries": [
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Genussbiertrinker",
   "teamId": "5665862203736064",
   "score": "1908752",
   "hubId": "4766541551763456",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "NPCompleteTeam",
   "teamId": "6147489098891264",
   "score": "1908634",
   "hubId": "0",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "NOS",
   "teamId": "6403556659691520",
   "score": "1907270",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Heisenbug's Certainty Principle",
   "teamId": "4813926986416128",
   "score": "1907250",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "While (True) break;",
   "teamId": "5365117050945536",
   "score": "1906905",
   "hubId": "4992773048500224",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "ThunderCats",
   "teamId": "4826591972556800",
   "score": "1906499",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ForthOfFirth",
   "teamId": "5241434072416256",
   "score": "1905934",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "Slovakia",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "archer",
   "teamId": "6250148145397760",
   "score": "1905866",
   "hubId": "5378351053144064",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Failman & Barbie",
   "teamId": "4528415075991552",
   "score": "1905572",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Flippers",
   "teamId": "6310332045721600",
   "score": "1903759",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "EG",
   "teamId": "5242813830660096",
   "score": "1903362",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "AdJoTo",
   "teamId": "6712936844230656",
   "score": "1900641",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Roots",
   "teamId": "4839390169792512",
   "score": "1900575",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "The Coding Dead",
   "teamId": "5028863792906240",
   "score": "1899008",
   "hubId": "4747093939847168",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Rowdy 3",
   "teamId": "4522005239955456",
   "score": "1897162",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TheUltimateColoc",
   "teamId": "6730143556960256",
   "score": "1896396",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Progineer",
   "teamId": "4574004677443584",
   "score": "1896151",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Mixoner's",
   "teamId": "6111021873758208",
   "score": "1895686",
   "hubId": "6448591136620544",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "💩 ENjS 🦄",
   "teamId": "5474779108737024",
   "score": "1895156",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "// TODO: name the team",
   "teamId": "6579550930599936",
   "score": "1893374",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Cristina's Secret",
   "teamId": "5071814338281472",
   "score": "1891314",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Skies",
   "teamId": "6210856643723264",
   "score": "1890744",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "codeworld",
   "teamId": "5290539440144384",
   "score": "1890437",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "TangledLight",
   "teamId": "4987573051064320",
   "score": "1889583",
   "hubId": "5841827282288640",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "m0jette",
   "teamId": "6343724208488448",
   "score": "1889231",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "hubsi",
   "teamId": "6225931307843584",
   "score": "1887009",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Skillaci",
   "teamId": "6459020055412736",
   "score": "1886902",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "rootBoot",
   "teamId": "5991678355701760",
   "score": "1886853",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "NTUAwannaCODE",
   "teamId": "6239632991715328",
   "score": "1886473",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "HAL4U",
   "teamId": "5433058534621184",
   "score": "1885266",
   "hubId": "5751703970250752",
   "countries": [
    "Latvia",
    "Latvia",
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "Romeoreos",
   "teamId": "4963321719554048",
   "score": "1885015",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Orichalcos",
   "teamId": "4616895361712128",
   "score": "1884872",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Quivr",
   "teamId": "6331850234527744",
   "score": "1884514",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Kayzr",
   "teamId": "4714706799427584",
   "score": "1883545",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "0x4D2",
   "teamId": "4715775910739968",
   "score": "1883114",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Tartle",
   "teamId": "4806926659485696",
   "score": "1881284",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "compiler whisperers",
   "teamId": "6323495986266112",
   "score": "1880710",
   "hubId": "0",
   "countries": [
    "Qatar",
    "Romania"
   ]
  },
  {
   "teamName": "3º A",
   "teamId": "5599239744782336",
   "score": "1879781",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Recovery",
   "teamId": "5332091369684992",
   "score": "1879716",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "KaHaeM",
   "teamId": "5135215773089792",
   "score": "1878795",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "GoDataDrivenYnformedAlliance",
   "teamId": "5173677540769792",
   "score": "1877997",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "zero",
   "teamId": "6291628671107072",
   "score": "1877876",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Epilog",
   "teamId": "4936255909396480",
   "score": "1877772",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Penta Force",
   "teamId": "5116713255305216",
   "score": "1875644",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Team Trappist",
   "teamId": "4573965217431552",
   "score": "1872493",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Baku EU 2",
   "teamId": "4701878268985344",
   "score": "1871155",
   "hubId": "5414985513566208",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "NBZ",
   "teamId": "6467831583473664",
   "score": "1870701",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Bad Hombres",
   "teamId": "4734239438274560",
   "score": "1870573",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Les Chtis Basques",
   "teamId": "6198014020419584",
   "score": "1870499",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hash Bash",
   "teamId": "6003779761602560",
   "score": "1870445",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Uruk-hai of Isengard",
   "teamId": "4837962428710912",
   "score": "1869402",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "hello_friends",
   "teamId": "4541044561543168",
   "score": "1869225",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "CerealKillers",
   "teamId": "4745142011428864",
   "score": "1869090",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "Dream Travellers",
   "teamId": "5415345284186112",
   "score": "1869028",
   "hubId": "6565180842442752",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Bears",
   "teamId": "6218652076474368",
   "score": "1868991",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Russia"
   ]
  },
  {
   "teamName": "Cryptic Hex 107",
   "teamId": "5935100483076096",
   "score": "1868821",
   "hubId": "0",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Code Trio",
   "teamId": "5655266787852288",
   "score": "1868747",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Uvecchj",
   "teamId": "6489405472636928",
   "score": "1866535",
   "hubId": "0",
   "countries": [
    "Spain",
    "Italy"
   ]
  },
  {
   "teamName": "jakeWeary",
   "teamId": "5903075596304384",
   "score": "1866272",
   "hubId": "4766541551763456",
   "countries": [
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Teamname?",
   "teamId": "6638456474173440",
   "score": "1865080",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Ravens",
   "teamId": "6134890550525952",
   "score": "1865040",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Albania"
   ]
  },
  {
   "teamName": "Has Kod",
   "teamId": "6569874906152960",
   "score": "1864238",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "dr. rekt",
   "teamId": "6512099073196032",
   "score": "1864129",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "SegmentationFault",
   "teamId": "5957799989215232",
   "score": "1863182",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "IRIS Team",
   "teamId": "5699904584286208",
   "score": "1863133",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Necromancy",
   "teamId": "4736282232094720",
   "score": "1862555",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "hoehel",
   "teamId": "4664710897074176",
   "score": "1862476",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Grumpy Cats",
   "teamId": "6024270245265408",
   "score": "1861555",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "carcdr",
   "teamId": "4827482238746624",
   "score": "1861459",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Weierstrass",
   "teamId": "5111660561825792",
   "score": "1861441",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "mexuy",
   "teamId": "6669013354545152",
   "score": "1860871",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "mentor",
   "teamId": "5138290097258496",
   "score": "1860161",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "meatloaf",
   "teamId": "6523774069374976",
   "score": "1859096",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "KAUSTAT",
   "teamId": "6320036926980096",
   "score": "1858323",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "BaYes👍",
   "teamId": "6249097824567296",
   "score": "1857919",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "GreatAgain",
   "teamId": "5201156607311872",
   "score": "1857103",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "DAISY",
   "teamId": "6367148758794240",
   "score": "1855219",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "TKHash",
   "teamId": "6499580652814336",
   "score": "1854969",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "P=NP <=> P=0 v N=1",
   "teamId": "4831230067474432",
   "score": "1854408",
   "hubId": "0",
   "countries": [
    "Moldova",
    "Germany"
   ]
  },
  {
   "teamName": "Red Team 🐍🐊😐",
   "teamId": "4816618521624576",
   "score": "1853000",
   "hubId": "5690886025379840",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Guldpojkarna",
   "teamId": "6477244339847168",
   "score": "1852027",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Do[n't] Panic",
   "teamId": "4859019848056832",
   "score": "1851844",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "abcde",
   "teamId": "6444719626256384",
   "score": "1851261",
   "hubId": "0",
   "countries": [
    "France",
    "Italy",
    "France"
   ]
  },
  {
   "teamName": "Crashtest Security",
   "teamId": "4859795089653760",
   "score": "1850676",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Syntax Terror",
   "teamId": "6065352412758016",
   "score": "1850611",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "B.Hash",
   "teamId": "6528618255613952",
   "score": "1850074",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "4boyz1semaphore",
   "teamId": "5229331055902720",
   "score": "1850022",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Insights @ Artefact",
   "teamId": "6544294148046848",
   "score": "1849254",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "PeanutButterJellyTime",
   "teamId": "5729521873453056",
   "score": "1849112",
   "hubId": "5082182590660608",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Bits Please AUB",
   "teamId": "5543279743467520",
   "score": "1848395",
   "hubId": "4917250343567360",
   "countries": [
    "Lebanon",
    "Lebanon",
    "Lebanon"
   ]
  },
  {
   "teamName": "Kloud",
   "teamId": "5197212485156864",
   "score": "1848112",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "NiYu",
   "teamId": "5162453918810112",
   "score": "1847685",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Noa's stars",
   "teamId": "5722153387294720",
   "score": "1846756",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "D.U.N.K.",
   "teamId": "6705363407601664",
   "score": "1846462",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "DevGuys",
   "teamId": "5792975988719616",
   "score": "1846194",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Secret Boot",
   "teamId": "6118226077417472",
   "score": "1845977",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Null Pointer Exceptions",
   "teamId": "5894251317559296",
   "score": "1845909",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Hackers Delight",
   "teamId": "5908361627303936",
   "score": "1845685",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Practice Progress",
   "teamId": "5723216861462528",
   "score": "1844665",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "CentraleSupélec",
   "teamId": "5164758370091008",
   "score": "1843775",
   "hubId": "4805185117356032",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Meowing Humans",
   "teamId": "5658155958665216",
   "score": "1843757",
   "hubId": "5654907889647616",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Flawless",
   "teamId": "6186191049195520",
   "score": "1842972",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "happy hippo",
   "teamId": "6438552053219328",
   "score": "1842972",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Calle is a Lie",
   "teamId": "6041736535080960",
   "score": "1842972",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "0xDEADC0DE",
   "teamId": "5660200631533568",
   "score": "1842619",
   "hubId": "4594856005468160",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "algo4fun",
   "teamId": "5515723904385024",
   "score": "1841797",
   "hubId": "6448591136620544",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "IMAGeek",
   "teamId": "6367555706945536",
   "score": "1841168",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "byte me",
   "teamId": "5074458091978752",
   "score": "1841128",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "GoogleIt",
   "teamId": "6636961825554432",
   "score": "1841115",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "CentralePipo",
   "teamId": "4921828308942848",
   "score": "1841112",
   "hubId": "4805185117356032",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Summitech",
   "teamId": "5121243372060672",
   "score": "1841087",
   "hubId": "5071734210297856",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Fresh Meat",
   "teamId": "5970628989419520",
   "score": "1840988",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Bombaleyo",
   "teamId": "5299046495289344",
   "score": "1840960",
   "hubId": "4715927375446016",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "HMP",
   "teamId": "5953382145589248",
   "score": "1840827",
   "hubId": "5842748150120448",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Nice Try",
   "teamId": "5814414854848512",
   "score": "1840614",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "NullPointerInception",
   "teamId": "6720522561781760",
   "score": "1840614",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "kpiguys",
   "teamId": "5414689295040512",
   "score": "1840614",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Instructor@SITE",
   "teamId": "5995895745150976",
   "score": "1840487",
   "hubId": "5042625404993536",
   "countries": [
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "Disciples",
   "teamId": "6586223967600640",
   "score": "1839559",
   "hubId": "4671317026537472",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Orrrrr",
   "teamId": "6070002721488896",
   "score": "1839046",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Jackals",
   "teamId": "5956346344112128",
   "score": "1838916",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Ludicrous Pajama Lords",
   "teamId": "5272685865074688",
   "score": "1838653",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "kgb_orgi",
   "teamId": "5686888753004544",
   "score": "1838548",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "DJCS",
   "teamId": "4707557490819072",
   "score": "1838162",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Team Dalk",
   "teamId": "5134733327466496",
   "score": "1837538",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "We must go deeper",
   "teamId": "6509544976941056",
   "score": "1837035",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "FiftyShadesOfBash",
   "teamId": "6367982854864896",
   "score": "1835606",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Teeming with Homophones",
   "teamId": "5754819834806272",
   "score": "1835296",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "test team",
   "teamId": "4531120301408256",
   "score": "1835106",
   "hubId": "6063418469515264",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Les fanfarons",
   "teamId": "5203936323567616",
   "score": "1835073",
   "hubId": "5436096754221056",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "00Agents",
   "teamId": "5124984288575488",
   "score": "1834912",
   "hubId": "0",
   "countries": [
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "YoWis!",
   "teamId": "5018438028230656",
   "score": "1834636",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "ACsapat",
   "teamId": "6341328489152512",
   "score": "1833882",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Poran",
   "teamId": "5103274369744896",
   "score": "1833321",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Let's make tabela great again",
   "teamId": "6244410404634624",
   "score": "1833300",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Team Pietro",
   "teamId": "5078578240684032",
   "score": "1832342",
   "hubId": "6478634030202880",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Null Point Busters",
   "teamId": "6679901499293696",
   "score": "1830642",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Mother of Dragons",
   "teamId": "5496726660055040",
   "score": "1829872",
   "hubId": "5983641666584576",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Step forward",
   "teamId": "6562810825801728",
   "score": "1828398",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "elgoog",
   "teamId": "4644225513684992",
   "score": "1828283",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Tactic Real-Time",
   "teamId": "6213033789489152",
   "score": "1826630",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Estonia"
   ]
  },
  {
   "teamName": "Home Alone",
   "teamId": "5094326610690048",
   "score": "1826499",
   "hubId": "6602827975622656",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Multiposting",
   "teamId": "5010224708583424",
   "score": "1825837",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Itanis",
   "teamId": "6457312470368256",
   "score": "1825195",
   "hubId": "4917250343567360",
   "countries": [
    "Lebanon",
    "Lebanon",
    "Lebanon",
    "Lebanon"
   ]
  },
  {
   "teamName": "Gulerodskage",
   "teamId": "4668630860038144",
   "score": "1824382",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark",
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "Fire Ferrets",
   "teamId": "5480979632226304",
   "score": "1824058",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "ANAMEN",
   "teamId": "4673284524212224",
   "score": "1823747",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Egypt",
    "Poland"
   ]
  },
  {
   "teamName": "Zradniky",
   "teamId": "4823215591391232",
   "score": "1823091",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Bonita power users",
   "teamId": "6344447172280320",
   "score": "1822697",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Just Another Team",
   "teamId": "4552104370765824",
   "score": "1821129",
   "hubId": "4701652514766848",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "<script>alert('pwned');</script>",
   "teamId": "5359681165852672",
   "score": "1820824",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "YoloCaml",
   "teamId": "4664919538532352",
   "score": "1820272",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Code and Recreation",
   "teamId": "5839306136485888",
   "score": "1820083",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "#PremioFisico",
   "teamId": "5657712503291904",
   "score": "1819783",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Donaudampfschifffahrtskapitänsanwärtersgehilfen",
   "teamId": "5012775315177472",
   "score": "1819682",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Never Mind",
   "teamId": "6023231064506368",
   "score": "1819350",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "TroIIson",
   "teamId": "5473910384492544",
   "score": "1819323",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "RashB",
   "teamId": "6225707097128960",
   "score": "1819220",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Navele",
   "teamId": "6531366028050432",
   "score": "1817185",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "NoLoveDeepWeb",
   "teamId": "5283997131210752",
   "score": "1816926",
   "hubId": "0",
   "countries": [
    "Austria",
    "France"
   ]
  },
  {
   "teamName": "HashBrownies",
   "teamId": "6453719394680832",
   "score": "1816524",
   "hubId": "0",
   "countries": [
    "Malta",
    "Malta",
    "Malta",
    "Malta"
   ]
  },
  {
   "teamName": "NoImagination",
   "teamId": "6282327650992128",
   "score": "1816242",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "team_name",
   "teamId": "5665905421844480",
   "score": "1815763",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "StockAI",
   "teamId": "5279133953163264",
   "score": "1813821",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Team Emse",
   "teamId": "5784254856298496",
   "score": "1813523",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "It's O(n)",
   "teamId": "5068774776504320",
   "score": "1813479",
   "hubId": "0",
   "countries": [
    "Sweden",
    "United Kingdom",
    "Estonia"
   ]
  },
  {
   "teamName": "undefined",
   "teamId": "5118918788120576",
   "score": "1813461",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "CL1357",
   "teamId": "4801695926190080",
   "score": "1813267",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Koalas",
   "teamId": "5835476569161728",
   "score": "1812108",
   "hubId": "0",
   "countries": [
    "Moldova",
    "Moldova",
    "Moldova"
   ]
  },
  {
   "teamName": "KeepCalm",
   "teamId": "5152025939542016",
   "score": "1808689",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Antrauki",
   "teamId": "5136464736157696",
   "score": "1808440",
   "hubId": "4685852605153280",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Holycow",
   "teamId": "5873113367576576",
   "score": "1807624",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "The Diabolical Squirrels",
   "teamId": "5298029594673152",
   "score": "1804980",
   "hubId": "6144857559007232",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "3.1415926535897932384626433832795028841971693993751058209749445",
   "teamId": "5635590200492032",
   "score": "1804859",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Sodifrance_NeRD",
   "teamId": "4633491316670464",
   "score": "1803584",
   "hubId": "5201755822358528",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "AtoS",
   "teamId": "5310338769616896",
   "score": "1798065",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "I'll_Overflow_Ur_NaN_M8",
   "teamId": "4966627032432640",
   "score": "1797664",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "EnJeTeI",
   "teamId": "5718159000600576",
   "score": "1797261",
   "hubId": "5666946347433984",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Red Shoe",
   "teamId": "6476647540719616",
   "score": "1796729",
   "hubId": "0",
   "countries": [
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "Team Bamboo",
   "teamId": "5326929624301568",
   "score": "1796507",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Quick Duos",
   "teamId": "5966853176295424",
   "score": "1796028",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "ahnigslos",
   "teamId": "4646566069534720",
   "score": "1795327",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Yee`",
   "teamId": "6592715810668544",
   "score": "1794416",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "TOFFEE",
   "teamId": "4601282820046848",
   "score": "1792343",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Benin"
   ]
  },
  {
   "teamName": "Candy Frogs",
   "teamId": "5762832297623552",
   "score": "1791865",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "ABJM",
   "teamId": "4638515086229504",
   "score": "1791723",
   "hubId": "0",
   "countries": [
    "Poland",
    "Switzerland",
    "Switzerland",
    "Poland"
   ]
  },
  {
   "teamName": "Whale",
   "teamId": "5089799916486656",
   "score": "1791297",
   "hubId": "6308495074787328",
   "countries": [
    "Denmark",
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "38,0367021",
   "teamId": "5138139840512000",
   "score": "1790497",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Booking.com",
   "teamId": "5758295268655104",
   "score": "1790406",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "pokecat",
   "teamId": "5914199360274432",
   "score": "1789992",
   "hubId": "4805185117356032",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "andlogn",
   "teamId": "5652881134845952",
   "score": "1789195",
   "hubId": "6508589212499968",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "QuadCore",
   "teamId": "4822484171882496",
   "score": "1788782",
   "hubId": "5800563518210048",
   "countries": [
    "Romania",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Hashit",
   "teamId": "5077004672040960",
   "score": "1788061",
   "hubId": "6125008703193088",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "OBWAN",
   "teamId": "6176952574541824",
   "score": "1787827",
   "hubId": "6440138506764288",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Aqua Dean Hunger Force",
   "teamId": "5663311194488832",
   "score": "1787333",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "STORM.legacy",
   "teamId": "5379913146171392",
   "score": "1786785",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "ICAD Sistemi",
   "teamId": "6533234338824192",
   "score": "1786707",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "DACHS",
   "teamId": "5710238879580160",
   "score": "1785421",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Deep Fried Theorems",
   "teamId": "6536302824521728",
   "score": "1784973",
   "hubId": "5944419287040000",
   "countries": [
    "France",
    "Netherlands",
    "United Kingdom",
    "Germany"
   ]
  },
  {
   "teamName": "if(noSuccess) tryAgain();",
   "teamId": "5625515750719488",
   "score": "1784873",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "MIP-MAP",
   "teamId": "6554522612662272",
   "score": "1784431",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "CheggIL",
   "teamId": "4926989249019904",
   "score": "1784399",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "WowCode Team",
   "teamId": "6603436921454592",
   "score": "1784001",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Team Overkill",
   "teamId": "6102025460776960",
   "score": "1783324",
   "hubId": "4992773048500224",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "PIKE IS THE KING OF WATERS LIKE LION IS THE KING OF JUNGLES",
   "teamId": "5541945619251200",
   "score": "1782407",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Nuclear Hamsters",
   "teamId": "6315379840253952",
   "score": "1779095",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "#winning",
   "teamId": "4736989089759232",
   "score": "1779032",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "SolidbrainKrk",
   "teamId": "4702206095785984",
   "score": "1778800",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Coffee Beans",
   "teamId": "4782702037303296",
   "score": "1778785",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Fantastic four20",
   "teamId": "6338910623891456",
   "score": "1778624",
   "hubId": "5732605190209536",
   "countries": [
    "Belgium",
    "Bulgaria",
    "Italy",
    "Netherlands"
   ]
  },
  {
   "teamName": "something",
   "teamId": "6409471634964480",
   "score": "1778009",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Moonlight",
   "teamId": "5097194776428544",
   "score": "1777042",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "TrinitIF",
   "teamId": "5320675145285632",
   "score": "1775387",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "Ireland",
    "France",
    "Ireland"
   ]
  },
  {
   "teamName": "Bandicoot Cumbersplash",
   "teamId": "5584338557075456",
   "score": "1774309",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "56K",
   "teamId": "5700553996763136",
   "score": "1773013",
   "hubId": "5645240186699776",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "GreeDizdar ¯\\_(ツ)_/¯",
   "teamId": "4861534014537728",
   "score": "1772886",
   "hubId": "5766567912538112",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Fantasy Team",
   "teamId": "5556332216188928",
   "score": "1772482",
   "hubId": "5165170082971648",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "while(True)",
   "teamId": "5675342538735616",
   "score": "1772482",
   "hubId": "5690886025379840",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "//TODO: Delete TODOs",
   "teamId": "6611021498155008",
   "score": "1772482",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Challenge Accepted",
   "teamId": "5487018691788800",
   "score": "1772482",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "TeamNotFoundException",
   "teamId": "6450258523455488",
   "score": "1772452",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "The Bad Coders",
   "teamId": "6685247190073344",
   "score": "1772328",
   "hubId": "4916204116377600",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "DaRTES",
   "teamId": "6339232746438656",
   "score": "1772213",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "#HashMentBons",
   "teamId": "5200072463613952",
   "score": "1772143",
   "hubId": "5218381573652480",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Absolute Zero",
   "teamId": "4689168051470336",
   "score": "1771299",
   "hubId": "5820837508677632",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Inirtin Mediavilestret",
   "teamId": "6238349668909056",
   "score": "1770469",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "UNIBUC - Mieii Fiorosi",
   "teamId": "6414853497421824",
   "score": "1770297",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Daibiao",
   "teamId": "4777797721522176",
   "score": "1769954",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "#define",
   "teamId": "5987417748144128",
   "score": "1769839",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "LaserKitten",
   "teamId": "5363003121729536",
   "score": "1765851",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "At least we tried",
   "teamId": "5426727283064832",
   "score": "1764915",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "'s Münchnerkindl & seine Buam",
   "teamId": "5174135692984320",
   "score": "1764474",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "DNA",
   "teamId": "4722306005860352",
   "score": "1763997",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Netherlands"
   ]
  },
  {
   "teamName": "TesterCDouter",
   "teamId": "5096077346734080",
   "score": "1763299",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "#respect",
   "teamId": "4897560468652032",
   "score": "1762868",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Here For The Pizza",
   "teamId": "5178770164023296",
   "score": "1761773",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Strike",
   "teamId": "6558477941997568",
   "score": "1761038",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "B(r)ing it O(n)!",
   "teamId": "5045917228990464",
   "score": "1760877",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Heaps are Most Certainly Sexy",
   "teamId": "4622713431785472",
   "score": "1760235",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "JET-MIEM",
   "teamId": "5592139090100224",
   "score": "1759871",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "HappyTroll",
   "teamId": "6515810394701824",
   "score": "1758350",
   "hubId": "6602827975622656",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "CapsLock",
   "teamId": "4719157660614656",
   "score": "1758191",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CS101",
   "teamId": "5286065694834688",
   "score": "1757429",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "NICETEAM",
   "teamId": "6358002424610816",
   "score": "1756833",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "AATA",
   "teamId": "5634728724004864",
   "score": "1756130",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ovidius",
   "teamId": "4597670886768640",
   "score": "1755898",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Fuzz & y",
   "teamId": "5346726269419520",
   "score": "1755718",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Cybersteins",
   "teamId": "4613466031652864",
   "score": "1753399",
   "hubId": "0",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "VR",
   "teamId": "6436721524736000",
   "score": "1752688",
   "hubId": "5739578472267776",
   "countries": [
    "United Kingdom",
    "Romania"
   ]
  },
  {
   "teamName": "Hash Doge",
   "teamId": "4864514990276608",
   "score": "1752310",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "ENSAM",
   "teamId": "5181670407798784",
   "score": "1751880",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "#BeMore",
   "teamId": "5171715143368704",
   "score": "1751877",
   "hubId": "0",
   "countries": [
    "Macedonia",
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "At Least We're Pretty",
   "teamId": "5707610896465920",
   "score": "1750098",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "SaltTea",
   "teamId": "6334708535263232",
   "score": "1749955",
   "hubId": "5044292523393024",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team 37",
   "teamId": "5778378535731200",
   "score": "1749890",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "AIM Tech #2",
   "teamId": "5563822303608832",
   "score": "1749026",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Kartoff",
   "teamId": "5637562127351808",
   "score": "1746669",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "team.asm",
   "teamId": "4679707312259072",
   "score": "1746142",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "KCDQ",
   "teamId": "5758448008429568",
   "score": "1745737",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "blacksmiths",
   "teamId": "5743117592428544",
   "score": "1745528",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "CodeUp",
   "teamId": "4797297879678976",
   "score": "1744779",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "A* Wars: The return of the Exception",
   "teamId": "6406039956094976",
   "score": "1744708",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Keyneo-2",
   "teamId": "5200029983703040",
   "score": "1743630",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SecBots",
   "teamId": "5282065201233920",
   "score": "1742018",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "UNIT Team",
   "teamId": "5610927424536576",
   "score": "1741272",
   "hubId": "4715927375446016",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "EvenBogoDoesBetter",
   "teamId": "5274970049478656",
   "score": "1741241",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "PariSteak",
   "teamId": "5283859423821824",
   "score": "1740827",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NoDijkstraNoCry",
   "teamId": "4512566244016128",
   "score": "1739837",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Fruit Flies",
   "teamId": "4757424007282688",
   "score": "1739282",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Kerim Labmez",
   "teamId": "5564102416007168",
   "score": "1739231",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "I Beat Myself",
   "teamId": "5287302376980480",
   "score": "1738863",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Orcas",
   "teamId": "5494807816306688",
   "score": "1736025",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Estonia"
   ]
  },
  {
   "teamName": "Codejunkies",
   "teamId": "5179465747398656",
   "score": "1735436",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Supaplex",
   "teamId": "6598860365365248",
   "score": "1734618",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "From Laval in OS courses",
   "teamId": "4764995967516672",
   "score": "1732196",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "IpsoSenso",
   "teamId": "5051802407927808",
   "score": "1730664",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Egg",
   "teamId": "6695103066275840",
   "score": "1729969",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "MOJO 2017",
   "teamId": "6000413580984320",
   "score": "1729721",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Top Kouderzy",
   "teamId": "5882493576151040",
   "score": "1729304",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Nincs ketto negy nelkul",
   "teamId": "5857200245309440",
   "score": "1728733",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "IpsoPlex",
   "teamId": "5092467426721792",
   "score": "1728139",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hard S'KI'lls",
   "teamId": "5845790396252160",
   "score": "1727054",
   "hubId": "5720755912310784",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "team86946161",
   "teamId": "5581035794333696",
   "score": "1726344",
   "hubId": "0",
   "countries": [
    "Austria",
    "Belgium",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Verhakselaars",
   "teamId": "4631196730392576",
   "score": "1726021",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Elgin",
   "teamId": "5748194042445824",
   "score": "1725684",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "JustJ",
   "teamId": "5673971034882048",
   "score": "1725491",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "MVP²",
   "teamId": "5358316238667776",
   "score": "1722687",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Netapsys DotNet",
   "teamId": "5269873399693312",
   "score": "1722530",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Across Borders",
   "teamId": "6196803577839616",
   "score": "1722417",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "uhh whatever",
   "teamId": "5462571133960192",
   "score": "1721911",
   "hubId": "0",
   "countries": [
    "Slovakia",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Sword",
   "teamId": "6030123950145536",
   "score": "1721851",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Les moutons électriques",
   "teamId": "4815987161432064",
   "score": "1721629",
   "hubId": "6026378671554560",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "t-servi.com",
   "teamId": "5053648438558720",
   "score": "1720909",
   "hubId": "6144857559007232",
   "countries": [
    "Switzerland",
    "Netherlands",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "0xDEADBABE",
   "teamId": "4993953426309120",
   "score": "1720657",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Vruja",
   "teamId": "4751134900092928",
   "score": "1720082",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "BOUN Analytics",
   "teamId": "5968416074629120",
   "score": "1719098",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "MoscowMule",
   "teamId": "6674030413217792",
   "score": "1718802",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "lefer",
   "teamId": "5936743576502272",
   "score": "1717749",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "El Romantico",
   "teamId": "5166689494761472",
   "score": "1716853",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "Lorem Ipsum",
   "teamId": "5853853660479488",
   "score": "1715121",
   "hubId": "6295925584560128",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Asymptix",
   "teamId": "4881722843856896",
   "score": "1714218",
   "hubId": "4514136859869184",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "pony7 --thug-life",
   "teamId": "6325027678978048",
   "score": "1713826",
   "hubId": "5842748150120448",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team HF",
   "teamId": "6481759424217088",
   "score": "1713162",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "AHMK",
   "teamId": "6338415427584000",
   "score": "1712788",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Grantas",
   "teamId": "6190629092589568",
   "score": "1712597",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Odrzutomeni",
   "teamId": "5790784548765696",
   "score": "1712177",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Xor the World",
   "teamId": "4955703521312768",
   "score": "1712109",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "The Kookies",
   "teamId": "4842962575949824",
   "score": "1711759",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "100tifikos",
   "teamId": "6368713737502720",
   "score": "1711575",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "MadSkillsException",
   "teamId": "5764106560733184",
   "score": "1710220",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "fant ikke på noe bedre",
   "teamId": "4625972506656768",
   "score": "1709711",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "KareliaTeam",
   "teamId": "6459288893521920",
   "score": "1709213",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "segfault+1",
   "teamId": "6350964986478592",
   "score": "1708235",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "FourException",
   "teamId": "5797475772268544",
   "score": "1705899",
   "hubId": "4535562237116416",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "PaT@TrHACK",
   "teamId": "5795699534856192",
   "score": "1704770",
   "hubId": "6441886759780352",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Goobysoft",
   "teamId": "6063482155827200",
   "score": "1703865",
   "hubId": "6158895055634432",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Pika Chu",
   "teamId": "5629807027027968",
   "score": "1702712",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Sudoers",
   "teamId": "6147288510496768",
   "score": "1702402",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "mutex::lock",
   "teamId": "5749004381978624",
   "score": "1702286",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "gingerninjas",
   "teamId": "6223779193683968",
   "score": "1701882",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Cack Hambridge",
   "teamId": "5520863034081280",
   "score": "1701247",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Les affreux",
   "teamId": "5550388451213312",
   "score": "1700430",
   "hubId": "5436096754221056",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "YolOCaml",
   "teamId": "6331443621920768",
   "score": "1699869",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Privalia IT",
   "teamId": "5039884947423232",
   "score": "1699681",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Bogosort",
   "teamId": "4994298634305536",
   "score": "1699386",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "hs2",
   "teamId": "4750358450536448",
   "score": "1697504",
   "hubId": "4842166262169600",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "DAixtra",
   "teamId": "4527302142590976",
   "score": "1697043",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "IOG",
   "teamId": "5351249406853120",
   "score": "1694719",
   "hubId": "0",
   "countries": [
    "Finland",
    "Finland",
    "Finland"
   ]
  },
  {
   "teamName": "3euro",
   "teamId": "4928893261709312",
   "score": "1694184",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Mamida",
   "teamId": "5829893984092160",
   "score": "1693199",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "MANIFESTANCI",
   "teamId": "4665480233091072",
   "score": "1690644",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "UAcoders",
   "teamId": "6710532132306944",
   "score": "1689788",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Beaf",
   "teamId": "5653106620628992",
   "score": "1689360",
   "hubId": "0",
   "countries": [
    "Morocco",
    "Morocco",
    "Morocco",
    "Morocco"
   ]
  },
  {
   "teamName": "Buldozerii",
   "teamId": "5558093421215744",
   "score": "1688680",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Bohema",
   "teamId": "5090761787834368",
   "score": "1688252",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Los gañanticos",
   "teamId": "5967361056178176",
   "score": "1686569",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Tea Party",
   "teamId": "5196314904100864",
   "score": "1686525",
   "hubId": "4775163228848128",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "WiztiTeam",
   "teamId": "6202820088823808",
   "score": "1686284",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "UFO",
   "teamId": "4534558624055296",
   "score": "1685905",
   "hubId": "5763337560260608",
   "countries": [
    "Luxembourg",
    "Luxembourg",
    "Luxembourg"
   ]
  },
  {
   "teamName": "5 more minutes",
   "teamId": "4655479670177792",
   "score": "1685142",
   "hubId": "6324625227120640",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "coolTeam",
   "teamId": "5611598982938624",
   "score": "1684260",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "#-men",
   "teamId": "5791627704532992",
   "score": "1683884",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "Slovakia",
    "United Kingdom"
   ]
  },
  {
   "teamName": "mifelse",
   "teamId": "4879143044907008",
   "score": "1683582",
   "hubId": "5803282098290688",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Goffo Team",
   "teamId": "4729075344080896",
   "score": "1683247",
   "hubId": "4715704574017536",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "3 Basketball Bats",
   "teamId": "4820444800614400",
   "score": "1682332",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Code diffusers",
   "teamId": "6518635744985088",
   "score": "1681747",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "#hashtag",
   "teamId": "5583486341611520",
   "score": "1679583",
   "hubId": "6478634030202880",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "segfault",
   "teamId": "4972995596517376",
   "score": "1679032",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "D comme Dépression",
   "teamId": "4958310700679168",
   "score": "1678571",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "// No Comment",
   "teamId": "5379875028336640",
   "score": "1675685",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Ludovico",
   "teamId": "5869263466266624",
   "score": "1675058",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Bad Reception",
   "teamId": "5506390537797632",
   "score": "1673543",
   "hubId": "5739578472267776",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Perfect Hashing",
   "teamId": "5861107122044928",
   "score": "1673134",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Liticos",
   "teamId": "5671907168878592",
   "score": "1672988",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Ginoul'HACK",
   "teamId": "5053088146653184",
   "score": "1672984",
   "hubId": "5720755912310784",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hamburger 3a djej",
   "teamId": "6717952292290560",
   "score": "1672896",
   "hubId": "4917250343567360",
   "countries": [
    "Lebanon",
    "Lebanon",
    "Lebanon",
    "Lebanon"
   ]
  },
  {
   "teamName": "One-way hash",
   "teamId": "5637465490587648",
   "score": "1671947",
   "hubId": "6210985626959872",
   "countries": [
    "Russia",
    "United Kingdom",
    "Slovakia",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Mirage",
   "teamId": "6007516584476672",
   "score": "1670776",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Cameroon",
    "Ukraine"
   ]
  },
  {
   "teamName": "Uppcode",
   "teamId": "4803481760169984",
   "score": "1668217",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Team Alpha Wolves",
   "teamId": "6204447680102400",
   "score": "1668064",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "FutureVision",
   "teamId": "6083039826280448",
   "score": "1667578",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "ElisionOne",
   "teamId": "4558165643362304",
   "score": "1667538",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "seventh letter in alphabet",
   "teamId": "5001071797731328",
   "score": "1667524",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "France",
    "France"
   ]
  },
  {
   "teamName": "IG2I",
   "teamId": "6498739912966144",
   "score": "1666969",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Refesh-s",
   "teamId": "5557831159775232",
   "score": "1666698",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "GoMind",
   "teamId": "4682207855640576",
   "score": "1666618",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "junoft",
   "teamId": "4812658024906752",
   "score": "1666618",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "The FouRs",
   "teamId": "5425456979378176",
   "score": "1666052",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "hashtronauts",
   "teamId": "5952490000351232",
   "score": "1664433",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "darona",
   "teamId": "5866884926799872",
   "score": "1663927",
   "hubId": "4883695106260992",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Have you tried turning it off and on again?",
   "teamId": "4902497265123328",
   "score": "1663711",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "import TeamName",
   "teamId": "5899138252144640",
   "score": "1663349",
   "hubId": "6029454941880320",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "T³",
   "teamId": "6568162086617088",
   "score": "1661603",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Eddy & De Pijlsters",
   "teamId": "6363737145475072",
   "score": "1661155",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Wow Team",
   "teamId": "6529922919038976",
   "score": "1660700",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "hashcolano",
   "teamId": "4823483825520640",
   "score": "1659230",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "CornelPanic",
   "teamId": "6438431727026176",
   "score": "1656708",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "KAUST-HHM",
   "teamId": "6334558748278784",
   "score": "1656392",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "daboom",
   "teamId": "5736517100109824",
   "score": "1655880",
   "hubId": "6274524702048256",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Bigoloto",
   "teamId": "4776092820832256",
   "score": "1654681",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rambus",
   "teamId": "5637707082498048",
   "score": "1653874",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "RUBE",
   "teamId": "5960761100730368",
   "score": "1653718",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "All sorts of broken",
   "teamId": "5067665601200128",
   "score": "1650914",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "AICU",
   "teamId": "6719306750492672",
   "score": "1650479",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Team VPV",
   "teamId": "5141842303647744",
   "score": "1648879",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Caracóis Hipocondríacos",
   "teamId": "5454821335236608",
   "score": "1648173",
   "hubId": "6079963757281280",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Algo-Rhythm",
   "teamId": "5520056922406912",
   "score": "1644898",
   "hubId": "5540597737717760",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Code busters",
   "teamId": "5861367504437248",
   "score": "1644896",
   "hubId": "6249764886675456",
   "countries": [
    "Malta",
    "Malta"
   ]
  },
  {
   "teamName": "rm -rf /",
   "teamId": "5516164004315136",
   "score": "1644522",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria",
    "Germany"
   ]
  },
  {
   "teamName": "Sodifrance #1",
   "teamId": "5119251916521472",
   "score": "1644372",
   "hubId": "5201755822358528",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Kebab sauce BBQ",
   "teamId": "5988862736203776",
   "score": "1644172",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team Dungeon and Dev",
   "teamId": "4607118673969152",
   "score": "1642594",
   "hubId": "4762512469786624",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "BlackRabbit",
   "teamId": "5941185981972480",
   "score": "1642410",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "KATZO",
   "teamId": "5717348862394368",
   "score": "1640488",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Team 1337",
   "teamId": "5087308835454976",
   "score": "1637762",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Solver's Google",
   "teamId": "6578567383089152",
   "score": "1637723",
   "hubId": "6606100203831296",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Peach",
   "teamId": "5059650118483968",
   "score": "1636242",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Three Weeks",
   "teamId": "5750905240551424",
   "score": "1635420",
   "hubId": "4552345895567360",
   "countries": [
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "DE0rz",
   "teamId": "5671386873856000",
   "score": "1634920",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "HORSE",
   "teamId": "6054158184480768",
   "score": "1634667",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ByteTeam",
   "teamId": "5448717515620352",
   "score": "1633796",
   "hubId": "4540926382833664",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Smokin' team",
   "teamId": "5606677822832640",
   "score": "1633463",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Team Bing",
   "teamId": "4885214518050816",
   "score": "1632170",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "A++",
   "teamId": "4885515635523584",
   "score": "1632165",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Galileo",
   "teamId": "5562121496559616",
   "score": "1632065",
   "hubId": "6576681288466432",
   "countries": [
    "Morocco",
    "Morocco",
    "United Arab Emirates"
   ]
  },
  {
   "teamName": "Gonna hashcode the Hardcode",
   "teamId": "5712425286369280",
   "score": "1630343",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "HardCoders",
   "teamId": "5841122035236864",
   "score": "1630265",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Oxagile",
   "teamId": "6022154437001216",
   "score": "1629059",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "FusterCluck",
   "teamId": "4712704740687872",
   "score": "1629048",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Cradmanshit",
   "teamId": "5790221371179008",
   "score": "1626865",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "IcyUmbrella",
   "teamId": "6132310147596288",
   "score": "1626127",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "MobyFlow",
   "teamId": "4666338689679360",
   "score": "1624754",
   "hubId": "5493471611715584",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "it works on paper",
   "teamId": "5930791892680704",
   "score": "1622047",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "!No odea actually;",
   "teamId": "5999342456406016",
   "score": "1621902",
   "hubId": "6210985626959872",
   "countries": [
    "Slovenia",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Ingénieurs Informaticiens ✧٩(•́⌄•́๑)و ✧",
   "teamId": "6213031910440960",
   "score": "1617903",
   "hubId": "6606100203831296",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Swift",
   "teamId": "6020175195275264",
   "score": "1615856",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "pony7 --overcooked",
   "teamId": "6551893354479616",
   "score": "1612469",
   "hubId": "5842748150120448",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Bottle",
   "teamId": "4503970672279552",
   "score": "1609686",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Les Triphasés 2.0",
   "teamId": "6310887371571200",
   "score": "1607402",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "TeamOP",
   "teamId": "5593404964601856",
   "score": "1607305",
   "hubId": "6504443965079552",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Risk Beatles",
   "teamId": "5385168374202368",
   "score": "1606063",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Scorebored [sic]",
   "teamId": "6172779141398528",
   "score": "1605187",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "HMB",
   "teamId": "6596915214942208",
   "score": "1604354",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "# Harsh Coders",
   "teamId": "5310596266328064",
   "score": "1603043",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Azerbaijan",
    "Turkey"
   ]
  },
  {
   "teamName": "The L-Team",
   "teamId": "5392239702310912",
   "score": "1601569",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Fora d'Horas",
   "teamId": "6508422312755200",
   "score": "1600798",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Cochambrosos",
   "teamId": "4983993934020608",
   "score": "1599192",
   "hubId": "5452279385686016",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "AT-ST",
   "teamId": "5080236634931200",
   "score": "1597779",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Planck's Constant",
   "teamId": "5391118178975744",
   "score": "1597693",
   "hubId": "4892331278860288",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Compiler c'est douter",
   "teamId": "6350995655229440",
   "score": "1595725",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Replicants",
   "teamId": "6158209068826624",
   "score": "1595494",
   "hubId": "5114465980776448",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Jumping Cat Exception",
   "teamId": "6288235646943232",
   "score": "1593490",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "UCU My Little Pony",
   "teamId": "6391256879988736",
   "score": "1593030",
   "hubId": "4735593493823488",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "FSI 2",
   "teamId": "5622470417580032",
   "score": "1591369",
   "hubId": "5082182590660608",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Asterisks",
   "teamId": "5886125239435264",
   "score": "1591122",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "An Englishman, Welshman and an Irishman...",
   "teamId": "6142629544722432",
   "score": "1588714",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "<insert_name>",
   "teamId": "4882364605923328",
   "score": "1588701",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "tutOriel",
   "teamId": "4756744597143552",
   "score": "1586731",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "hc2000",
   "teamId": "6554664145256448",
   "score": "1584995",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Gildas2000",
   "teamId": "5326078415470592",
   "score": "1584833",
   "hubId": "5735750448447488",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Nowy Obóz",
   "teamId": "6146450455003136",
   "score": "1583776",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "UniKorn",
   "teamId": "5066680174641152",
   "score": "1583466",
   "hubId": "6400147932053504",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Robburned",
   "teamId": "6609913732136960",
   "score": "1582956",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "5a5ab762b85ad4c1b941b7d2cc01a6bc61c932cf5f69315e059e18e7a597d6f8",
   "teamId": "4666153804759040",
   "score": "1581725",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "Bi-Kernel Laplacien Triphasé",
   "teamId": "4552469174550528",
   "score": "1581065",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Woteva",
   "teamId": "5007133338763264",
   "score": "1580526",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "Belgium"
   ]
  },
  {
   "teamName": "XRAY",
   "teamId": "5219057225695232",
   "score": "1578770",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "irc.love",
   "teamId": "6712345145376768",
   "score": "1574245",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "HTAG",
   "teamId": "5960667685191680",
   "score": "1573219",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NPcompete",
   "teamId": "5362042391232512",
   "score": "1572362",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "EMMA",
   "teamId": "4883157228716032",
   "score": "1570583",
   "hubId": "5165170082971648",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Okay Google",
   "teamId": "4552021759754240",
   "score": "1570147",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "OverRage",
   "teamId": "4584162879078400",
   "score": "1569678",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Giants",
   "teamId": "5125436132556800",
   "score": "1565233",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Get-schwifty",
   "teamId": "5700211137576960",
   "score": "1564387",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "picaron",
   "teamId": "5830503064141824",
   "score": "1563829",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "dashdashhelp",
   "teamId": "5004172227248128",
   "score": "1560561",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Sabanci University",
   "teamId": "4953216533921792",
   "score": "1556916",
   "hubId": "5080306965020672",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "#comisia",
   "teamId": "4784941795639296",
   "score": "1556746",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "IndianFoodGermanBeer",
   "teamId": "6669438757634048",
   "score": "1556680",
   "hubId": "6711077593153536",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Trigonometry",
   "teamId": "5087002282164224",
   "score": "1556563",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Eccentric Raccoons++",
   "teamId": "6658256206299136",
   "score": "1550409",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "Jeronimo",
   "teamId": "5409062015467520",
   "score": "1549530",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "RGUCode",
   "teamId": "4658039806230528",
   "score": "1549059",
   "hubId": "6358233077776384",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Route 2 Success",
   "teamId": "4767998686527488",
   "score": "1548414",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Mito",
   "teamId": "6471245344276480",
   "score": "1547796",
   "hubId": "5547296812957696",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Stupid Robots",
   "teamId": "6413628089565184",
   "score": "1547079",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "DijkstraNonVaASinikstra",
   "teamId": "5750685660348416",
   "score": "1546381",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "HashDose",
   "teamId": "5435873885683712",
   "score": "1544059",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "{\"members\":[\"Marco\",\"Marco\",\"Luca\"],\"size\":3,\"name\":\"A Team\"}",
   "teamId": "6355640863686656",
   "score": "1542250",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "std::lag",
   "teamId": "6434468277518336",
   "score": "1539885",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "SSQZ",
   "teamId": "6732579071852544",
   "score": "1538891",
   "hubId": "4651937261682688",
   "countries": [
    "Qatar",
    "Qatar",
    "Qatar",
    "Qatar"
   ]
  },
  {
   "teamName": "JustStarting",
   "teamId": "6718288306372608",
   "score": "1537824",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "DataScienceIstanbul",
   "teamId": "5097508577476608",
   "score": "1536624",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "The TeraFlops",
   "teamId": "5127936071958528",
   "score": "1535529",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CAD team",
   "teamId": "5422191797600256",
   "score": "1534788",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Les Bûcherons",
   "teamId": "5409908124024832",
   "score": "1534671",
   "hubId": "4762512469786624",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rubber Duck Pythoon",
   "teamId": "6613363664617472",
   "score": "1534159",
   "hubId": "5381469333618688",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "EASYPEASYLEMONSQUEEZY",
   "teamId": "6198653098131456",
   "score": "1533991",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Hirando",
   "teamId": "4884103530807296",
   "score": "1533538",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "MettatO(n)",
   "teamId": "6220412610412544",
   "score": "1529587",
   "hubId": "6125008703193088",
   "countries": [
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "A komanda",
   "teamId": "5728815686877184",
   "score": "1529463",
   "hubId": "5803282098290688",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "LambdaUC3M",
   "teamId": "5646405666340864",
   "score": "1528177",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "AVA",
   "teamId": "6011700419493888",
   "score": "1527697",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Orion",
   "teamId": "6179522307162112",
   "score": "1526251",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "DeathSeekers",
   "teamId": "5148062758469632",
   "score": "1525191",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "InfoCoders",
   "teamId": "4620921021136896",
   "score": "1523311",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "Limbo",
   "teamId": "4619002580041728",
   "score": "1523189",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "#TODO",
   "teamId": "5192864434749440",
   "score": "1522086",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "HashCoffee",
   "teamId": "6031190981083136",
   "score": "1520194",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Good horse",
   "teamId": "5286968174837760",
   "score": "1519024",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "steluta",
   "teamId": "6087877033197568",
   "score": "1517934",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Cuir Moustache",
   "teamId": "6027595623694336",
   "score": "1517109",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Cydonia",
   "teamId": "6275551601885184",
   "score": "1513055",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Datamatikerna",
   "teamId": "6055262930599936",
   "score": "1511103",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Capybaras",
   "teamId": "6023405547552768",
   "score": "1510607",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Narcos",
   "teamId": "6462199539171328",
   "score": "1508428",
   "hubId": "5405339956543488",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Simple, clair, précis",
   "teamId": "5863346142183424",
   "score": "1507992",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "flaming-epsilon",
   "teamId": "6470934496018432",
   "score": "1507146",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "∞",
   "teamId": "4948856068374528",
   "score": "1506108",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Foobar",
   "teamId": "5301004396396544",
   "score": "1505446",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Russia"
   ]
  },
  {
   "teamName": "Nuclear Power",
   "teamId": "4866102450454528",
   "score": "1502389",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "ZAL",
   "teamId": "5727270236848128",
   "score": "1501780",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Too young, sometimes naïve",
   "teamId": "4989362173378560",
   "score": "1500592",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Rhodium",
   "teamId": "5189257467527168",
   "score": "1499588",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Ezio & Da Vinci",
   "teamId": "6639108503896064",
   "score": "1499102",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Team Avatar",
   "teamId": "6263762185093120",
   "score": "1497859",
   "hubId": "4842390003122176",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Gogole challenge",
   "teamId": "6064381750149120",
   "score": "1497316",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SWAT",
   "teamId": "5647201845903360",
   "score": "1496109",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "BetaGO",
   "teamId": "5304875235672064",
   "score": "1495380",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Zeferinos",
   "teamId": "6299401018408960",
   "score": "1491344",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "AloneInThePark",
   "teamId": "4808118580019200",
   "score": "1490272",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Wreck-It Wrabbits",
   "teamId": "6137190237077504",
   "score": "1489747",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Souvlijies",
   "teamId": "6327142212173824",
   "score": "1485155",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "Patalie Nortman",
   "teamId": "6593584467804160",
   "score": "1485148",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "icarus",
   "teamId": "6159224560156672",
   "score": "1484460",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy",
    "Switzerland"
   ]
  },
  {
   "teamName": "Max Flow",
   "teamId": "5309617953308672",
   "score": "1483202",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Moomin",
   "teamId": "4707643188838400",
   "score": "1481436",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Czech Republic"
   ]
  },
  {
   "teamName": "Tea'm or coffee ?",
   "teamId": "4902625912815616",
   "score": "1479163",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Echipa",
   "teamId": "5711609175474176",
   "score": "1477144",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Oxford",
   "teamId": "6602075953692672",
   "score": "1476824",
   "hubId": "5107179300323328",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Poland",
    "United Kingdom"
   ]
  },
  {
   "teamName": "StackAlaaf",
   "teamId": "5073685870280704",
   "score": "1475297",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "NaN Myth",
   "teamId": "6207865601654784",
   "score": "1474624",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "forty two",
   "teamId": "6257688094703616",
   "score": "1474335",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "I $ BILKENT",
   "teamId": "5631800898486272",
   "score": "1473746",
   "hubId": "4842390003122176",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "The Thagomizers",
   "teamId": "4830702793129984",
   "score": "1473388",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark",
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "We will make code great again!",
   "teamId": "5403189520105472",
   "score": "1472442",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Exact and clear",
   "teamId": "6412884791787520",
   "score": "1472089",
   "hubId": "5137258231365632",
   "countries": [
    "Uganda",
    "Uganda",
    "Uganda"
   ]
  },
  {
   "teamName": "HiPay'HP",
   "teamId": "5394162572591104",
   "score": "1472069",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Vulcan",
   "teamId": "6612608085917696",
   "score": "1469382",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "SadTransistors",
   "teamId": "5631350732226560",
   "score": "1468814",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "best team",
   "teamId": "6617522468028416",
   "score": "1466898",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Flying raccoons",
   "teamId": "4541343128879104",
   "score": "1466187",
   "hubId": "5500468516093952",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Fjållberget",
   "teamId": "5529398207840256",
   "score": "1464520",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Bacon",
   "teamId": "5474251029086208",
   "score": "1463809",
   "hubId": "6125008703193088",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "Try Or Catch",
   "teamId": "5239868758163456",
   "score": "1461844",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "ChuCode",
   "teamId": "5944464048652288",
   "score": "1461444",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Que Du Sale",
   "teamId": "6606655395463168",
   "score": "1461062",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Avocado",
   "teamId": "5625644129976320",
   "score": "1461030",
   "hubId": "5042625404993536",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "ATeamHasNoName",
   "teamId": "5167613449601024",
   "score": "1456896",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "N/A",
   "teamId": "5175059312279552",
   "score": "1455905",
   "hubId": "5728758644342784",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "BZU codebro",
   "teamId": "5753698579906560",
   "score": "1449244",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Wacky Wabbits",
   "teamId": "6289259526881280",
   "score": "1448737",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "piletina",
   "teamId": "4507267864985600",
   "score": "1447541",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Datapocalypse",
   "teamId": "5059080230010880",
   "score": "1447021",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "@memo#2498F1",
   "teamId": "5683674506854400",
   "score": "1446565",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "SUPINFO",
   "teamId": "6298701140066304",
   "score": "1445125",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Les Seb's",
   "teamId": "4906678684221440",
   "score": "1444723",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Coda Masters",
   "teamId": "5009419066671104",
   "score": "1444579",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "HashMates",
   "teamId": "6360501424488448",
   "score": "1444225",
   "hubId": "5426936595611648",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Gruppo Abeliano",
   "teamId": "4805185855553536",
   "score": "1442035",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "PZKS Team",
   "teamId": "4543706099089408",
   "score": "1440027",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "ElliEinhorn",
   "teamId": "5821493497823232",
   "score": "1439495",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "WALUIGI TIME",
   "teamId": "5758882068561920",
   "score": "1439067",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "git blame",
   "teamId": "5818474404249600",
   "score": "1438654",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "yarg",
   "teamId": "5135882835197952",
   "score": "1435188",
   "hubId": "5644916856193024",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "The Defenders of Eboracia",
   "teamId": "5724978066489344",
   "score": "1431642",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "MicroTeam",
   "teamId": "6405854131650560",
   "score": "1430332",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Oberon4Lyef",
   "teamId": "4619523680370688",
   "score": "1429127",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Romania",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Exponential coders",
   "teamId": "5046956275531776",
   "score": "1426448",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "The unnamed team",
   "teamId": "4958769054220288",
   "score": "1426008",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "temporal",
   "teamId": "6546175075287040",
   "score": "1425959",
   "hubId": "5452279385686016",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "BUNO",
   "teamId": "5090517243133952",
   "score": "1424091",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "Fourier Cat",
   "teamId": "5794707128975360",
   "score": "1422622",
   "hubId": "6523840171606016",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Coding Gamers",
   "teamId": "6167403452956672",
   "score": "1421023",
   "hubId": "0",
   "countries": [
    "Togo",
    "Togo",
    "Togo"
   ]
  },
  {
   "teamName": "EPITECH Toulouse Pedago",
   "teamId": "6006770401017856",
   "score": "1419406",
   "hubId": "6390278634078208",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "CubeOfPi",
   "teamId": "5659899648278528",
   "score": "1419299",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Z-combinator",
   "teamId": "6210115023667200",
   "score": "1416144",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "AI@UoM",
   "teamId": "5092380923396096",
   "score": "1416030",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Germany"
   ]
  },
  {
   "teamName": "Team Burton",
   "teamId": "4520220949479424",
   "score": "1414053",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "54 55 4D",
   "teamId": "6666512744054784",
   "score": "1413037",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "JJM",
   "teamId": "5029254030950400",
   "score": "1412440",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Team <div>",
   "teamId": "5247523195191296",
   "score": "1411286",
   "hubId": "6158895055634432",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Brainstorm",
   "teamId": "5122829288734720",
   "score": "1411098",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "old bridge",
   "teamId": "6466102120939520",
   "score": "1410956",
   "hubId": "5500468516093952",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Axxes Team 1",
   "teamId": "4544507647361024",
   "score": "1408672",
   "hubId": "5117366962749440",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Replug",
   "teamId": "6432503128653824",
   "score": "1408408",
   "hubId": "6265377361231872",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Genesys",
   "teamId": "5897180820799488",
   "score": "1408408",
   "hubId": "6265377361231872",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "nucleus",
   "teamId": "5401797950701568",
   "score": "1408408",
   "hubId": "6265377361231872",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Loading...",
   "teamId": "6603383167254528",
   "score": "1407047",
   "hubId": "6323578999930880",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "CodeXfrr",
   "teamId": "6679826068930560",
   "score": "1406473",
   "hubId": "5088095686885376",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "BDJ",
   "teamId": "4540487557971968",
   "score": "1406191",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "WEST",
   "teamId": "4602704991092736",
   "score": "1405007",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "LU Team Caterpillar",
   "teamId": "5403756455788544",
   "score": "1401235",
   "hubId": "6265377361231872",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "UWr Pieprzu",
   "teamId": "6139924252196864",
   "score": "1400746",
   "hubId": "4594856005468160",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Next Level",
   "teamId": "5192495000453120",
   "score": "1397383",
   "hubId": "0",
   "countries": [
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "hasm65536",
   "teamId": "5944529010032640",
   "score": "1397258",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "ROP++",
   "teamId": "5214507781586944",
   "score": "1395379",
   "hubId": "0",
   "countries": [
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "coding_monkeys",
   "teamId": "5556868013359104",
   "score": "1394740",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "TAB",
   "teamId": "6492994790227968",
   "score": "1394243",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "BKJXZ",
   "teamId": "6358595331424256",
   "score": "1394061",
   "hubId": "4530579538182144",
   "countries": [
    "Ghana",
    "Ghana"
   ]
  },
  {
   "teamName": "GDG Braga",
   "teamId": "6433510566920192",
   "score": "1391486",
   "hubId": "6224891120451584",
   "countries": [
    "Poland",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Forge",
   "teamId": "5974705450254336",
   "score": "1387809",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Kuaternion",
   "teamId": "5090842855342080",
   "score": "1387724",
   "hubId": "0",
   "countries": [
    "Italy",
    "Switzerland",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Team MaiLøv",
   "teamId": "6629325306593280",
   "score": "1385909",
   "hubId": "5074919532527616",
   "countries": [
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Back to Basics",
   "teamId": "5714847580815360",
   "score": "1385655",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "ValueError",
   "teamId": "4555560544370688",
   "score": "1385437",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "in memoriam Lorin Fortuna",
   "teamId": "6012036500684800",
   "score": "1382635",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Tsimpo",
   "teamId": "5195562143973376",
   "score": "1382085",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Joint Venture",
   "teamId": "4722913408188416",
   "score": "1379001",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "LLI/\\AHr",
   "teamId": "5739004087500800",
   "score": "1378106",
   "hubId": "6565180842442752",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "The Thirty Five",
   "teamId": "4857554928664576",
   "score": "1377472",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "23",
   "teamId": "5877011654377472",
   "score": "1375154",
   "hubId": "4950858194223104",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "insightful",
   "teamId": "6609001588457472",
   "score": "1373711",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "CAPZLOCK_CREW",
   "teamId": "4682134774087680",
   "score": "1372858",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "4x4",
   "teamId": "4747147492720640",
   "score": "1372668",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Ido tomer ofir",
   "teamId": "5904842170040320",
   "score": "1368516",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "c++'s Avengers",
   "teamId": "4601446028804096",
   "score": "1368363",
   "hubId": "6589328624975872",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Wildcard",
   "teamId": "6704797881204736",
   "score": "1368294",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "SlumberTeam",
   "teamId": "6305816290263040",
   "score": "1366105",
   "hubId": "6310929918590976",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Unicorn",
   "teamId": "6017771288657920",
   "score": "1366004",
   "hubId": "5739578472267776",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "Spain"
   ]
  },
  {
   "teamName": "Splink Studio",
   "teamId": "5602057780199424",
   "score": "1365735",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "MehCastle U.",
   "teamId": "5038032675667968",
   "score": "1364934",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Burger Time",
   "teamId": "5348395602411520",
   "score": "1364636",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Team Olimar",
   "teamId": "5838903214866432",
   "score": "1364288",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "#FingerFood",
   "teamId": "4949958734118912",
   "score": "1358623",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "TEK2D EPITECH",
   "teamId": "5988880788488192",
   "score": "1357810",
   "hubId": "6197159053492224",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Algorithmists",
   "teamId": "6017436952297472",
   "score": "1357524",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Austria",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "; DROP TABLE \"TEAMS\";--",
   "teamId": "4935033991200768",
   "score": "1354999",
   "hubId": "5841604480860160",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "dinkskes",
   "teamId": "5353253009096704",
   "score": "1354777",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "ramiawar.com",
   "teamId": "5189731188998144",
   "score": "1353031",
   "hubId": "4917250343567360",
   "countries": [
    "Lebanon",
    "Lebanon",
    "Lebanon",
    "Lebanon"
   ]
  },
  {
   "teamName": "Sur Un Malentendu Ca Peut Marcher",
   "teamId": "6626023617593344",
   "score": "1350890",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Sailors",
   "teamId": "5761068945113088",
   "score": "1349425",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "The Penetrators",
   "teamId": "5296469514911744",
   "score": "1348113",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Botlhale Two",
   "teamId": "6742064171581440",
   "score": "1346562",
   "hubId": "5325767500103680",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "DataSci",
   "teamId": "5095782873038848",
   "score": "1345107",
   "hubId": "5540597737717760",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "‮ylruC ixaM",
   "teamId": "6639588667817984",
   "score": "1343856",
   "hubId": "6522670732541952",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Los pollos hermanos",
   "teamId": "5157419680268288",
   "score": "1343349",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Roar Like Doves",
   "teamId": "6086376747433984",
   "score": "1342624",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Les Daltons",
   "teamId": "5074540971425792",
   "score": "1342399",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Minamisenju",
   "teamId": "4856664863801344",
   "score": "1340739",
   "hubId": "4873656224186368",
   "countries": [
    "Italy",
    "Iceland",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Steakfault",
   "teamId": "5719380180598784",
   "score": "1340187",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Demain",
   "teamId": "6252557957595136",
   "score": "1339661",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Technische dienst lijn 23",
   "teamId": "6502470293389312",
   "score": "1337597",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CocopalmFamily",
   "teamId": "5808502563930112",
   "score": "1337466",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "TimeOut",
   "teamId": "4854029632929792",
   "score": "1337300",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Netherlands",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Noica",
   "teamId": "6215699823329280",
   "score": "1335986",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "UBB Fruntea",
   "teamId": "6434213599379456",
   "score": "1335314",
   "hubId": "5781331527073792",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "ComplexIT",
   "teamId": "6443711718227968",
   "score": "1335164",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Hello world",
   "teamId": "6173459155517440",
   "score": "1334946",
   "hubId": "0",
   "countries": [
    "France",
    "Ukraine",
    "France"
   ]
  },
  {
   "teamName": "Name of Team",
   "teamId": "5466327082860544",
   "score": "1333734",
   "hubId": "0",
   "countries": [
    "Austria",
    "Iran",
    "Iran"
   ]
  },
  {
   "teamName": "JediTeam",
   "teamId": "4515240733573120",
   "score": "1331409",
   "hubId": "5481129956081664",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "LASER",
   "teamId": "5855270999687168",
   "score": "1331236",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "A-team",
   "teamId": "5658961265033216",
   "score": "1330613",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "AK-RGU",
   "teamId": "6723606885171200",
   "score": "1329678",
   "hubId": "6358233077776384",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Tenacious C++",
   "teamId": "5223881547710464",
   "score": "1327789",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Cyber Hash",
   "teamId": "5127228476096512",
   "score": "1327778",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Jinkie Jie",
   "teamId": "4575709511024640",
   "score": "1326296",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "WEBdeBS",
   "teamId": "6739596712869888",
   "score": "1325699",
   "hubId": "4954063850438656",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "duiemragnea",
   "teamId": "6184307102056448",
   "score": "1324278",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Andromeda",
   "teamId": "4810492019212288",
   "score": "1324215",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Admin",
   "teamId": "6481705401581568",
   "score": "1323892",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Explosive kittens",
   "teamId": "4662178745417728",
   "score": "1323869",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Macedonia",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "ByteMe",
   "teamId": "6253614787985408",
   "score": "1320698",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Semicolon",
   "teamId": "4959773875240960",
   "score": "1320109",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Consensus Tchue",
   "teamId": "6216056574050304",
   "score": "1317956",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "R5D5",
   "teamId": "4662126668939264",
   "score": "1312330",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "DRADN",
   "teamId": "6564450966437888",
   "score": "1311491",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Heracles",
   "teamId": "4880848750903296",
   "score": "1310781",
   "hubId": "5540597737717760",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "M&M",
   "teamId": "5344227605086208",
   "score": "1308912",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "INSA Lyon 2",
   "teamId": "5782007179116544",
   "score": "1306180",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "V@loar3",
   "teamId": "5501967526789120",
   "score": "1305388",
   "hubId": "4629206549921792",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Żółć",
   "teamId": "6393186796699648",
   "score": "1302611",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "KETON",
   "teamId": "5051929579225088",
   "score": "1302277",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "(╯°□°）╯ ︵ ǝpoɔ ɥsɐɥ",
   "teamId": "4550781252403200",
   "score": "1301341",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "🇷🇪N🇩🇪RB🇺🇬",
   "teamId": "5160010082418688",
   "score": "1300080",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Bing Boys",
   "teamId": "5191093297610752",
   "score": "1299058",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "#code-spartans.reply",
   "teamId": "4863706731118592",
   "score": "1298247",
   "hubId": "5699128336056320",
   "countries": [
    "Italy",
    "United Kingdom",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Gollum's Cult",
   "teamId": "6607192601919488",
   "score": "1297352",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "5-28",
   "teamId": "6431976995160064",
   "score": "1297202",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "The Skyrmions",
   "teamId": "6641855940788224",
   "score": "1296476",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Omnom beginz",
   "teamId": "5636456710144000",
   "score": "1292094",
   "hubId": "4594856005468160",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "no.js",
   "teamId": "4824923981742080",
   "score": "1291766",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Corazzata Potëmkin",
   "teamId": "6550115640672256",
   "score": "1291175",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "MBARUZZELLI",
   "teamId": "5321527494967296",
   "score": "1290658",
   "hubId": "4852035560144896",
   "countries": [
    "Italy",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "straighTeam",
   "teamId": "5885862508232704",
   "score": "1287789",
   "hubId": "4671317026537472",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Totally Girlcoders",
   "teamId": "6352738606645248",
   "score": "1287383",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "whatever",
   "teamId": "6151973313183744",
   "score": "1286116",
   "hubId": "5659826029854720",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Cable Monkeys",
   "teamId": "6691963445182464",
   "score": "1286074",
   "hubId": "6358233077776384",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Hashslingingslashers",
   "teamId": "4761188009246720",
   "score": "1282086",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "chuchughezii",
   "teamId": "6286688452083712",
   "score": "1280429",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Elision1",
   "teamId": "6250294509830144",
   "score": "1277529",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "025",
   "teamId": "5169361299963904",
   "score": "1276161",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "tRipleY",
   "teamId": "4587173852479488",
   "score": "1274265",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Dat'Ass",
   "teamId": "5731068866985984",
   "score": "1274012",
   "hubId": "4685852605153280",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Plebs",
   "teamId": "6451104095141888",
   "score": "1271286",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Holy See",
    "Romania"
   ]
  },
  {
   "teamName": "Look at my Python (skills)",
   "teamId": "4679132994600960",
   "score": "1270762",
   "hubId": "5165170082971648",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Impôssible",
   "teamId": "4955793715625984",
   "score": "1268975",
   "hubId": "5218381573652480",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The ElectroSorcerers",
   "teamId": "6608245338669056",
   "score": "1266213",
   "hubId": "4775163228848128",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "BinaryHawks",
   "teamId": "5218418684854272",
   "score": "1265572",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rocket",
   "teamId": "4845575728005120",
   "score": "1264850",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "// TODO: Choose teamname",
   "teamId": "5169210640564224",
   "score": "1262698",
   "hubId": "6440138506764288",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Matic Oskar Hajšen in Koda modrosti",
   "teamId": "5950076832710656",
   "score": "1260114",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "LazyHaus",
   "teamId": "6485865345843200",
   "score": "1257170",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "D4W",
   "teamId": "5909939021152256",
   "score": "1256982",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "UC",
   "teamId": "4894178651668480",
   "score": "1256689",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "PoliMagia",
   "teamId": "6289035114840064",
   "score": "1256261",
   "hubId": "5690886025379840",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "TomAaLe",
   "teamId": "5021106209554432",
   "score": "1253978",
   "hubId": "0",
   "countries": [
    "Austria",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "uCode",
   "teamId": "5135938401337344",
   "score": "1253143",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Mantua Me Genuit",
   "teamId": "5883124667908096",
   "score": "1252060",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "#mangoicani",
   "teamId": "6407965108076544",
   "score": "1249089",
   "hubId": "0",
   "countries": [
    "Italy",
    "Switzerland",
    "Germany"
   ]
  },
  {
   "teamName": "p03pch1n33s",
   "teamId": "5546510229962752",
   "score": "1247479",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Team Psyduck",
   "teamId": "4749889560903680",
   "score": "1247280",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Anchors",
   "teamId": "4671985497931776",
   "score": "1246168",
   "hubId": "4643428797251584",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Tahia Blaise",
   "teamId": "6713066699882496",
   "score": "1244013",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hellebore Technologies",
   "teamId": "4615853832142848",
   "score": "1243696",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Goudale",
   "teamId": "5521683641270272",
   "score": "1243207",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "HornHub",
   "teamId": "6492496842457088",
   "score": "1242613",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "NinjaPirateRockstar",
   "teamId": "4824147397967872",
   "score": "1240069",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "LookingForInternship",
   "teamId": "6755011887366144",
   "score": "1239905",
   "hubId": "6504443965079552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "CompilePlz",
   "teamId": "6116877994557440",
   "score": "1238578",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Transistor Tank",
   "teamId": "6335415929798656",
   "score": "1234757",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Potatoes",
   "teamId": "5939341561954304",
   "score": "1230577",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "git stash my hash",
   "teamId": "4931470242086912",
   "score": "1230400",
   "hubId": "5173732637147136",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "Mr Robot",
   "teamId": "6050043001831424",
   "score": "1226101",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "KeshCode",
   "teamId": "5016071434141696",
   "score": "1226041",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "You Lost",
   "teamId": "5051255806230528",
   "score": "1223225",
   "hubId": "6404554434281472",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Derootatii",
   "teamId": "6430997742616576",
   "score": "1220400",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "now",
   "teamId": "5727143065550848",
   "score": "1219621",
   "hubId": "5666946347433984",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Egon",
   "teamId": "5105204085129216",
   "score": "1219611",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Boom!",
   "teamId": "5019660214861824",
   "score": "1216622",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "TypeScript Anonymous",
   "teamId": "5535011931422720",
   "score": "1214904",
   "hubId": "5744735251595264",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "while(False)",
   "teamId": "6485286129238016",
   "score": "1214007",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Big Electron",
   "teamId": "5424372835680256",
   "score": "1211459",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Ardent Monkey",
   "teamId": "6571642889175040",
   "score": "1211453",
   "hubId": "4615318169190400",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "SqoobaTeam",
   "teamId": "6270337712914432",
   "score": "1210780",
   "hubId": "6144857559007232",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Internet friends",
   "teamId": "6253560027152384",
   "score": "1209588",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "jajajaja-va",
   "teamId": "4711659721457664",
   "score": "1208781",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Font 16pt Coders",
   "teamId": "5761100687605760",
   "score": "1207274",
   "hubId": "6651476264878080",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "We're coolholics",
   "teamId": "5802431426330624",
   "score": "1203894",
   "hubId": "5841827282288640",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Los Techos Hermanos",
   "teamId": "5588206846214144",
   "score": "1202974",
   "hubId": "5044292523393024",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Chamallows",
   "teamId": "4660011129110528",
   "score": "1200705",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Newnode++",
   "teamId": "6379589601329152",
   "score": "1200705",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Dinglebop",
   "teamId": "5737388911362048",
   "score": "1200154",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "inDev Team",
   "teamId": "5411116419121152",
   "score": "1199119",
   "hubId": "6565180842442752",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Creative Cactus Curry",
   "teamId": "5993821812817920",
   "score": "1198495",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "404 team not found",
   "teamId": "6602937027526656",
   "score": "1191834",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "les singes salés",
   "teamId": "6323983532163072",
   "score": "1191289",
   "hubId": "4674291962478592",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "chiga",
   "teamId": "5476463205679104",
   "score": "1189589",
   "hubId": "4543895413194752",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Midvel",
   "teamId": "6231361757118464",
   "score": "1188767",
   "hubId": "6565180842442752",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "VanVan",
   "teamId": "5263285523841024",
   "score": "1186320",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Trollstars",
   "teamId": "5896070101991424",
   "score": "1184108",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Estonia",
    "Estonia"
   ]
  },
  {
   "teamName": "In JS We Trust",
   "teamId": "5179843972956160",
   "score": "1183657",
   "hubId": "4602220129550336",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "[\"Hip\", \"Hip\"]",
   "teamId": "4912758747299840",
   "score": "1179102",
   "hubId": "6029454941880320",
   "countries": [
    "Ireland",
    "Italy",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "moabyte",
   "teamId": "4880944783687680",
   "score": "1175444",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "perfectials",
   "teamId": "5423284262797312",
   "score": "1174312",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "HackStreet Boyz",
   "teamId": "6544730288553984",
   "score": "1172385",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Bug Life",
   "teamId": "5591998631247872",
   "score": "1167875",
   "hubId": "5452279385686016",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "BonsoirHashCode",
   "teamId": "5778444570853376",
   "score": "1165043",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hack Street Boys",
   "teamId": "5802735630811136",
   "score": "1163884",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "R&M_challenge",
   "teamId": "6360167826325504",
   "score": "1163650",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Mfk",
   "teamId": "5206634636771328",
   "score": "1163650",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "50 nuances - Fourmis - Paquito",
   "teamId": "6428080654516224",
   "score": "1163650",
   "hubId": "6390278634078208",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Three Amigos",
   "teamId": "4652239452897280",
   "score": "1163650",
   "hubId": "5654907889647616",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "SuperDuperTeam",
   "teamId": "5733309296410624",
   "score": "1163650",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "DKLW",
   "teamId": "5483039404589056",
   "score": "1163650",
   "hubId": "5661462143959040",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Anaptixis",
   "teamId": "6681622908764160",
   "score": "1163307",
   "hubId": "6651476264878080",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Nick's Sweet Beard",
   "teamId": "4886273764360192",
   "score": "1163307",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "lancelot",
   "teamId": "4781432874467328",
   "score": "1163307",
   "hubId": "0",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Kenya",
    "Nigeria"
   ]
  },
  {
   "teamName": "69 lemputės",
   "teamId": "6519083965087744",
   "score": "1163307",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "J.A.R.V.I.S.",
   "teamId": "6000156956688384",
   "score": "1163307",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "TensorFriends",
   "teamId": "5215189406318592",
   "score": "1162046",
   "hubId": "5426936595611648",
   "countries": [
    "Hungary",
    "Slovakia",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Hanzo",
   "teamId": "6273477334007808",
   "score": "1159892",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "SDGE17",
   "teamId": "5312876491309056",
   "score": "1159666",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "Russia",
    "France",
    "Russia"
   ]
  },
  {
   "teamName": "Zeppelin-VP",
   "teamId": "5815514903347200",
   "score": "1153828",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team Azure",
   "teamId": "6662289516134400",
   "score": "1152000",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Imagination",
   "teamId": "5011738952990720",
   "score": "1151501",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "INTeam",
   "teamId": "5693685471641600",
   "score": "1149679",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team CARL",
   "teamId": "5205232531275776",
   "score": "1149591",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Italy",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Atomówki",
   "teamId": "4648617654616064",
   "score": "1147267",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Hunta",
   "teamId": "4602004374552576",
   "score": "1143178",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Polytechnique ALPHA",
   "teamId": "6014264850513920",
   "score": "1138551",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Ohne mein Team",
   "teamId": "5496693441167360",
   "score": "1138219",
   "hubId": "0",
   "countries": [
    "Germany",
    "Ghana"
   ]
  },
  {
   "teamName": "PixelCan",
   "teamId": "4685896964112384",
   "score": "1136877",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Jo & Hayut & Ariel",
   "teamId": "5135345494523904",
   "score": "1136316",
   "hubId": "5841827282288640",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "PA Team",
   "teamId": "6094203587133440",
   "score": "1136303",
   "hubId": "5645240186699776",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "BaBarth",
   "teamId": "6681175292641280",
   "score": "1136203",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "C-Team",
   "teamId": "6717433876316160",
   "score": "1134064",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Arkan",
   "teamId": "5096949694857216",
   "score": "1132201",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Manchester",
   "teamId": "5173282873540608",
   "score": "1131633",
   "hubId": "5739578472267776",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "VirtualVagrants",
   "teamId": "5488835395846144",
   "score": "1131462",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "HashCookie",
   "teamId": "5414021427625984",
   "score": "1126724",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Taoist",
   "teamId": "5459494930743296",
   "score": "1123002",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "#AltaIntrebare?",
   "teamId": "6192450427158528",
   "score": "1121163",
   "hubId": "4629206549921792",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Bits please",
   "teamId": "6626866504925184",
   "score": "1120600",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CirelBross",
   "teamId": "5021495709401088",
   "score": "1117992",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TOP55",
   "teamId": "4703991594221568",
   "score": "1110687",
   "hubId": "6026378671554560",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "StarLord",
   "teamId": "5878307325214720",
   "score": "1109094",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "We will choose team name tomorrow",
   "teamId": "4808425670180864",
   "score": "1108787",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "NewFolder",
   "teamId": "6631256431263744",
   "score": "1106840",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Singles In Your Area",
   "teamId": "5167320318083072",
   "score": "1106170",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "MOCERUE",
   "teamId": "6297262661566464",
   "score": "1105751",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Dragulici",
   "teamId": "4903948091654144",
   "score": "1105748",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Hashmeisters",
   "teamId": "6714298080428032",
   "score": "1105202",
   "hubId": "5931430634848256",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Einzigste",
   "teamId": "5907239835533312",
   "score": "1101866",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Normal Ones",
   "teamId": "6498888760426496",
   "score": "1098954",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Floki",
   "teamId": "6087840324648960",
   "score": "1098812",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "101010",
   "teamId": "4585738528096256",
   "score": "1098350",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "LegendaryFellows",
   "teamId": "5140772655464448",
   "score": "1088381",
   "hubId": "0",
   "countries": [
    "Finland",
    "Finland",
    "Finland",
    "Finland"
   ]
  },
  {
   "teamName": "Boo",
   "teamId": "4824290742501376",
   "score": "1088083",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "WDCteam",
   "teamId": "6146605677805568",
   "score": "1084234",
   "hubId": "5745582165458944",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Dynamic Duo",
   "teamId": "6048585061761024",
   "score": "1084033",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "RAR",
   "teamId": "4817148211888128",
   "score": "1081876",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Dreamteam",
   "teamId": "5613521316347904",
   "score": "1079649",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "crash",
   "teamId": "5735520869023744",
   "score": "1079603",
   "hubId": "4883695106260992",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hiding under your sink",
   "teamId": "5698124924321792",
   "score": "1074068",
   "hubId": "0",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Soomaney Squad",
   "teamId": "5326206996054016",
   "score": "1074065",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "T-Coders",
   "teamId": "6200654552891392",
   "score": "1073806",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "BCrypters",
   "teamId": "6229172867301376",
   "score": "1070979",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Hash-toow",
   "teamId": "5996007749844992",
   "score": "1070873",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "Risotto",
   "teamId": "5552491106140160",
   "score": "1068220",
   "hubId": "5199323260256256",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Olaf",
   "teamId": "5152509391798272",
   "score": "1067710",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "HashGirls",
   "teamId": "6487429519245312",
   "score": "1066382",
   "hubId": "0",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "IllegalArgumentException",
   "teamId": "6142646993027072",
   "score": "1066068",
   "hubId": "0",
   "countries": [
    "France",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Space Hippies",
   "teamId": "4892890161479680",
   "score": "1065575",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "RIPDB'); DROP TABLE Teams;",
   "teamId": "4986998532079616",
   "score": "1065091",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Zynertia",
   "teamId": "6625922148990976",
   "score": "1064772",
   "hubId": "5405339956543488",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Pango",
   "teamId": "4822218890543104",
   "score": "1063230",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Pork Solvers",
   "teamId": "6555702587817984",
   "score": "1061871",
   "hubId": "4747890253627392",
   "countries": [
    "Italy",
    "Ireland",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "WhatTheHash",
   "teamId": "5966790429507584",
   "score": "1060809",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Les sombres",
   "teamId": "4845753499385856",
   "score": "1059537",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Blockchain Boys 4 Liberty",
   "teamId": "6199756703399936",
   "score": "1058564",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Angry Beavers",
   "teamId": "5801389896761344",
   "score": "1057615",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Bytes the dust",
   "teamId": "5695042949742592",
   "score": "1057068",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Null Pointer Exception",
   "teamId": "6379855218212864",
   "score": "1056819",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Code Artisans",
   "teamId": "5166442332815360",
   "score": "1055574",
   "hubId": "5083772265431040",
   "countries": [
    "Morocco",
    "Morocco",
    "Morocco"
   ]
  },
  {
   "teamName": "Funny team name",
   "teamId": "5285238980739072",
   "score": "1055008",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "FooWalksIntoaBar",
   "teamId": "6193927627472896",
   "score": "1054550",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Jakabol",
   "teamId": "5362542419378176",
   "score": "1054548",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Black Profit",
   "teamId": "5840297401516032",
   "score": "1053870",
   "hubId": "0",
   "countries": [
    "Norway",
    "Norway",
    "Switzerland"
   ]
  },
  {
   "teamName": "Utcnan",
   "teamId": "6343039429640192",
   "score": "1051507",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Beauty&TheBeAsT",
   "teamId": "6319241888268288",
   "score": "1051477",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Kat&Rene",
   "teamId": "4577519302868992",
   "score": "1050345",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "We make the best team names. Everyone says so.",
   "teamId": "6613323332190208",
   "score": "1050306",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Better than Avengers",
   "teamId": "6176890297516032",
   "score": "1046883",
   "hubId": "5173732637147136",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "Beyin takımı",
   "teamId": "5565048047009792",
   "score": "1046682",
   "hubId": "5112178910691328",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "KSPU_NotFound",
   "teamId": "6291478414360576",
   "score": "1042024",
   "hubId": "5278654527438848",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Hashbrowns",
   "teamId": "4881331464962048",
   "score": "1041798",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "100% win next week",
   "teamId": "5231564170461184",
   "score": "1041390",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Quattro Formaggi",
   "teamId": "5831375546482688",
   "score": "1040291",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "SuperCode",
   "teamId": "6296182678618112",
   "score": "1038936",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Peters",
   "teamId": "5057346136965120",
   "score": "1038506",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "NoC#",
   "teamId": "6032578591064064",
   "score": "1037065",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Nupoex",
   "teamId": "5294813872128000",
   "score": "1036780",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "deadc0de",
   "teamId": "6353115422916608",
   "score": "1036257",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "The B-team",
   "teamId": "5214298401931264",
   "score": "1034681",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "NoTrainingAsAlways",
   "teamId": "5911317370109952",
   "score": "1034681",
   "hubId": "5983641666584576",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Karshim",
   "teamId": "5358468374462464",
   "score": "1034681",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "The Troll Team",
   "teamId": "5623905540636672",
   "score": "1034595",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Beetroot Hunters",
   "teamId": "6250856613675008",
   "score": "1033912",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "much code such bugs",
   "teamId": "5324943470362624",
   "score": "1033078",
   "hubId": "5690886025379840",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Coding4Fun",
   "teamId": "6019484242411520",
   "score": "1032716",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "3DS",
   "teamId": "5111021081460736",
   "score": "1031732",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "LOL",
   "teamId": "4827792751460352",
   "score": "1031382",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "399",
   "teamId": "5443538925912064",
   "score": "1029919",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Seal Jobs",
   "teamId": "6246967185244160",
   "score": "1028913",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Serbia",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Les Semi-Croustillants",
   "teamId": "6176516299816960",
   "score": "1028143",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Noons",
   "teamId": "4916243576389632",
   "score": "1027718",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "RomanianCroissant🥐",
   "teamId": "5044175015772160",
   "score": "1027634",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "France",
    "France"
   ]
  },
  {
   "teamName": "python magicians",
   "teamId": "4722729999663104",
   "score": "1026319",
   "hubId": "0",
   "countries": [
    "Serbia",
    "Serbia",
    "Serbia"
   ]
  },
  {
   "teamName": "Banane In Pigiama",
   "teamId": "5553470425792512",
   "score": "1026319",
   "hubId": "6338302147821568",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Hash Every Day",
   "teamId": "6272956569223168",
   "score": "1026168",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "leberkäse",
   "teamId": "6521313388658688",
   "score": "1023875",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "The Diggers",
   "teamId": "4720528292052992",
   "score": "1023393",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Paprika",
   "teamId": "6453110046195712",
   "score": "1022975",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "#CrashCode",
   "teamId": "5534898920095744",
   "score": "1022305",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "hash innen",
   "teamId": "5312135609450496",
   "score": "1020957",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Orichalcum",
   "teamId": "6702407933231104",
   "score": "1020821",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "JURandom",
   "teamId": "6564745909895168",
   "score": "1020792",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Binary Pangolin",
   "teamId": "4545078676684800",
   "score": "1020792",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "ImperialNUS",
   "teamId": "5137225817784320",
   "score": "1020792",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "name_availability = {};",
   "teamId": "6292710801539072",
   "score": "1020792",
   "hubId": "6079963757281280",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Elitarne Koło Miłośników Teleinformatyki i Różowych Jednorożców",
   "teamId": "6578257608572928",
   "score": "1020792",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "CVUT-AIR",
   "teamId": "6246095038447616",
   "score": "1020790",
   "hubId": "6260741212471296",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic",
    "Ukraine"
   ]
  },
  {
   "teamName": "caps lock",
   "teamId": "6268908898091008",
   "score": "1020790",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "who let the dogs code",
   "teamId": "5074810480623616",
   "score": "1020714",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Curry",
   "teamId": "4576768488898560",
   "score": "1019974",
   "hubId": "6224891120451584",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Hexed",
   "teamId": "5584983875911680",
   "score": "1019756",
   "hubId": "0",
   "countries": [
    "Moldova",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Unable to unable data",
   "teamId": "5701047314022400",
   "score": "1018604",
   "hubId": "5481129956081664",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "_NOP",
   "teamId": "5500022242148352",
   "score": "1018163",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "The Arrangers",
   "teamId": "6115525415403520",
   "score": "1017778",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Goulash Code",
   "teamId": "6558957703266304",
   "score": "1015678",
   "hubId": "5165170082971648",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "The_base",
   "teamId": "5669545607954432",
   "score": "1015499",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "crack and code",
   "teamId": "5771106015248384",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Hadrumet",
   "teamId": "5985750763962368",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Sky",
   "teamId": "6672916271857664",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "TeamA",
   "teamId": "6264519911276544",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "ayoub saghrouni",
   "teamId": "5164566707175424",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "TheZeroes",
   "teamId": "5486279353434112",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "innovators",
   "teamId": "5086085038211072",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Grinta",
   "teamId": "6239632052191232",
   "score": "1014876",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Meelo Dreamteam",
   "teamId": "4968368574562304",
   "score": "1014700",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "mutate",
   "teamId": "4658354949455872",
   "score": "1014348",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Metrobus",
   "teamId": "4859513433751552",
   "score": "1013974",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "My Hobby:",
   "teamId": "6134379986288640",
   "score": "1013573",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Team Six",
   "teamId": "4735689862152192",
   "score": "1012676",
   "hubId": "5732605190209536",
   "countries": [
    "Germany",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "SoWhat",
   "teamId": "6664250235813888",
   "score": "1010772",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Team Vla2u",
   "teamId": "4887219529580544",
   "score": "1008497",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Faucille et Marteau",
   "teamId": "5148659222052864",
   "score": "1008497",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SIGKILL",
   "teamId": "5710005877604352",
   "score": "1008410",
   "hubId": "6224891120451584",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": ".hidden",
   "teamId": "5531480193236992",
   "score": "1007517",
   "hubId": "6224891120451584",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Nekem mindegy",
   "teamId": "5221005261799424",
   "score": "1005225",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Code Roipo",
   "teamId": "5397537141817344",
   "score": "1004487",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "N6-219C-GT11",
   "teamId": "6753842045648896",
   "score": "1003991",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Jamiryo",
   "teamId": "5930044836806656",
   "score": "1002867",
   "hubId": "5112178910691328",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Lemurienii",
   "teamId": "5375671664640000",
   "score": "1002867",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "VSF4Ever",
   "teamId": "4972090969030656",
   "score": "1002867",
   "hubId": "6249764886675456",
   "countries": [
    "Malta",
    "Malta",
    "Malta"
   ]
  },
  {
   "teamName": "I C my code",
   "teamId": "5701900133466112",
   "score": "1002679",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "☑ More Magic",
   "teamId": "4525883326988288",
   "score": "1002515",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "qwerty ;qsterrqce",
   "teamId": "6748281673613312",
   "score": "1002467",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "An okayish team",
   "teamId": "6061523650740224",
   "score": "1002252",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "MJC",
   "teamId": "5192799473369088",
   "score": "1001461",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "DECTRIS Tiger Team",
   "teamId": "4819870482956288",
   "score": "1001369",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "!qsln",
   "teamId": "5051570681020416",
   "score": "999685",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "steakHashE",
   "teamId": "6350279469432832",
   "score": "999384",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Tompeki",
   "teamId": "6037729062158336",
   "score": "998586",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Nadine",
   "teamId": "5598113658044416",
   "score": "998427",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SEGV",
   "teamId": "6159525677629440",
   "score": "998356",
   "hubId": "5739578472267776",
   "countries": [
    "Austria",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "This name is OK",
   "teamId": "5261980860416000",
   "score": "997757",
   "hubId": "5032995148791808",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Veus Dult",
   "teamId": "6459724094504960",
   "score": "996854",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "CodeRed",
   "teamId": "5374876491710464",
   "score": "994889",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "LNU Logycode",
   "teamId": "5358763921899520",
   "score": "994667",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "TuningMaster",
   "teamId": "5463851906629632",
   "score": "994368",
   "hubId": "5720755912310784",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "peseci",
   "teamId": "5971475634847744",
   "score": "994062",
   "hubId": "5378351053144064",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Coconut Jelly Man",
   "teamId": "6356072507899904",
   "score": "993985",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "FEWL",
   "teamId": "6552128168394752",
   "score": "993546",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "INH",
   "teamId": "5915947076419584",
   "score": "993546",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team cS",
   "teamId": "6732148165836800",
   "score": "993546",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "ktu11best",
   "teamId": "5891381205663744",
   "score": "993464",
   "hubId": "0",
   "countries": [
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Los unicornios mágicos",
   "teamId": "5207656838987776",
   "score": "993317",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Bate palma",
   "teamId": "5429222390628352",
   "score": "993296",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Think#",
   "teamId": "6180613698617344",
   "score": "993295",
   "hubId": "4892331278860288",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Collision",
   "teamId": "6218494504861696",
   "score": "993295",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Bho!",
   "teamId": "6286104537858048",
   "score": "993295",
   "hubId": "5500468516093952",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Memes",
   "teamId": "5472185418252288",
   "score": "992960",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "My Awesome Team",
   "teamId": "5268053138866176",
   "score": "992923",
   "hubId": "5751703970250752",
   "countries": [
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "Actors Anonymous",
   "teamId": "4765779866157056",
   "score": "992791",
   "hubId": "6711077593153536",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Team Red Owl",
   "teamId": "5827367670906880",
   "score": "992773",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "ToT",
   "teamId": "4804699786051584",
   "score": "990196",
   "hubId": "4775163228848128",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CalzoneDevelopers",
   "teamId": "5612104715337728",
   "score": "988256",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "HashCash",
   "teamId": "5782263803412480",
   "score": "987814",
   "hubId": "4766541551763456",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "rug beaters",
   "teamId": "6553939772178432",
   "score": "985991",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Transient Global Amnesia",
   "teamId": "6358428364570624",
   "score": "985765",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "420-code",
   "teamId": "5495912696643584",
   "score": "985307",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "FatherCitizens",
   "teamId": "4732262142705664",
   "score": "985307",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Don't Panic",
   "teamId": "4713333148090368",
   "score": "985307",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "hackANBY",
   "teamId": "5705095589134336",
   "score": "985307",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Code Monkey Crew",
   "teamId": "6503515782381568",
   "score": "985307",
   "hubId": "5630897948721152",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Jarofdidz",
   "teamId": "4706563474325504",
   "score": "985307",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Steep Dive",
   "teamId": "6543073236484096",
   "score": "985080",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "VISA",
   "teamId": "4807672977162240",
   "score": "984025",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "CyCl",
   "teamId": "5642094123155456",
   "score": "983353",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "DROP TABLES AHAHAHAHAHA!!!11!!one!!!11!!",
   "teamId": "6516170635083776",
   "score": "982849",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "ShallowLearners",
   "teamId": "6506881426128896",
   "score": "982169",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Bronenosec Potëmkin",
   "teamId": "6002582539468800",
   "score": "981151",
   "hubId": "5745582165458944",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "SnackOverflow",
   "teamId": "5891348255211520",
   "score": "980100",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Science for dummies",
   "teamId": "5208988748611584",
   "score": "977495",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Germany"
   ]
  },
  {
   "teamName": "Unicaen",
   "teamId": "6296002625536000",
   "score": "977260",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "EAGLES",
   "teamId": "4862379049353216",
   "score": "974316",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Piniata",
   "teamId": "5417093671419904",
   "score": "973606",
   "hubId": "5493471611715584",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Gergle Hersh Cerd",
   "teamId": "6222520231395328",
   "score": "973498",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "String cheese;",
   "teamId": "5075412849786880",
   "score": "973444",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Team",
   "teamId": "5032673965768704",
   "score": "972805",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "tmp42",
   "teamId": "5833966082850816",
   "score": "972536",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Suicide Squad",
   "teamId": "4566864898293760",
   "score": "971546",
   "hubId": "5540597737717760",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "#Code",
   "teamId": "5201693075570688",
   "score": "971302",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Estonia",
    "Estonia",
    "Estonia"
   ]
  },
  {
   "teamName": "CONLOBO",
   "teamId": "6378565855608832",
   "score": "971302",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "TeamDuLove",
   "teamId": "5887446747185152",
   "score": "971302",
   "hubId": "4685852605153280",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "HashSet",
   "teamId": "4777538614198272",
   "score": "971168",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Marc Doe",
   "teamId": "6368062982848512",
   "score": "969758",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Red Potato",
   "teamId": "6263189276721152",
   "score": "968422",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "EPS rules",
   "teamId": "5545669355896832",
   "score": "964928",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "git submit",
   "teamId": "6523744809910272",
   "score": "963834",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Legendary Lions",
   "teamId": "6170374026821632",
   "score": "963686",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Hashashinos",
   "teamId": "5988089642090496",
   "score": "963267",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Switzerland",
    "France",
    "Portugal"
   ]
  },
  {
   "teamName": "MInaTori",
   "teamId": "6589922538422272",
   "score": "962849",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "The Cookies",
   "teamId": "4511682621603840",
   "score": "960409",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "property of undefined",
   "teamId": "5385134752661504",
   "score": "958921",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "NISX",
   "teamId": "6242037770747904",
   "score": "957747",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Stellar Group",
   "teamId": "4827749197807616",
   "score": "957210",
   "hubId": "6733142383656960",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "The Shire",
   "teamId": "6500349049307136",
   "score": "956266",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "DEMCODE",
   "teamId": "5251174454263808",
   "score": "953915",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "HASTEGA",
   "teamId": "5308985519374336",
   "score": "953915",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Team Cucumber",
   "teamId": "5970029103284224",
   "score": "953266",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Nothing Cooler Than Absolute Zero",
   "teamId": "6368066002747392",
   "score": "952745",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "ValarMorghulis",
   "teamId": "4639845989220352",
   "score": "952644",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Googling Stack Overflow",
   "teamId": "5192030405787648",
   "score": "951977",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "ceng@booking",
   "teamId": "5095095409836032",
   "score": "951795",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Turkey"
   ]
  },
  {
   "teamName": "Hashella",
   "teamId": "5323034692943872",
   "score": "951643",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "skdgjkdsaljlskajdaskld",
   "teamId": "6678987208130560",
   "score": "949885",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Citrus",
   "teamId": "5414751572066304",
   "score": "949656",
   "hubId": "0",
   "countries": [
    "Bosnia and Herzegovina",
    "Bosnia and Herzegovina"
   ]
  },
  {
   "teamName": "Cellar Dwellers",
   "teamId": "4850084168597504",
   "score": "949481",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "HashPotatoesSr",
   "teamId": "5176993658175488",
   "score": "947979",
   "hubId": "4917250343567360",
   "countries": [
    "Lebanon",
    "Lebanon",
    "Lebanon",
    "Lebanon"
   ]
  },
  {
   "teamName": "Damn Coders",
   "teamId": "5651045640306688",
   "score": "945775",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "rrrrrrrrrrrrrrrrrrrrrrrrrrrrro",
   "teamId": "6468639574196224",
   "score": "945464",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "The Fruitbaskets",
   "teamId": "6481025723006976",
   "score": "943639",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Malacostraca",
   "teamId": "6609293042253824",
   "score": "943321",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "PornstarZanpako",
   "teamId": "5658157233733632",
   "score": "942392",
   "hubId": "4685852605153280",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "returnnull",
   "teamId": "6040134713606144",
   "score": "942035",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "FairyPatrol",
   "teamId": "4740133005819904",
   "score": "940013",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Black Horse",
   "teamId": "4879411010600960",
   "score": "938249",
   "hubId": "4643428797251584",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Ain't nobody got polynomial time fo dat",
   "teamId": "5639593042903040",
   "score": "937339",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Scarlet Guardian",
   "teamId": "6556061486022656",
   "score": "936614",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Les Dzodzets",
   "teamId": "6257224238235648",
   "score": "936388",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Mille et une lignes de code",
   "teamId": "6035298848866304",
   "score": "936293",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Poultry leg 🍗",
   "teamId": "5342665377841152",
   "score": "936293",
   "hubId": "0",
   "countries": [
    "Poland",
    "Austria",
    "Austria",
    "Poland"
   ]
  },
  {
   "teamName": "Make UAntwerpen Great Again",
   "teamId": "5396911620096000",
   "score": "936293",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "202",
   "teamId": "6519767938629632",
   "score": "936289",
   "hubId": "4552345895567360",
   "countries": [
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "DreamTeam",
   "teamId": "5845315332603904",
   "score": "936213",
   "hubId": "4594856005468160",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "normies-hedgehogs",
   "teamId": "6500510110580736",
   "score": "934467",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Squad",
   "teamId": "5029625612730368",
   "score": "933146",
   "hubId": "5128325034934272",
   "countries": [
    "Oman",
    "Oman"
   ]
  },
  {
   "teamName": "It's LUPUS !!!",
   "teamId": "5387162245660672",
   "score": "932755",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "🤓",
   "teamId": "6474267323531264",
   "score": "931734",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "#39C??kies",
   "teamId": "6329998365425664",
   "score": "928611",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Code Cleaners",
   "teamId": "6147696599498752",
   "score": "927505",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "1nf1Corp",
   "teamId": "5720369633689600",
   "score": "926848",
   "hubId": "4856442062372864",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "WashingMachines",
   "teamId": "5671018043539456",
   "score": "926432",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "localhost",
   "teamId": "4899405693976576",
   "score": "926410",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Germany"
   ]
  },
  {
   "teamName": "NIET MARGINAAL",
   "teamId": "5723698166235136",
   "score": "925973",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CYQ",
   "teamId": "4758224213377024",
   "score": "925521",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Catalysts 5",
   "teamId": "4583614935203840",
   "score": "924750",
   "hubId": "6010233621053440",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "OneDanet",
   "teamId": "5089290425991168",
   "score": "924186",
   "hubId": "5807719806140416",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "whatever works",
   "teamId": "5351692795117568",
   "score": "919553",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Poland",
    "Kenya"
   ]
  },
  {
   "teamName": "Krypton Team",
   "teamId": "5760515162767360",
   "score": "919299",
   "hubId": "6441886759780352",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "xDDDDDDDDDDDDDDDDDDDD",
   "teamId": "5472467275481088",
   "score": "919108",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "MÖBİ",
   "teamId": "6131648454197248",
   "score": "918150",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Dev Cave",
   "teamId": "5621509150212096",
   "score": "916818",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "TheBestPessimistsz",
   "teamId": "5253300530184192",
   "score": "916572",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "DAG",
   "teamId": "4867921905975296",
   "score": "916179",
   "hubId": "5423102867537920",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Partners in Crime",
   "teamId": "5097379527131136",
   "score": "915851",
   "hubId": "4954063850438656",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Rogue P2",
   "teamId": "5301135191572480",
   "score": "915633",
   "hubId": "4747093939847168",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hack and Backslash",
   "teamId": "5307547242201088",
   "score": "914062",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Fradogmi",
   "teamId": "4880054651715584",
   "score": "912389",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "A pipe named pepe",
   "teamId": "5743942561693696",
   "score": "910406",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Space Team",
   "teamId": "5291374005977088",
   "score": "907764",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "LiisGRPG",
   "teamId": "5742793926377472",
   "score": "906997",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "noa",
   "teamId": "6028297783738368",
   "score": "906997",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Codespotting",
   "teamId": "6300035599826944",
   "score": "906997",
   "hubId": "5944419287040000",
   "countries": [
    "United Kingdom",
    "Romania",
    "United Kingdom"
   ]
  },
  {
   "teamName": "aplonCode",
   "teamId": "4860151035068416",
   "score": "906997",
   "hubId": "5423102867537920",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "WildHogs",
   "teamId": "6063677643948032",
   "score": "906843",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Russia",
    "Belgium"
   ]
  },
  {
   "teamName": "LA3",
   "teamId": "5874373940477952",
   "score": "905553",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "FatPigs",
   "teamId": "4580522827186176",
   "score": "905510",
   "hubId": "6523840171606016",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "comp-utad-ores",
   "teamId": "4835675090190336",
   "score": "904169",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "SquattingSlavs",
   "teamId": "5674871367401472",
   "score": "904076",
   "hubId": "6308495074787328",
   "countries": [
    "Denmark",
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "DROP TABLE *",
   "teamId": "5768060950544384",
   "score": "903791",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Shanghai Chicken Haters",
   "teamId": "5104724189642752",
   "score": "902050",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Eitbit",
   "teamId": "5316793501483008",
   "score": "900943",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "HackURV",
   "teamId": "6228630694789120",
   "score": "900717",
   "hubId": "5405339956543488",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Letkult",
   "teamId": "4913288370454528",
   "score": "899823",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "CentOs",
   "teamId": "5429989512052736",
   "score": "899286",
   "hubId": "4805185117356032",
   "countries": [
    "France",
    "Nigeria",
    "Ukraine",
    "Nigeria"
   ]
  },
  {
   "teamName": "GrammarNazis",
   "teamId": "5946528652853248",
   "score": "898817",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "CodeShouldWorkNow",
   "teamId": "6571253657763840",
   "score": "897163",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "MM",
   "teamId": "4941488588849152",
   "score": "896233",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "TwoDanet",
   "teamId": "4720642913992704",
   "score": "895971",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TMTeam",
   "teamId": "4957645718945792",
   "score": "895872",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "b27",
   "teamId": "4770095704309760",
   "score": "895272",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "France"
   ]
  },
  {
   "teamName": "Unicorns",
   "teamId": "4789259579949056",
   "score": "893874",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "New World Makers",
   "teamId": "5338230756999168",
   "score": "893558",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "Spark Boys",
   "teamId": "4533999741435904",
   "score": "891396",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "FH* Reloaded",
   "teamId": "5556304030466048",
   "score": "890821",
   "hubId": "5630897948721152",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Germany"
   ]
  },
  {
   "teamName": "Codeborns",
   "teamId": "4790303055675392",
   "score": "889475",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "NATI CON LA CAMICIA",
   "teamId": "6555032572919808",
   "score": "889120",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "case.break",
   "teamId": "6470050470952960",
   "score": "888612",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "CubeteTeam",
   "teamId": "5125132263620608",
   "score": "888452",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "sudo rm rf",
   "teamId": "4741147154972672",
   "score": "888061",
   "hubId": "0",
   "countries": [
    "Bahrain",
    "Bahrain"
   ]
  },
  {
   "teamName": "HRYT",
   "teamId": "5469168740597760",
   "score": "887832",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Netherlands",
    "Austria"
   ]
  },
  {
   "teamName": "BIRL",
   "teamId": "5531483951333376",
   "score": "887457",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SuperGut",
   "teamId": "4815145347842048",
   "score": "886928",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "25th Bam",
   "teamId": "6705483398250496",
   "score": "885555",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "TruCode",
   "teamId": "4610856302149632",
   "score": "884371",
   "hubId": "0",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "sonne++",
   "teamId": "5438578372902912",
   "score": "884178",
   "hubId": "0",
   "countries": [
    "Macedonia",
    "Macedonia",
    "Macedonia"
   ]
  },
  {
   "teamName": "1998–99 Australian Figure Skating Champions",
   "teamId": "4884253787553792",
   "score": "883801",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "team",
   "teamId": "6006751610535936",
   "score": "882730",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "Hungary",
    "Hungary",
    "United Kingdom"
   ]
  },
  {
   "teamName": "null-2",
   "teamId": "5785346516189184",
   "score": "882585",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "RADLab",
   "teamId": "4704631275913216",
   "score": "878688",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "MariahPromises :)",
   "teamId": "4629847036919808",
   "score": "874961",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "JamminMexiCan",
   "teamId": "6480881640275968",
   "score": "874730",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Bash in Space",
   "teamId": "5782680213913600",
   "score": "873708",
   "hubId": "5202988410863616",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Everything",
   "teamId": "5138456862785536",
   "score": "872244",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Rwanda",
    "Russia",
    "Rwanda"
   ]
  },
  {
   "teamName": "Gang of Four",
   "teamId": "4803535782805504",
   "score": "871912",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Ghana",
    "Poland"
   ]
  },
  {
   "teamName": "Expecto Penalum",
   "teamId": "5979416492507136",
   "score": "870873",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "PepperoniPls?",
   "teamId": "5949716256784384",
   "score": "870737",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "IDC (Intelligent Dancing Coders)",
   "teamId": "5699865124274176",
   "score": "869969",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Coxmmunication",
   "teamId": "6695752612970496",
   "score": "869619",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Pastutatis",
   "teamId": "5450314169712640",
   "score": "868557",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "DegTeam",
   "teamId": "6273188833001472",
   "score": "864713",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "CodeRockers",
   "teamId": "5446105303089152",
   "score": "864289",
   "hubId": "5094915289645056",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "GoogLeCode",
   "teamId": "6723509375991808",
   "score": "864057",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Legends Of Tomorrow",
   "teamId": "6008537243189248",
   "score": "861785",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "banana",
   "teamId": "5459688002945024",
   "score": "860896",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "whiteXmas",
   "teamId": "5798897205116928",
   "score": "860065",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Winter Kirin",
   "teamId": "5303082959241216",
   "score": "860004",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Athens Ghetto",
   "teamId": "5828707700703232",
   "score": "857545",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Cyprus",
    "Czech Republic"
   ]
  },
  {
   "teamName": "TAD",
   "teamId": "6016373075476480",
   "score": "856906",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Original-Organization-Name",
   "teamId": "6301471997952000",
   "score": "852450",
   "hubId": "6390278634078208",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team Tof",
   "teamId": "5392538001211392",
   "score": "851978",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "And Equals",
   "teamId": "6142157165428736",
   "score": "851837",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "V4Voskoi",
   "teamId": "6447886627766272",
   "score": "849344",
   "hubId": "6002229748170752",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "PyJavaS Bananas",
   "teamId": "6290262871506944",
   "score": "848995",
   "hubId": "0",
   "countries": [
    "Slovakia",
    "Slovakia",
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "kagemaru",
   "teamId": "6651090992889856",
   "score": "848636",
   "hubId": "6308495074787328",
   "countries": [
    "Denmark",
    "Denmark",
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "R∧SΚ",
   "teamId": "4545845798109184",
   "score": "846324",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Macedonia",
    "Germany"
   ]
  },
  {
   "teamName": "Eniac",
   "teamId": "5748788291436544",
   "score": "845930",
   "hubId": "5634869988163584",
   "countries": [
    "Cyprus",
    "Iran",
    "Iran",
    "Cyprus"
   ]
  },
  {
   "teamName": "No Free Lunch",
   "teamId": "5209212892217344",
   "score": "845547",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Embrace the Bugs",
   "teamId": "6061561835683840",
   "score": "845517",
   "hubId": "4892331278860288",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Gyrating Flibbittygibbitts",
   "teamId": "6577920185204736",
   "score": "844615",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Nifflers",
   "teamId": "5194879512608768",
   "score": "842899",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "WAHTWIT",
   "teamId": "5982084204068864",
   "score": "842543",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "RunsOnToast",
   "teamId": "4909398942023680",
   "score": "842116",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "OldLameDucks",
   "teamId": "4534395415298048",
   "score": "841442",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Pipeline Gallery",
   "teamId": "6119034605010944",
   "score": "839867",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Kappa//",
   "teamId": "4943590102925312",
   "score": "839494",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "ErrSeg",
   "teamId": "5447053484228608",
   "score": "839077",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Slow!",
   "teamId": "5860763524661248",
   "score": "837835",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "adgica",
   "teamId": "6478510818328576",
   "score": "835352",
   "hubId": "6063418469515264",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Datasse",
   "teamId": "6582946974662656",
   "score": "835256",
   "hubId": "6310929918590976",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "This is EM",
   "teamId": "6721613483474944",
   "score": "834864",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Beltalowda",
   "teamId": "6529388799590400",
   "score": "832022",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Math $\\pi$rates",
   "teamId": "5124437552660480",
   "score": "830880",
   "hubId": "5540597737717760",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "StreamCode",
   "teamId": "5631797945696256",
   "score": "830531",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "AnyThing",
   "teamId": "5637408045400064",
   "score": "829648",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "#nerds",
   "teamId": "5222193491345408",
   "score": "828789",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Mind the GAP🚀✈💻",
   "teamId": "5583998986223616",
   "score": "828732",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "ZimtZwiebel",
   "teamId": "6264929812217856",
   "score": "823594",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "DETash",
   "teamId": "6331517978542080",
   "score": "823454",
   "hubId": "5423102867537920",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "TheJacobian",
   "teamId": "6329074142150656",
   "score": "822705",
   "hubId": "5112178910691328",
   "countries": [
    "Kazakhstan",
    "Turkey"
   ]
  },
  {
   "teamName": "ATeam",
   "teamId": "6667609034457088",
   "score": "822518",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Sonic",
   "teamId": "6751602488639488",
   "score": "822323",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "V2MSoftware",
   "teamId": "4749581866762240",
   "score": "821392",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Team Alpha",
   "teamId": "4924216377868288",
   "score": "821221",
   "hubId": "5937954421735424",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Probably Approximately Correct",
   "teamId": "5786134374252544",
   "score": "820563",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Astana",
   "teamId": "4642923400396800",
   "score": "819924",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "KPI-EVO",
   "teamId": "5979785859694592",
   "score": "816636",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "ᕯ",
   "teamId": "6158966795010048",
   "score": "813668",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Django Unhashed",
   "teamId": "6262885407784960",
   "score": "812647",
   "hubId": "6733142383656960",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "C'est pas faux !",
   "teamId": "6056941189070848",
   "score": "810979",
   "hubId": "4883695106260992",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "DROP TABLE participants'--",
   "teamId": "5428622705819648",
   "score": "808655",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "The Crew",
   "teamId": "6161336341889024",
   "score": "807678",
   "hubId": "0",
   "countries": [
    "Mauritius",
    "Mauritius",
    "Mauritius",
    "Mauritius"
   ]
  },
  {
   "teamName": "Questionable Intelligence",
   "teamId": "6125998693154816",
   "score": "807116",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Code Monkeys Or Not",
   "teamId": "6531108531339264",
   "score": "806262",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "iQezBan",
   "teamId": "4611636979564544",
   "score": "806055",
   "hubId": "0",
   "countries": [
    "Armenia",
    "Armenia",
    "Armenia",
    "Armenia"
   ]
  },
  {
   "teamName": "I Ludrus",
   "teamId": "6145950963728384",
   "score": "805998",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "MDL",
   "teamId": "6690065539399680",
   "score": "801999",
   "hubId": "6503063468638208",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "Natural Neural Networks",
   "teamId": "5208474426277888",
   "score": "800969",
   "hubId": "5342612496056320",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "El Credo",
   "teamId": "4892404360413184",
   "score": "800549",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "INTCoders",
   "teamId": "6054327164600320",
   "score": "800458",
   "hubId": "0",
   "countries": [
    "France",
    "Tunisia",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Don't hate Mondays; hate capitalism",
   "teamId": "6035778811461632",
   "score": "800409",
   "hubId": "5931430634848256",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Jason Statham; Reloaded",
   "teamId": "6286327674830848",
   "score": "800340",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Cookie Bytes",
   "teamId": "6284891008270336",
   "score": "800054",
   "hubId": "5728758644342784",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "PEDAGOGIA",
   "teamId": "4621772498403328",
   "score": "799891",
   "hubId": "6508589212499968",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Dirty Bits",
   "teamId": "4932145088823296",
   "score": "799057",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "Romania",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Ezintathu Wiergots",
   "teamId": "5136398701035520",
   "score": "798883",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "Alligator3",
   "teamId": "5783939713073152",
   "score": "798462",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Legends27",
   "teamId": "4872999631060992",
   "score": "797615",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Demitech",
   "teamId": "4852916363984896",
   "score": "796741",
   "hubId": "5807719806140416",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "·",
   "teamId": "5833861997002752",
   "score": "796211",
   "hubId": "6079963757281280",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Ohhh..",
   "teamId": "5391079255834624",
   "score": "795647",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Zapp Brannigan",
   "teamId": "6670585178357760",
   "score": "795595",
   "hubId": "6297094285426688",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "TITM",
   "teamId": "6380670590910464",
   "score": "795368",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "OOPs",
   "teamId": "5266841152782336",
   "score": "793405",
   "hubId": "5769271594450944",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Arjomi",
   "teamId": "5987316145324032",
   "score": "793356",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Spark_IT",
   "teamId": "5813682294489088",
   "score": "793229",
   "hubId": "5417095013597184",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "IVU",
   "teamId": "6488830886543360",
   "score": "792306",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Perpetually Clueless",
   "teamId": "6184290190622720",
   "score": "791689",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Asmaton",
   "teamId": "4841018230833152",
   "score": "791366",
   "hubId": "5841604480860160",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "FromLondonWithLove",
   "teamId": "5472744703524864",
   "score": "791334",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Gumball",
   "teamId": "5252247726325760",
   "score": "791071",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "SynTax Collectors",
   "teamId": "6543984843292672",
   "score": "791069",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Mom's Spaghetti",
   "teamId": "5183870974558208",
   "score": "788880",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Noob Team",
   "teamId": "5483101681614848",
   "score": "788504",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "The correct table next to the window",
   "teamId": "5818659624714240",
   "score": "787612",
   "hubId": "0",
   "countries": [
    "Czech Republic",
    "Czech Republic",
    "Czech Republic"
   ]
  },
  {
   "teamName": "Namek",
   "teamId": "5013698800254976",
   "score": "787267",
   "hubId": "5114465980776448",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Diversity Injection",
   "teamId": "6545470365106176",
   "score": "786076",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "MLM",
   "teamId": "5915498789208064",
   "score": "785743",
   "hubId": "0",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Dorabadora",
   "teamId": "6612345421824000",
   "score": "785600",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "MFG",
   "teamId": "6230928166748160",
   "score": "784697",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The One Token Ring",
   "teamId": "5889232379838464",
   "score": "782672",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Sloth Coders",
   "teamId": "4709880531255296",
   "score": "782669",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "ClassMen",
   "teamId": "5817419587125248",
   "score": "782422",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "PractiseRound",
   "teamId": "5041894723682304",
   "score": "782231",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "#Rebel",
   "teamId": "5282544895393792",
   "score": "781069",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "HOOLI",
   "teamId": "4844129196441600",
   "score": "780918",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "NerdPulp",
   "teamId": "5469058682060800",
   "score": "780618",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "IDSE Bitsy Spider",
   "teamId": "5383133365010432",
   "score": "779941",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy",
    "Germany",
    "Italy"
   ]
  },
  {
   "teamName": "CraftJS",
   "teamId": "4965689857146880",
   "score": "779129",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Squinters",
   "teamId": "5135955245662208",
   "score": "778684",
   "hubId": "5217872620027904",
   "countries": [
    "Kenya",
    "South Africa",
    "Iran",
    "Nigeria"
   ]
  },
  {
   "teamName": "Zaali",
   "teamId": "4875034438926336",
   "score": "778684",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "We Still Don't Have A Name",
   "teamId": "4735125543714816",
   "score": "777203",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "Czech Republic"
   ]
  },
  {
   "teamName": "42first",
   "teamId": "5362148154802176",
   "score": "777203",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "ProjectKitchenFTW",
   "teamId": "5117847663542272",
   "score": "777203",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "PKHALI",
   "teamId": "5742415700819968",
   "score": "777203",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "ASeriousTeamName",
   "teamId": "4701521182720000",
   "score": "777203",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "TeamTryCatch",
   "teamId": "5705847812390912",
   "score": "776904",
   "hubId": "5732975631138816",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "bigminders",
   "teamId": "5682712232853504",
   "score": "775819",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "py_code",
   "teamId": "5918876848095232",
   "score": "775477",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Turkey",
    "Austria",
    "Oman"
   ]
  },
  {
   "teamName": "Pragmatic",
   "teamId": "5907117965836288",
   "score": "774545",
   "hubId": "0",
   "countries": [
    "Albania",
    "Albania",
    "Albania",
    "Albania"
   ]
  },
  {
   "teamName": "Genetic Programmers",
   "teamId": "5459780009197568",
   "score": "773869",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "HKN polito",
   "teamId": "5266301329080320",
   "score": "773246",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Unemployed",
   "teamId": "6283270933184512",
   "score": "772750",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "rt-team",
   "teamId": "6694806981967872",
   "score": "772412",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Ifri-Seniors",
   "teamId": "5176217074401280",
   "score": "769545",
   "hubId": "5081966902771712",
   "countries": [
    "Benin",
    "Benin",
    "Benin",
    "Benin"
   ]
  },
  {
   "teamName": "Take Me to Church Turing",
   "teamId": "5898954306748416",
   "score": "768739",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "BetaGo",
   "teamId": "5598266599145472",
   "score": "767811",
   "hubId": "5983641666584576",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "TeamyMcTeamFace",
   "teamId": "4771610821132288",
   "score": "767811",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team Pils++",
   "teamId": "5999186763841536",
   "score": "767811",
   "hubId": "5074919532527616",
   "countries": [
    "Norway",
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "pizza.js",
   "teamId": "6726229969338368",
   "score": "766572",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "TheLastJedi",
   "teamId": "5978303089344512",
   "score": "766065",
   "hubId": "4833820872278016",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "wehkamp-joined-forces",
   "teamId": "5543464427061248",
   "score": "765064",
   "hubId": "6510667775344640",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "TheLastMohicans",
   "teamId": "5285563183661056",
   "score": "764566",
   "hubId": "6113594290733056",
   "countries": [
    "Romania",
    "Serbia"
   ]
  },
  {
   "teamName": "The team and \"The Soma\"",
   "teamId": "5795105218756608",
   "score": "764566",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Quadruple Precision",
   "teamId": "5746007031676928",
   "score": "762200",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Sweden",
    "Netherlands"
   ]
  },
  {
   "teamName": "PowerBuff Dudz",
   "teamId": "6222886377357312",
   "score": "760338",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "SaniTeQ",
   "teamId": "4845388695601152",
   "score": "756654",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "PW-EE",
   "teamId": "4885845341372416",
   "score": "756487",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Hash Strings Or Die Tryin",
   "teamId": "4906662510985216",
   "score": "755879",
   "hubId": "5944419287040000",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "PekingPalace",
   "teamId": "5607911485079552",
   "score": "754815",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "TeamName#42",
   "teamId": "5122186654253056",
   "score": "752929",
   "hubId": "0",
   "countries": [
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Team Advicement",
   "teamId": "6048722030952448",
   "score": "751692",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "OneTimeMisanthrope",
   "teamId": "6522174529601536",
   "score": "750992",
   "hubId": "6144857559007232",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "alGoal",
   "teamId": "6485710794129408",
   "score": "747421",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "⚡ Troublemakers ⚡",
   "teamId": "6261115679932416",
   "score": "744656",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Five.13",
   "teamId": "5867647753256960",
   "score": "734865",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Tecnocchio",
   "teamId": "5547776305790976",
   "score": "734016",
   "hubId": "6441886759780352",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Tsouvlia",
   "teamId": "6273347746791424",
   "score": "734016",
   "hubId": "0",
   "countries": [
    "Austria",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "CafelasoM2M",
   "teamId": "4919681630601216",
   "score": "734016",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Parkcode",
   "teamId": "6289778681053184",
   "score": "734016",
   "hubId": "6565180842442752",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Try Out",
   "teamId": "5036629966192640",
   "score": "734016",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Mozambique",
    "Austria",
    "Germany"
   ]
  },
  {
   "teamName": "Keyneo-1",
   "teamId": "6170175585910784",
   "score": "734002",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "2b|2b",
   "teamId": "4848841111109632",
   "score": "731826",
   "hubId": "4917250343567360",
   "countries": [
    "Lebanon",
    "Lebanon"
   ]
  },
  {
   "teamName": "R2D2",
   "teamId": "6001843469549568",
   "score": "730253",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Hashin Cocuklar",
   "teamId": "5088454585090048",
   "score": "729953",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Temp 2",
   "teamId": "5189864064548864",
   "score": "729645",
   "hubId": "5944419287040000",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Zonnebloempjes",
   "teamId": "5378605395738624",
   "score": "729028",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "SHA7",
   "teamId": "6094862327742464",
   "score": "728294",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Shqipe2Krena",
   "teamId": "4860477721018368",
   "score": "727940",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "jarvis",
   "teamId": "5396016857612288",
   "score": "726447",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "The Challengers",
   "teamId": "6042969660456960",
   "score": "725555",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Poland"
   ]
  },
  {
   "teamName": "Error418",
   "teamId": "5698454563061760",
   "score": "723999",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "🙌🙏🙆🙅🙋",
   "teamId": "4890368478806016",
   "score": "723155",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "base",
   "teamId": "6360404519288832",
   "score": "723140",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "PFUDOR",
   "teamId": "5782715580284928",
   "score": "721445",
   "hubId": "4721081336201216",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Coding Llamas",
   "teamId": "5654916949344256",
   "score": "721348",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "PolyKnut",
   "teamId": "6344670846124032",
   "score": "720518",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "L' équipe",
   "teamId": "6619846582206464",
   "score": "720084",
   "hubId": "4762512469786624",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Maia carpoolers",
   "teamId": "6103488232685568",
   "score": "719711",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Surprise",
   "teamId": "6537766535954432",
   "score": "717854",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Null is not nil but None",
   "teamId": "5564052889665536",
   "score": "717230",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "New folder(2)",
   "teamId": "4816227478274048",
   "score": "717161",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "The Skeptics",
   "teamId": "4608372468875264",
   "score": "713803",
   "hubId": "5661462143959040",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "The Lispers",
   "teamId": "5133062920732672",
   "score": "713443",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "SugarePower",
   "teamId": "5625203828719616",
   "score": "713214",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Pop",
   "teamId": "5880014641823744",
   "score": "708051",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Kruszyguazy",
   "teamId": "6662912017956864",
   "score": "704484",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "James Clerk Haxwell",
   "teamId": "5744579559030784",
   "score": "704134",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "WeAreReadyForMySummerCar->FeelsGoodMan",
   "teamId": "6493433883525120",
   "score": "701938",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "Juascode",
   "teamId": "4710723955458048",
   "score": "699437",
   "hubId": "0",
   "countries": [
    "Spain",
    "Germany"
   ]
  },
  {
   "teamName": "JC",
   "teamId": "6051785349267456",
   "score": "698201",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "Italy"
   ]
  },
  {
   "teamName": "Cookies",
   "teamId": "6374001915985920",
   "score": "695813",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "TheBayesians",
   "teamId": "4600263570620416",
   "score": "694940",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Algorhythm",
   "teamId": "6474665413312512",
   "score": "694297",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Boom boom boom let me hear you say waymo",
   "teamId": "4974062157692928",
   "score": "692995",
   "hubId": "6448591136620544",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "DivisionZero",
   "teamId": "6268047421603840",
   "score": "688837",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "VertVertVertVertVertVertVertVertVertVertVertVertVertVertVertVert",
   "teamId": "4900822227877888",
   "score": "683035",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Failure to comply",
   "teamId": "4970643028180992",
   "score": "681622",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Estonia",
    "Estonia"
   ]
  },
  {
   "teamName": "BleuTeam",
   "teamId": "6320502729605120",
   "score": "678136",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Super C++",
   "teamId": "6574366435311616",
   "score": "671606",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "CodeIne",
   "teamId": "5209398649552896",
   "score": "670616",
   "hubId": "5107936288309248",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "meme_refinery4.10-rc8",
   "teamId": "5733493980004352",
   "score": "669846",
   "hubId": "4629206549921792",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Quantum program",
   "teamId": "4709045495660544",
   "score": "669112",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "flysqrl",
   "teamId": "5088549275697152",
   "score": "667532",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Two bits don't make a byte",
   "teamId": "4736096541868032",
   "score": "667043",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Bacalhau à FCUL",
   "teamId": "5894996293058560",
   "score": "666893",
   "hubId": "6079963757281280",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Oui Bien Sûr",
   "teamId": "4679213122584576",
   "score": "666788",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Oyzi and Ponch",
   "teamId": "4726067524796416",
   "score": "666670",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "3Kidz&1Fozzil",
   "teamId": "4808324939776000",
   "score": "666185",
   "hubId": "6158895055634432",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "M.A.C.",
   "teamId": "4535857046355968",
   "score": "665815",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Volchari",
   "teamId": "5957929039560704",
   "score": "661838",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Defcode 1",
   "teamId": "5775243545149440",
   "score": "659968",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "HaViFa",
   "teamId": "5451757748486144",
   "score": "659874",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Frenchies@KTH",
   "teamId": "4779543357292544",
   "score": "658840",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "VPLab-42",
   "teamId": "5435090591023104",
   "score": "657097",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SUPREME",
   "teamId": "5671275808686080",
   "score": "655473",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "MTG eternal kids",
   "teamId": "6014970231783424",
   "score": "653622",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Pipotron",
   "teamId": "6148960058081280",
   "score": "649994",
   "hubId": "4805185117356032",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "go go go go",
   "teamId": "5644230869385216",
   "score": "649158",
   "hubId": "0",
   "countries": [
    "Spain",
    "Egypt",
    "Spain"
   ]
  },
  {
   "teamName": "TPinf (thisTeam.points->∞)",
   "teamId": "5055003165196288",
   "score": "644384",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Bits Plz",
   "teamId": "5168990590599168",
   "score": "641954",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Null Fucks Given",
   "teamId": "6280374514614272",
   "score": "640590",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Automaton",
   "teamId": "4752971401265152",
   "score": "640395",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Cntrl + Alt + Defeat",
   "teamId": "6384004357947392",
   "score": "635472",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Margherita Hacker",
   "teamId": "4574654089920512",
   "score": "635116",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Les tortues ninFortran",
   "teamId": "6570588407595008",
   "score": "634723",
   "hubId": "4883695106260992",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Χ",
   "teamId": "6727491079110656",
   "score": "633266",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Point Blank",
   "teamId": "5343728852008960",
   "score": "631263",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Jetstream",
   "teamId": "6535808030867456",
   "score": "630231",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Machine Learners",
   "teamId": "5827422968610816",
   "score": "629234",
   "hubId": "6125008703193088",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "de_B.U.G Mafia",
   "teamId": "4947628781469696",
   "score": "627429",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "java++",
   "teamId": "6246624460275712",
   "score": "626450",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "PioneersTech",
   "teamId": "5147105786068992",
   "score": "624195",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "MAI KRUTO",
   "teamId": "4774423957602304",
   "score": "622785",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "PIG-G",
   "teamId": "5545851422244864",
   "score": "621109",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Team Rocket EPFL",
   "teamId": "5943048118730752",
   "score": "620609",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Odin",
   "teamId": "5697551747514368",
   "score": "614799",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "5273909c02b8ce7ae42a4e21542b3326",
   "teamId": "6183541792571392",
   "score": "611618",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "ebury.py",
   "teamId": "5661570658992128",
   "score": "611596",
   "hubId": "5114465980776448",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Smartacus",
   "teamId": "5088455054852096",
   "score": "609423",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "AcademiaProgramatorilor",
   "teamId": "6547120706289664",
   "score": "609259",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Maximum_Entropy",
   "teamId": "6180487869497344",
   "score": "609132",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "GeFeTe",
   "teamId": "4859241844178944",
   "score": "608736",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Epi4bGI",
   "teamId": "4756221349330944",
   "score": "607260",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Bash-k-OS",
   "teamId": "5137990858833920",
   "score": "603889",
   "hubId": "6440138506764288",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "sgt.p",
   "teamId": "4632403079331840",
   "score": "600159",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Stroopwafel",
   "teamId": "4585330036441088",
   "score": "597280",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "HashSoc",
   "teamId": "4928113456709632",
   "score": "596539",
   "hubId": "5739578472267776",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Les Jacky Tuning",
   "teamId": "6264359118438400",
   "score": "594910",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Chafinoulinou",
   "teamId": "5862228376944640",
   "score": "594101",
   "hubId": "5218381573652480",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Orienté Chaos",
   "teamId": "5238859977719808",
   "score": "590842",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "TestCicles",
   "teamId": "6036860337913856",
   "score": "588037",
   "hubId": "6224891120451584",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "tafsiamamoy",
   "teamId": "6415552973111296",
   "score": "587884",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Centaurea",
   "teamId": "5048649029517312",
   "score": "586305",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Classic",
   "teamId": "5755811905142784",
   "score": "584786",
   "hubId": "0",
   "countries": [
    "Italy",
    "Spain",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Les Codeurs Flowters",
   "teamId": "4669448782872576",
   "score": "584201",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Code Slingers",
   "teamId": "6172244417970176",
   "score": "583812",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Team.getInstance();",
   "teamId": "5148948125712384",
   "score": "581000",
   "hubId": "5426936595611648",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "HashTag",
   "teamId": "4557673601171456",
   "score": "580892",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "WaffleMafia",
   "teamId": "4679409885773824",
   "score": "578753",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "Slovakia"
   ]
  },
  {
   "teamName": "Diversity",
   "teamId": "5319694550564864",
   "score": "578630",
   "hubId": "5661462143959040",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Abadeuses",
   "teamId": "6124192323862528",
   "score": "577993",
   "hubId": "6224891120451584",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "#Zirkus",
   "teamId": "4785110909976576",
   "score": "576660",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Les amateurs de code anonymes",
   "teamId": "5091695205023744",
   "score": "576387",
   "hubId": "4674291962478592",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Gazebo",
   "teamId": "6028232889466880",
   "score": "576238",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Mark and his mates",
   "teamId": "6069116146286592",
   "score": "575661",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "⁠⁠⁠dull pointers",
   "teamId": "6268512351813632",
   "score": "573706",
   "hubId": "5313581134381056",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Test",
   "teamId": "5673461879930880",
   "score": "572787",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Beyond-C",
   "teamId": "6149867437031424",
   "score": "569647",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Koudou",
   "teamId": "5365866187194368",
   "score": "569021",
   "hubId": "6504443965079552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Багери",
   "teamId": "5910067333300224",
   "score": "568716",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "Final Version 2",
   "teamId": "5404304265445376",
   "score": "567721",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Artemis",
   "teamId": "5991481592512512",
   "score": "566202",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Mayte team!!!",
   "teamId": "5672943531065344",
   "score": "565884",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Team Second Try",
   "teamId": "6156895614140416",
   "score": "564651",
   "hubId": "0",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Team Easy On",
   "teamId": "5297582381203456",
   "score": "560892",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "HackWord",
   "teamId": "6725479826456576",
   "score": "559858",
   "hubId": "6727668984709120",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Italy",
    "Germany"
   ]
  },
  {
   "teamName": "3M",
   "teamId": "4882322662883328",
   "score": "557707",
   "hubId": "0",
   "countries": [
    "Ireland",
    "France",
    "Ireland"
   ]
  },
  {
   "teamName": "Unlimited Power",
   "teamId": "5691998354800640",
   "score": "555548",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Codey McCodeface",
   "teamId": "5746794688413696",
   "score": "554897",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "sudo inda hash hell",
   "teamId": "6074709468774400",
   "score": "554263",
   "hubId": "5690886025379840",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "20,000 lines into the code",
   "teamId": "5153086528028672",
   "score": "550946",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "JavaDreamTeam",
   "teamId": "5459652166811648",
   "score": "547887",
   "hubId": "4671317026537472",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "paff pastry",
   "teamId": "6425460724465664",
   "score": "547491",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Teacode.pl",
   "teamId": "4905607022772224",
   "score": "546618",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Rolling Hash",
   "teamId": "5927025474797568",
   "score": "545711",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Team Raclette",
   "teamId": "4821239637999616",
   "score": "544779",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "eTuitus Red",
   "teamId": "6287187943358464",
   "score": "543815",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "The Unhashables",
   "teamId": "5309337438257152",
   "score": "540653",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "LordOfTheDom",
   "teamId": "5736229807063040",
   "score": "539507",
   "hubId": "4715704574017536",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "PowerSpikeGG",
   "teamId": "5177729506869248",
   "score": "538659",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Lambda losers",
   "teamId": "5354355674841088",
   "score": "534393",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Chinslam",
   "teamId": "6501326422802432",
   "score": "534124",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "nerdyyy",
   "teamId": "6672129554644992",
   "score": "532176",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "ContinuKnut",
   "teamId": "6423067622375424",
   "score": "530067",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Newbuildings",
   "teamId": "6078691910090752",
   "score": "529292",
   "hubId": "6602827975622656",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Bronze",
   "teamId": "6311444844904448",
   "score": "526628",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Team7",
   "teamId": "6018304267255808",
   "score": "526148",
   "hubId": "4671317026537472",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Farfalle al sugo",
   "teamId": "5698958080868352",
   "score": "524167",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "4Gada",
   "teamId": "4962173621108736",
   "score": "524012",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Musketeers",
   "teamId": "4846610613796864",
   "score": "522247",
   "hubId": "5725403872231424",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "LaDoble",
   "teamId": "6263890765676544",
   "score": "519987",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "G̴̨̻̗̙̠̰͉̰̜͔̭̍͒̀͌̎̋̈́̌͑̄̉̌̉̄̇̎͘͠͝LITCH",
   "teamId": "6580386905718784",
   "score": "519828",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Supatates",
   "teamId": "6010871021043712",
   "score": "518187",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "UCU Team 1",
   "teamId": "5761901967441920",
   "score": "516441",
   "hubId": "4735593493823488",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Ali Makes Coffee",
   "teamId": "6620320102350848",
   "score": "516069",
   "hubId": "5763337560260608",
   "countries": [
    "Luxembourg",
    "France",
    "Luxembourg",
    "Luxembourg"
   ]
  },
  {
   "teamName": "CodeBenders",
   "teamId": "5638466150858752",
   "score": "513791",
   "hubId": "5042625404993536",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "NTUA Paladins",
   "teamId": "6302893565018112",
   "score": "510728",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "NoBrainers",
   "teamId": "6418220953108480",
   "score": "508488",
   "hubId": "5941301006565376",
   "countries": [
    "Slovakia",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Akol",
   "teamId": "5501431796727808",
   "score": "506360",
   "hubId": "6274524702048256",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Team Tony",
   "teamId": "5752842203693056",
   "score": "506213",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Snowflakes",
   "teamId": "4949034846388224",
   "score": "504445",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Les semi-croustillants",
   "teamId": "5615705844088832",
   "score": "504341",
   "hubId": "5735750448447488",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "EMP1",
   "teamId": "4807588889755648",
   "score": "504283",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Tech8",
   "teamId": "5926532627300352",
   "score": "500792",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Hash Ketchup",
   "teamId": "5572815965126656",
   "score": "500470",
   "hubId": "5000405339602944",
   "countries": [
    "Poland",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Jousting Ponies",
   "teamId": "5163135207997440",
   "score": "500106",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Paranoia",
   "teamId": "5859254313418752",
   "score": "498909",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "YourTeam",
   "teamId": "5568940562448384",
   "score": "498298",
   "hubId": "6504443965079552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Delfic",
   "teamId": "4902850995945472",
   "score": "497428",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "El Cartel",
   "teamId": "4592031259164672",
   "score": "497265",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Un nombre original",
   "teamId": "6239963301543936",
   "score": "496526",
   "hubId": "5174621762486272",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "42born2hashcode",
   "teamId": "4999137451835392",
   "score": "495818",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Error: NameFormatException",
   "teamId": "6601198169751552",
   "score": "495691",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Supersonic Wizards",
   "teamId": "6482917924536320",
   "score": "494826",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Alhambra",
   "teamId": "6176558981054464",
   "score": "494284",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "A Moža Tak i Treba?",
   "teamId": "4798792796733440",
   "score": "493594",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "Shawirma",
   "teamId": "5780680839528448",
   "score": "493486",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Leaky Memory",
   "teamId": "6646806628794368",
   "score": "489696",
   "hubId": "5735750448447488",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SharkNet",
   "teamId": "5175058037211136",
   "score": "489283",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "cudaHashcode",
   "teamId": "6009183300222976",
   "score": "488966",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Not a Harry Potter Name",
   "teamId": "5789293658243072",
   "score": "488758",
   "hubId": "5384749346455552",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "DOCO",
   "teamId": "6221339450933248",
   "score": "487693",
   "hubId": "6640431018278912",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Zion",
   "teamId": "5659454380965888",
   "score": "484977",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Asgard",
   "teamId": "6175293442097152",
   "score": "484297",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NG Team",
   "teamId": "4883809057112064",
   "score": "483998",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Trash Panda",
   "teamId": "5072753191288832",
   "score": "483424",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "25603c4a",
   "teamId": "6227831226892288",
   "score": "478550",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Bogo solve",
   "teamId": "4780326383517696",
   "score": "477975",
   "hubId": "0",
   "countries": [
    "Germany",
    "Romania"
   ]
  },
  {
   "teamName": "sabba2",
   "teamId": "5666148355932160",
   "score": "477317",
   "hubId": "5419392015794176",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "The Backdoor Club for Men",
   "teamId": "6622199486087168",
   "score": "475743",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "redmd",
   "teamId": "6380700789899264",
   "score": "475000",
   "hubId": "4629206549921792",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Oops",
   "teamId": "6321970266243072",
   "score": "470738",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "ThoughtBots",
   "teamId": "6227374618181632",
   "score": "470695",
   "hubId": "0",
   "countries": [
    "France",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Teamy McMuppets",
   "teamId": "4882757796757504",
   "score": "470352",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "CAFEBABE",
   "teamId": "5245159218348032",
   "score": "469437",
   "hubId": "6249764886675456",
   "countries": [
    "Malta",
    "Malta",
    "Malta"
   ]
  },
  {
   "teamName": "Challenge",
   "teamId": "4969980865019904",
   "score": "468882",
   "hubId": "0",
   "countries": [
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Bytesaur.java",
   "teamId": "6521107968425984",
   "score": "468538",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Entropy Sources",
   "teamId": "6240443666792448",
   "score": "468410",
   "hubId": "6204749871316992",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "BurdenBoyz",
   "teamId": "6502291515375616",
   "score": "468295",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Les baleines volantes",
   "teamId": "5122107734228992",
   "score": "467405",
   "hubId": "5044292523393024",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rattrapage",
   "teamId": "4875863032070144",
   "score": "466845",
   "hubId": "4685852605153280",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "TUMmy Ache",
   "teamId": "5285565062709248",
   "score": "466232",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Team Dogsbody",
   "teamId": "5924495135080448",
   "score": "464931",
   "hubId": "4543895413194752",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Peace Lords",
   "teamId": "5731940544020480",
   "score": "464129",
   "hubId": "6729602793734144",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Axxes DotNet #1",
   "teamId": "6624308516356096",
   "score": "464056",
   "hubId": "5117366962749440",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Mnawer",
   "teamId": "4712443083227136",
   "score": "463254",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Youth Developers",
   "teamId": "6310000796368896",
   "score": "460709",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "EiffelPower",
   "teamId": "5709256942682112",
   "score": "458922",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "99paraffa",
   "teamId": "5758366605377536",
   "score": "457752",
   "hubId": "0",
   "countries": [
    "Germany",
    "Italy"
   ]
  },
  {
   "teamName": "Hashbrown Tables",
   "teamId": "4851071474204672",
   "score": "456920",
   "hubId": "5931430634848256",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "nullpointer",
   "teamId": "5967879941914624",
   "score": "455245",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Petarda",
   "teamId": "6321462050816000",
   "score": "455131",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Aperture Potatos",
   "teamId": "5054763519442944",
   "score": "455083",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Closers",
   "teamId": "6468631521132544",
   "score": "453682",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Lazy Kings",
   "teamId": "5979945109028864",
   "score": "453323",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Google_It",
   "teamId": "5190284971343872",
   "score": "451132",
   "hubId": "5088095686885376",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "KCBL",
   "teamId": "5201154728263680",
   "score": "450752",
   "hubId": "4629206549921792",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Catch Me",
   "teamId": "5260989796712448",
   "score": "448089",
   "hubId": "4867149818494976",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "God is real, unless declared as integer",
   "teamId": "5515741956669440",
   "score": "447319",
   "hubId": "6651476264878080",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Bogosolve",
   "teamId": "5862182138937344",
   "score": "446983",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Born to math",
   "teamId": "6627140510416896",
   "score": "446430",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "echo $teamname",
   "teamId": "5015514162135040",
   "score": "444801",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "🚃",
   "teamId": "5712857400344576",
   "score": "443641",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Winners",
   "teamId": "5942269387472896",
   "score": "443187",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Angels of SegFault",
   "teamId": "6239152290922496",
   "score": "441321",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Insert Team Name",
   "teamId": "6199406663565312",
   "score": "440339",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "MIPTEAM",
   "teamId": "4993567952994304",
   "score": "438856",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "NEOM",
   "teamId": "6505497372917760",
   "score": "434518",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Télécode",
   "teamId": "4763202885779456",
   "score": "434147",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "JKK",
   "teamId": "6307074245918720",
   "score": "430136",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "$team_name",
   "teamId": "5127349808922624",
   "score": "429043",
   "hubId": "6026378671554560",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Kefna",
   "teamId": "6379465852583936",
   "score": "428329",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Aauj_Avengers",
   "teamId": "5193304132026368",
   "score": "428136",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "NosheepNocry",
   "teamId": "5753513829203968",
   "score": "427392",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Wowcracy",
   "teamId": "6755091075825664",
   "score": "425674",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Italy",
    "Switzerland"
   ]
  },
  {
   "teamName": "SockSeed",
   "teamId": "5922234707214336",
   "score": "424732",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "Sparklane",
   "teamId": "4541774705983488",
   "score": "424629",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Damaged Butt Titans",
   "teamId": "4904997674287104",
   "score": "424449",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "The Lost Methods",
   "teamId": "6639617927282688",
   "score": "424115",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "Minesty Python & the Holy Code",
   "teamId": "6505077338537984",
   "score": "423980",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hardis Ouest",
   "teamId": "5855843304079360",
   "score": "423455",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "PHANTOMS",
   "teamId": "5979640703221760",
   "score": "423394",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Turing",
   "teamId": "4738215302922240",
   "score": "423380",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Solanoides",
   "teamId": "6266672562307072",
   "score": "423003",
   "hubId": "6589328624975872",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Hash Winners",
   "teamId": "5793715058638848",
   "score": "421743",
   "hubId": "5720755912310784",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Runtime Exception",
   "teamId": "5690374655836160",
   "score": "421680",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "GGWP Team",
   "teamId": "5057641885728768",
   "score": "421020",
   "hubId": "6310929918590976",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "LJR",
   "teamId": "6719826575753216",
   "score": "420284",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "WonderM4n",
   "teamId": "4705079630233600",
   "score": "420095",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "ATON",
   "teamId": "4896903271546880",
   "score": "418451",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Huchris",
   "teamId": "5606538437722112",
   "score": "418451",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "teamSH",
   "teamId": "4715446808870912",
   "score": "418366",
   "hubId": "6218891520901120",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "OWLS",
   "teamId": "6536392414855168",
   "score": "417963",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Innovation Factory",
   "teamId": "6190450247467008",
   "score": "417602",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Los vatos locos",
   "teamId": "4654430624415744",
   "score": "416896",
   "hubId": "5044292523393024",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Technion omega",
   "teamId": "5359990202171392",
   "score": "415504",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "MasterCatch",
   "teamId": "6750288295755776",
   "score": "415059",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Euplos",
   "teamId": "5832120589090816",
   "score": "414475",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Ratjes",
   "teamId": "5424768777977856",
   "score": "414342",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "P Hash Code",
   "teamId": "5780254631133184",
   "score": "414173",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Four Guys",
   "teamId": "4916071710588928",
   "score": "413385",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Los Simios Mutantes del Espacio",
   "teamId": "6022822304415744",
   "score": "412765",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Hapoel Taub",
   "teamId": "4799521129234432",
   "score": "412646",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "TEAM",
   "teamId": "5605380675600384",
   "score": "412538",
   "hubId": "5550644337311744",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Not Enough Relatively Dumb Stuff",
   "teamId": "5821735089733632",
   "score": "412183",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Armata",
   "teamId": "4626529979990016",
   "score": "411775",
   "hubId": "5232333170933760",
   "countries": [
    "Cameroon",
    "Cameroon",
    "Congo (the Democratic Republic of the)"
   ]
  },
  {
   "teamName": "Brzeszczot",
   "teamId": "6346783970033664",
   "score": "411647",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "SEBIXY",
   "teamId": "5118514255888384",
   "score": "410631",
   "hubId": "5493471611715584",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Team BOEY",
   "teamId": "5938451429982208",
   "score": "409462",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "TF17",
   "teamId": "5023419586314240",
   "score": "407650",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "PiedPiper",
   "teamId": "4741291506139136",
   "score": "406167",
   "hubId": "0",
   "countries": [
    "Italy",
    "United Kingdom",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "RoFe Team",
   "teamId": "4801268644052992",
   "score": "405416",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "upmc_dac_m2",
   "teamId": "5696939446239232",
   "score": "404918",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "hackeri123",
   "teamId": "4863523859464192",
   "score": "402359",
   "hubId": "5936020612710400",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Devoluteam",
   "teamId": "6000855157309440",
   "score": "401580",
   "hubId": "5720755912310784",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "CodeForFondue",
   "teamId": "6413277982621696",
   "score": "400342",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "56d7c50b9d5b7f6f31c14acbc409e6d1",
   "teamId": "6442148551458816",
   "score": "400021",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "SilverCow",
   "teamId": "5425455100329984",
   "score": "399692",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Focus",
   "teamId": "4984282770571264",
   "score": "399385",
   "hubId": "5044292523393024",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NeverOddOrEven",
   "teamId": "5342493780475904",
   "score": "399247",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "Germany",
    "Netherlands"
   ]
  },
  {
   "teamName": "Pathfinder Society Latvia",
   "teamId": "6277925846384640",
   "score": "398622",
   "hubId": "5751703970250752",
   "countries": [
    "Latvia",
    "Latvia",
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "Ammargelluti",
   "teamId": "5216933632802816",
   "score": "397249",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "La Hipnocueva Difadiana",
   "teamId": "6688829192798208",
   "score": "396711",
   "hubId": "5078849964474368",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Photis",
   "teamId": "6687273810657280",
   "score": "394718",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "CapBE",
   "teamId": "5402459644100608",
   "score": "392306",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "BambergPlanners",
   "teamId": "5534317019136000",
   "score": "388937",
   "hubId": "6711077593153536",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Happy Bits",
   "teamId": "6534238555865088",
   "score": "388374",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "DTM_ResEl",
   "teamId": "4828224932544512",
   "score": "388374",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "LittleBitWeirdGroup",
   "teamId": "6384685043154944",
   "score": "384989",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Trump's Intelligence Advisory",
   "teamId": "4821797983748096",
   "score": "383776",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Codetsinf",
   "teamId": "4750631180959744",
   "score": "382266",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Suhina",
   "teamId": "5420392206303232",
   "score": "382043",
   "hubId": "4755584351993856",
   "countries": [
    "Finland",
    "Finland",
    "Finland",
    "Finland"
   ]
  },
  {
   "teamName": "We like trains",
   "teamId": "4673928433762304",
   "score": "381844",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Информатика",
   "teamId": "6457946246479872",
   "score": "381106",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Wolfgang",
   "teamId": "4986108131672064",
   "score": "381106",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "💾🔬",
   "teamId": "5034757024907264",
   "score": "380933",
   "hubId": "5218286547501056",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Bierdonka",
   "teamId": "4726929135501312",
   "score": "380809",
   "hubId": "5493471611715584",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Naajak",
   "teamId": "6410257278435328",
   "score": "379960",
   "hubId": "5750033093754880",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "I would tell you a UDP joke, but you might not get it.",
   "teamId": "5150676850049024",
   "score": "378007",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Camouflage",
   "teamId": "4717505977253888",
   "score": "377350",
   "hubId": "5426936595611648",
   "countries": [
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Turkey In Progress",
   "teamId": "5016633537986560",
   "score": "376537",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "RoaringCodeCats",
   "teamId": "4624258479161344",
   "score": "376012",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Schilling",
   "teamId": "5886713918390272",
   "score": "372597",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "on va gagner",
   "teamId": "6737874430984192",
   "score": "371782",
   "hubId": "6606100203831296",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "!Worst",
   "teamId": "4882885370707968",
   "score": "370495",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Marmara OP",
   "teamId": "4865581685669888",
   "score": "368876",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "THE HAPPY DEVS",
   "teamId": "6338451733479424",
   "score": "367386",
   "hubId": "5032995148791808",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "PC-ros",
   "teamId": "6367598925053952",
   "score": "366718",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "M0ly3n",
   "teamId": "4548430563115008",
   "score": "364837",
   "hubId": "5378351053144064",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "350b++",
   "teamId": "5841850434846720",
   "score": "364575",
   "hubId": "4669383217512448",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Goof Troop",
   "teamId": "4964077633798144",
   "score": "364565",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "we#",
   "teamId": "5588784385097728",
   "score": "363433",
   "hubId": "5042625404993536",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "den exw fantasia(I have no imagination)",
   "teamId": "5161998115405824",
   "score": "361243",
   "hubId": "6651476264878080",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Stellae",
   "teamId": "5458285360578560",
   "score": "360745",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "And yet it compiles...",
   "teamId": "4726346966106112",
   "score": "357437",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "MegaCodeSnake",
   "teamId": "4731318122315776",
   "score": "356492",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Triton",
   "teamId": "4992326170574848",
   "score": "356325",
   "hubId": "5082182590660608",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "JCT 2012",
   "teamId": "5410087774453760",
   "score": "356170",
   "hubId": "4902624503529472",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "CoderPrideAndPretty",
   "teamId": "5157680062660608",
   "score": "352772",
   "hubId": "5218381573652480",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "KnedlDev",
   "teamId": "5587093912813568",
   "score": "352169",
   "hubId": "0",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "S-V-S",
   "teamId": "4794041220726784",
   "score": "350839",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "The Dynamically Programmed",
   "teamId": "5723376379232256",
   "score": "350404",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "NHNP",
   "teamId": "5120759450042368",
   "score": "348153",
   "hubId": "4878183723696128",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "no matter what it is",
   "teamId": "5791943585955840",
   "score": "345305",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "LaVieEnCode",
   "teamId": "5120984667389952",
   "score": "344804",
   "hubId": "5436096754221056",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "TableTeam",
   "teamId": "6008690452725760",
   "score": "343241",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "n7ption",
   "teamId": "6189520655482880",
   "score": "343042",
   "hubId": "5842748150120448",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Angry Geese",
   "teamId": "5253130543431680",
   "score": "342897",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Malivianos",
   "teamId": "5402542255112192",
   "score": "342525",
   "hubId": "0",
   "countries": [
    "Denmark",
    "Denmark"
   ]
  },
  {
   "teamName": "Epi3AJzr",
   "teamId": "5133870307475456",
   "score": "340862",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "ENSAE",
   "teamId": "5634360497668096",
   "score": "339319",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "baguette",
   "teamId": "5578281914990592",
   "score": "337520",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SGS",
   "teamId": "4998481731125248",
   "score": "337068",
   "hubId": "6002229748170752",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "We tried to find a name, but guess what?",
   "teamId": "5595623919190016",
   "score": "336827",
   "hubId": "5888717453524992",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "RedMoud",
   "teamId": "4915900717203456",
   "score": "335049",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "D̳̙͔͈͈ͦ⚆⚆D̳̙͔͈͈ͦ",
   "teamId": "5013000599633920",
   "score": "333512",
   "hubId": "4715927375446016",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "HallenbodenJungs",
   "teamId": "5856799806717952",
   "score": "329593",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "YouCanYouUp",
   "teamId": "6648069349179392",
   "score": "329522",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Vienna Scala User Group",
   "teamId": "6581590301868032",
   "score": "328604",
   "hubId": "0",
   "countries": [
    "Austria",
    "Austria"
   ]
  },
  {
   "teamName": "MB Coder Strike",
   "teamId": "5152283100708864",
   "score": "325462",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "L7ou team",
   "teamId": "6475665603821568",
   "score": "324775",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "A Team Name",
   "teamId": "5548300627345408",
   "score": "321683",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "SHA-2 Hash",
   "teamId": "6611615814254592",
   "score": "321587",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Ocono team",
   "teamId": "6493516897189888",
   "score": "320959",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Theta",
   "teamId": "5120724553433088",
   "score": "319484",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Oak's Hashers",
   "teamId": "6255789115179008",
   "score": "317882",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "tigoa",
   "teamId": "6258961686724608",
   "score": "317783",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "LAIT",
   "teamId": "5575743052447744",
   "score": "317429",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Default",
   "teamId": "4834061256228864",
   "score": "316891",
   "hubId": "4946699726356480",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "RamenTesBaskets",
   "teamId": "6700140190498816",
   "score": "315422",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Gens'bons",
   "teamId": "5384281463455744",
   "score": "313426",
   "hubId": "4762512469786624",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "IfWeWinWeGoForABeer",
   "teamId": "4749109487468544",
   "score": "312200",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "FenceTeam",
   "teamId": "4715402517020672",
   "score": "312067",
   "hubId": "5107936288309248",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "iGoogle",
   "teamId": "5639571903610880",
   "score": "311238",
   "hubId": "6297094285426688",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Peak",
   "teamId": "5993048517378048",
   "score": "310615",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Konkret",
   "teamId": "6289020820652032",
   "score": "310601",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "BlackDevilsTeam",
   "teamId": "5724479581847552",
   "score": "308540",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "fear_of_calculus",
   "teamId": "5809339344355328",
   "score": "308497",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "roboto-ftw",
   "teamId": "5143695850471424",
   "score": "308403",
   "hubId": "6026378671554560",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Hedgehog team",
   "teamId": "5338302697701376",
   "score": "306037",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "QUANTUM",
   "teamId": "6423740791390208",
   "score": "305734",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Fridge Raiders",
   "teamId": "5267398156353536",
   "score": "303908",
   "hubId": "0",
   "countries": [
    "Slovakia",
    "Czech Republic",
    "Slovakia"
   ]
  },
  {
   "teamName": "Wait what is going on?",
   "teamId": "5242507747131392",
   "score": "302911",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Kong Fu Pandas",
   "teamId": "5610509202096128",
   "score": "302837",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "KPP",
   "teamId": "5898290264539136",
   "score": "302758",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Coffee Compilers",
   "teamId": "5097281816625152",
   "score": "301563",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Wa",
   "teamId": "6691883921178624",
   "score": "299211",
   "hubId": "6522670732541952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "SentinelJS",
   "teamId": "4680518322880512",
   "score": "298713",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "DanielCOBryanRC",
   "teamId": "5006902752706560",
   "score": "295616",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "#teamUnlucky",
   "teamId": "5324201850306560",
   "score": "295095",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Something",
   "teamId": "4578859332665344",
   "score": "295010",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "The Winners",
   "teamId": "6300561733320704",
   "score": "293869",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "CPUMons 2",
   "teamId": "4700335570419712",
   "score": "291585",
   "hubId": "5547296812957696",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "TheRealMinProgStaff",
   "teamId": "5939225799163904",
   "score": "288509",
   "hubId": "6072168123203584",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Chapines",
   "teamId": "5670311991181312",
   "score": "288269",
   "hubId": "5436096754221056",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Alpha",
   "teamId": "5971147875155968",
   "score": "287503",
   "hubId": "0",
   "countries": [
    "Germany",
    "Romania"
   ]
  },
  {
   "teamName": "MONSter",
   "teamId": "4585754701332480",
   "score": "285874",
   "hubId": "5547296812957696",
   "countries": [
    "Belgium",
    "Italy",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "While(True){code}",
   "teamId": "5719493460361216",
   "score": "283638",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Who is 67?",
   "teamId": "5456568380293120",
   "score": "283270",
   "hubId": "6297094285426688",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "MinionPower",
   "teamId": "6237486313373696",
   "score": "277159",
   "hubId": "4535562237116416",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Cheesy",
   "teamId": "4514009688571904",
   "score": "276434",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "BananaCode",
   "teamId": "6350564212342784",
   "score": "276270",
   "hubId": "4747890253627392",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Pemar",
   "teamId": "5609873278500864",
   "score": "275841",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Oods",
   "teamId": "5343276336939008",
   "score": "275319",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "The Eleven Ds",
   "teamId": "6280598725328896",
   "score": "274305",
   "hubId": "5419392015794176",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "StringNotFoundException",
   "teamId": "5441741884751872",
   "score": "272933",
   "hubId": "6128413739843584",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "PuntoyComa",
   "teamId": "4563254105866240",
   "score": "272124",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "180 Grados",
   "teamId": "6229932271206400",
   "score": "271720",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "UberNerds",
   "teamId": "5371892294746112",
   "score": "270250",
   "hubId": "5941301006565376",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "#codematterwhat",
   "teamId": "5706328513183744",
   "score": "269749",
   "hubId": "5426936595611648",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Die Vorherrscher",
   "teamId": "5022757423153152",
   "score": "267714",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "SofDev",
   "teamId": "5142576474619904",
   "score": "266140",
   "hubId": "0",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "MARBLE",
   "teamId": "5688716597133312",
   "score": "264256",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Cyber Cats",
   "teamId": "5544022839918592",
   "score": "263941",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "404 NOTFOUND",
   "teamId": "4848045669744640",
   "score": "262688",
   "hubId": "5262452031750144",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Black Bamba",
   "teamId": "6483253535965184",
   "score": "261426",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Skills & the Codin' Crew",
   "teamId": "4753187022045184",
   "score": "260672",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Pixxa",
   "teamId": "4860672538050560",
   "score": "260591",
   "hubId": "5930565601591296",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "au thé",
   "teamId": "5964747904122880",
   "score": "260148",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "CodeyMcCodeface",
   "teamId": "6297742624161792",
   "score": "259201",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Tauriel",
   "teamId": "5347116239028224",
   "score": "256333",
   "hubId": "0",
   "countries": [
    "Madagascar",
    "Madagascar"
   ]
  },
  {
   "teamName": "WeCanMakePizza",
   "teamId": "6097170604228608",
   "score": "256331",
   "hubId": "4715927375446016",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Power woof",
   "teamId": "5376445832495104",
   "score": "254880",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Hungry Code",
   "teamId": "4709111866327040",
   "score": "252781",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Ege University Code Line",
   "teamId": "6102487438196736",
   "score": "252051",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "As you wish",
   "teamId": "4797553161797632",
   "score": "251840",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "GEinside",
   "teamId": "6223639137484800",
   "score": "249538",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team42",
   "teamId": "6567384965971968",
   "score": "249140",
   "hubId": "5699128336056320",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Germany"
   ]
  },
  {
   "teamName": "sublinear",
   "teamId": "4589449379840000",
   "score": "248343",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "TamExRot",
   "teamId": "5068292263772160",
   "score": "247898",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Smartappeurs",
   "teamId": "6483309370540032",
   "score": "247193",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Freshmen",
   "teamId": "5082898776457216",
   "score": "247161",
   "hubId": "0",
   "countries": [
    "Morocco",
    "Morocco",
    "Morocco",
    "Morocco"
   ]
  },
  {
   "teamName": "noma",
   "teamId": "5631728488022016",
   "score": "245421",
   "hubId": "6218891520901120",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "Croquetas de cocido",
   "teamId": "6355963791540224",
   "score": "244899",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Skerface",
   "teamId": "4668262298157056",
   "score": "243464",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "#teamjay",
   "teamId": "6662955236065280",
   "score": "243242",
   "hubId": "6218891520901120",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "Babtous Tranquilles",
   "teamId": "6402740079034368",
   "score": "241151",
   "hubId": "4825119939624960",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Sputnik",
   "teamId": "4513970228559872",
   "score": "240407",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Databoere",
   "teamId": "5431760112320512",
   "score": "239238",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "sdk-j?",
   "teamId": "5207803337637888",
   "score": "236510",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Jedi Academy",
   "teamId": "6314782906908672",
   "score": "231210",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "The latent people",
   "teamId": "6222404334387200",
   "score": "229214",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Pythonic Spartans",
   "teamId": "5712167521222656",
   "score": "229023",
   "hubId": "4892331278860288",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "ScorpionTech",
   "teamId": "5712751905210368",
   "score": "226865",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "☕☕☕",
   "teamId": "6620356072701952",
   "score": "223838",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Vraa",
   "teamId": "4604798317887488",
   "score": "223819",
   "hubId": "6113594290733056",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "#hellOOworld!",
   "teamId": "4897331157663744",
   "score": "223791",
   "hubId": "4954063850438656",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Mona-Boys",
   "teamId": "5199654979371008",
   "score": "222552",
   "hubId": "6026378671554560",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Segmentation Fault",
   "teamId": "6546254532182016",
   "score": "222485",
   "hubId": "6589328624975872",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Prosti Liudy",
   "teamId": "4818860830097408",
   "score": "222437",
   "hubId": "0",
   "countries": [
    "Estonia",
    "Ukraine"
   ]
  },
  {
   "teamName": "n00ne",
   "teamId": "6688252593438720",
   "score": "220028",
   "hubId": "5634869988163584",
   "countries": [
    "Cyprus",
    "Cyprus",
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "Surfers",
   "teamId": "6243827899695104",
   "score": "219989",
   "hubId": "0",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Engel Power",
   "teamId": "5728959769608192",
   "score": "216673",
   "hubId": "6297094285426688",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Popokatepetl",
   "teamId": "5040052518256640",
   "score": "214905",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Bits Please",
   "teamId": "5733754362396672",
   "score": "214839",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "F. U. L.",
   "teamId": "6150707304464384",
   "score": "214208",
   "hubId": "0",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Teamname",
   "teamId": "4649565567320064",
   "score": "212842",
   "hubId": "6324625227120640",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "11H30 RAB",
   "teamId": "6555934314725376",
   "score": "210128",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "PyTeam",
   "teamId": "5631381400977408",
   "score": "208759",
   "hubId": "4742957617905664",
   "countries": [
    "Norway",
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "Creative Thinkers",
   "teamId": "6282798822326272",
   "score": "208226",
   "hubId": "0",
   "countries": [
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "shooting-8",
   "teamId": "6216974421983232",
   "score": "208140",
   "hubId": "5841827282288640",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Hot Wheels",
   "teamId": "5437984392347648",
   "score": "208044",
   "hubId": "4756671180046336",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TTS team",
   "teamId": "5644791094181888",
   "score": "208037",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Coding Monkeys",
   "teamId": "6576255348506624",
   "score": "207647",
   "hubId": "6448591136620544",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CyborgsAbed",
   "teamId": "5062675587399680",
   "score": "205889",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "viu",
   "teamId": "6265264417013760",
   "score": "205889",
   "hubId": "0",
   "countries": [
    "Belarus",
    "Belarus",
    "Belarus"
   ]
  },
  {
   "teamName": "0xCAFEBABE",
   "teamId": "6105984615317504",
   "score": "205889",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Terawiz",
   "teamId": "6593809215389696",
   "score": "204394",
   "hubId": "6561201823678464",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "sudo",
   "teamId": "5919967971115008",
   "score": "202943",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Hush Code",
   "teamId": "5629048428429312",
   "score": "202544",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "XMWhite",
   "teamId": "4693082175963136",
   "score": "200705",
   "hubId": "0",
   "countries": [
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "Αρφούθκια",
   "teamId": "5551388440395776",
   "score": "200169",
   "hubId": "5645240186699776",
   "countries": [
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "BaraBashka",
   "teamId": "4866272437207040",
   "score": "198880",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "TN2CY",
   "teamId": "4591467477598208",
   "score": "196652",
   "hubId": "6026378671554560",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "The_Pempers",
   "teamId": "5340767472058368",
   "score": "196269",
   "hubId": "0",
   "countries": [
    "Cyprus",
    "Cyprus"
   ]
  },
  {
   "teamName": "El Góog",
   "teamId": "6211957631746048",
   "score": "192819",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Antonio e Errica",
   "teamId": "4760335189803008",
   "score": "191288",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "##ins",
   "teamId": "5662456495996928",
   "score": "191181",
   "hubId": "4805530728005632",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Brugnetti",
   "teamId": "5534391375757312",
   "score": "190511",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Neko",
   "teamId": "6369368183144448",
   "score": "186610",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "APlus",
   "teamId": "5018142682120192",
   "score": "186454",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Public Static Boys",
   "teamId": "5385321650847744",
   "score": "184078",
   "hubId": "5886235096645632",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Murphys' Crew",
   "teamId": "5630612601831424",
   "score": "182986",
   "hubId": "5931430634848256",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "France"
   ]
  },
  {
   "teamName": "GROVERADES",
   "teamId": "5232749581434880",
   "score": "182202",
   "hubId": "5397940264763392",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "ST2",
   "teamId": "4930163833831424",
   "score": "181588",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "noobs",
   "teamId": "6346352728473600",
   "score": "180708",
   "hubId": "0",
   "countries": [
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Sodifrance-Rennes-java",
   "teamId": "5151470345256960",
   "score": "180002",
   "hubId": "5201755822358528",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Alumni Mathematica",
   "teamId": "5062270048534528",
   "score": "179001",
   "hubId": "5481129956081664",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Beznazwy",
   "teamId": "6124323857235968",
   "score": "178924",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "SHIELD",
   "teamId": "6202678891773952",
   "score": "178476",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Power4----",
   "teamId": "5664246490726400",
   "score": "178438",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "from teams import name",
   "teamId": "6673971827179520",
   "score": "174864",
   "hubId": "6029454941880320",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "BizNoobs",
   "teamId": "5178177190100992",
   "score": "173989",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Belgium"
   ]
  },
  {
   "teamName": "D3KRYPT",
   "teamId": "6655825858789376",
   "score": "168679",
   "hubId": "5634869988163584",
   "countries": [
    "Cyprus",
    "Turkey"
   ]
  },
  {
   "teamName": "Henlo World",
   "teamId": "5379640147312640",
   "score": "168632",
   "hubId": "5123864979832832",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Les cadres dynamiques et motivés",
   "teamId": "5668943775662080",
   "score": "167272",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Юность",
   "teamId": "5679793399922688",
   "score": "165607",
   "hubId": "4910236997517312",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Tallaght CompSoc TeamA",
   "teamId": "6073561101893632",
   "score": "165532",
   "hubId": "4833820872278016",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "CinAli",
   "teamId": "5736297318580224",
   "score": "165515",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Let's C#",
   "teamId": "5686287927345152",
   "score": "164607",
   "hubId": "5042625404993536",
   "countries": [
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan",
    "Azerbaijan"
   ]
  },
  {
   "teamName": "Pal Beginners",
   "teamId": "5718386633867264",
   "score": "164584",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "turing-complete",
   "teamId": "5848597157380096",
   "score": "163930",
   "hubId": "4936954646888448",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "USALtics",
   "teamId": "5445707750178816",
   "score": "163884",
   "hubId": "5807719806140416",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Team '); DROP TABLE Teams; --",
   "teamId": "5204460309577728",
   "score": "162645",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Kanzu Code",
   "teamId": "5144216145494016",
   "score": "162118",
   "hubId": "0",
   "countries": [
    "Uganda",
    "Uganda",
    "Uganda",
    "Uganda"
   ]
  },
  {
   "teamName": "sed '1!G;h;$!d'",
   "teamId": "5221089349206016",
   "score": "161870",
   "hubId": "4756896531611648",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Alemañoles",
   "teamId": "6195172564008960",
   "score": "161357",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "#4$",
   "teamId": "6377442990096384",
   "score": "160274",
   "hubId": "4560691285458944",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "HashTek",
   "teamId": "6299561542811648",
   "score": "159004",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team-Scotch",
   "teamId": "5280583773061120",
   "score": "158898",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "StraksKnaltIeMisschienWel",
   "teamId": "6061096905474048",
   "score": "158280",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "HACERMEN",
   "teamId": "5067726737375232",
   "score": "157313",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "Les 4 As",
   "teamId": "5883307740889088",
   "score": "157251",
   "hubId": "5983641666584576",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "​",
   "teamId": "4641854423302144",
   "score": "153561",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Echipa Rachetă 🚀",
   "teamId": "6410917629657088",
   "score": "152766",
   "hubId": "4892331278860288",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Speedy team",
   "teamId": "5796006088146944",
   "score": "152766",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "PROMOTIC",
   "teamId": "4926248232943616",
   "score": "152544",
   "hubId": "5459743099322368",
   "countries": [
    "Togo",
    "Togo"
   ]
  },
  {
   "teamName": "xXx_G3Ck0-$qU@D_xXx",
   "teamId": "5262845222584320",
   "score": "151107",
   "hubId": "6522670732541952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Googleros",
   "teamId": "5136952751816704",
   "score": "150104",
   "hubId": "5452279385686016",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Team Vanguard",
   "teamId": "5800310249357312",
   "score": "147535",
   "hubId": "0",
   "countries": [
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "RoboTUM",
   "teamId": "6727957687042048",
   "score": "147006",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Elder_Iron",
   "teamId": "4549499808645120",
   "score": "146339",
   "hubId": "6108803657367552",
   "countries": [
    "United Kingdom",
    "Iraq",
    "United Kingdom",
    "Qatar"
   ]
  },
  {
   "teamName": "dtqty",
   "teamId": "5705526428041216",
   "score": "145651",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Biobest",
   "teamId": "5690146418589696",
   "score": "142962",
   "hubId": "6572544966524928",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "HashCat",
   "teamId": "6093716578107392",
   "score": "142730",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "EpiSwag",
   "teamId": "6690947953852416",
   "score": "142607",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Code Tsars",
   "teamId": "6500127053185024",
   "score": "141188",
   "hubId": "0",
   "countries": [
    "Malta",
    "Bulgaria"
   ]
  },
  {
   "teamName": "Code for fun",
   "teamId": "5233769166405632",
   "score": "140595",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Les shlags",
   "teamId": "5326600052670464",
   "score": "139082",
   "hubId": "6606100203831296",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "HCT",
   "teamId": "4714742165798912",
   "score": "138503",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Mon sac est fait !",
   "teamId": "5205950327685120",
   "score": "138030",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "les sabauteurs",
   "teamId": "6491405048348672",
   "score": "137751",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Gryfno",
   "teamId": "6206896012787712",
   "score": "137001",
   "hubId": "5493471611715584",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Roosters",
   "teamId": "5438018483650560",
   "score": "135762",
   "hubId": "4635775366856704",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Eureka",
   "teamId": "5246878950096896",
   "score": "135646",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "DonNU_Fearless",
   "teamId": "6196519573127168",
   "score": "134950",
   "hubId": "6602827975622656",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "ft_putchar",
   "teamId": "5575950553055232",
   "score": "134736",
   "hubId": "4715927375446016",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "BioRevolution",
   "teamId": "5014994538201088",
   "score": "133629",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CSCI152",
   "teamId": "5338113182269440",
   "score": "132713",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "THE team!",
   "teamId": "4520784462610432",
   "score": "132343",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "MotherPoliExperts",
   "teamId": "5644980542504960",
   "score": "131855",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Unprogramers",
   "teamId": "5544685271515136",
   "score": "130510",
   "hubId": "6540885420408832",
   "countries": [
    "Georgia",
    "Georgia",
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "MythoKoko",
   "teamId": "5855157787033600",
   "score": "129906",
   "hubId": "5453207232839680",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Tugas de Bigode",
   "teamId": "4886643936854016",
   "score": "129906",
   "hubId": "6079963757281280",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Pilote2lignes",
   "teamId": "4587490874753024",
   "score": "128146",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "iGOLAN",
   "teamId": "4716183999741952",
   "score": "127492",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Google Task Force",
   "teamId": "5664900399497216",
   "score": "125902",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "MECians",
   "teamId": "4683474803884032",
   "score": "125852",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Epita and chill",
   "teamId": "4786144654917632",
   "score": "124947",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "War-room",
   "teamId": "4919364339892224",
   "score": "124658",
   "hubId": "5774946588426240",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "2ror2.718l",
   "teamId": "5688643247144960",
   "score": "123449",
   "hubId": "6412182296199168",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Nemishayeve",
   "teamId": "4570111826460672",
   "score": "122697",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Unitunes",
   "teamId": "4533061358190592",
   "score": "122358",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Team Overcliking",
   "teamId": "6520464058875904",
   "score": "120273",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "DevTwist",
   "teamId": "5815233650098176",
   "score": "120188",
   "hubId": "5737226507911168",
   "countries": [
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Taikila",
   "teamId": "5541169102585856",
   "score": "118279",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Unexpected Pressure",
   "teamId": "6681174151790592",
   "score": "117555",
   "hubId": "6219412285685760",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "PornCode s karlikami",
   "teamId": "5593335238492160",
   "score": "116461",
   "hubId": "4715927375446016",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Amber",
   "teamId": "4580025416286208",
   "score": "116314",
   "hubId": "0",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Polyteam",
   "teamId": "4931902758715392",
   "score": "114718",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team++",
   "teamId": "5394979086139392",
   "score": "114657",
   "hubId": "6224891120451584",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Spark",
   "teamId": "4580714758537216",
   "score": "114174",
   "hubId": "5774946588426240",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "saarnix",
   "teamId": "6022444884164608",
   "score": "113714",
   "hubId": "6156894674616320",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "ULUS-SENTEPE-HATTI",
   "teamId": "4785890513649664",
   "score": "112698",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "#DCoders",
   "teamId": "4988214007824384",
   "score": "112312",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia",
    "Saudi Arabia"
   ]
  },
  {
   "teamName": "Crackers",
   "teamId": "6732318353915904",
   "score": "111950",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Alexa",
   "teamId": "6408590562689024",
   "score": "111423",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "Winning",
   "teamId": "6710140484976640",
   "score": "110141",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Kurdistan",
   "teamId": "5248444331458560",
   "score": "108639",
   "hubId": "6022693052743680",
   "countries": [
    "Iraq",
    "Iraq"
   ]
  },
  {
   "teamName": "Grab 'em by the bit",
   "teamId": "6565277210771456",
   "score": "107564",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Frivor",
   "teamId": "5113504109428736",
   "score": "106698",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "ISTIC DEV",
   "teamId": "6307852440305664",
   "score": "106667",
   "hubId": "5459271793770496",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Les rejetés de la rangée 4",
   "teamId": "5513871833956352",
   "score": "106556",
   "hubId": "4775163228848128",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Almöhi",
   "teamId": "6097231471968256",
   "score": "105347",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Asssio",
   "teamId": "4504879594733568",
   "score": "105091",
   "hubId": "0",
   "countries": [
    "Madagascar",
    "Mauritius"
   ]
  },
  {
   "teamName": "BanzaiCoders",
   "teamId": "5679664349577216",
   "score": "104969",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "nightwish",
   "teamId": "5177074323030016",
   "score": "104879",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "/dev/random",
   "teamId": "5689154012708864",
   "score": "104779",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium",
    "Netherlands",
    "Belgium"
   ]
  },
  {
   "teamName": "Schlaggos 2.0",
   "teamId": "5333965720256512",
   "score": "104779",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "GhostShadow",
   "teamId": "4594044793520128",
   "score": "104779",
   "hubId": "6218891520901120",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "THE GONSALES & CO",
   "teamId": "6242625241743360",
   "score": "104779",
   "hubId": "5107936288309248",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "More than conquerors",
   "teamId": "4631409935253504",
   "score": "104779",
   "hubId": "6218891520901120",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "MKMTest",
   "teamId": "6130222256619520",
   "score": "104779",
   "hubId": "5699128336056320",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Blazing Phoenix",
   "teamId": "5980044967018496",
   "score": "104779",
   "hubId": "5661462143959040",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Team Genius",
   "teamId": "5653792808763392",
   "score": "104779",
   "hubId": "6218891520901120",
   "countries": [
    "Kenya",
    "Kenya",
    "Kenya",
    "Kenya"
   ]
  },
  {
   "teamName": "back-frontEND",
   "teamId": "5579314519080960",
   "score": "104779",
   "hubId": "5459743099322368",
   "countries": [
    "Togo",
    "Togo",
    "Togo"
   ]
  },
  {
   "teamName": "Epictek",
   "teamId": "6574507632361472",
   "score": "104779",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "RavenStrike",
   "teamId": "4694886263554048",
   "score": "104779",
   "hubId": "0",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "P-t&Papa ftw",
   "teamId": "5696011733303296",
   "score": "104779",
   "hubId": "4669383217512448",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Schrödinger's Code",
   "teamId": "5213361562189824",
   "score": "104779",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Titanic",
   "teamId": "5032063744868352",
   "score": "104779",
   "hubId": "5876531087802368",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "EMPeroRs",
   "teamId": "5028568916557824",
   "score": "104779",
   "hubId": "5654545635999744",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "B=NB",
   "teamId": "6054013363552256",
   "score": "104779",
   "hubId": "4651937261682688",
   "countries": [
    "Qatar",
    "Qatar",
    "Qatar",
    "Qatar"
   ]
  },
  {
   "teamName": "Epicode",
   "teamId": "5743018606854144",
   "score": "104779",
   "hubId": "5463428718133248",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Random()",
   "teamId": "6243191976099840",
   "score": "104779",
   "hubId": "4852035560144896",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "3ng11n33r5",
   "teamId": "6327054635106304",
   "score": "104779",
   "hubId": "5654545635999744",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "DuckDuckGo",
   "teamId": "5242082948022272",
   "score": "104779",
   "hubId": "5800563518210048",
   "countries": [
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Firehawks",
   "teamId": "5157069640433664",
   "score": "104169",
   "hubId": "6711077593153536",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Godzillax",
   "teamId": "5498211846324224",
   "score": "99737",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "K.Racsh Code",
   "teamId": "6277909002059776",
   "score": "98088",
   "hubId": "5686814933254144",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Green Star",
   "teamId": "5016554617962496",
   "score": "96770",
   "hubId": "0",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Switzerland"
   ]
  },
  {
   "teamName": "Team xPair",
   "teamId": "4868627153027072",
   "score": "95588",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Preceq",
   "teamId": "5568096064503808",
   "score": "94518",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "HashCoders",
   "teamId": "6205257415655424",
   "score": "93315",
   "hubId": "5342796374343680",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "A_Seven_A",
   "teamId": "5645073152737280",
   "score": "93175",
   "hubId": "5820837508677632",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "y u do this google?!",
   "teamId": "4839592301690880",
   "score": "92020",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "NienteNome",
   "teamId": "6153410449506304",
   "score": "91979",
   "hubId": "6587443536986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Team CSV",
   "teamId": "6122990068563968",
   "score": "91933",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "GoldenWarriors",
   "teamId": "4595416230264832",
   "score": "91638",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "Congo (the Democratic Republic of the)",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Team Pong|A",
   "teamId": "4857668543971328",
   "score": "91526",
   "hubId": "5635224322965504",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Karma Tec",
   "teamId": "5144942464729088",
   "score": "91055",
   "hubId": "6158895055634432",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "XD",
   "teamId": "6622442889936896",
   "score": "90516",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Log.wtf()",
   "teamId": "6562292409827328",
   "score": "89220",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Z³F",
   "teamId": "5226879501991936",
   "score": "88758",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Stras-IT",
   "teamId": "4672588403965952",
   "score": "86695",
   "hubId": "4830703933980672",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "FAMs",
   "teamId": "5311210312433664",
   "score": "86020",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "skoed",
   "teamId": "6614531023306752",
   "score": "85872",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "Vaina",
   "teamId": "4897447927087104",
   "score": "85660",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Kalarama",
   "teamId": "5265757747281920",
   "score": "83869",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "plop",
   "teamId": "4628777925607424",
   "score": "83420",
   "hubId": "6440370032345088",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Team Coderus",
   "teamId": "4878535105708032",
   "score": "83126",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "kind",
   "teamId": "4926328360927232",
   "score": "82812",
   "hubId": "5156808922497024",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "BinärFabrik",
   "teamId": "6624473604161536",
   "score": "82741",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Les nains décis",
   "teamId": "6269564618801152",
   "score": "82705",
   "hubId": "6606100203831296",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Powered by ICSD",
   "teamId": "4697629942349824",
   "score": "81790",
   "hubId": "5654545635999744",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "High5-IT",
   "teamId": "4936349324935168",
   "score": "81066",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Rooster",
   "teamId": "5109205451145216",
   "score": "80169",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Just code",
   "teamId": "5205059658842112",
   "score": "79132",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "We will never walk alone",
   "teamId": "6437341946183680",
   "score": "78852",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "Light Beam",
   "teamId": "5474143923339264",
   "score": "78852",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "EpiStrasTeamNumber1",
   "teamId": "5428530900893696",
   "score": "78852",
   "hubId": "4602220129550336",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Noobs in the Shell",
   "teamId": "6522827029086208",
   "score": "78838",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Rangée 4",
   "teamId": "6384743562084352",
   "score": "78805",
   "hubId": "4775163228848128",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "C4G",
   "teamId": "4903512488017920",
   "score": "78278",
   "hubId": "0",
   "countries": [
    "Uganda",
    "Uganda",
    "Uganda"
   ]
  },
  {
   "teamName": "IPCV WARRIOS",
   "teamId": "4932243134873600",
   "score": "77522",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "EZ",
   "teamId": "5344169891463168",
   "score": "76501",
   "hubId": "4602220129550336",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Objects",
   "teamId": "4505077767208960",
   "score": "74133",
   "hubId": "5074919532527616",
   "countries": [
    "Norway",
    "Norway",
    "Norway"
   ]
  },
  {
   "teamName": "RoundCorner",
   "teamId": "6569534597103616",
   "score": "73377",
   "hubId": "6651476264878080",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "<cod3 it/>",
   "teamId": "5638721432977408",
   "score": "72913",
   "hubId": "5968066169012224",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Scorpion",
   "teamId": "6294018820407296",
   "score": "71725",
   "hubId": "4812037402132480",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "LeanApexMolder",
   "teamId": "6753879358177280",
   "score": "69763",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "BOOKZ",
   "teamId": "5732439766859776",
   "score": "68780",
   "hubId": "5749903439429632",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "SaxonwoldShebeen",
   "teamId": "6051909366448128",
   "score": "66230",
   "hubId": "0",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Core Rage",
   "teamId": "6045264246734848",
   "score": "64426",
   "hubId": "5774946588426240",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Draxis",
   "teamId": "5918508286214144",
   "score": "64088",
   "hubId": "5197679093088256",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "ajolote",
   "teamId": "5692397048561664",
   "score": "64043",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Team Three-And-A-Half Star",
   "teamId": "6012885897576448",
   "score": "62961",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Impériaux",
   "teamId": "5082407472463872",
   "score": "62434",
   "hubId": "5241248851951616",
   "countries": [
    "Togo",
    "Togo"
   ]
  },
  {
   "teamName": "ElemonZ",
   "teamId": "5834003529596928",
   "score": "61614",
   "hubId": "5731969266614272",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TPPBCBPGAMQFVIPA",
   "teamId": "5142897858969600",
   "score": "61594",
   "hubId": "5797216933380096",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Free Points/Pints",
   "teamId": "6591475773079552",
   "score": "61172",
   "hubId": "6324625227120640",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "coconut",
   "teamId": "6501654987800576",
   "score": "60124",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "D&O",
   "teamId": "5676682098769920",
   "score": "59917",
   "hubId": "5123864979832832",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "The Unicorns",
   "teamId": "5312580943872000",
   "score": "59525",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "COsbor krew",
   "teamId": "4848805543411712",
   "score": "59338",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Eder",
   "teamId": "5747674888273920",
   "score": "59270",
   "hubId": "5440298305978368",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Rhinos",
   "teamId": "6428167023624192",
   "score": "58626",
   "hubId": "0",
   "countries": [
    "Hungary",
    "Hungary",
    "Hungary",
    "Hungary"
   ]
  },
  {
   "teamName": "Entry Level Position",
   "teamId": "6252289723465728",
   "score": "58454",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Khal Drono",
   "teamId": "5708202259775488",
   "score": "56856",
   "hubId": "6113594290733056",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Coded",
   "teamId": "5864659328434176",
   "score": "56843",
   "hubId": "5128325034934272",
   "countries": [
    "Oman",
    "Oman",
    "Oman"
   ]
  },
  {
   "teamName": "Who asked for fun?",
   "teamId": "5290134371041280",
   "score": "56206",
   "hubId": "0",
   "countries": [
    "Austria",
    "Switzerland"
   ]
  },
  {
   "teamName": "GUTech",
   "teamId": "6363079545716736",
   "score": "55601",
   "hubId": "5128325034934272",
   "countries": [
    "Oman",
    "Oman",
    "Oman",
    "Oman"
   ]
  },
  {
   "teamName": "Couch potatoes",
   "teamId": "5158770380374016",
   "score": "54991",
   "hubId": "6056421565136896",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "CA squad",
   "teamId": "5757309842096128",
   "score": "54307",
   "hubId": "4552345895567360",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "2/3 Beard",
   "teamId": "5280269099597824",
   "score": "54032",
   "hubId": "6522670732541952",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "GIDD",
   "teamId": "4762113507590144",
   "score": "53561",
   "hubId": "6125008703193088",
   "countries": [
    "Bulgaria",
    "Bulgaria",
    "Bulgaria",
    "Bulgaria"
   ]
  },
  {
   "teamName": "хакер",
   "teamId": "5407079149862912",
   "score": "53393",
   "hubId": "4939374659633152",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Thomaeum Elite",
   "teamId": "4585995152392192",
   "score": "53092",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "FeelsBadMan",
   "teamId": "5418830381711360",
   "score": "51505",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "The Metastables",
   "teamId": "5488630378266624",
   "score": "50057",
   "hubId": "5876531087802368",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "NeverTrustASafetyExpert",
   "teamId": "6015617429667840",
   "score": "49832",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "#Good_Fellas",
   "teamId": "5327392205701120",
   "score": "47809",
   "hubId": "4715927375446016",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "YAAT",
   "teamId": "5290859415207936",
   "score": "45167",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "badness 10000",
   "teamId": "5369534693244928",
   "score": "44132",
   "hubId": "5540597737717760",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Narwhals",
   "teamId": "4680818903482368",
   "score": "44039",
   "hubId": "6723079006846976",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Belin's Army",
   "teamId": "4692587180982272",
   "score": "43794",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": ";DROP TABLE teams",
   "teamId": "5085386434936832",
   "score": "43712",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "The Hashers",
   "teamId": "5972435560038400",
   "score": "42881",
   "hubId": "0",
   "countries": [
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "31415926",
   "teamId": "4999589295816704",
   "score": "39694",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Kazakhstan",
    "Ukraine"
   ]
  },
  {
   "teamName": "MOMA",
   "teamId": "4909088899072000",
   "score": "39385",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "Switzerland"
   ]
  },
  {
   "teamName": "Smartinis",
   "teamId": "4886101227470848",
   "score": "37499",
   "hubId": "5732605190209536",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Belgium",
    "Netherlands"
   ]
  },
  {
   "teamName": "MucBoyz",
   "teamId": "5213332839596032",
   "score": "37042",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "if((pizza||coffee)==0) team=leave;",
   "teamId": "6601678669217792",
   "score": "36608",
   "hubId": "0",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Engines",
   "teamId": "5824445549641728",
   "score": "36608",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Grim team",
   "teamId": "5274829053755392",
   "score": "36339",
   "hubId": "6093677319421952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Real Matrice",
   "teamId": "6108472743559168",
   "score": "36339",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "XERUM",
   "teamId": "6114113914667008",
   "score": "35982",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Pef code",
   "teamId": "5931522037121024",
   "score": "34853",
   "hubId": "4857554190467072",
   "countries": [
    "Slovenia",
    "Slovenia",
    "Slovenia",
    "Slovenia"
   ]
  },
  {
   "teamName": "Deux Pierre d'un coût",
   "teamId": "5762338107949056",
   "score": "34721",
   "hubId": "6522670732541952",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Möö3",
   "teamId": "6321832021983232",
   "score": "34519",
   "hubId": "5968289909964800",
   "countries": [
    "Sweden",
    "Sweden",
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "Herman",
   "teamId": "4833944151261184",
   "score": "34067",
   "hubId": "6156894674616320",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Deemazing",
   "teamId": "6012001134313472",
   "score": "33482",
   "hubId": "5977935466987520",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Tri-Continental Potentially Interesting People",
   "teamId": "6256180426964992",
   "score": "31774",
   "hubId": "5038819124445184",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "Fireproof",
   "teamId": "5950610683723776",
   "score": "30814",
   "hubId": "5774946588426240",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "Just a Team",
   "teamId": "5361430828154880",
   "score": "30182",
   "hubId": "5751703970250752",
   "countries": [
    "Latvia",
    "Latvia",
    "Latvia"
   ]
  },
  {
   "teamName": "kuryatnik",
   "teamId": "4669838551154688",
   "score": "29948",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Stupiak",
   "teamId": "5299472502358016",
   "score": "29358",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "UFC",
   "teamId": "4505828581179392",
   "score": "29268",
   "hubId": "4833820872278016",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "random()",
   "teamId": "6542698232152064",
   "score": "28720",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Lynx",
   "teamId": "6262852658659328",
   "score": "28546",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Excuse My French",
   "teamId": "6033731320020992",
   "score": "27072",
   "hubId": "5842748150120448",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Who is tourist?",
   "teamId": "6665327333081088",
   "score": "26654",
   "hubId": "0",
   "countries": [
    "Egypt",
    "Egypt",
    "Egypt",
    "Egypt"
   ]
  },
  {
   "teamName": "193",
   "teamId": "5931012882169856",
   "score": "26516",
   "hubId": "0",
   "countries": [
    "Russia",
    "Russia"
   ]
  },
  {
   "teamName": "society",
   "teamId": "5691125939568640",
   "score": "26501",
   "hubId": "4671317026537472",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "BlackCoding",
   "teamId": "4729257880190976",
   "score": "26062",
   "hubId": "5417095013597184",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Tunisia",
    "Tunisia"
   ]
  },
  {
   "teamName": "TBA Corp",
   "teamId": "6712250119225344",
   "score": "25748",
   "hubId": "6550668684820480",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Coders in the Wind",
   "teamId": "6720900787339264",
   "score": "24606",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "Road To Zero",
   "teamId": "5938376469381120",
   "score": "24228",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "Most Wanted",
   "teamId": "4818333555752960",
   "score": "23757",
   "hubId": "0",
   "countries": [
    "Netherlands",
    "Netherlands",
    "Netherlands",
    "Netherlands"
   ]
  },
  {
   "teamName": "S'tekHash&",
   "teamId": "4922685154918400",
   "score": "22580",
   "hubId": "5044292523393024",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Team Pigritia",
   "teamId": "5825497816629248",
   "score": "22580",
   "hubId": "6337896541847552",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Median Earth",
   "teamId": "5716087752622080",
   "score": "22338",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "High5",
   "teamId": "5690638058127360",
   "score": "22174",
   "hubId": "0",
   "countries": [
    "Georgia",
    "Georgia"
   ]
  },
  {
   "teamName": "Planoprax",
   "teamId": "6577550818017280",
   "score": "19148",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "👁‍🗨",
   "teamId": "5392595110854656",
   "score": "18704",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "WolfPack",
   "teamId": "5912496070197248",
   "score": "15451",
   "hubId": "6224412097380352",
   "countries": [
    "Jordan",
    "Jordan",
    "Jordan",
    "Jordan"
   ]
  },
  {
   "teamName": "Build a firewall",
   "teamId": "6674200534188032",
   "score": "15157",
   "hubId": "4946268216360960",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "T.O.P. of Hell",
   "teamId": "5476031561465856",
   "score": "11056",
   "hubId": "6238078817533952",
   "countries": [
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Rain",
   "teamId": "5038737318739968",
   "score": "10937",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "iTeam",
   "teamId": "5402744990990336",
   "score": "9987",
   "hubId": "6400147932053504",
   "countries": [
    "Nigeria",
    "Nigeria",
    "Nigeria",
    "Nigeria"
   ]
  },
  {
   "teamName": "EpiHashCode",
   "teamId": "6751730331025408",
   "score": "9116",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Fetele de la Poli",
   "teamId": "4885800512651264",
   "score": "7628",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "ZugiMonster",
   "teamId": "6416439346987008",
   "score": "6150",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Ever Est",
   "teamId": "6647919562194944",
   "score": "5703",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "creamdreamteam",
   "teamId": "4909464574492672",
   "score": "5703",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "G-Force",
   "teamId": "4567875490676736",
   "score": "5660",
   "hubId": "6317611881070592",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "NordishCodersByNature",
   "teamId": "6216116166721536",
   "score": "5455",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Droiders",
   "teamId": "5358042166067200",
   "score": "5419",
   "hubId": "5419392015794176",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "OzVNGRS",
   "teamId": "6069211105329152",
   "score": "4974",
   "hubId": "5096876076433408",
   "countries": [
    "Turkey",
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "HenrikNMatthias100years",
   "teamId": "5270311486357504",
   "score": "4920",
   "hubId": "0",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "Mitochondria is the powerhouse of the cell",
   "teamId": "6289097727410176",
   "score": "4840",
   "hubId": "6029454941880320",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Fingers Crossed",
   "teamId": "6541607444676608",
   "score": "4667",
   "hubId": "5776152937365504",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "MemeTeam2",
   "teamId": "6512777074049024",
   "score": "4262",
   "hubId": "5766567912538112",
   "countries": [
    "Croatia",
    "Croatia",
    "Croatia",
    "Croatia"
   ]
  },
  {
   "teamName": "Swipe",
   "teamId": "4523750942834688",
   "score": "4258",
   "hubId": "0",
   "countries": [
    "Belgium",
    "Belgium",
    "Belgium",
    "Belgium"
   ]
  },
  {
   "teamName": "GD Lviv",
   "teamId": "5327651178807296",
   "score": "3887",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "Stingin' Roger",
   "teamId": "5137604043341824",
   "score": "3773",
   "hubId": "6210985626959872",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Octetul cel Voinic",
   "teamId": "4891608382177280",
   "score": "3105",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Make C Great Again",
   "teamId": "6409504585416704",
   "score": "2634",
   "hubId": "0",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "Espondas Jünger",
   "teamId": "6166792024096768",
   "score": "2445",
   "hubId": "6043150250409984",
   "countries": [
    "Germany",
    "Germany",
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "UNIPA Team",
   "teamId": "5224988642639872",
   "score": "2440",
   "hubId": "6698592592986112",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "GasPeople",
   "teamId": "5862454869360640",
   "score": "1995",
   "hubId": "0",
   "countries": [
    "Saudi Arabia",
    "Saudi Arabia",
    "Egypt"
   ]
  },
  {
   "teamName": "Team Hot Wheels",
   "teamId": "4979987065077760",
   "score": "1758",
   "hubId": "4721081336201216",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "The Papayas",
   "teamId": "5877901719240704",
   "score": "1612",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland",
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "keskon fou la",
   "teamId": "6578199089643520",
   "score": "1212",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "RandomTeam",
   "teamId": "5436757575204864",
   "score": "1203",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "IBWT",
   "teamId": "5627679139168256",
   "score": "1096",
   "hubId": "4751520172081152",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "It Wasn't Our Volt!",
   "teamId": "5840672942718976",
   "score": "1037",
   "hubId": "5776152937365504",
   "countries": [
    "Russia",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "Mango",
   "teamId": "4944102814646272",
   "score": "951",
   "hubId": "0",
   "countries": [
    "Sweden",
    "Sweden",
    "Turkey"
   ]
  },
  {
   "teamName": "NADE",
   "teamId": "6446647462592512",
   "score": "910",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "coding",
   "teamId": "5223102279581696",
   "score": "874",
   "hubId": "5128325034934272",
   "countries": [
    "Oman",
    "Oman",
    "Oman",
    "Oman"
   ]
  },
  {
   "teamName": "DarthFletcher",
   "teamId": "6277188185751552",
   "score": "866",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "LAN-isters",
   "teamId": "5957111385161728",
   "score": "848",
   "hubId": "0",
   "countries": [
    "Malta",
    "Malta",
    "Malta",
    "Malta"
   ]
  },
  {
   "teamName": "Caffeina Torvalds",
   "teamId": "5571609347751936",
   "score": "812",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "The Basement Dwellers",
   "teamId": "5831863427923968",
   "score": "546",
   "hubId": "5405116215590912",
   "countries": [
    "Sweden",
    "Sweden"
   ]
  },
  {
   "teamName": "YACT",
   "teamId": "6426332535717888",
   "score": "388",
   "hubId": "6708378810187776",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "FSociety",
   "teamId": "6716358523879424",
   "score": "376",
   "hubId": "5937954421735424",
   "countries": [
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "Esternocleidomastoideotorrinolaringólogo",
   "teamId": "5434290653364224",
   "score": "376",
   "hubId": "5937954421735424",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "What a great team we are!",
   "teamId": "6271081614671872",
   "score": "376",
   "hubId": "0"
  },
  {
   "teamName": "Frenemies",
   "teamId": "4661714352078848",
   "score": "376",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "Pakore Wale",
   "teamId": "5278728347189248",
   "score": "376",
   "hubId": "6156894674616320",
   "countries": [
    "Germany",
    "Germany"
   ]
  },
  {
   "teamName": "COMPMSC",
   "teamId": "6225708439306240",
   "score": "376",
   "hubId": "6324625227120640",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Feesh Inc.",
   "teamId": "6572979899072512",
   "score": "376",
   "hubId": "5509218169782272",
   "countries": [
    "South Africa",
    "South Africa",
    "South Africa"
   ]
  },
  {
   "teamName": "NA Crew",
   "teamId": "6299919837036544",
   "score": "376",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "BlackBox",
   "teamId": "4678743092101120",
   "score": "376",
   "hubId": "0",
   "countries": [
    "Ukraine",
    "Ukraine",
    "Ukraine",
    "Ukraine"
   ]
  },
  {
   "teamName": "(｡◕‿‿◕｡)",
   "teamId": "6248729195577344",
   "score": "366",
   "hubId": "0",
   "countries": [
    "Luxembourg",
    "Germany"
   ]
  },
  {
   "teamName": "Un nom qui déchire",
   "teamId": "5938213260623872",
   "score": "284",
   "hubId": "0",
   "countries": [
    "Switzerland",
    "France",
    "Switzerland"
   ]
  },
  {
   "teamName": "WeRule",
   "teamId": "5874810215202816",
   "score": "280",
   "hubId": "4833820872278016",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Gueush",
   "teamId": "5664680752185344",
   "score": "268",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Nullers",
   "teamId": "5440209990713344",
   "score": "267",
   "hubId": "5941494011658240",
   "countries": [
    "Israel",
    "Israel",
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "Triangulation For The Win",
   "teamId": "5344384102957056",
   "score": "229",
   "hubId": "4762512469786624",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Gazoz",
   "teamId": "5740842065068032",
   "score": "194",
   "hubId": "0",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "nerds",
   "teamId": "5816486908133376",
   "score": "165",
   "hubId": "6241458352816128",
   "countries": [
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of",
    "Palestine, State of"
   ]
  },
  {
   "teamName": "V2lubmluZw==",
   "teamId": "4867084454461440",
   "score": "52",
   "hubId": "6358233077776384",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "LostVariables",
   "teamId": "5657066848911360",
   "score": "0",
   "hubId": "6651476264878080",
   "countries": [
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂",
   "teamId": "5958036145307648",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Poland",
    "Poland"
   ]
  },
  {
   "teamName": "Pauli's Pals",
   "teamId": "4525472352305152",
   "score": "0",
   "hubId": "0",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "PI",
   "teamId": "5492746232004608",
   "score": "0",
   "hubId": "4539782713573376",
   "countries": [
    "Turkey",
    "Turkey"
   ]
  },
  {
   "teamName": "sThor",
   "teamId": "6046482473943040",
   "score": "0",
   "hubId": "5032995148791808",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "MTM",
   "teamId": "4805527305453568",
   "score": "0",
   "hubId": "4815594104815616",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "The Old Gang",
   "teamId": "5319171302752256",
   "score": "0",
   "hubId": "4712480932626432",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "Rub3d0",
   "teamId": "6252408975917056",
   "score": "0",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "JBT",
   "teamId": "4833499018166272",
   "score": "0",
   "hubId": "6651476264878080",
   "countries": [
    "Greece",
    "Greece",
    "Greece",
    "Greece"
   ]
  },
  {
   "teamName": "groovyGarbageCollectors",
   "teamId": "4585452241682432",
   "score": "0",
   "hubId": "4852035560144896",
   "countries": [
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "GameofThreads",
   "teamId": "6014645424881664",
   "score": "0",
   "hubId": "6586258528665600",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Palocki engineering",
   "teamId": "5741753738985472",
   "score": "0",
   "hubId": "6167116159909888",
   "countries": [
    "Lithuania",
    "Lithuania",
    "Lithuania",
    "Lithuania"
   ]
  },
  {
   "teamName": "RAM",
   "teamId": "4544701256433664",
   "score": "0",
   "hubId": "4602858737500160",
   "countries": [
    "Spain",
    "Spain",
    "Spain"
   ]
  },
  {
   "teamName": "TeamOverflow",
   "teamId": "5083956076609536",
   "score": "0",
   "hubId": "5734144332005376",
   "countries": [
    "Slovakia",
    "Slovakia"
   ]
  },
  {
   "teamName": "FUT",
   "teamId": "4522669953253376",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Iran",
    "Iran",
    "Iran"
   ]
  },
  {
   "teamName": "00101010",
   "teamId": "5076590341914624",
   "score": "0",
   "hubId": "6142193135779840",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "NameMe",
   "teamId": "5675456288260096",
   "score": "0",
   "hubId": "6522670732541952",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "WillCodeForSoju",
   "teamId": "5769530567557120",
   "score": "0",
   "hubId": "6212905611558912",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "theAdjuders",
   "teamId": "5272242611027968",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Romania",
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "NPSNS",
   "teamId": "5738009265700864",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "NU bees",
   "teamId": "6538880006225920",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Kazakhstan",
    "Kazakhstan",
    "Kazakhstan"
   ]
  },
  {
   "teamName": "Glory Owl",
   "teamId": "5668217255100416",
   "score": "0",
   "hubId": "0",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "TheBitowls",
   "teamId": "5557248587726848",
   "score": "0",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "l337Noobs",
   "teamId": "6300176461332480",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Israel",
    "Israel"
   ]
  },
  {
   "teamName": "54 65 61 6D",
   "teamId": "5995028430192640",
   "score": "0",
   "hubId": "5550644337311744",
   "countries": [
    "Ireland",
    "Ireland",
    "Ireland",
    "Ireland"
   ]
  },
  {
   "teamName": "Tekathon",
   "teamId": "5151582819713024",
   "score": "0",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "Poppulus",
   "teamId": "5009899029266432",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "ENSICAEN 1",
   "teamId": "5234139003355136",
   "score": "0",
   "hubId": "0",
   "countries": [
    "France",
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "PonyCorn",
   "teamId": "6098895503360000",
   "score": "0",
   "hubId": "6365149585735680",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "DISI WOLFS",
   "teamId": "5278493197729792",
   "score": "0",
   "hubId": "5691274988355584",
   "countries": [
    "Italy",
    "Italy",
    "Italy",
    "Italy"
   ]
  },
  {
   "teamName": "Heavnerd",
   "teamId": "4841804478283776",
   "score": "0",
   "hubId": "5463428718133248",
   "countries": [
    "Tunisia",
    "Tunisia",
    "Senegal"
   ]
  },
  {
   "teamName": "<Enter team name here>",
   "teamId": "6240516144365568",
   "score": "0",
   "hubId": "4649046681583616",
   "countries": [
    "France",
    "France",
    "France"
   ]
  },
  {
   "teamName": "BDRS",
   "teamId": "6361552684843008",
   "score": "0",
   "hubId": "4913978115358720",
   "countries": [
    "France",
    "France"
   ]
  },
  {
   "teamName": "Codeplay",
   "teamId": "4693281355071488",
   "score": "0",
   "hubId": "4892331278860288",
   "countries": [
    "Romania",
    "Romania",
    "Romania"
   ]
  },
  {
   "teamName": "Duck Fried Rice",
   "teamId": "4805657026887680",
   "score": "0",
   "hubId": "5610966481895424",
   "countries": [
    "United Kingdom",
    "United Kingdom",
    "United Kingdom"
   ]
  },
  {
   "teamName": "2B||!2B",
   "teamId": "5683583507234816",
   "score": "0",
   "hubId": "5139029167177728",
   "countries": [
    "Portugal",
    "Portugal",
    "Portugal",
    "Portugal"
   ]
  },
  {
   "teamName": "TQL",
   "teamId": "6632661154004992",
   "score": "0",
   "hubId": "0",
   "countries": [
    "Spain",
    "Spain",
    "Spain",
    "Spain"
   ]
  }
 ]
}



def main():
    teams = []
    hypnotoad_position = None
    hypnotoad_score = None
    for position, entry in enumerate(data['entries']):
        teamName = entry['teamName']
        score = int(entry['score'])
        if teamName == "The Hypnotoad":
            hypnotoad_position = position
            hypnotoad_score = score
        teams.append(score)

    teams = sorted(teams, reverse=True)

    gnuplot = subprocess.Popen(
        ["/usr/bin/env", "gnuplot", "--persist"],
        stdin=subprocess.PIPE,
        universal_newlines=True)
    gnuplot_input = "set autoscale\n"
    gnuplot_input += "set terminal png size 480,360\n"
    gnuplot_input += "set xlabel 'Position'\n"
    gnuplot_input += "set ylabel 'Score'\n"
    gnuplot_input += (
        "set label at " + str(hypnotoad_position) + ", " + str(hypnotoad_score)
        + " 'The Hypnotoad' point pointtype 7 pointsize 2\n")

    gnuplot_input += "plot '-' using 1:2 title 'Results'\n"

    for position, score in enumerate(teams):
        gnuplot_input += str(position) + " " + str(score) + "\n"

    gnuplot_input += "e\n"

    output, err = gnuplot.communicate(gnuplot_input)

    if output:
        print(output)

    if err:
        print(err)


if __name__ == '__main__':
    main()
