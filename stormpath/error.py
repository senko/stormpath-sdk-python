class Error(RuntimeError):
    """Error returned from the StormPath API service.

    The string content of the error is the low-level message, intended for
    the developer. The error also contains the following attributes:

    :py:attr:`status` - The corresponding HTTP status code.
    :py:attr:`code` - A Stormpath-specific error code that can be used to
        obtain more information.
    :py:attr:`developer_message` - A clear, plain text explanation with
        technical details that might assist a developer calling the
        Stormpath API.
    :py:attr:`message` - A simple, easy to understand message that you can
        show directly to your application end-user.
    :py:attr:`more_info` - A fully qualified URL that may be accessed to
        obtain more information about the error.

    """
    def __init__(self, error):
        if error is None:
            error = {}

        def try_int(val):
            try:
                return int(val)
            except:
                return -1

        msg = error.get('developerMessage')
        super(Error, self).__init__(msg)
        self.status = try_int(error.get('status', -1))
        self.code = try_int(error.get('code', -1))
        self.developer_message = msg
        self.more_info = error.get('moreInfo')
        self.message = error.get('message')
