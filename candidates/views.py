from django.shortcuts import render
from .models import Candidate

# Create your views here.
def candidates(request):
    candidates = Candidate.objects.all().order_by('positions').all()
    candidate_count = candidates.count()
    
    context = {

        'candidates':candidates,
        'candidate_count':candidate_count
        
    }
    
    return render(request, 'members/candidate.html', context)