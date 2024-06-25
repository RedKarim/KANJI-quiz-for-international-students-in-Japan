from django.views.generic import TemplateView
import MySQLdb

class AnswerView(TemplateView):
    template_name = 'auth/thirdresult.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Answer Page'
        # ... other context variables ...

        # Database connection and query
        connection = MySQLdb.connect(
            host='localhost',
            user='web_weavers',
            passwd='c6SrEGYv',
            db='kanjiquiz'
        )
        cursor = connection.cursor()

        sql = """
            SELECT q.q_id, q.que, q.exp, 
                COALESCE(a.cho, 'Not Chosen') AS UserAnswer
            FROM question_tbl q
            LEFT JOIN test_taker_tbl tt ON q.q_id = tt.q_id
            LEFT JOIN answer_tbl a ON q.q_id = a.q_id AND a.cho_n = tt.test_take_ans
            ORDER BY q.q_id ASC
            LIMIT 26
        """

        cursor.execute(sql)
        rows = cursor.fetchall()
        context['rows'] = rows

        connection.close()
        return context
