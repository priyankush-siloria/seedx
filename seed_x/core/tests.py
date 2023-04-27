import json
import base64

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from core.models import Tag


def create_user(superuser=False, **kwargs):
    return (
        User.objects.create_superuser(**kwargs)
        if superuser
        else User.objects.create_user(**kwargs)
    )


class TestTag(APITestCase):
    USERNAME = "user"
    EMAIL = "user@seedx.com"
    PASSWORD = "user@123"
    DATA = {}
    CORE_URL = "/api/tags/"

    def setUp(self) -> None:
        self.user = create_user(
            username=self.USERNAME,
            email=self.EMAIL,
            password=self.PASSWORD,
            superuser=True
        )
        self.__load_tag_data()

    def __load_tag_data(self):
        # Using single .json file. Should use multiple files for more data.
        with open("core/fixtures/tags.json") as f:
            self.DATA = json.load(f)

    def __populate_database(self):
        tag = Tag(**self.DATA["automated_short_name"]["new_name"])
        tag.short_name = "G"
        tag.save()

    def test_tag_creation(self):
        """Test we are able to create new tags"""
        data = self.DATA["good_tag_data"]
        url = self.CORE_URL
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        # self.client.credentials(
        #     HTTP_AUTHORIZATION=f"Basic {self.__get_auth_credentials()}")
        self.client.force_login(self.user)
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_automated_tag_short_names(self):
        """Test the short names we are giving to tags automatically"""
        url = self.CORE_URL
        data = self.DATA["automated_short_name"]["new_name"]
        self.client.force_login(self.user)
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["short_name"], "G")
        data = self.DATA["automated_short_name"]["repeated"]
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["short_name"], "Ge")

    def test_existing_shortnames_fails_creation(self):
        """Test that giving a short_name that already exists fails tag creation"""
        url = self.CORE_URL
        data = self.DATA["bad_data"]["existing_short_name"]
        self.__populate_database()
        self.client.force_login(self.user)
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_existing_tag_type_tag_value_fails(self):
        """Test an existing combination of tag_type and value fails creation"""
        url = self.CORE_URL
        data = self.DATA["bad_data"]["repeated_tag"]
        self.__populate_database()
        self.client.force_login(self.user)
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
