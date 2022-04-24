import json, requests

def main():
    datasets = getDataSets()
    printData(datasets)

def printData(datasets):
    count = 0
    steps = 0

    for set in datasets:
        for data in set:
            value = data.get('value')

            if count % 4 == 0:
                if count != 0:
                    print(f"{steps},", end="", flush=True)
                steps = int(value)
            else:
                steps = steps + int(value)
            
            count = count + 1
        
        print(steps)
        steps = 0
        count = 0

def getDataSets():
    auth_token = ""
    payload = {'accept': 'application/x-www-form-urlencoded'}
    headers = {'authorization': 'Bearer ' + auth_token}
    
    dates = ["2022-04-18","2022-04-19","2022-04-20","2022-04-21","2022-04-22","2022-04-23","2022-04-24"]
    datasets = [] 

    for date in dates:
        uri = f"https://api.fitbit.com/1/user/-/activities/steps/date/{date}/1d/15min.json"
        response = requests.get(uri, params=payload, headers=headers)
        apiJson = json.loads(response.content)

        datasets.append(apiJson.get("activities-steps-intraday").get("dataset"))
    return datasets

if __name__ == "__main__":
    main()
