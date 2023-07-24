import datetime
from rest_framework.exceptions import ValidationError, NotFound
from modules.common.constant import PAGE_SIZE_DEFAULT
from django.core.paginator import Paginator
from django.db.models import Q
from modules.common import common
from modules.models.nation.nation import Nation


def get_nation(request):
    search = common.get_request(request, 'search')
    page = int(common.get_request(request, 'page')) if common.get_request(request, 'page') else 10

    if not search:
        search = ''

    query = Nation.objects.filter(name__icontains=search).order_by('name')
    paginator = Paginator(query, PAGE_SIZE_DEFAULT)
    nation = paginator.page(page)

    return nation


def create_nation(request):
    nation = Nation.objects.create(
        name=request.data['name'],
        created_date=datetime.datetime.now(),
        created_by='admin',
        updated_date=datetime.datetime.now(),
        updated_by='admin',
    )
    return nation


def update_nation(request, nation_id):
    nation = Nation.objects.get(id=nation_id)
    if not nation:
        raise NotFound(f"Nation id {nation_id} is not exist.")

    nation.name = request['name']
    nation.updated_date = datetime.datetime.now()
    nation.updated_by = 'admin'

    nation.save()

    return nation


def get_nation_by_id(nation_id):
    nation = Nation.objects.filter(
        id=nation_id,
        deleted_by__isnull=True,
        deleted_date__isnull=True,
    )
    if not nation:
        raise NotFound(f"Nation id {nation_id} is not exist.")

    return nation


def delete_nation(nation_id):
    nation = Nation.objects.get(id=nation_id)
    if not nation:
        raise NotFound(f"Nation id {nation_id} is not exist.")

    nation.deleted_date = datetime.datetime.now()
    nation.deleted_by = 'admin'

    nation.save()

    return nation
