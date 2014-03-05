# -*- coding: utf-8 -*-
"""
Difficulty constants.
"""
WIND_TURBULENCE = 'WindTurbulence'
FLUTTER_EFFECT = 'FlutterEffect'
STALL_SPINS = 'StallSpins'
BLACK_OUTS_RED_OUTS = 'BlackoutsRedouts'
ENGINE_OVERHEAT = 'EngineOverheat'
TORQUE_GYRO_EFFECTS = 'TorqueGyroEffects'
REALISTIC_LANDING = 'RealisticLanding'
TAKEOFF_LANDING = 'TakeoffLanding'
COCKPIT_ALWAYS_ON = 'CockpitAlwaysOn'
NO_OUT_SIDE_VIEWS = 'NoOutSideViews'
HEAD_SHAKE = 'HeadShake'
NO_ICONS = 'NoIcons'
REALISTIC_GUNNERY = 'RealisticGunnery'
LIMITED_AMMO = 'LimitedAmmo'
LIMITED_FUEL = 'LimitedFuel'
VULNERABILITY = 'Vulnerability'
NO_PADLOCK = 'NoPadlock'
CLOUDS = 'Clouds'
NO_MAP_ICONS = 'NoMapIcons'
SEPARATE_ENGINE_START = 'SeparateEStart'
NO_INSTANT_SUCCESS = 'NoInstantSuccess'
NO_MINI_MAP_PATH = 'NoMinimapPath'
NO_SPEED_BAR = 'NoSpeedBar'
COMPLEX_ENGINE_MANAGEMENT = 'ComplexEManagement'
RELIABILITY = 'Reliability'
OVERLOAD_LIMITS = 'GLimits'
REALISTIC_PILOT_VULNERABILITY = 'RealisticPilotVulnerability'
REALISTIC_NAVIGATION_INSTRUMENT = 'RealisticNavigationInstruments'
NO_PLAYER_ICON = 'NoPlayerIcon'
NO_FOG_OF_WAR_ICONS = 'NoFogOfWarIcons'
BOMB_FUZES = 'BombFuzes'
REALISTIC_TORPEDOING = 'RealisticTorpedoing'
REALISTIC_MISSILES_VARIATION = 'RealisticMissilesVariation'
NO_SELF_VIEW = 'NoSelfView'
NO_FOE_VIEW = 'NoFoeView'
NO_FRIENDLY_VIEW = 'NoFriendlyView'
NO_PLANES_VIEW = 'NoPlanesView'
NO_AIR_CARRIER_VIEW = 'NoACarrierView'


NUMBERS_MAP_4_12_2 = {
    WIND_TURBULENCE: 0,
    FLUTTER_EFFECT: 1,
    STALL_SPINS: 2,
    BLACK_OUTS_RED_OUTS: 3,
    ENGINE_OVERHEAT: 4,
    TORQUE_GYRO_EFFECTS: 5,
    REALISTIC_LANDING: 6,
    TAKEOFF_LANDING: 7,
    COCKPIT_ALWAYS_ON: 8,
    NO_OUT_SIDE_VIEWS: 9,
    HEAD_SHAKE: 10,
    NO_ICONS: 11,
    REALISTIC_GUNNERY: 12,
    LIMITED_AMMO: 13,
    LIMITED_FUEL: 14,
    VULNERABILITY: 15,
    NO_PADLOCK: 16,
    CLOUDS: 17,
    NO_MAP_ICONS: 18,
    SEPARATE_ENGINE_START: 19,
    NO_INSTANT_SUCCESS: 20,
    NO_MINI_MAP_PATH: 21,
    NO_SPEED_BAR: 22,
    COMPLEX_ENGINE_MANAGEMENT: 23,
    RELIABILITY: 24,
    OVERLOAD_LIMITS: 25,
    REALISTIC_PILOT_VULNERABILITY: 26,
    REALISTIC_NAVIGATION_INSTRUMENT: 27,
    NO_PLAYER_ICON: 28,
    NO_FOG_OF_WAR_ICONS: 29,
    BOMB_FUZES: 30,
    REALISTIC_TORPEDOING: 31,
    REALISTIC_MISSILES_VARIATION: 32,
    NO_SELF_VIEW: 33,
    NO_FOE_VIEW: 34,
    NO_FRIENDLY_VIEW: 35,
    NO_PLANES_VIEW: 36,
    NO_AIR_CARRIER_VIEW: 37,
}

NUMBERS_MAPS = {
    '4.12': NUMBERS_MAP_4_12_2,
    '4.12.1': NUMBERS_MAP_4_12_2,
    '4.12.2': NUMBERS_MAP_4_12_2,
}

DEFAULT_GAME_VERSION = '4.12.2'
