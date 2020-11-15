from awsomdesktop import *
import pytest
import os
from collections import UserDict
from textwrap import dedent
import json

class Test_Project_Class:
    def test_initialisation(self):
        """ Create a simple Project object with CleverDict properties """
        pass

class Test_File_Handling:
    def test_copy_media_from_device(self):
        """
        Candidate for xfail as this may take time and requires a device
        with actual media to be connected.
        """
        x = CleverDict({"total": 6, "usergroup": "Knights of Ni"})
        assert x.total == 6
        assert x["total"] == 6
        assert x.usergroup == "Knights of Ni"
        assert x["usergroup"] == "Knights of Ni"

class Test_Pymiere_Automation:
    def test_create_prproj_from_template(self):
        """ Create then strike down example prproj file """
        pass
