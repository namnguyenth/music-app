def get_request(request, keyword):
    item = request.GET.get(keyword)
    return item
