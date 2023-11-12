class TourPackage:
    def __init__(self, code, client_name, resort_name, room_number, accommodation_type, check_in_date, check_out_date, number_of_people, price):
        self.code = code#Эта строка присваивает атрибуту code экземпляра класса значение параметра code.
        self.client_name = client_name#Эта строка присваивает атрибуту clientname экземпляра класса значение параметра clientname.
        self.resort_name = resort_name# Эта строка присваивает атрибуту resortname экземпляра класса значение параметра resortname.
        self.room_number = room_number#Эта строка присваивает атрибуту roomnumber экземпляра класса значение параметра roomnumber.
        self.accommodation_type = accommodation_type#Эта строка присваивает атрибуту accommodationtype экземпляра класса значение параметра accommodationtype.
        self.check_in_date = check_in_date#Эта строка присваивает атрибуту checkindate экземпляра класса значение параметра checkindate.
        self.check_out_date = check_out_date#Эта строка присваивает атрибуту checkoutdate экземпляра класса значение параметра checkoutdate.
        self.number_of_people = number_of_people#Эта строка присваивает атрибуту numberofpeople экземпляра класса значение параметра numberofpeople.
        self.price = price#Эта строка присваивает атрибуту price экземпляра класса значение параметра price.

    def __str__(self):
        return f"Code: {self.code}, Client Name: {self.client_name}, Resort Name: {self.resort_name}, Room Number: {self.room_number}, Accommodation Type: {self.accommodation_type}, Check-in Date: {self.check_in_date}, Check-out Date: {self.check_out_date}, Number of People: {self.number_of_people}, Price: {self.price}"
        #Метод str() возвращает строковое представление экземпляра класса со значениями его атрибутов в определенном формате


class InternationalTourPackage(TourPackage):
    def __init__(self, code, client_name, resort_name, room_number, accommodation_type, check_in_date, check_out_date, number_of_people, price, passport, insurance):
        super().__init__(code, client_name, resort_name, room_number, accommodation_type, check_in_date, check_out_date, number_of_people, price)
        #Эта строка вызывает конструктор родительского класса TourPackage с передачей ему аргументов инициализации, чтобы инициализировать атрибуты родительского класса.
        self.passport = passport#Эта строка присваивает атрибуту passport экземпляра класса значение параметра passport.
        self.insurance = insurance#Эта строка присваивает атрибуту insurance экземпляра класса значение параметра insurance.

    def __str__(self):
        return super().__str__() + f", Passport: {self.passport}, Insurance: {self.insurance}"# Возвращает строковое представление экземпляра класса с значениями его атрибутов в определенном формате. В данном случае, метод вызывает метод str() родительского класса (TourPackage) и добавляет информацию о паспорте и страховке.


class SanatoriumTourPackage(TourPackage):
    def __init__(self, code, client_name, resort_name, room_number, accommodation_type, check_in_date, check_out_date, number_of_people, price, medical_policy, diagnosis, referral):
        super().__init__(code, client_name, resort_name, room_number, accommodation_type, check_in_date, check_out_date, number_of_people, price)
        self.medical_policy = medical_policy # Присваивание атрибуту medical_policy экземпляра класса значение параметра medical_policy.
        self.diagnosis = diagnosis# Присваивание атрибуту diagnosis экземпляра класса значение параметра diagnosis.
        self.referral = referral# Присваивание атрибуту referral экземпляра класса значение параметра referral.

    def __str__(self):
        return super().__str__() + f", Medical Policy: {self.medical_policy}, Diagnosis: {self.diagnosis}, Referral: {self.referral}"


class ChildrenHealthTourPackage(TourPackage):
    def __init__(self, code, client_name, resort_name, room_number, accommodation_type, check_in_date, check_out_date, number_of_people, price, age, birth_certificate, gender):
        super().__init__(code, client_name, resort_name, room_number, accommodation_type, check_in_date, check_out_date, number_of_people, price)
        self.age = age # Присваивание атрибуту age экземпляра класса значение параметра age.
        self.birth_certificate = birth_certificate # Присваивание атрибуту birth_certificate экземпляра класса значение параметра birth_certificate.
        self.gender = gender# Присваивание атрибуту gender экземпляра класса значение параметра gender.

    def __str__(self):
        return super().__str__() + f", Age: {self.age}, Birth Certificate: {self.birth_certificate}, Gender: {self.gender}"

# Создание объекта tour1 класса InternationalTourPackage с передачей аргументов в конструктор.
tour1 = InternationalTourPackage("001", "John Doe", "Resort ABC", "101", "Deluxe Room", "2022-01-01", "2022-01-05", 2, 2000, "123456", "Yes")
print(tour1)
# Создание объекта tour2 класса SanatoriumTourPackage с передачей аргументов в конструктор.
tour2 = SanatoriumTourPackage("002", "Jane Smith", "Resort XYZ", "202", "Standard Room", "2022-02-01", "2022-02-07", 1, 1500, "789012", "Covid-19", "Doctor's referral")
print(tour2)
# Создание объекта tour3 класса ChildrenHealthTourPackage с передачей аргументов в конструктор.
tour3 = ChildrenHealthTourPackage("003", "Michael Johnson", "Resort DEF", "303", "Junior Suite", "2022-03-01", "2022-03-10", 3, 3000, 8, "456789", "Male")
print(tour3)