# -*- coding: utf-8 -*-
from .utils import translations

_ = translations.ugettext


def validate_difficulty(value):
    if not isinstance(value, (int, long)):
        raise TypeError(_("Difficulty is not an integer"))
    if value < 0:
        raise ValueError(_("Difficulty must be a positive integer"))


def validate_settings(value):
    if not isinstance(value, dict):
        raise TypeError(_("Settings must be a dictionary"))
