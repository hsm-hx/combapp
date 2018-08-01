# CombApp - 部活動のための備品管理ツール

## What is it?
部活動の備品（書籍・コンピュータなど）の貸出処理を一元化するためのツールです。
ブラウザ上から誰でも備品を貸出することができ、Slackと連携することで備品が借りられたことや返却されたことをリアルタイムで確認することができます。

## How to use
1. `git clone https://github.com/hsm-hx/combapp`
2. `cd combapp; touch config.py`
3. config.pyに以下を記述します
``` python config.py
# Djangoのシークレットキー
# ジェネレーターなどを利用して任意の文字列を設定してください
django_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

#Slackのトークン
slack_token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
```
4. `./manage.py migrate`
5. `./manage.py runserver`

## Detail
### 備品モデルについて
* 種別としてBook, Device, Computerを用意しています
* Remarkには保証書の所在などを書くことを想定しています

### 貸出処理について
* 貸出期間は2週間に設定されています
* Extendで貸出を1週間延長することができます
* Nameは自己申告制になっています

### 備品の追加について
* 備品の追加メニューより新規備品の登録ができます
* 備考は任意入力項目です
* 備品情報の変更や削除は/adminのみからとしています

### adminについて
* [URL]/adminにアクセスすると管理者ページにログインできます
* 管理者ページトップ→Equipmentより備品の追加・編集・削除ができます

#### 管理者アカウントの作り方
1. `./manage.py createsuperuser`
2. ユーザー名、メールアドレス、パスワードを入力

### 今後の実装予定について
* 部員も管理したい
* 貸出者が自己申告制になっており信頼性がない
  * 貸出処理をするためにログイン・ログアウトをしなければいけない手間をどう解決するか？
* adminページからの新規追加に任意入力を実装する
* Slackでメンションするようにしたい
* 貸出期限の切れた備品についてSlackで通知したい
  * 別アプリとして実装？
