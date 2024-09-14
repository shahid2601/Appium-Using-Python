import pytest

def setup_function(function):
    print("running in functional level")

def teardown_function(function):
    print("closing teardown in function")

def setup_module(module):
    print("running in module level")

def teardown_module(module):
    print("closing teardown in module")

def test_demo1():
    print("Demo pytest1")

def test_demo2():
    print("Demo pytest2")