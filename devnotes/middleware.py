from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.template.loader import render_to_string
from . models import Devnote
from . forms import DevnoteForm
from django.conf import settings
import re

class DevnotesMiddleware(MiddlewareMixin):
    """ inject devnote view into html that is rendered"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """ skip middleware if debug is not true"""

        if not settings.DEBUG:
            return self.get_response(request)

        """if request is admin or ajax based skip the injection else inject"""

        if request.is_ajax() or 'admin' in request.path:
            response = self.get_response(request)
        else:
            response = self.inject_notes(self.get_response(request))
        return response

    def inject_notes(self, response):
        """content injection"""

        content = response.content.decode(response.charset)
        insert_before_end_body_tag = '</body>'
        pattern = re.escape(insert_before_end_body_tag)
        bits = re.split(pattern, content, flags=re.IGNORECASE)
        notes = Devnote.objects.order_by('-created_at')
        try:
            bits[-2] += render_to_string(
                "devnotes/list.html", {'devnotes': notes, 'notes_form':
                                       DevnoteForm()})
            response.content = insert_before_end_body_tag.join(bits)
        except IndexError:
            pass
        return response
