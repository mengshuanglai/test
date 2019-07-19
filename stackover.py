

# import requests
# proxies = { "http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080", }
# request = requests.get('https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U',proxies=proxies)
# with open("stc.zip", "wb") as file:
#     file.write(request.content)


# import shutil , os
# shutil.move('stc/survey_results_public.csv','mysurvey.csv')
# shutil.rmtree('stc')
# os.remove('stc.zip')

# import requests
# request=requests.get('https://www.google.com.hk')
# print(request.status_code)

name = input('你的名字？')
print('hello,',name)


