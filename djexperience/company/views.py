from django.shortcuts import render
from .models import Company
from djexperience.utils.lists import COMPANY_TYPE


def company_list(request):
    companies = Company.objects.values('name',
                                       'companytipe',
                                       'contact_company__name',
                                       'contact_company__email',
                                       'contact_company__phone',
                                       'status_company__status',
                                       'status_company__is_completed',
                                       'proposal_company__code',
                                       'proposal_company__price')
    res = []
    choices = dict(COMPANY_TYPE)
    for obj in companies:
        new_obj = obj
        new_obj['companytipe'] = choices.get(obj['companytipe'], None)
        res.append(new_obj)
    return render(request, 'company/company_list.html', {'companies': companies})
