class Subject:
    _id = None
    _name = None
    _teachers = []
    _products = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value

    @property
    def teachers(self):
        return self._teachers

    @teachers.setter
    def teachers(self, value):
        self._teachers = value
