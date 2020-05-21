import json, requests

def main():
    date = "2020-05-20"
    auth_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMjdHNUwiLCJzdWIiOiIzS0xZSk0iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3YWN0IiwiZXhwIjoxNTkwMDk2NjIwLCJpYXQiOjE1OTAwMTAyMjB9.tGmkZvHMyBWOav5xuHRxZj_gw6LTY2-LyUvwZHwwUqs"
    uri = f"https://api.fitbit.com/1/user/-/activities/steps/date/{date}/1d/15min.json"
    payload = {'accept': 'application/x-www-form-urlencoded'}
    headers = {'authorization': 'Bearer ' + auth_token}
    response = requests.get(uri, params=payload, headers=headers)
    apiJson = json.loads(response.content)

    datasets = apiJson.get("activities-steps-intraday").get("dataset")
    
    count = 0
    steps = 0
    by_quarter_list = []
    for data in datasets:
        time = data.get('time')
        value = data.get('value')
        

        if count % 4 == 0:
            if count != 0:
                print(f"{time} : {steps}\t {by_quarter_list}")
                by_quarter_list = []
            steps = int(value)
            by_quarter_list.append(value)
        else:
            steps = steps + int(value)
            by_quarter_list.append(value)
        
        count = count + 1
        if count >= len(datasets):
            print(f"{time} : {steps}\t {by_quarter_list}")
            by_quarter_list = []


    #print(datasets)

if __name__ == "__main__":
    main()
