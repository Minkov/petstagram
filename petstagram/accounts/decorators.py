from django.shortcuts import redirect


def user_required(model_class, methods=None):
    if methods is None:
        methods = ['GET', 'POST']

    def decorator(view_func):
        def wrapper(request, pk, *args, **kwargs):
            model_obj = model_class.objects.get(pk=pk)

            if request.method not in methods or model_obj.user.user_id == request.user.id:
                return view_func(request, pk, *args, **kwargs)
            return redirect('login')

        return wrapper

    return decorator
