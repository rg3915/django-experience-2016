from django.shortcuts import render
from .models import Company
from djexperience.utils.utils import get_field_display
from djexperience.utils.lists import COMPANY_TYPE


def company_list(request):
    companies = Company.objects.values('name',
                                       'companytype',
                                       'contact_company__name',
                                       'contact_company__email',
                                       'contact_company__phone',
                                       'status_company__status',
                                       'status_company__is_completed',
                                       'proposal_company__code',
                                       'proposal_company__price')
    # Chama a função que retorna get_FOO_display manualmente.
    get_field_display(companies, 'companytype', COMPANY_TYPE)
    return render(request, 'company/company_list.html', {'companies': companies})
