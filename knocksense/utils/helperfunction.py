from rest_framework.response import Response


def get_context(status, success, message, data):
    """
    This helps us to reading the json easil,
    for help of this function we can easily figure out what our falut or where the code is broke
    the out put of this fuction is ---->>
                status = status.HTTP_200_OK,
                success=False,
                message=f"This is trial",
                data={}
    
    1. get_context(status, success, message, data):
        a. status is return HTTP respone
        b. success is booloen feild , it return the method is suceess or not
        c. message is string , it return the massage what we wrote
        d. data is return api
    """
    context = {}
    
    context["status"]   = status
    context["success"]  = success
    context["message"]  = message
    context["data"]     = data
    
    return Response(context, status = status)
