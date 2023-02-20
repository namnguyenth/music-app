import datetime

from django.db.models import Q

from modules.common import common
from modules.models.nation.nation import Nation


def get_nation(request):
    search = common.get_request(request, 'search')
    if not search:
        search = ''

    nation = Nation.objects.filter(
        Q(name__icontains=search)
    )
    # nation1 = Nation.objects.raw('SELECT * FROM modules_nation')
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

    nation.name = request['name']
    nation.updated_date = datetime.datetime.now()
    nation.updated_by = 'admin'

    nation.save()

    return nation


def get_nation_by_id(nation_id):
    nation = Nation.objects.filter(
        id__icontains=nation_id,
        deleted_by__isnull=True,
        deleted_date__isnull=True,
    )
    return nation


def delete_nation(nation_id):
    nation = Nation.objects.get(id=nation_id)

    nation.deleted_date = datetime.datetime.now()
    nation.deleted_by = 'admin'

    nation.save()

    return nation
