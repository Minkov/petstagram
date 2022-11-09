def megabytes_to_bytes(mb):
    return mb * 1024 * 1024


def is_owner(request, obj):
    return request.user == obj.user


# class OwnerRequired:
#     def get(self, request, *args, **kwargs):
#         result = super().get(request, *args, **kwargs)
#
#         if request.user == self.object.user:
#             return result
#         else:
#             return '...'
#    def post(....)
