# github-action-training 

自身が作成した[NumericCharacter2String](https://github.com/Villager-B/NumericCharacter2String)レポジトリの内容をgithub actionで自動実行できないかを検討するリポジトリ

`./dirs`にファイルをpushすることで`./dirs/original`と`./dirs/escape`にそれぞれファイルを移動，保存させる．

今回は`.gml`ファイルのpushをトリガーにして実行させる．

## Useage

数値文字参照になっている任意のファイル名をコマンドライン引数として与えることで
`filename-unescape.fileextension`の文字列に変更されたファイルが生成される．

```
python numetric_char_str.py [filename]
```

## Sample

### test.txt
```
&#25991;&#31456;&#9834;
&#x3042;&#x3044;&#x3046;&#x3048;&#x304a;
&gt;
```

### test-unescape.txt
```
文章♪
あいうえお
>
```