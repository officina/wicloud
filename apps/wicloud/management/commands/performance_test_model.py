from django.core.management.base import BaseCommand, CommandError
import uuid

import logging

from apps.wicloud.models import *

l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())


class Command(BaseCommand):
    help = 'Launches performance test one to one'
    testSerialNumber = "performance_test"
    def clear(self):
        Energy_interval.objects.all().delete()
        Light_management_module.objects.filter(node__serialNumber=self.testSerialNumber).delete()
        Energy_meter_module.objects.filter(node__serialNumber=self.testSerialNumber).delete()
        Motion_management_module.objects.filter(node__serialNumber=self.testSerialNumber).delete()
        Twilight_management_module.objects.filter(node__serialNumber=self.testSerialNumber).delete()
        Node.objects.filter(serialNumber=self.testSerialNumber).delete()
        Light_fixture.objects.filter(serialNumber=self.testSerialNumber).delete()
        Installation.objects.filter(serialNumber=self.testSerialNumber).delete()

    def add_arguments(self, parser):
        parser.add_argument('--count', nargs='?', type=int)

    def handle(self, *args, **options):

        user = User.objects.all().first()

        self.clear()
        #exit(1)
        count = options.get('count', 1)
        installation = Installation(serialNumber=self.testSerialNumber, last_modifier=user, creator=user)
        installation.save()

        for i in range(0, count):

            node = Node(serialNumber=self.testSerialNumber, last_modifier=user, creator=user)
            node.save()

            lightFixture = Light_fixture(name="{}_{}".format(self.testSerialNumber,i), serialNumber=self.testSerialNumber, last_modifier=user, creator=user)
            lightFixture.installation = installation
            lightFixture.save()
            lightFixture.nodes.add(node)

            lightManagementModule = Light_management_module(name="{}_{}".format(self.testSerialNumber,i), last_modifier=user, creator=user)
            lightManagementModule.node = node
            lightManagementModule.save()

            energyMeterModule = Energy_meter_module(name="{}_{}".format(self.testSerialNumber,i), last_modifier=user, creator=user)
            energyMeterModule.node = node
            energyMeterModule.save()

            twilightManagementModule = Twilight_management_module(name="{}_{}".format(self.testSerialNumber,i), last_modifier=user, creator=user)
            twilightManagementModule.node = node
            twilightManagementModule.save()

            if i%2==0:
                motionManagementModule = Motion_management_module(name="{}_{}".format(self.testSerialNumber,i), last_modifier=user, creator=user)
                motionManagementModule.node = node
                motionManagementModule.save()

            for j in range(0,100):
                energyInterval = Energy_interval(mac="{}_{}".format(self.testSerialNumber,i), last_modifier=user, creator=user)
                energyInterval.node = node
                energyInterval.save()

            print(f"creating installation {i}")



        for installation in Installation.objects.all():
            print ("Installation: {}".format(installation))

            for lightFixture in installation.lightFixtures.all():
                print ("Light fixture: {}".format(lightFixture))
                for node in lightFixture.nodes.all().select_related("lightManagementModule").select_related("energyMeterModule").select_related("twilightManagementModule").select_related("motionManagementModule"):
                    print("Related node {}: {}".format(node.name, node.serialNumber))
                    print("Light management module: {}".format(node.lightManagementModule.name if node.lightManagementModule else None))
                    print("Energy meter module {}".format(node.energyMeterModule.name if node.energyMeterModule else None))
                    print("Twilight management module {}".format(node.twilightManagementModule.name if node.twilightManagementModule else None))
                    print("Motion managemnt module {}".format(node.motionManagementModule.name if node.motionManagementModule else None))

            for energyInterval in installation.energyIntervals.all():
                print ("Energy interval: {}".format(energyInterval.mac))

