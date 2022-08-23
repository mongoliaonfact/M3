from production_function import FirmProduction


class Firm(FirmProduction):
    '''
	This is a firm class.
	'''

    def __init__(self, id):
        self.__id = id
        self.__labor = '0'
        self.__y = ''
        self.__share = ''
        self.__expansion = ''

    # firm labor attributes
    def get_labor(self):
        return self.__labor

    def set_labor(self, labor):
        self.__labor = labor

    # firm production method
    def set_y(self, y):
        self.__y = y

    # @property
    def get_y(self):
        return self.__y

    # firm's production with respect overall industry
    def set_share(self, share):
        self.__share = share

    def get_share(self):
        return self.__share

    # when firm decides to exit, production will accept 0 and therefore
    # will only produce domestically
    def to_exit(self):
        self.__y = 0

    # return self.__y

    #
    def to_expand(self, expand):
        self.__expansion = expand

    @property
    def get_expansion(self):
        return self.__expansion

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (
            self.__id, self.__labor,
            self.__y, self.__share, self.__expansion)
