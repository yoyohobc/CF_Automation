import requests

url = "https://office.cf139.com/ValidateCodeLog/createValidateNo"

payload = "18856818076"
headers = {
  'Connection': 'close',
  'authority': 'office.cf139.com',
  'accept': 'application/json, text/plain, */*',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://office.cf139.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://office.cf139.com/home/validater/validateNo',
  'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'lang_type=0; JSESSIONID=84871DBC50AD6CCE38923B5F4F7FC5DF; cf88_id="user:763:869480c1-ce0e-4232-9a65-65b9336b2cec"'
}

response = requests.request("POST", url, headers=headers, data = payload,verify = False)

print(response.text.encode('utf8'))
