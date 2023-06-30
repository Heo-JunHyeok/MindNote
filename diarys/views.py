from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm


# Create your views here.
def page_list(request):
    pages = Page.objects.all()
    context = {"pages": pages}
    return render(request, "diarys/page_list.html", context)


def info(request):
    return render(request, "diarys/info.html")


def page_detail(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {"object": page}
    return render(request, "diarys/page_detail.html", context)


def page_create(request):
    if request.method == "POST":
        new_page = Page(
            title=request.POST["title"],
            content=request.POST["content"],
            feeling=request.POST["feeling"],
            score=request.POST["score"],
        )
        new_page.save()
        return redirect("page-detail", page_id=new_page.id)
    else:
        form = PageForm()
        return render(request, "diarys/page_form.html", {"form": form})
