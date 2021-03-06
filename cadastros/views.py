from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from braces.views import GroupRequiredMixin

from .forms import GrupoProdutoForm, ProdutoForm
from pages.models import GrupoProduto, Produto

class GrupoProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = GrupoProduto
    context_object_name = 'db'
    template_name = 'cadastros/grupo_produto/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_queryset(self):

        search = self.request.GET.get('search')

        queryset = GrupoProduto.objects.order_by('descricao')

        if search:
            queryset = queryset.filter(descricao__istartswith=search)

        return queryset

class GrupoProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = GrupoProduto
    form_class = GrupoProdutoForm
    template_name = 'cadastros/grupo_produto/form.html'
    success_url = reverse_lazy('cadastros:grupo_produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class GrupoProdutoEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = GrupoProduto
    form_class = GrupoProdutoForm
    template_name = 'cadastros/grupo_produto/form.html'
    success_url = reverse_lazy('cadastros:grupo_produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class GrupoProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = GrupoProduto
    template_name = 'cadastros/grupo_produto/confirm_delete.html'
    success_url = reverse_lazy('cadastros:grupo_produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = Produto
    context_object_name = 'db'
    template_name = 'cadastros/produto/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'


    def get_queryset(self):

        search = self.request.GET.get('search')

        queryset = Produto.objects.order_by('descricao')

        if search:
            queryset = queryset.filter(descricao__istartswith=search)

        return queryset

class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto/form.html'
    success_url = reverse_lazy('cadastros:produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class ProdutoEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto/form.html'
    success_url = reverse_lazy('cadastros:produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = Produto
    template_name = 'cadastros/produto/confirm_delete.html'
    success_url = reverse_lazy('cadastros:produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'
