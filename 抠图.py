import requests
# 还有48次
frequency = 48
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'ef4aw23uk5fSJJr6HLNEVfwN'},
)

if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
    print('成功')
    print(frequency - 1)
else:
    print("Error:", response.status_code, response.text)

