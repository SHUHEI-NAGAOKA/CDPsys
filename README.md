# CDPsys
citizen data processing system for city hall.

市民課からもらったデータを加工する際に用いるプログラム

1. csvデータから生年月日を抽出しリスト化
2. 生年月日リストから現在の年齢を計算しリスト化
3. リストを元のcsvに挿入する
以上のフローを踏んでデータを加工する

a. ターゲットフォルダから特定の名称のフォルダを抽出
b. 取り出したフォルダから特定のファイルパスを抽出、リスト化　2023/06/08
c. リスト化したパスを使用してcsv modulで各ファイルから生年月日の列を取得、リスト化　2023/06_09
