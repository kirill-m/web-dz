from django.core.management.base import BaseCommand, CommandError
from hello_django.models import Question

class Command(BaseCommand):
	args = '<question_id question_id ...>'
	help = 'Generate questions'
	
	def handle(self, *args, **options):
		for question_id in args:
			try:
				question = Question.objects.get(pk=int(question_id))
			except Question.DoesNotExist:
				raise CommandError('Question "%s" does not exist' % question_id)

			self.stdout.write('Successfully did smth with question "%s"' % question_id);
