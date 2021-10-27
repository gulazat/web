from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import My_data,Classification,Tag_name
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django_comments.models import Comment
from django.utils.safestring import mark_safe
from django.db.models import Q

from helpers import pagination_data
# Create your views here.


def make_paginator(objects,page,num= 10):
    paginator = Paginator(objects, num)
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return object_list,paginator



def main(request):
    datas = My_data.objects.all()
    page = request.GET.get('page', 1)
    datas,paginator = make_paginator(datas, page)
    page_data = pagination_data(paginator,page)

    return render(request,'my_data/main.html',locals())




def data_detail(request,pk):
    datas = My_data.objects.get(id = pk)
    datas.increase_visiting()

    comment_list = list()
    def get_comment_list(comments):
        for comment in comments:
            comment_list.append(comment)
            children = comment.child_comment.all()
            if len(children) > 0:
                get_comment_list(children)


    top_comments = Comment.objects.filter(object_pk = pk,parent_comment = None,
                                          content_type__app_label = 'my_data').order_by('-submit_date')
    get_comment_list(top_comments)


    return render(request, 'my_data/detail.html', locals())





def category(request,pk):
    cats = Classification.objects.get(pk = pk)
    datas = My_data.objects.filter(category = cats)[:5]

    page = request.GET.get('page', 1)
    datas, paginator = make_paginator(datas, page)
    page_data = pagination_data(paginator, page)



    return render(request, 'my_data/index.html', locals())


def tag(request,pk):
    tag_name = Tag_name.objects.get(pk = pk)
    datas = My_data.objects.filter(tags = tag_name)

    page = request.GET.get('page', 1)
    datas, paginator = make_paginator(datas, page)
    page_data = pagination_data(paginator, page)



    return render(request, 'my_data/all_categ.html', locals())


def search(request):
    keyword = request.GET.get('keyword',None)
    if not keyword:
        error_message = "请输入关键字"
        return render(request, 'my_data/main.html', locals())
    datas = My_data.objects.filter(Q(title__icontains=keyword)|Q(body__icontains = keyword)|Q(abstract__icontains = keyword))

    paginator = Paginator(datas, 10)

    try:
        page = int(request.GET.get('page', 1))
        datas = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        datas = paginator.page(1)

    return render(request, 'my_data/main.html', locals())




def all_tags(request):
    datas = My_data.objects.all()
    page = request.GET.get('page', 1)
    datas, paginator = make_paginator(datas, page)
    page_data = pagination_data(paginator, page)
    return render(request,'my_data/all_tags.html', locals())

def all_categ(request):
    datas = My_data.objects.all()
    page = request.GET.get('page', 1)
    datas, paginator = make_paginator(datas, page)
    page_data = pagination_data(paginator, page)
    return render(request,'my_data/all_categ.html', locals())

def reply(request, pk):
    if not request.session.get('login',None) and not request.user.is_authenticated:
        return redirect("/")
    parent_comment= get_object_or_404(Comment, pk = pk)
    return render(request, 'my_data/reply.html',locals())

