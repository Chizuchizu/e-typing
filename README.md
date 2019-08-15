e-typing Ranking Scripting
===

e-typing(https://www.e-typing.ne.jp)  
のランキングをスクレイピングして、  スコアのヒストグラムと偏差値、上位n%の目安を導出するプログラムです。

## Usage
main_run.pyを実行し、スクレイピングしたい回（第何回のデータか）を数で入力します。  
スクレイピングされたデータが残っていればスクレイピングは実行委されませんが、なかった場合にはスクレイピングが実行されます。  
  
後は実行を待つだけです。
色んな統計量が出てきます。

## Requirement
・Python3

## Warning
main2_js.pyのtime.sleep()は必ず1以上にしてください。  
1未満にしてしまうとe-typing側の負荷が大きくなってしまい、サイトへの攻撃とみなされる可能性があります。

## Author
[Twitter](https://twitter.com/chizu_potato)

## License
MIT
