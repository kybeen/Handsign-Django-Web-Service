from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import render

# Create your views here.
def test1(request):
    return HttpResponse("blog/test1 응답!")


def test2(request, no):
    print('no 타입:', type(no))
    return HttpResponse(f'no:{no}')


def test3(request, year, month, day):
    return HttpResponse(f'년:{year}, 월:{month}, 일:{day}')


# def list(request):
#     post_list = Post.objects.all()
#     titles = ''

#     for post in post_list:
#         titles += post.title

    return HttpResponse(titles)

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_all = post.comments.all()
    tag_list = post.tag.all()
    return render(request, 'blog/detail.html', {'post': post, 'comment_all':comment_all, 'tag_list':tag_list})



def list(request):
    post_list = Post.objects.all()    
    search_key = request.GET.get("keyword")
    if search_key:
        post_list = Post.objects.filter(title__icontains=search_key)
    return render(request, 'blog/list.html', {'post_all':post_list, 'q':search_key})

def test4(request):
    return render(request, 'blog/test4.html', {'score':70})

def test5(request):
    var ='''
    Miracles happen to only those who believe in them.
    Think like a man of action and act like man of thought.
    Courage is very important. Like a muscle, it is strengthened by use.
    Life is the art of drawing sufficient conclusions from insufficient premises.
    By doubting we come at the truth.
    A man that has no virtue in himself, ever envies virtue in others.
    When money speaks, the truth keeps silent.
    Better the last smile than the first laughter.
    '''

    return render(request, 'blog/test5.html', {'var':var})


from django.utils import timezone
def test6(request):
    d1 = timezone.now()
    d2 = timezone.datetime(2001,3,19)
    d3 = timezone.datetime(2030,3,19)

    return render(request, 'blog/test6.html', {'date1':d1, 'date2':d2, 'date3':d3})

    

def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all':post_list})


def test7(request):
    print('요청방식 : ', request.method)
    print('GET방식으로 전달된 질의 문자열 :', request.GET)
    print('Post방식으로 전달된 질의 문자열 :', request.POST)
    print('업로드 파일 : ', request.FILES)
    return render(request, 'blog/form_test.html')

from .forms import PostForm

from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, PostModelForm

# def post_create(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             post = Post.objects.create(**form.cleaned_data)
#             return redirect(post)
#     else:
#         form = PostModelForm()
#         return render(request, 'blog/post_form.html', {'form':form})


# def post_create(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostModelForm()
#         return render(request, 'blog/post_form.html', {'form':form})


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'blog/post_update.html', {'form':form})

def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
    else:
        return render(request, 'blog/post_delete.html', {'post':post})


def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
    else:
        form = PostModelForm()
        return render(request, 'blog/post_form.html', {'form':form})
