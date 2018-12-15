import json
import urllib.request as urlreq
from datetime import datetime

url = "https://api.darksky.net/forecast/[Your API Key]/[Your Coodinate]?lang=ja&units=si"
urlreq.urlretrieve(url, 'data.json')

f = open("data.json", "r", encoding="utf-8_sig")
data = json.load(f)

curtimeUnix = data["currently"]["time"]
curtimeNormal = datetime.fromtimestamp(curtimeUnix)

print(str(curtimeNormal) + "のデータを取得しました")
print("")
print("天候状況要約:{}".format(data["currently"]["summary"]))
print("")

curcloudCover = data["currently"]["cloudCover"]
curprecip = data["currently"]["precipIntensity"]

if curcloudCover < 0.3:
    curweather = "晴れ"
else:
    if curprecip < 1:
        curweather = "曇り"
    else:
        curweather = "雨"

print("天候:" + curweather)
print("気温:" + str(data["currently"]["temperature"]) + "℃")
print("湿度:" + str(int((data["currently"]["humidity"]) * 100)) + "%")
print("降水確率:" + str(int((data["currently"]["precipProbability"]) * 100)) + "%")
print("気圧:" + str(int(data["currently"]["pressure"])) + "hPa")
print("最大風速:" + str(int(data["currently"]["windSpeed"])) + "m/s")
print("最大瞬間風速:" + str(int(data["currently"]["windGust"])) + "m/s")

print("")
input("ENTERを押して終了")