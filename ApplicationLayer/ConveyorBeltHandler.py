from flask import request
from DomainLayer import ConveyorBelt


class ConveyorBeltHandler:
    def activateConveyorBelt(self):
        ConveyorBelt().activateConveyorBelt()

    def deactivateConveyorBelt(self):
        ConveyorBelt().deactivateConveyorBelt()

    def jamConveyorBelt(self):
        ConveyorBelt().jamConveyorBelt()

    def unjamConveyorBelt(self):
        ConveyorBelt().unjamConveyorBelt()
