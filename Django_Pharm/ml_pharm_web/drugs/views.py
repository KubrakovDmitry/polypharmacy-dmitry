from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse

from .forms import AddDrugForm, AddDrugGroupForm
from . import services


add_menu = [
    {'name_model': "Добавить группу ЛС", 'pk': "1", 'url_name': 'add_DrugGroup'},
    {'name_model': "Добавить ЛС", 'pk': "1", 'url_name': 'add_Drug'},
    {'name_model': "Изменить побочки", 'pk': "1", 'url_name': 'update_SideEffects'},
]


@staff_member_required
def addpage_views(request):
    context = {
        'add_element': add_menu,
        'title': 'Добавить данные в БД',
        'add_element_selected': 0,
    }
    return render(request, 'drugs/addElementDB.html', context)


@staff_member_required
def addDrug_views(request):
    if request.method == 'POST':
        form = AddDrugForm(request.POST)
        if form.is_valid():
            try:
                services.handle_add_drug(form.cleaned_data['name'])
                return redirect('home')
            except Exception as e:
                form.add_error(None, f'Ошибка добавления ЛС: {e}')
    else:
        form = AddDrugForm()

    context = {
        'form': form,
        'title': 'Добавление нового ЛС',
        'add_element': add_menu,
        'add_element_selected': 0,
        'form_action': reverse('add_Drug'),
    }

    return render(request, 'drugs/addDrugGroup.html', context=context)


@staff_member_required
def addDrugGroup_views(request):
    if request.method == 'POST':
        form = AddDrugGroupForm(request.POST)
        if form.is_valid():
            try:
                services.handle_add_drug_group(form.cleaned_data)
                return redirect('home')
            except Exception as e:
                form.add_error(None, f'Ошибка добавления группы ЛС: {e}')
    else:
        form = AddDrugGroupForm()

    context = {
        'form': form,
        'title': 'Добавление новой группы ЛС',
        'add_element': add_menu,
        'add_element_selected': 0,
        'form_action': reverse('add_DrugGroup'),
    }

    return render(request, 'drugs/addDrugGroup.html', context=context)


@staff_member_required
def updateSideEffects_views(request):
    tipe_view, title, side_effects, form_check = services.get_side_effects_view(request)
    form_add = services.get_add_side_effect_form(request)
    form_update = services.get_update_side_effect_form(request, title)

    context = {
        'form_check_type_view': form_check,
        'side_effects': side_effects,
        'title_type_view_side_effects': title,
        'tipe_view': tipe_view,
        'form_add_SideEffect': form_add,
        'form_add_SideEffect_rande': form_update,
        'title': 'Изменить побочки',
        'add_element': add_menu,
        'add_element_selected': 0,
    }

    return render(request, 'drugs/updateSideEffects.html', context=context)
