# -*- coding: utf-8 -*-

import six

from candv import ValueConstant

from .settings import SETTINGS
from .utils import translations


_ = translations.ugettext


def validate_difficulty(value):
    if not isinstance(value, six.integer_types):
        raise TypeError(_("Difficulty is not an integer."))

    if value < 0:
        raise ValueError(_("Difficulty must be a positive integer."))


def validate_settings(value):
    if not isinstance(value, dict):
        raise TypeError(
            _("Settings must be an instance of '{type}' or its subclass.")
            .format(type=dict))


def validate_game_version(value):
    if not isinstance(value, ValueConstant):
        raise TypeError(
            _("Type '{actual}' is invalid for game version. '{expected}' was "
              "expected.")
            .format(actual=type(value), expected=ValueConstant))

    if value not in SETTINGS:
        supported_versions = ', '.join([
            "'{0}'".format(x) for x in SETTINGS.keys()
        ])
        raise ValueError(
            _("Unknown game version '{actual}'. Supported versions: "
              "{supported}.")
            .format(actual=value, supported=supported_versions))
