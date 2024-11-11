import random  
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import MySQLdb

class SecondQuiz1View(TemplateView):
    template_name = 'auth/login_pages/second1.html'

    data = {}  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Quiz page'
        context['heading'] = '正しい答えを選びなさい。'
        context['paragraph'] = '回答を選択したら、[Submit] をクリックします。 結果を確認するには、[Show results] をクリックします'
        context['mysql_to_html'] = 'mysql_to_html'
        context['logout'] = 'logout'


        
        # Retrieve and prepare data as needed
        connection = MySQLdb.connect(
            host='db',
            user='web_weavers',
            passwd='c6SrEGYv',
            db='kanjiquiz'
        )
        cursor = connection.cursor()

        sql = """
            SELECT
                ROW_NUMBER() OVER (ORDER BY q.q_id) AS RowNumber,
                q.que AS Question,
                MAX(CASE WHEN a.cho_n = 1 THEN a.cho ELSE NULL END) AS Option1,
                MAX(CASE WHEN a.cho_n = 2 THEN a.cho ELSE NULL END) AS Option2,
                MAX(CASE WHEN a.cho_n = 3 THEN a.cho ELSE NULL END) AS Option3,
                MAX(CASE WHEN a.cho_n = 4 THEN a.cho ELSE NULL END) AS Option4
            FROM
                question_tbl q
            JOIN
                answer_tbl a ON q.q_id = a.q_id
            GROUP BY
                q.q_id, q.que
            ORDER BY
                q.q_id
            LIMIT 25, 10;
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        context['rows'] = rows
        connection.close()

        # Store data in the class attribute
        self.data['rows'] = rows

        return context



    def post(self, request):
        print(request.POST)
        connection = MySQLdb.connect(
            host='db',
            user='web_weavers',
            passwd='c6SrEGYv',
            db='kanjiquiz'
        )

        if request.method == 'POST':
            correct_count, incorrect_count = self.compare_answers()
            context = self.get_context_data()
            context['correct_count'] = correct_count
            context['incorrect_count'] = incorrect_count


        cursor = connection.cursor()
        print(request.POST)
        for row in self.data['rows']:

            question_number = row[0]
            answer = request.POST.get(f'answer{question_number}')

            sql = """
                INSERT INTO test_taker_tbl (q_id, test_take_ans)
                VALUES (%s, %s)
            """
            print(sql)
            cursor.execute(sql, (question_number, answer))

        connection.commit()
        connection.close()

        return render(request, self.template_name, context)

    def compare_answers(self):
        print('aaa',self)
        connection = MySQLdb.connect(
            host='db',
            user='web_weavers',
            passwd='c6SrEGYv',
            db='kanjiquiz'
        )
        cursor = connection.cursor()

        correct_count = 0
        incorrect_count = 0

        for row in self.data['rows']:
            question_number = row[0]
            answer = self.request.POST.get(f'answer{question_number}')

            sql = "SELECT ans FROM question_tbl WHERE q_id = %s"
            cursor.execute(sql, (question_number,))
            correct_answer = cursor.fetchone()[0]
            if answer == str(correct_answer):
                correct_count += 1
            else:
                incorrect_count += 1
        connection.close()

        return correct_count, incorrect_count
