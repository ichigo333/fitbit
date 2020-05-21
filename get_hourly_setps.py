import json, requests

def formatList(by_quarter_list):
    if len(by_quarter_list) == 4:
        return f"{by_quarter_list[0]}\t{by_quarter_list[1]}\t{by_quarter_list[2]}\t{by_quarter_list[3]}"
    else:
        return "no list"


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

    print("")
    print("Time     | Total | By 15min \t\t\t | \t Graph")
    print("----------------------------------------------------------------")

    for data in datasets:
        time = data.get('time')
        value = data.get('value')
        dots = "......."

        if count % 4 == 0:
            if count != 0:
                print(f"{time} | {steps}\t | {formatList(by_quarter_list)}\t | \t {dots}")
                by_quarter_list = []
            steps = int(value)
            by_quarter_list.append(value)
        else:
            steps = steps + int(value)
            by_quarter_list.append(value)
        
        count = count + 1
        if count >= len(datasets):
            print(f"{time} | {steps}\t | {formatList(by_quarter_list)}\t | \t {dots}")
            by_quarter_list = []


if __name__ == "__main__":
    main()
