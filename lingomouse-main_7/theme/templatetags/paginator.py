from django import template
import pprint

register = template.Library()


def paginator(context, adjacent_pages=2):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    model_name = str(context['opts']).split('.')[1]
    obj_id = "";
    if hasattr(context['original'], 'pk'):
        obj_id = context['original'].pk
    if hasattr(context['original'], 'id'):
        obj_id = context['original'].id

    app_label = context['app_label']
    available_app = context['available_apps']
    prev_url = ''
    next_url = ''

    if obj_id != "":
        for app in available_app:
            if app_label in app['app_label']:
                for models in app['models']:
                    if str(models['object_name']).lower() == model_name:
                        model = models['model']

                        if model.objects.filter(pk__lt=obj_id).order_by('pk').count() > 0:
                            prev_data = model.objects.filter(
                                pk__lt=obj_id).order_by('-pk').first()
                            prev_url = models['admin_url']+str(prev_data.pk)+'/change'
                        
                        if model.objects.filter(pk__gt=obj_id).order_by('pk').count() > 1:
                            next_data = model.objects.filter(
                                pk__gt=obj_id).order_by('pk').first()
                            next_url =  models['admin_url']+str(next_data.pk)+'/change'

    # obj.objects.get(pk__gt=obj_id)
    # pprint.pprint(object=obj)
    # page_numbers = [n for n in
    #                 range(context['object_id'] - adjacent_pages,
    #                       context['object_id'] + adjacent_pages + 1)
    #                 if n > 0 and n <= context['object_id']]

    # current_page = context['page_obj'].number
    # number_of_pages = context['paginator'].num_pages
    # page_obj = context['page_obj']
    # paginator = context['paginator']
    # startPage = max(current_page - adjacent_pages, 1)
    # endPage = current_page + adjacent_pages + 1
    # if endPage > number_of_pages:
    #     endPage = number_of_pages + 1
    # page_numbers = [n for n in range(startPage, endPage)
    #                 if 0 < n <= number_of_pages]


    return {
        'next_url': next_url,
        'prev_url': prev_url,
    }


register.inclusion_tag('admin/paginator.html', takes_context=True)(paginator)
