from modules.models.nation.nation import Nation


def get_nation(request):
    nation = Nation.objects.all()
    return nation