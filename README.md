# WillowPecoe_beta

全国のWillowファンの皆様こんにちは。そしてβテストへようこそ。

## ビルドガイド(玄人向け)

MCUにProMicroを採用し、CherryMXスイッチ、PCB 3層サンドイッチと、ごくオーソドックスなスタイルを
採用しているので難しいところはないと思います。

基板がリバーシブルになっているので、パーツの取付面だけ注意ください。

## パーツリスト

- Pro Micro x1
- タクトスイッチ(2本足) x1
- MX用スイッチソケット x49
- ダイオード (THM or SMD) x50 
- フルカラーシリアルLED WS2812B x15 (opt)
- ロータリーエンコーダ x1  (opt)
- 六角スペーサー(M2 7mm)  x13
- 六角スペーサー(M2 3.5mm) x6
- ネジ (M2 3mm) x38@

## パーツの取付け
### 基板の表裏を決定
まず ロータリーエンコーダの位置を右か左か決めます。
 - 左側に置く場合、PCBのSide Aが表面になります。
 - 右側に置く場合、PCBのSide Bが表面になります。

### パーツのはんだ付け

#### ダイオード
- ダイオードは すべて裏面に取り付けます。 SMD、THM どちらでも使えます。

### スイッチソケット
- スイッチソケットはすべて裏面に取り付けます。

### RGB LED
- 表面側のパッドをジャンプさせます (Jump front sideと書いてあるところ)

- 表面に 3個、 裏面に12個取り付けます。
  - Side Aが表面の場合、 シルクのLED1からLED13に取り付けます。
  - Side Bが表面の場合、 シルクのLED16からLED30に取り付けます。



### ロータリーエンコーダ
- 表面からさして裏面をはんだ付けします。

### Pro Micro
 - ProMicroはコンスルーを使て表面取り付けます。
 - ProMicroの実装面が内向きになるようにしてください。

### タクトスイッチ
  - 表面に取り付けます


## 組み立て

- トッププレートとPCBを、3.5mmスペーサを使って取り付けます。
- スイッチを差し込みます。
- PCBと化粧板を7mmスペーサを使って取り付けます。
- トッププレートとボトムプレートを7mmスペーサを使って取り付けます。

## ファームウェア

- コンパイルしてください。ロリコンの位置によってキーマップが異なります。
  - Side A用: default
  - Side B用: side_b
  

## 既知の問題点

- アンダーグローの光がうまく廻りません。
  - 表側の3個だけを光らすには 最初の5個だけを取り付けるか、ジャンパを這わせて表側の3個だけ光らせる方法もあります。  
  - アクリルプレートオプションを考慮します
  - 次の版では、簡単に表面の3つだけ優先的に光らせられるよう配線を見直します。




- PCBの表面に細かい油染みのような汚れ?があります。
  - 製造委託先の品質に依存する問題かと思います。実質影響はありません。
  - 次の発注は別なところを考えてみます(量産のときはJLCPCBの価格は魅力なんだけど)
  
- ネジとスイッチが干渉する恐れがあるかも?
  - 作者手元のスイッチでは今の所大丈夫だけどかなりギリギリ。
  - 次の基板ではもう少し余裕持たせるようにします

- ファームウェアは開発途中です

- トッププレートのLEDを透過するスリットはアクリルを埋め込む
  計画がありますが未実装です。



以上です
