import requests
import json
import asyncio

script_path = 'script.json'
with open(script_path, 'r') as f:
  script = json.loads(f.read())

i = 0
count = 0
script_small_parts = []
script_parts = {}
for x in reversed(script):
  if i > 10:
    i = 0
    script_parts.update({count:script_small_parts})
    count += 1
    script_small_parts = []
    script_small_parts.append(x)
  script_small_parts.append(x)
  i += 1
  if count == 179:
    script_parts.update({count:script_small_parts})

steam64 = 'TARGETS STEAMID64 BIT'
your_steam64 = 'YOUR STEAMID64'
session_id = 'YOUR SESSION ID FOR STEAM WEB'
steam_login = 'YOUR steamLogin cookie FOR STEAM WEB'
steam_login_secure = 'YOUR steamLoginSecure cookie FOR STEAM WEB'
steam_machine_auth = 'YOUR steamMachineAuth cookie FOR STEAM WEB'
cookies = {
  'steamMachineAuth{0}'.format(your_steam64): steam_machine_auth,
  'steamLoginSecure': steam_login_secure,
  'sessionid': session_id,
  'steamLogin': steam_login
}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0.1 Waterfox/47.0.1'}
api = 'https://steamcommunity.com/comment/Profile/post/{0}/-1/'.format(steam64)
async def main():
  """Bee Movie Script poster for steam profiles!"""
  message = ''
  for x in script_parts:
    for s in script_parts[x]:
      if len(s) < 1000 and len(message) < 800:
        message += s
      else:
        payload = {'comment': message, 'count': '6', 'sessionid': session_id}
        r = requests.post(api, headers=headers, cookies=cookies, data=payload)
        if r.json()['success'] == 'false':
          print(payload)
          print(len(message))
          print(r.text)
          print("either you got ratelimited by steam for posting too many comments or something went wrong, rip.")
          return
        message = ''
        message += str(s)
        await asyncio.sleep(5)
  last_comment = 'Bee Movie (2007) - 6.2/10\nhttp://www.imdb.com/title/tt0389790/\n\nBarry B. Benson, a bee just graduated from college, is disillusioned at his lone career choice: making honey. On a special trip outside the hive, Barry\'s life is saved by Vanessa, a florist in New York City. As their relationship blossoms, he discovers humans actually eat honey, and subsequently decides to sue them.'
  payload = {'comment': last_comment, 'count': '6', 'sessionid': session_id}
  r = requests.post(api, headers=headers, cookies=cookies, data=payload)
  print("done")

loop = asyncio.get_event_loop()  
loop.run_until_complete(main())  
loop.close() 