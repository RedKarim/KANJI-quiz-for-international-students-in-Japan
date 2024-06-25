from django import forms


#このフォームは専門学校のオープンキャンパスの申込フォームです。 エレメントは以下にあります。

class LoginEmailForm(forms.Form):
    login_user_email = forms.CharField(label='メールアドレス' , required=False , widget =forms.TextInput(attrs={'placeholder':'例:abc@gmail.com' , 'size':'17'}))

class LoginPassForm(forms.Form):
    login_user_passwd = forms.CharField(label='パスワード' , required=False , widget =forms.PasswordInput(attrs={'placeholder':'パスワードを入力' , 'size':'15'}))
    # login_user_email = forms.CharField(label='パスワード' , required=False , widget =forms.TextInput(attrs={'placeholder':'メールアドレスを入力してください。' , 'size':'30'}))

class LoginSecurityCodeForm(forms.Form):
    login_security_code = forms.CharField(label='セキュリティコード' , required=False , widget =forms.TextInput(attrs={'placeholder':'セキュリティコード' , 'size':'15'}))