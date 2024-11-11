from django.urls import path
from . import login_views, mysql_to_html_views, mysql_to_html_views_second, mysql_to_html_views_third, logout_views, rsc
from .answer_views import AnswerView
from . import regist_views
from .second1 import SecondQuiz1View
from .second2 import SecondQuiz2View
from .second3 import SecondQuiz3View
from .third1 import ThirdQuiz1View
from .third2 import ThirdQuiz2View
from .third3 import ThirdQuiz3View
from .fourth1 import FourthQuiz1View
from .fourth2 import FourthQuiz2View
from .fourth3 import FourthQuiz3View





urlpatterns = [
    # ... [existing URL patterns] ...
    path('', login_views.TopView.as_view(), name='index'),
    path('login_email', login_views.LoginEmailView.as_view(), name='login_email'),
    path('login_passwd', login_views.LoginPassView.as_view(), name='login_passwd'),
    path('login_security_code', login_views.LoginSecurityCodeView.as_view(), name='login_security_code'),
    path('mysql_to_html', mysql_to_html_views.MysqlToHtmlView.as_view(), name='mysql_to_html'),
    path('mysql_to_html_views_second', mysql_to_html_views_second.MysqlToHtmlView.as_view(), name='mysql_to_html_second'),
    path('mysql_to_html_views_third', mysql_to_html_views_third.MysqlToHtmlView.as_view(), name='mysql_to_html_third'),
    path('logout', logout_views.MysqlToHtmlView.as_view(), name='logout'),
    path('regist_email', regist_views.RegistEmailView.as_view(), name='regist_email'),
    path('regist_passwd', regist_views.RegistPassView.as_view(), name='regist_passwd'),
    path('regist_security_code', regist_views.RegistSecurityCodeView.as_view(), name='regist_security_code'),
    path('regist_end_page', regist_views.RegistSecurityCodeView.as_view(), name='regist_end_page'),
    path('answer', AnswerView.as_view(), name='answer'),
    # Add the new URL pattern for the RSC page
    path('rsc/', rsc.RSCView.as_view(), name='rsc'),
    path('second1/', SecondQuiz1View.as_view(), name='second1'),
    path('second2/', SecondQuiz2View.as_view(), name='second2'),
    path('second3/', SecondQuiz3View.as_view(), name='second3'),
    path('third1/', ThirdQuiz1View.as_view(), name='third1'),
    path('third2/', ThirdQuiz2View.as_view(), name='third2'),
    path('third3/', ThirdQuiz3View.as_view(), name='third3'),
    path('fourth1/', FourthQuiz1View.as_view(), name='fourth1'),
    path('fourth2/', FourthQuiz2View.as_view(), name='fourth2'),
    path('fourth3/', FourthQuiz3View.as_view(), name='fourth3')
]