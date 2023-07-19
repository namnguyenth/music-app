def json_response(api):
    def wrapper(*args, **kwargs):
        try:
            response_data = api(*args, **kwargs)
            formatted_response = {
                "data": response_data,
                "success": True,
                "message": "Success"
            }
        except Exception as e:
            formatted_response = {
                "data": None,
                "success": False,
                "message": str(e)
            }
        return formatted_response

    return wrapper
