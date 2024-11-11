from django import forms


#このフォームは専門学校のオープンキャンパスの申込フォームです。 エレメントは以下にあります。

class RegistEmailForm(forms.Form):
    regist_user_email = forms.CharField(label='メールアドレス' , required=False , widget =forms.TextInput(attrs={'placeholder':'例:abc@gmail.com' , 'size':'20'}))

class RegistPassForm(forms.Form):
    regist_user_passwd = forms.CharField(label='パスワード' , required=False , widget =forms.PasswordInput(attrs={'placeholder':'パスワードを入力' , 'size':'20'}))
    # regist_user_email = forms.CharField(label='パスワード' , required=False , widget =forms.TextInput(attrs={'placeholder':'メールアドレスを入力してください。' , 'size':'30'}))

class RegistSecurityCodeForm(forms.Form):
    regist_security_code = forms.CharField(label='セキュリティコード' , required=False , widget =forms.TextInput(attrs={'placeholder':'セキュリティコード' , 'size':'20'}))