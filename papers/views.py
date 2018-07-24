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
        for i, sub_category in enumerate(sub_categories):
            papers = (Paper.objects.filter(sub_category=sub_category).
                      order_by('display_order'))
            paper_list = list(papers)
            for paper in paper_list:
                if (paper.full_text_link and
                    (paper.full_text_link.find('rfrench.org') != -1 or
                     not paper.full_text_link.startswith('http'))):
                    paper.full_text_link = (paper.full_text_link.
                            replace('http://rfrench.org/papers', '/papers'))
                    paper.full_static_content = True
                else:
                    paper.full_static_content = False
                if (paper.abstract_text_link and
                    (paper.abstract_text_link.find('rfrench.org') != -1 or
                     not paper.abstract_text_link.startswith('http'))):
                    paper.abstract_text_link = (paper.abstract_text_link.
                            replace('http://rfrench.org/papers', '/papers'))
                    paper.abstract_static_content = True
                else:
                    paper.abstract_static_content = False
            if len(paper_list) > 0:
                sub_category_dict[category.name].append(sub_category)
                category_used = True
                paper_dict[(category.name,
                            sub_category.name)] = paper_list
            sub_category.not_last_entry = i != len(sub_categories)-1
            print(sub_category.name, sub_category.not_last_entry)
        if category_used:
            category_list.append(category.name)

    return render(request, 'papers/papers.html',
                  {'categories': category_list,
                   'sub_categories': sub_category_dict,
                   'papers': paper_dict})
