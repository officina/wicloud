from django.urls import reverse, resolve

from test_plus.test import TestCase


class TestAddressURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_address_list_reverse(self):
        """users:list should reverse to /address/."""
        self.assertEqual(reverse("api:address_list"), "/api/address/list/")

    def test_address_detail_reverse(self):
        """users:list should reverse to /address/id."""

        self.assertEqual(reverse("api:address_retrieve", kwargs={"pk": "testuuid"}), "/api/address/retrieve/testuuid/")

    def test_address_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/address/list/").view_name, "api:address_list")


class TestCustomerURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_customer_list_reverse(self):
        """users:list should reverse to /customer/."""
        self.assertEqual(reverse("api:customer_list"), "/api/customer/list/")

    def test_customer_detail_reverse(self):
        """users:list should reverse to /customer/id."""

        self.assertEqual(
            reverse(
                "api:customer_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/customer/retrieve/testuuid/")

    def test_customer_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/customer/list/").view_name, "api:customer_list")


class TestEnergy_intervalURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_energy_interval_list_reverse(self):
        """users:list should reverse to /energy_interval/."""
        self.assertEqual(reverse("api:energy_interval_list"), "/api/energy_interval/list/")

    def test_energy_interval_detail_reverse(self):
        """users:list should reverse to /energy_interval/id."""

        self.assertEqual(
            reverse(
                "api:energy_interval_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/energy_interval/retrieve/testuuid/")

    def test_energy_interval_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/energy_interval/list/").view_name, "api:energy_interval_list")


class TestEnergy_meter_moduleURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_energy_meter_module_list_reverse(self):
        """users:list should reverse to /energy_meter_module/."""
        self.assertEqual(reverse("api:energy_meter_module_list"), "/api/energy_meter_module/list/")

    def test_energy_meter_module_detail_reverse(self):
        """users:list should reverse to /energy_meter_module/id."""

        self.assertEqual(
            reverse(
                "api:energy_meter_module_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/energy_meter_module/retrieve/testuuid/")

    def test_energy_meter_module_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/energy_meter_module/list/").view_name, "api:energy_meter_module_list")


class TestEnergy_meter_peak_measureURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_energy_meter_peak_measure_list_reverse(self):
        """users:list should reverse to /energy_meter_peak_measure/."""
        self.assertEqual(reverse("api:energy_meter_peak_measure_list"), "/api/energy_meter_peak_measure/list/")

    def test_energy_meter_peak_measure_detail_reverse(self):
        """users:list should reverse to /energy_meter_peak_measure/id."""

        self.assertEqual(
            reverse(
                "api:energy_meter_peak_measure_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/energy_meter_peak_measure/retrieve/testuuid/")

    def test_energy_meter_peak_measure_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(
            resolve("/api/energy_meter_peak_measure/list/").view_name,
            "api:energy_meter_peak_measure_list")


class TestError_light_level_and_adc_mismatchURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_error_light_level_and_adc_mismatch_list_reverse(self):
        """users:list should reverse to /error_light_level_and_adc_mismatch/."""
        self.assertEqual(reverse("api:error_light_level_and_adc_mismatch_list"),
                         "/api/error_light_level_and_adc_mismatch/list/")

    def test_error_light_level_and_adc_mismatch_detail_reverse(self):
        """users:list should reverse to /error_light_level_and_adc_mismatch/id."""

        self.assertEqual(
            reverse(
                "api:error_light_level_and_adc_mismatch_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/error_light_level_and_adc_mismatch/retrieve/testuuid/")

    def test_error_light_level_and_adc_mismatch_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(
            resolve("/api/error_light_level_and_adc_mismatch/list/").view_name,
            "api:error_light_level_and_adc_mismatch_list")


class TestError_light_level_and_power_mismatchURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_error_light_level_and_power_mismatch_list_reverse(self):
        """users:list should reverse to /error_light_level_and_power_mismatch/."""
        self.assertEqual(reverse("api:error_light_level_and_power_mismatch_list"),
                         "/api/error_light_level_and_power_mismatch/list/")

    def test_error_light_level_and_power_mismatch_detail_reverse(self):
        """users:list should reverse to /error_light_level_and_power_mismatch/id."""

        self.assertEqual(
            reverse(
                "api:error_light_level_and_power_mismatch_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/error_light_level_and_power_mismatch/retrieve/testuuid/")

    def test_error_light_level_and_power_mismatch_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(
            resolve("/api/error_light_level_and_power_mismatch/list/").view_name,
            "api:error_light_level_and_power_mismatch_list")


class TestError_node_offlineURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_error_node_offline_list_reverse(self):
        """users:list should reverse to /error_node_offline/."""
        self.assertEqual(reverse("api:error_node_offline_list"), "/api/error_node_offline/list/")

    def test_error_node_offline_detail_reverse(self):
        """users:list should reverse to /error_node_offline/id."""

        self.assertEqual(
            reverse(
                "api:error_node_offline_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/error_node_offline/retrieve/testuuid/")

    def test_error_node_offline_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/error_node_offline/list/").view_name, "api:error_node_offline_list")


class TestGatewayURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_gateway_list_reverse(self):
        """users:list should reverse to /gateway/."""
        self.assertEqual(reverse("api:gateway_list"), "/api/gateway/list/")

    def test_gateway_detail_reverse(self):
        """users:list should reverse to /gateway/id."""

        self.assertEqual(reverse("api:gateway_retrieve", kwargs={"pk": "testuuid"}), "/api/gateway/retrieve/testuuid/")

    def test_gateway_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/gateway/list/").view_name, "api:gateway_list")


class TestIme_power_counterURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_ime_power_counter_list_reverse(self):
        """users:list should reverse to /ime_power_counter/."""
        self.assertEqual(reverse("api:ime_power_counter_list"), "/api/ime_power_counter/list/")

    def test_ime_power_counter_detail_reverse(self):
        """users:list should reverse to /ime_power_counter/id."""

        self.assertEqual(
            reverse(
                "api:ime_power_counter_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/ime_power_counter/retrieve/testuuid/")

    def test_ime_power_counter_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/ime_power_counter/list/").view_name, "api:ime_power_counter_list")


class TestIme_power_measureURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_ime_power_measure_list_reverse(self):
        """users:list should reverse to /ime_power_measure/."""
        self.assertEqual(reverse("api:ime_power_measure_list"), "/api/ime_power_measure/list/")

    def test_ime_power_measure_detail_reverse(self):
        """users:list should reverse to /ime_power_measure/id."""

        self.assertEqual(
            reverse(
                "api:ime_power_measure_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/ime_power_measure/retrieve/testuuid/")

    def test_ime_power_measure_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/ime_power_measure/list/").view_name, "api:ime_power_measure_list")


class TestInstallationURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_installation_list_reverse(self):
        """users:list should reverse to /installation/."""
        self.assertEqual(reverse("api:installation_list"), "/api/installation/list/")

    def test_installation_detail_reverse(self):
        """users:list should reverse to /installation/id."""

        self.assertEqual(
            reverse(
                "api:installation_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/installation/retrieve/testuuid/")

    def test_installation_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/installation/list/").view_name, "api:installation_list")


class TestLight_management_measureURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_light_management_measure_list_reverse(self):
        """users:list should reverse to /light_management_measure/."""
        self.assertEqual(reverse("api:light_management_measure_list"), "/api/light_management_measure/list/")

    def test_light_management_measure_detail_reverse(self):
        """users:list should reverse to /light_management_measure/id."""

        self.assertEqual(
            reverse(
                "api:light_management_measure_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/light_management_measure/retrieve/testuuid/")

    def test_light_management_measure_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/light_management_measure/list/").view_name, "api:light_management_measure_list")


class TestLight_management_moduleURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_light_management_module_list_reverse(self):
        """users:list should reverse to /light_management_module/."""
        self.assertEqual(reverse("api:light_management_module_list"), "/api/light_management_module/list/")

    def test_light_management_module_detail_reverse(self):
        """users:list should reverse to /light_management_module/id."""

        self.assertEqual(
            reverse(
                "api:light_management_module_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/light_management_module/retrieve/testuuid/")

    def test_light_management_module_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/light_management_module/list/").view_name, "api:light_management_module_list")


class TestLight_profileURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_light_profile_list_reverse(self):
        """users:list should reverse to /light_profile/."""
        self.assertEqual(reverse("api:light_profile_list"), "/api/light_profile/list/")

    def test_light_profile_detail_reverse(self):
        """users:list should reverse to /light_profile/id."""

        self.assertEqual(
            reverse(
                "api:light_profile_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/light_profile/retrieve/testuuid/")

    def test_light_profile_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/light_profile/list/").view_name, "api:light_profile_list")


class TestLight_profile_slotURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_light_profile_slot_list_reverse(self):
        """users:list should reverse to /light_profile_slot/."""
        self.assertEqual(reverse("api:light_profile_slot_list"), "/api/light_profile_slot/list/")

    def test_light_profile_slot_detail_reverse(self):
        """users:list should reverse to /light_profile_slot/id."""

        self.assertEqual(
            reverse(
                "api:light_profile_slot_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/light_profile_slot/retrieve/testuuid/")

    def test_light_profile_slot_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/light_profile_slot/list/").view_name, "api:light_profile_slot_list")


class TestMotion_eventURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_motion_event_list_reverse(self):
        """users:list should reverse to /motion_event/."""
        self.assertEqual(reverse("api:motion_event_list"), "/api/motion_event/list/")

    def test_motion_event_detail_reverse(self):
        """users:list should reverse to /motion_event/id."""

        self.assertEqual(
            reverse(
                "api:motion_event_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/motion_event/retrieve/testuuid/")

    def test_motion_event_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/motion_event/list/").view_name, "api:motion_event_list")


class TestNodeURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_node_list_reverse(self):
        """users:list should reverse to /node/."""
        self.assertEqual(reverse("api:node_list"), "/api/node/list/")

    def test_node_detail_reverse(self):
        """users:list should reverse to /node/id."""

        self.assertEqual(reverse("api:node_retrieve", kwargs={"pk": "testuuid"}), "/api/node/retrieve/testuuid/")

    def test_node_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/node/list/").view_name, "api:node_list")


class TestNode_moduleURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_node_module_list_reverse(self):
        """users:list should reverse to /node_module/."""
        self.assertEqual(reverse("api:node_module_list"), "/api/node_module/list/")

    def test_node_module_detail_reverse(self):
        """users:list should reverse to /node_module/id."""

        self.assertEqual(
            reverse(
                "api:node_module_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/node_module/retrieve/testuuid/")

    def test_node_module_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/node_module/list/").view_name, "api:node_module_list")


class TestWilamp_alertURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_wilamp_alert_list_reverse(self):
        """users:list should reverse to /wilamp_alert/."""
        self.assertEqual(reverse("api:wilamp_alert_list"), "/api/wilamp_alert/list/")

    def test_wilamp_alert_detail_reverse(self):
        """users:list should reverse to /wilamp_alert/id."""

        self.assertEqual(
            reverse(
                "api:wilamp_alert_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/wilamp_alert/retrieve/testuuid/")

    def test_wilamp_alert_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/wilamp_alert/list/").view_name, "api:wilamp_alert_list")


class TestFeeder_pillarURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_feeder_pillar_list_reverse(self):
        """users:list should reverse to /feeder_pillar/."""
        self.assertEqual(reverse("api:feeder_pillar_list"), "/api/feeder_pillar/list/")

    def test_feeder_pillar_detail_reverse(self):
        """users:list should reverse to /feeder_pillar/id."""

        self.assertEqual(
            reverse(
                "api:feeder_pillar_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/feeder_pillar/retrieve/testuuid/")

    def test_feeder_pillar_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/feeder_pillar/list/").view_name, "api:feeder_pillar_list")


class TestTwilight_management_moduleURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_twilight_management_module_list_reverse(self):
        """users:list should reverse to /twilight_management_module/."""
        self.assertEqual(reverse("api:twilight_management_module_list"), "/api/twilight_management_module/list/")

    def test_twilight_management_module_detail_reverse(self):
        """users:list should reverse to /twilight_management_module/id."""

        self.assertEqual(
            reverse(
                "api:twilight_management_module_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/twilight_management_module/retrieve/testuuid/")

    def test_twilight_management_module_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(
            resolve("/api/twilight_management_module/list/").view_name,
            "api:twilight_management_module_list")


class TestTwilight_measureURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_twilight_measure_list_reverse(self):
        """users:list should reverse to /twilight_measure/."""
        self.assertEqual(reverse("api:twilight_measure_list"), "/api/twilight_measure/list/")

    def test_twilight_measure_detail_reverse(self):
        """users:list should reverse to /twilight_measure/id."""

        self.assertEqual(
            reverse(
                "api:twilight_measure_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/twilight_measure/retrieve/testuuid/")

    def test_twilight_measure_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/twilight_measure/list/").view_name, "api:twilight_measure_list")


class TestMotion_management_moduleURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_motion_management_module_list_reverse(self):
        """users:list should reverse to /motion_management_module/."""
        self.assertEqual(reverse("api:motion_management_module_list"), "/api/motion_management_module/list/")

    def test_motion_management_module_detail_reverse(self):
        """users:list should reverse to /motion_management_module/id."""

        self.assertEqual(
            reverse(
                "api:motion_management_module_retrieve",
                kwargs={
                    "pk": "testuuid"}),
            "/api/motion_management_module/retrieve/testuuid/")

    def test_motion_management_module_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/motion_management_module/list/").view_name, "api:motion_management_module_list")
