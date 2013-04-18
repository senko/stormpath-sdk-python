__author__ = 'ecrisostomo'

from stormpath.resource.resource import Resource

class ResourceError(RuntimeError):

    def __init__(self, error):
        super(ResourceError, self).__init__(error.message if error else None)
        self.error = error

    @property
    def status(self):
        return self.error.status if self.error else -1

    @property
    def code(self):
        return self.error.code if self.error else -1

    @property
    def developer_message(self):
        return self.error.developer_message if self.error else None

    @property
    def more_info(self):
        return self.error.more_info if self.error else None

    @property
    def message(self):
        return self.error.message if self.error else None


class Error(Resource):

    STATUS = "status"
    CODE = "code"
    MESSAGE = "message"
    DEV_MESSAGE = "developerMessage"
    MORE_INFO = "moreInfo"

    def __init__(self, properties):
        super(Error, self).__init__(properties=properties)

    @property
    def status(self):
        return self._get_property_(Error.STATUS)

    @property
    def code(self):
        return self._get_property_(Error.CODE)

    @property
    def message(self):
        return self._get_property_(Error.MESSAGE)

    @property
    def developer_message(self):
        return self._get_property_(Error.DEV_MESSAGE)

    @property
    def more_info(self):
        return self._get_property_(Error.MORE_INFO)
