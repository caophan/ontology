class Product:
    _id = None
    _name = None
    _link = None
    _summary = None
    _subject = None
    _year = None
    _teachers = []

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
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def teachers(self):
        return self._teachers

    @teachers.setter
    def teachers(self, value):
        self._teachers = value
