# Download Japan Real Estate Transaction Prices

## Disclaimer
It's an open-source tool that uses Japan Ministry of Land, Infrastructure, Transportation and Tourism (MLIT)'s publicly available APIs, and is intended for research and educational purposes.

Refer to MLIT's official documentation ([here](https://www.e-gov.go.jp/digital-government/api/webland.html)) for details on your rights to use the data downloaded.

## Quick Start

1. Construct a data field object using the `CityList` or `TradeList` class to specify the data to download.

2. Pass the data field object to `Request` class to construct the request.

3. Run the `.execute()` method to send request to download the data.

4. Reference the `Response` object data using `.json()` or `.df()`

```python
import jre

# city list for Tokyo (area code 13)
city_list = jre.data.CityList(13)

# make request
req = jre.Request(city_list)

# execute request
res = req.execute()

# get data in dict/json format
res.json()

# get data in pd.DataFrame format
res.df()

```

## Area Code List

| Area Code | Japanese Name | English Name |
| ---- | ---- | ---- |
| 01 | 北海道 | Hokkaido |
| 02 | 青森県 | Aomori Prefecture |
| 03 | 岩手県 | Iwate Prefecture |
| 04 | 宮城県 | Miyagi Prefecture | 
| 05 | 秋田県 | Akita Prefecture | 
| 06 | 山形県 | Yamagata Prefecture | 
| 07 | 福島県 | Fukushima Prefecture | 
| 08 | 茨城県 | Ibaraki Prefecture | 
| 09 | 栃木県 | Tochigi Prefecture | 
| 10 | 群馬県 | Gunma Prefecture | 
| 11 | 埼玉県 | Saitama Prefecture |
| 12 | 千葉県 | Chiba Prefecture |
| 13 | 東京都 | Tokyo |
| 14 | 神奈川県 | Kanagawa Prefecture | 
| 15 | 新潟県 | Niigata Prefecture |
| 16 | 富山県 | Toyama Prefecture |
| 17 | 石川県 | Ishikawa Prefecture |
| 18 | 福井県 | Fukui Prefecture |
| 19 | 山梨県 | Yamanashi Prefecture |
| 20 | 長野県 | Nagano Prefecture |
| 21 | 岐阜県 | Gifu Prefecture |
| 22 | 静岡県 | Shizuoka Prefecture |
| 23 | 愛知県 | Aichi Prefecture |
| 24 | 三重県 | Mie Prefecture |
| 25 | 滋賀県 | Shiga Prefecture | 
| 26 | 京都府 | Kyoto Prefecture |
| 27 | 大阪府 | Osaka Prefecture |
| 28 | 兵庫県 | Hyogo Prefecture |
| 29 | 奈良県 | Nara Prefecture |
| 30 | 和歌山県 | Wakayama Prefecture |
| 31 | 鳥取県 | Tottori Prefecture |
| 32 | 島根県 | Shimane Prefecture |
| 33 | 岡山県 | Okayama Prefecture |
| 34 | 広島県 | Hiroshima Prefecture |
| 35 | 山口県 | Yamaguchi Prefecture |
| 36 | 徳島県 | Tokushima Prefecture |
| 37 | 香川県 | Kagawa Prefecture | 
| 38 | 愛媛県 | Ehime Prefecture |
| 39 | 高知県 | Kochi Prefecture |
| 40 | 福岡県 | Fukuoka Prefecture |
| 41 | 佐賀県 | Saga Prefecture |
| 42 | 長崎県 | Nagasaki Prefecture |
| 43 | 熊本県 | Kumamoto Prefecture |
| 44 | 大分県 | Oita Prefecture |
| 45 | 宮崎県 | Miyazaki Prefecture |
| 46 | 鹿児島県 | Kagoshima Prefecture |
| 47 | 沖縄県 | Okinawa Prefecture |