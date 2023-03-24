#!/usr/bin/python3
"""task for changes to console"""

import unittest
import io
from console import HBNBCommand
import sys


class Test(unittest.TestCase):
    def test_create_instance(self):
        """create state"""
        output = io.StringIO()
        sys.stdout = output
        console = HBNBCommand()
        console.onecmd("create State id='test' name=test2")
        sys.stdout = sys.__stdout__
        expected_output = output.getvalue()
        self.assertIn("1", expected_output)
