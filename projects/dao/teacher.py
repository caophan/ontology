class Teacher:
    _id = None
    _name = None
    _birthdate = None
    _birthplace = None
    _hometown = None
    _address = None
    _year = None
    _email = None
    _phone = None
    _subject = None
    _title = None
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
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value):
        self._birthdate = value
    
    @property
    def birthplace(self):
        return self._birthplace

    @birthplace.setter
    def birthplace(self, value):
        self._birthplace = value
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        self._hometown = value
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def products(self):
        return self._products
    
    @products.setter
    def products(self, value):
        self._products = value