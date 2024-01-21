## fitbit_weekly

- this program prints weekly step count in one hour increments
- for example
```
['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07']
0,0,446,291,0,0,0,30,0,375,868,266,823,381,111,212,553,363,773,895,883,410,856,376
0,18,0,52,0,0,0,810,752,1077,656,175,1058,65,415,8,74,1088,384,532,342,357,1209,0
58,317,0,19,0,0,270,1126,117,0,0,0,0,0,548,98,1651,1748,125,384,969,35,22,6
0,12,78,417,142,0,273,829,160,0,0,0,333,240,83,2176,1943,2120,135,378,168,528,8,414
0,0,242,150,0,8,327,858,838,254,0,0,0,61,57,516,192,1282,1086,514,765,94,0,4
0,6,60,5,0,0,25,12,0,743,1150,953,551,232,36,34,1253,1289,196,475,236,114,72,0
123,262,0,0,0,0,104,8,9,678,824,453,702,737,307,282,484,241,330,787,402,203,101,324
```
- each line represents a day
- this can easily be imported into excel or other program for analysis 


## Prerequisites

### Create new dev app
- register a new app under https://dev.fitbit.com/apps/new
  - all URLs should be `http://127.0.0.1:8080/`
  - Auth 2.0 Application Type should be `Personal`
  - Default Access Type should be `Read Only`
- write down `Client ID` and `Client Secret` after creating an app

### Download API wrapper

- download https://github.com/orcasgit/python-fitbit/tree/master
- `python-fitbit-master` folder should be on same level as `fitbit`
- for example
```
- Documents
 |--- python-fitbit-master
 |--- fitbit
```
- `pip install cherrypy`

### Config file

- config file needs to be `weeklyConfig.json` and be on the same level as the `fitbit_weekly.py`
- config should contain:
```
{
    "client_id" : "your id",
    "client_secret" : "your secret",
    "year": 2024,
    "month": 1,
    "day": 1
}
```
- where `Client ID` and `Client Secret` are from the app you've registered above
- year, month, and day is the start of the week
