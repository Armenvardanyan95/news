from django.test import TestCase


class BaseTest(TestCase):

    serializer_class = object
    valid_data = object

    def __fill_data(self):
        for x in range(1, 5):
            self.serializer_class().create(self.valid_data)
