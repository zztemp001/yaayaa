#coding=utf-8

from ajax.exceptions import AJAXError
from ajax.decorators import login_required

@login_required
def right_back_at_you(request):
    if len(request.POST):
        return request.POST
    else:
        raise AJAXError(500, 'Nothing to echo back.')