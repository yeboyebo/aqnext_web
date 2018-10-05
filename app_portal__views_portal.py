
# @class_declaration aqnext #
class aqnext(web):

    def aqnext_cms(self, request):
        return render(request, "portal/cms.html", {})

    def __init__(self, context=None):
        super(aqnext, self).__init__(context)

    def cms(self, request):
        return self.ctx.aqnext_cms(request)

