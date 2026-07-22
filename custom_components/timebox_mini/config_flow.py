import logging

import voluptuous as vol

from homeassistant import config_entries

from . import ATTR_MAC

_LOGGER = logging.getLogger(__name__)

DOMAIN = "timebox_mini"


class TimeboxMiniConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Timebox Mini."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            mac_addr = user_input[ATTR_MAC].strip()
            if not mac_addr:
                errors["base"] = "invalid_mac"
            else:
                await self.async_set_unique_id(mac_addr)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title=mac_addr, data={ATTR_MAC: mac_addr})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        ATTR_MAC,
                        default=(user_input or {}).get(ATTR_MAC, ""),
                    ): str,
                }
            ),
            errors=errors,
        )
