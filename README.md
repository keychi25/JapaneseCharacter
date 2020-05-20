# 人工知能概論・ひらがな判定器

## やったこと1(データセット，学習，適用)
1. etlcdbからひらがなデータの収集(セットから画像) → hiragana.npzの作成
2. 1で取得した画像の学習(kerasのSequentialモデル) → model_V{n}.savの作成
3. 作成したモデルをWebアプリ(Flask)から，画像をFormして適用 → 結果の表示

## やったこと2(入力データの前処理)
1. 「白」を明確化
2. 「白・黒」を反転
3. サイズを32×32に変更

## 実行方法
- 依存関係の設定

```
pipenv install -r requirements.txt
```

- pyhton3(3.7)での実行
```
python3 app.py
```

- docker-composeで実行
```
docker-compose up --build
```

## 作成したモデル
|version|精度|作成日|エポック数|オプティマイザ|備考|
|:--:|:--:|:--:|:--:|:--:|:--:|
|V1|0.996|2020/05/18|400|Adadelta|いい感じ|
|V2|0.992|2020/05/20|100|SGD|なぜか精度の割にクラスの分類が絞れない|
|V3|0.970|2020/05/21|400|Adadelta|戻した|

## モデルの概要(Summary)
<img width="620" alt="summary" src="https://user-images.githubusercontent.com/38200453/82467742-f620c400-9afc-11ea-8e1e-f08493f6b238.png">

## 精度・損失値
- 精度

![精度を示すグラフのファイル名](https://user-images.githubusercontent.com/38200453/82470949-fae77700-9b00-11ea-9110-30e555a09513.png)

- 損失値

![損失値を示すグラフのファイル名](https://user-images.githubusercontent.com/38200453/82471014-105ca100-9b01-11ea-8375-6c261b984276.png)

## 参考サイト
[kerasのSequentialモデル](https://keras.io/ja/getting-started/sequential-model-guide/)  
[kerasのオプティマイザ(最適化アルゴリズム)の利用方法](https://keras.io/ja/optimizers/)  
[etlcdb(ひらがなのデータセット)](http://etlcdb.db.aist.go.jp/?lang=ja)  
[参照論文](https://pdfs.semanticscholar.org/f3ee/6bfaec669a2c8d087e2f11fa48aa7b45d6ea.pdf?_ga=2.15362358.1247571733.1589733184-821604392.1589733184)  
