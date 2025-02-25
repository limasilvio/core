"""Water heater entities for the Overkiz (by Somfy) integration."""
from pyoverkiz.enums.ui import UIWidget

from .atlantic_pass_apc_dhw import AtlanticPassAPCDHW
from .hitachi_dhw import HitachiDHW

WIDGET_TO_WATER_HEATER_ENTITY = {
    UIWidget.ATLANTIC_PASS_APC_DHW: AtlanticPassAPCDHW,
    UIWidget.HITACHI_DHW: HitachiDHW,
}
