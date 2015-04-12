# -*- coding: utf-8 -*-
__author__ = 'Irsen'
# общая фикстура

import pytest
from fixture.application import Application

@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
