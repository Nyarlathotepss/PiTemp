from django.test import TestCase
from website.models import CustomUser, Temperature
import datetime


class ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = CustomUser.objects.create_user(id=1, username='usertest', password='test123', email='test@test.com',
                                              adress='50 rue du test', city='Test', postal_code='00000')
        Temperature.objects.create(id=1, temperature=22.01, date='29.85 2020-07-23 09:24:36.534325+00:00',
                                   idUser=user)

    def test_email_name_label(self):
        """ Check the label email"""
        user = CustomUser.objects.get(pk='1')
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_user_email_max_lenght(self):
        """ Check the max length """
        user = CustomUser.objects.get(pk='1')
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 254)

    def test_user_adress_label(self):
        """ Check the label adress"""
        user = CustomUser.objects.get(pk='1')
        field_label = user._meta.get_field('adress').verbose_name
        self.assertEquals(field_label, 'adress')

    def test_user_adress_max_lenght(self):
        """ Check the max length """
        user = CustomUser.objects.get(pk='1')
        max_length = user._meta.get_field('adress').max_length
        self.assertEquals(max_length, 254)

    def test_user_city_label(self):
        """ Check the label adress"""
        user = CustomUser.objects.get(pk='1')
        field_label = user._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    def test_user_city_max_lenght(self):
        """ Check the max length """
        user = CustomUser.objects.get(pk='1')
        max_length = user._meta.get_field('city').max_length
        self.assertEquals(max_length, 254)

    def test_user_postal_code_label(self):
        """ Check the label adress"""
        user = CustomUser.objects.get(pk='1')
        field_label = user._meta.get_field('postal_code').verbose_name
        self.assertEquals(field_label, 'postal code')

    def test_user_postal_code_max_lenght(self):
        """ Check the max length """
        user = CustomUser.objects.get(pk='1')
        max_length = user._meta.get_field('postal_code').max_length
        self.assertEquals(max_length, 5)

    def test_temperature_temperature_label(self):
        """ Check the label temperature"""
        temperature = Temperature.objects.get(pk='1')
        field_label = temperature._meta.get_field('temperature').verbose_name
        self.assertEquals(field_label, 'temperature')

    def test_temperature_temperature_is_float(self):
        """ Check that the temperature is a float """
        temperature = Temperature.objects.get(pk='1')
        temp_type = type(temperature.temperature)
        self.assertEquals(temp_type, float)

    def test_temperature_date_label(self):
        """ Check the label date"""
        temperature = Temperature.objects.get(pk='1')
        field_label = temperature._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_temperature_temperature_is_datetime(self):
        """ Check that the temperature is a float """
        temperature = Temperature.objects.get(pk='1')
        date_type = type(temperature.date)
        self.assertEquals(date_type, datetime.datetime)