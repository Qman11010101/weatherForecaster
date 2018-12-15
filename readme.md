# 天気予報取得プログラム by Dark Sky

[Powered by Dark Sky](https://darksky.net/poweredby/)  

Dark Sky APIを使用して天気の情報を取得します。

## 使用言語

Python

## 注意

コードそのままでは動きません。  
[Your API Key]をDark SkyのAPIキーに、[Your Coodinate]を座標(「35.6501,139.7010」のような形式)にそれぞれ置き換えてください。  
  
天候は以下の独自の基準に沿っています。  
・cloudCoverの値が0.3未満なら、晴れ  
・cloudCoverの値が0.3以上で、かつprecipIntensityの値が1(mm/h)未満なら、曇り  
・cloudCoverの値が0.3以上で、かつprecipIntensityの値が1(mm/h)以上なら、雨

## 更新履歴

形式はyyyy.mm.ddです。

### 2018.12.15

温度の表記を「℃」に変更

### 2018.12.14

初コミット  
現在の天候状況要約・天候・気温・湿度・降水確率・気圧・最大風速・最大瞬間風速の表示に対応

## 改善点

・このままでは取得したjsonファイルが残ってしまうので、削除できるようにしたい。  
・表示できる情報を(例えば予報などを)増やしたい。  
・最終的にGUIかHTMLファイルにでもまとめて見やすくしたい。