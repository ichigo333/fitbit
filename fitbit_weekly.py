import json, requests, datetime, os, sys
sys.path.append("..\\python-fitbit-master")
import fitbit
import gather_keys_oauth2


def main():
    auth_server = gather_keys_oauth2.OAuth2Server('', '')
    auth_server.browser_authorize()
    
    print('TOKEN\n=====\n')
    for key, value in auth_server.fitbit.client.session.token.items():
        if key == "access_token":
            access_token = value

    config = getConfig('weeklyConfig.json')
    datasets = getDataSets(config, access_token)
    printData(datasets)

def getConfig(path):
  location = os.path.dirname(os.path.abspath(__file__))
  path = os.path.join(location, path)
  with open(path) as jsonFile:
    config = json.load(jsonFile)
  return config

def getWeekDateList(start_date):
    date_list = []
    for day_num in range(7):
        date_list.append((start_date + datetime.timedelta(days=day_num)).strftime('%Y-%m-%d'))
    return date_list

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

def getDataSets(config, access_token):
    payload = {'accept': 'application/x-www-form-urlencoded'}
    headers = {'authorization': 'Bearer ' + access_token}
    
    dates = getWeekDateList(datetime.date(config['year'],config['month'],config['day']))
    print(dates)
    datasets = [] 

    for date in dates:
        uri = f"https://api.fitbit.com/1/user/-/activities/steps/date/{date}/1d/15min.json"
        response = requests.get(uri, params=payload, headers=headers)
        apiJson = json.loads(response.content)

        datasets.append(apiJson.get("activities-steps-intraday").get("dataset"))
    return datasets

if __name__ == "__main__":
    main()
