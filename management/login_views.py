from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .login_forms import LoginEmailForm , LoginPassForm , LoginSecurityCodeForm
import MySQLdb
import random
from django.core.mail import send_mail
from datetime import datetime

class TopView(TemplateView):
  def __init__(self):
    self.params = {
      'title':'Welcome',
      'heading':'Web Weavers 漢字クイズへようこそ！ ',
      'paragraph':'日本語能力試験に合格できるよう、漢字多肢選択クイズを4章用意しました。 テストにアクセスするには、ログインするかユーザを登録してください。',
      'login_email':'login_email',
      'regist_email':'regist_email',
      'logo': 'kanji_image.jpg',
    }

  # <form action="" method="POST">以外のページの遷移は、「GET」メソッドになります。
  def get(self, request):
    # dt = '2023-09-29 06:39:22'
    # db_date_of_expiry = datetime.strptime(dt , "%Y-%m-%d %H:%M:%S")
    # ddoe = db_date_of_expiry.timestamp()
    # print(ddoe)
    # dt_now = datetime.now()
    # dt_now_data = datetime.strptime(dt_now , "%Y-%m-%d %H:%M:%S")
    # dnd = dt_now_data.timestamp()
    # ddd = dnd - ddoe
    # print(ddd)
    if 'eMail' in request.session:
      request.session.clear()
    return render(request, 'index.html' , self.params)
  
  def post(self, request):
    if 'eMail' in request.session:
      request.session.clear()
    return render(request, 'index.html' , self.params)
  
#-------------------メールアドレスを処理するためのクラス-----------------------------------------------

class LoginEmailView(TemplateView):
  def __init__(self):
    self.params = {
      'title':'メールアドレス入力',
      'heading':'メールアドレスを入力してください',
      'paragraph':'Welcome back!',
      'form':LoginEmailForm(),
      'login_email':'login_email'
    }

  # <form action="" method="POST">からのデータ送信のため実行しません。
  def get(self, request):
    self.params['form'] = LoginEmailForm(request.GET)
    return render(request, 'auth/login_email.html', self.params)

  # <form action="" method="POST">からのデータ送信のためこちらを実行します。
  def post(self, request):
    # MariaDB(MySQL)へ接続パラメータ
    connection = MySQLdb.connect(
      host='db',
      user='web_weavers',
      passwd='c6SrEGYv',
      db='user_manage_dv'
    )

    # MariaDB(MySQL)へ接続
    cursor = connection.cursor()

    # 送信されてきたメールアドレスと同じメールアドレスがDBに存在するかを調べるSQL文
    sql = "SELECT email FROM user_tbl WHERE email = '" + request.POST['login_user_email'] + "'"
    # 問い合わせの実行
    rows = cursor.execute(sql)

    if rows != 1: # 同じメールアドレスが存在しない場合の処理
      self.params = {
        'title':'メールアドレス入力',
        'heading':'メールアドレスを入力してください',
        'paragraph':'Welcome back!',
        'form':LoginEmailForm(),
        'login_email':'login_email'
      }
      self.params['message'] ='上記メールアドレスでログインできません。'
      self.params['form'] = LoginEmailForm(request.POST)
      return render(request, 'auth/login_email.html' , self.params)
    else: # 同じメールアドレスが存在する場合の処理
      # request.session['eMail']変数のセッション名(キー)が存在するかを調べて存在しない場合は、セッション変数にメールアドレスを格納しておく
      if not 'eMail' in request.session:
        # この時点でセッションがスタートし、 request.session['eMail']にメールアドレスが格納されます。
        request.session['eMail'] = request.POST['login_user_email']

      self.params = {
        'title':'パスワード入力',
        'heading':'パスワードを入力してください',
        'paragraph':'Welcome back!',
        'form':LoginPassForm(),
        'login_passwd':'login_passwd',
      }

      # 接続を閉じる
      connection.close()
      return render(request, 'auth/login_passwd.html' , self.params)

#-------------------パスワードを処理するためのクラス-----------------------------------------------

class LoginPassView(TemplateView):
  def __init__(self):
    self.params = {
      'title':'パスワード入力',
      'heading':'パスワードを入力してください',
      'paragraph':'Welcome back!',
      'form':LoginPassForm(),
      'login_passwd':'login_passwd',
    }
  
  def get(self, request):
    self.params['form'] = LoginPassForm(request.GET)
    return render(request, 'auth/login_passwd.html', self.params)
  
  def post(self, request):
    # MariaDB(MySQL)へ接続パラメータ
    connection = MySQLdb.connect(
      host='db',
      user='web_weavers',
      passwd='c6SrEGYv',
      db='user_manage_dv'
    )

    # MariaDB(MySQL)へ接続
    cursor = connection.cursor()

    # 送信されてきたパスワードと同じパスワードがDBに存在するかを調べるSQL文
    # セッション変数「request.session['eMail']」に登録されているメールアドレスを使って行(row)を特定するための条件
    sql = "SELECT * FROM user_tbl WHERE email = '" + request.session['eMail'] + "' AND passwd = '" + request.POST['login_user_passwd'] + "'"

    # 問い合わせの実行
    rows = cursor.execute(sql)

    if rows != 1:
      self.params = {
        'title':'パスワード入力',
        'heading':'パスワードを入力してください',
        'paragraph':'Welcome back!',
        'form':LoginPassForm(),
        'login_passwd':'login_passwd',
      }
      self.params['message'] ='上記パスワードでは、ログインできません。'
      self.params['form'] = LoginPassForm(request.POST)
      return render(request, 'auth/login_passwd.html' , self.params)
    else:
      #セキュリティコードの生成
      security_code = ''
      for i in range(1,8):
        sc = random.randint(0,9)
        security_code += str(sc)

      # セキュリティコードをsecurity_code列に書き込むSQL文
      # セッション変数「request.session['eMail']」に登録されているメールアドレスを使って行(row)を特定するための条件
      sql ="UPDATE user_tbl SET security_code = '" +  security_code + "' WHERE email = '" + request.session['eMail'] + "'"
      cursor.execute(sql)
      # バッファのデータをデータベースにコミットする
      connection.commit()
      
      # 登録されているメールアドレスにセキュリティーコードを送信する
      # 「subject」、「message」、「from_email」は、LoginPassViewクラス先頭あたりでリストまたは、辞書にしておくのがベストです。
      # そうするとプリグラムが見やすくなるし、内容を自由ね編集できます。
      # メールの件名
      subject = 'SECURITY CODE セキュリティコードの送信'
      # メールの本文
      # 「\n」は、メール文を改行させるためのエスケープシーケンスです。
      message = 'Your SECURITY CODE is:'+ security_code + 'セキュリティコードは、以下になります。\n' + \
                'セキュリティコード：' + security_code
      # メールの送信者(実際は、スパムメール等を防ぐためにGmailアドレスに置き換えて送信されます。)
      from_email = 'WebWeavers74@gmail.com'
      # メールの送信先
      to = request.session['eMail']
      # メールの送信
      send_mail(subject,message,from_email,[to],fail_silently=False,)

      self.params = {
        'title':'セキュリティコード入力',
        'heading':'セキュリティコードを入力してください',
        'paragraph':'セキュリティコードが入力したのメールアドレスに送信されます。',
        'form':LoginSecurityCodeForm(),
        'login_security_code':'login_security_code',
      }
      # 接続を閉じる
      connection.close()
      self.params['message'] = 'セキュリティコードは、' + to +'宛に送信しました。'
      return render(request, 'auth/login_security_code.html' , self.params)

# --------------------------セキュリティコードを処理するためのクラス-----------------------------------------------------------

class LoginSecurityCodeView(TemplateView):
  def __init__(self):
    self.params = {
      'title':'セキュリティコード入力',
      'heading':'セキュリティコードを入力してください',
      'paragraph':'セキュリティコードが入力したのメールアドレスに送信されます。',
      'form':LoginSecurityCodeForm(),
      'login_security_code':'login_security_code',
    }
  
  def get(self, request):
    self.params['form'] = LoginSecurityCodeForm(request.GET)
    return render(request, 'auth/login_security_code.html', self.params)
  
  def post(self, request):
    # MariaDB(MySQL)へ接続パラメータ
    connection = MySQLdb.connect(
      host='db',
      user='web_weavers',
      passwd='c6SrEGYv',
      db='user_manage_dv'
    )

    # MariaDB(MySQL)へ接続
    cursor = connection.cursor()

    # 送信されてきたセキュリティコードと同じセキュリティコードがDBに存在するかを調べるSQL文
    # セッション変数「request.session['eMail']」に登録されているメールアドレスを使って行(row)を特定するための条件
    sql = "SELECT * FROM user_tbl WHERE security_code = '" +  request.POST['login_security_code'] + "' AND email = '" + request.session['eMail'] + "'"
    # 問い合わせの実行
    rows = cursor.execute(sql)
    if rows != 1:
      self.params = {
        'title':'セキュリティコード入力',
        'heading':'セキュリティコードを入力してください',
        'paragraph':'セキュリティコードが入力したのメールアドレスに送信されました。',
        'form':LoginSecurityCodeForm(),
        'login_security_code':'login_security_code',
      }
      self.params['message'] ='上記セキュリティコードでは、ログインできません。セキュリティコードが入力したのメールアドレスに送信されました。'
      self.params['form'] = LoginSecurityCodeForm(request.POST)
      return render(request, 'auth/login_security_code.html' , self.params)
    else:
      # SQL文の条件に合ったすべての行を取得する。（この場合は、1行のみになります。）
      # セッション変数「request.session['eMail']」に登録されているメールアドレスを使って行(row)を特定するための条件
      # この時点でログインを認めるのでセキュリティコードを「NULL」にします。
      sql = "UPDATE user_tbl SET security_code = NULL WHERE email = '" + request.session['eMail'] + "'"
      cursor.execute(sql)
      # バッファのデータをデータベースにコミットする
      connection.commit()

      self.params = {
        'title':'クイズに答えてみましょう',
        'heading':'クイズに答えてみましょう',
        'paragraph':'この4章からお選びいただけます。 各章には 25 の質問があり、3 つのクイズに分かれています。',
        'page1':'page1',
        'mysql_to_html':'mysql_to_html',
      }
      self.params['eMail'] =  request.session['eMail']
      # 接続を閉じる
      connection.close()
      return render(request, 'auth/login_pages/login_page1.html' , self.params)
