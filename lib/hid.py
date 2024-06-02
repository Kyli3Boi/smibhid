from ulogging import uLogger
from asyncio import get_event_loop
from slack_api import Wrapper
from display import Display
from space_state import SpaceState

class HID:
    
    def __init__(self, loglevel: int) -> None:
        """
        Human Interface Device for event spaces providing buttons and status LEDs for space open state.
        Create HID instance and then run startup() to start services for button monitoring and LED output.
        """
        self.log = uLogger("HID", loglevel)
        self.version = "1.1.0"     
        self.slack_api = Wrapper(loglevel)
        self.loop_running = False
        self.display = Display(loglevel, ["LCD1602"])
        self.spaceState = SpaceState(loglevel)
        
    def startup(self) -> None:
        """
        Initialise all aysnc services for the HID.
        """
        self.log.info("Starting HID")
        self.log.info(f"SMIBHID firmware version: {self.version}")
        self.display.clear()
        self.display.print_startup(self.version)
        self.log.info("Starting network monitor")
        self.spaceState.startup()
      
        self.log.info("Entering main loop")        
        self.loop_running = True
        loop = get_event_loop()
        loop.run_forever()        
