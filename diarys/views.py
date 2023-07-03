from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm


# Create your views here.
def index(request):
    return render(request, "diarys/index.html")


def page_list(request):
    object_list = Page.objects.all()
    return render(request, "diarys/page_list.html", {"object_list": object_list})


def info(request):
    return render(request, "diarys/info.html")


def page_detail(request, page_id):
    object = Page.objects.get(id=page_id)
    return render(request, "diarys/page_detail.html", {"object": object})


def page_create(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            new_page = form.save()
            return redirect("page-detail", page_id=new_page.id)
    else:
        form = PageForm()
    return render(request, "diarys/page_form.html", {"form": form})


def page_update(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == "POST":
        form = PageForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect("page-detail", page_id=object.id)
    else:
        form = PageForm(instance=object)
    return render(request, "diarys/page_form.html", {"form": form})


def page_delete(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == "POST":
        object.delete()
        return redirect("page-list")
    else:
        return render(request, "diarys/page_confirm_delete.html", {"object": object})
