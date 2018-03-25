from django.shortcuts import render
from .models import PaperCategory, PaperSubCategory, Paper

def papers(request):
    paper_dict = {}
    category_list = []
    sub_category_dict = {}

    for category in PaperCategory.objects.all():
        category_used = False
        sub_categories = (PaperSubCategory.objects.
                          filter(category__name=category.name))
        sub_category_dict[category.name] = []
        for sub_category in sub_categories:
            papers = (Paper.objects.filter(sub_category=sub_category).
                      order_by('display_order'))
            paper_list = list(papers)
            if len(paper_list) > 0:
                sub_category_dict[category.name].append(sub_category.name)
                category_used = True
                paper_dict[(category.name,
                            sub_category.name)] = paper_list
        if category_used:
            category_list.append(category.name)

    return render(request, 'papers/papers.html',
                  {'categories': category_list,
                   'sub_categories': sub_category_dict,
                   'papers': paper_dict})
