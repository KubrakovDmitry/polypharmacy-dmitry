from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


# addpage_views, addDrug_views, addDrugGroup_views, updateSideEffects_views

@staff_member_required
def addpage_views(request):
    context = {
        'add_element': add_menu,
        'menu': get_menu_for_user(request.user),
        'title': 'Добавить данные в БД',
        'add_element_selected': 0,
    }
    return render(request, 'pharm/addElementDB.html', context=context)


@staff_member_required
def addDrug_views(request):
    form = addDrug(request)
    context = {
        'add_element': add_menu,
        'menu': get_menu_for_user(request.user),
        'form': form,
        'title': 'Добавление нового ЛС',
        'add_element_selected': 0,
    }
    return render(request, 'pharm/addDrugGroup.html', context=context)


@staff_member_required
def addDrugGroup_views(request):
    form = addDrugGroup(request)
    context = {
        'add_element': add_menu,
        'menu': get_menu_for_user(request.user),
        'form': form,
        'title': 'Добавление новой группы ЛС',
        'add_element_selected': 0,
    }
    return render(request, 'pharm/addDrugGroup.html', context=context)


@staff_member_required
def updateSideEffects_views(request):
    tipe_view, title_type_view_side_effects, side_effects, form_check_type_view,  = CheckSideEffectsView(request)
    form_add_SideEffect = AddNewSideEffect(request)
    form_add_SideEffect_rande = UpdateSeideEffectRande(request, title_type_view_side_effects)
    context = {
        'add_element': add_menu,                       
        'menu': get_menu_for_user(request.user), 

        'form_check_type_view': form_check_type_view, 
        "side_effects": side_effects,
        "title_type_view_side_effects": title_type_view_side_effects,
        "tipe_view": tipe_view,

        "form_add_SideEffect": form_add_SideEffect,
        "form_add_SideEffect_rande": form_add_SideEffect_rande,

        'title': 'Изменить побочки',
        'add_element_selected': 0,
    }
    return render(request, 'pharm/updateSideEffects.html', context=context)
