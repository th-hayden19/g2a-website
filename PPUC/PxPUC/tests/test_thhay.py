from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase
import json
from ..models import *

from django.test import TestCase


class test_DeptMod(TestCase):
    def setUp(self):
        file = open("/PxPUC/static/app/mastersheets/Model master spreadsheet.xlsx")
        dataframDict = pd.read_excel(
            file,
            sheet_name=[
                "Provisions",
                "Contracts",
                "Police departments",
                "Municipalities",
            ],
        )
        for sheet in dataframDict.values():
            for dbframe in sheet.intertuples(index=False):
                if sheet == "Police departments":
                    tfval = None
                    if dbframe.police_bill_of_rights == "X":
                        tfval = True
                    else:
                        tfval = False
                    dept_obj = Department.objects.create(
                        deptName=dbframe.Police_Agency_Name,
                        webLink=dbframe.Police_Department_Website,
                        fullOfficers2019=dbframe.Full_Time_Police_2019,
                        partOfficers2019=dbframe.Part_Time_police_2019,
                        hasBill=tfval,
                    )
                    dept_obj.save()

    def test_dept_obj(self):
        target_name = "Pittsburgh City"
        field_name = "fullOfficers2019"
        comparison = 996
        testDept = Department.objects.get(deptName=target_name)
        field_object = Department._meta.get_field(field_name)
        field_value = testDept.value_from_object(field_object)
        self.assertEqual(field_value, comparison)
