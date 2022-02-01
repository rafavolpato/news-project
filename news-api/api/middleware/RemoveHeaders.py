class RemoveHeaders:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        # del response['Server']
        response.__setitem__('Server', '')
        return response
