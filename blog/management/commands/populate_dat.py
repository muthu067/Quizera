from django.core.management import BaseCommand
from blog.models import course

class Command(BaseCommand):
    help='This command inserts post data'

    def handle(self, *args, **options):
        
        course.objects.all().delete()

        titles=[
        'Python',
        'Java',
        'R',
        'Go',
        'C',
        'C++',
        'Ruby',
        'Php'
        ]


        img_urls=[

            "https://picsum.photos/id/1/200/300",
            "https://picsum.photos/id/2/200/300",
            "https://picsum.photos/id/3/200/300",
            "https://picsum.photos/id/4/200/300",
            "https://picsum.photos/id/5/200/300",
            "https://picsum.photos/id/6/200/300",
            "https://picsum.photos/id/7/200/300",
            "https://picsum.photos/id/8/200/300",
        ]

        for title, img_url in zip( titles, img_urls):
            course.objects.create(title=title, img_url=img_url)

        self.stdout.write(self.style.SUCCESS("Completed successfully"))