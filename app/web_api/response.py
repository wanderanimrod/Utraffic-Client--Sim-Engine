from flask import Response


class InsecureResponse(Response):
    """
    This Response class is insecure because it allows all *origins* to fetch data from this API by adding the
    'Access-Control-Allow-Origin: *' header to all responses from this API
    This has been done to allow the web-client's ajax to call the API without getting blocked on the grounds of
    fear of XSS (Cross Site Scripting)
    """
    def __init__(self, rv, status=None, headers=None, mimetype=None, content_type=None, direct_passthrough=False):
        Response.__init__(self, rv, status=status, headers=headers,  mimetype=mimetype, content_type=content_type,
                          direct_passthrough=direct_passthrough)
        self.headers['Access-Control-Allow-Origin'] = "*"