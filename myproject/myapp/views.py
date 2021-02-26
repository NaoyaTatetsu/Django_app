from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"
index = IndexView.as_view()


# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin


# # 機能を反映させるために必ずLoginRequiredMixinを先に記述する
# class IndexView(LoginRequiredMixin, generic.TemplateView):
#     template_name = "index.html"
# # 403を出してエラーを明示的にしたければ下の1行のコメントアウトを外す
# #raise_exception = True
# index = IndexView.as_view()
