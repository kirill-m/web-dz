from django.core.management.base import BaseCommand, CommandError
from hello_django.models import Question
from django.utils import timezone
from optparse import make_option

class Command(BaseCommand):
        args = '[number]'
        help = 'Add <number> questions'
	option_list = BaseCommand.option_list + (
	make_option('-n',
	    action='store',
	    type='int',
	    dest='num',
	    default=False,
	    help='Create number questions'),
	)
	
        def handle(self, *args, **options):
                for number in args:
                       # try:
                       #         question = Question.objects.get(pk=int(number))
                       # except Question.DoesNotExist:
                       #         raise CommandError('Question "%s" does not exist' % number)
			header = 'Header '+n;
                       	text = 'Text for question '+n;
                        date = timezone.now();
                        q = Question(question_header=header, question_text=text, pub_date=date)
                        q.save();
                        self.stdout.write('Successfully added "%s" questions ' % n);

