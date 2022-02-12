from random import random
from urllib import response
from django.contrib.auth.models import User


from rest_framework.test import APIClient


class setupMedical:
    def medicalShopTemplate():
        return {
            "name": "Test Medical",
            "address": "TestUser Medical Shop Address",
            "pincode": 400607,
            "phone": "+911234567891",
            "latitude": random(),
            "longitude": random(),
            "email": "testuser" + "@email.com",
            "website": "https://testuser" + ".com",
        }

    def setupMedicalShop(client: APIClient, header: str, **kwargs):
        name = (kwargs.get("name") != None and kwargs.get("name") or "Test Medical",)
        address = (
            kwargs.get("address") != None
            and kwargs.get("address")
            or "TestUser Medical Shop Address",
        )
        pincode = (kwargs.get("pincode") != None and kwargs.get("pincode") or 400607,)
        phone = (
            kwargs.get("phone") != None and kwargs.get("phone") or "+911234567891",
        )
        latitude = (
            kwargs.get("latitude") != None and kwargs.get("latitude") or random(),
        )
        longitude = (
            kwargs.get("longitude") != None and kwargs.get("longitude") or random(),
        )
        email = (
            kwargs.get("email") != None
            and kwargs.get("email")
            or "testuser" + "@email.com",
        )
        website = (
            kwargs.get("website") != None
            and kwargs.get("website")
            or "https://testuser" + ".com",
        )
        payload = {
            "name": name,
            "address": address,
            "pincode": pincode,
            "phone": phone,
            "latitude": latitude,
            "longitude": longitude,
            "email": email,
            "website": website,
        }
        response = client.post("/api/", payload, HTTP_AUTHORIZATION=header)
        return response

    def setupCustomMedical(client: APIClient, header: str, payload: dict):
        response = client.post("/api/", payload, HTTP_AUTHORIZATION=header)
        return response
