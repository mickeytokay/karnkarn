from django.shortcuts import render, get_object_or_404
from .models import Member
from block.models import Block
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.
def members(request, block_slug=None):
    blocks = None
    members = None

    if block_slug != None:
        blocks = get_object_or_404(Block, slug=block_slug)
        members = Member.objects.filter(block=blocks)
        paginator = Paginator(members, 10)
        page = request.GET.get('page')
        paged_members = paginator.get_page(page)
        member_count = members.count()
    
    else:
        members = Member.objects.all().order_by('block').all()
        paginator = Paginator(members, 10)
        page = request.GET.get('page')
        paged_members = paginator.get_page(page)
        member_count = members.count()
    context = {

        'members':paged_members,
        'member_count':member_count,
    }
    
    return render(request, 'members/members.html', context)



def search(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            members = Member.objects.order_by('-block').filter(full_name__icontains=keyword)
            member_count = members.count()
            
    context = {

        'members':members,
        'member_count':member_count,
    }
    return render(request, 'members/members.html', context)

    