from .models import Block


def menu_links(request):
    links = Block.objects.all()
    return dict(links=links)