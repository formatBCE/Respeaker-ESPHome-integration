"""A stand-in for voice_assistant::Timer on Voice Incubator satellites.

The device packages read the first active timer from the first_active_timer
global (seconds_left, total_seconds). The Voice Incubator app keeps the timers,
so the voice_assistant component is absent, and its Timer type with it. This
component only brings the type: its header is included in every build that
lists it.
"""

import esphome.config_validation as cv

CODEOWNERS = ["@formatBCE"]

CONFIG_SCHEMA = cv.Schema({})


async def to_code(config):
    pass
