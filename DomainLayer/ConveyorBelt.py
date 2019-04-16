from InfrastructureLayer.ConveyorBeltDao import ConveyorBeltDao


class ConveyorBelt:
    def activateConveyorBelt(self):
        ConveyorBeltDao().activateConveyorBelt()

    def deactivateConveyorBelt(self):
        ConveyorBeltDao().deactivateConveyorBelt()

    def jamConveyorBelt(self):
        ConveyorBeltDao().jamConveyorBelt()

    def unjamConveyorBelt(self):
        ConveyorBeltDao().unjamConveyorBelt()
