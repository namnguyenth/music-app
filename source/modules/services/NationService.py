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
