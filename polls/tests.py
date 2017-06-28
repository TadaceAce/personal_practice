import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# separate test class for each model or view
# Create your tests here.
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        ''' was_published recently() should return False for questions who pub_date is in the future'''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        '''was_published_recently() should return False for questions whose pub_date is older than 1 day'''
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        '''was published recently() should return True for questions whose pub_date is within the last day'''
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    ''' creates a question with the given question_text and published the given
    number of days offset to now'''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(TestCase):

    def test_index_view_with_no_questions(self):
        ''' If no questions exist, an appropriate message should eb displayed'''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        ''' questions with a pub date in the future'''
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_index_view_with_future_question(self):
        ''' even if both past and future exist, only past should be displayed'''
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],['<Question: Past question.>']
        )

    def test_index_view_with_two_past_question(self):
        ''' the questions index page may display multiple questions'''
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],['<Question: Past question 2.>', '<Question: Past question 1.>']
    )

class QuestionIndexDetailTests(TestCase):

    def test_detail_view_with_with_a_future_question(self):
        ''' the detail view of a question witha  pub date in future shoudl return a 404'''
        future_question = create_question(question_text='Future question.', days = 5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # def test_detail_view_with_a_past_question(self):
    #     """
    #     The detail view of a question with a pub_date in the past should
    #     display the question's text.
    #     """
    #     past_question = create_question(question_text='Past Question.', days=0)
    #     url = reverse('polls:detail', args=(past_question.id,))
    #     response = self.client.get(url)
    #     self.assertContains(response, past_question.question_text)

