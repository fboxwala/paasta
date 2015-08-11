import contextlib
import mock

import marathon_tools
import monitoring_tools


class TestMonitoring_Tools:

    general_page = True
    fake_general_service_config = {
        'team': 'general_test_team',
        'runbook': 'y/general_test_runbook',
        'tip': 'general_test_tip',
        'notification_email': 'general_test_notification_email',
        'page': general_page
    }

    empty_service_config = marathon_tools.MarathonServiceConfig('myservicename', 'myinstance', {}, {})
    job_page = False
    fake_job_config = marathon_tools.MarathonServiceConfig(
        'myservicename',
        'myinstance',
        {
            'team': 'job_test_team',
            'runbook': 'y/job_test_runbook',
            'tip': 'job_test_tip',
            'notification_email': 'job_test_notification_email',
            'page': job_page
        },
        {},
    )
    empty_job_config = {}
    monitor_page = True
    fake_monitor_config = {
        'team': 'monitor_test_team',
        'runbook': 'y/monitor_test_runbook',
        'tip': 'monitor_test_tip',
        'notification_email': 'monitor_test_notification_email',
        'page': monitor_page
    }
    empty_monitor_config = {}
    framework = 'fake_framework'
    instance = 'fake_instance'
    service_name = 'fake_service'
    soa_dir = '/fake/soa/dir'

    def test_get_team(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_team(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('team', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_runbook(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_runbook(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('runbook', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_tip(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_tip(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('tip', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_notification_email(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_notification_email(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('notification_email', self.framework,
                                                                      self.service_name, self.instance,
                                                                      self.soa_dir)

    def test_get_page(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_page(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('page', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_alert_after(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_alert_after(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('alert_after', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_realert_every(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_realert_every(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('realert_every', self.framework,
                                                                      self.service_name, self.instance,
                                                                      self.soa_dir)

    def test_get_check_every(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_check_every(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('check_every', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_irc_channels(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_irc_channels(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('irc_channels', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_dependencies(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_dependencies(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('dependencies', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_ticket(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_ticket(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('ticket', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_project(self):
        with mock.patch('monitoring_tools.__get_monitoring_config_value') as get_monitoring_config_value_patch:
            monitoring_tools.get_project(self.framework, self.service_name, self.instance, self.soa_dir)
            get_monitoring_config_value_patch.assert_called_once_with('project', self.framework, self.service_name,
                                                                      self.instance, self.soa_dir)

    def test_get_monitoring_config_value_with_job_config(self):
        expected = 'job_test_team'
        with contextlib.nested(
            mock.patch('service_configuration_lib.read_service_configuration', autospec=True,
                       return_value=self.fake_general_service_config),
            mock.patch('marathon_tools.load_marathon_service_config', autospec=True,
                       return_value=self.fake_job_config),
            mock.patch('marathon_tools.read_monitoring_config', autospec=True, return_value=self.fake_monitor_config),
            mock.patch('marathon_tools.get_cluster', autospec=True, return_value='clustername'),
        ) as (
            service_configuration_lib_patch,
            read_service_patch,
            read_monitoring_patch,
            get_cluster_patch,
        ):
            actual = monitoring_tools.get_team(self.framework, self.service_name, self.instance, self.soa_dir)
            assert expected == actual
            service_configuration_lib_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)
            read_service_patch.assert_called_once_with(self.service_name, self.instance, 'clustername',
                                                       soa_dir=self.soa_dir)
            read_monitoring_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)

    def test_get_monitoring_config_value_with_monitor_config(self):
        expected = 'monitor_test_team'
        with contextlib.nested(
            mock.patch('service_configuration_lib.read_service_configuration', autospec=True,
                       return_value=self.fake_general_service_config),
            mock.patch('marathon_tools.load_marathon_service_config', autospec=True,
                       return_value=self.empty_job_config),
            mock.patch('marathon_tools.read_monitoring_config', autospec=True, return_value=self.fake_monitor_config),
            mock.patch('marathon_tools.get_cluster', autospec=True, return_value='clustername'),
        ) as (
            service_configuration_lib_patch,
            read_service_patch,
            read_monitoring_patch,
            get_cluster_patch,
        ):
            actual = monitoring_tools.get_team(self.framework, self.service_name, self.instance, self.soa_dir)
            assert expected == actual
            service_configuration_lib_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)
            read_service_patch.assert_called_once_with(self.service_name, self.instance, 'clustername',
                                                       soa_dir=self.soa_dir)
            read_monitoring_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)

    def test_get_monitoring_config_value_with_service_config(self):
        expected = 'general_test_team'
        with contextlib.nested(
            mock.patch('service_configuration_lib.read_service_configuration', autospec=True,
                       return_value=self.fake_general_service_config),
            mock.patch('marathon_tools.load_marathon_service_config', autospec=True,
                       return_value=self.empty_job_config),
            mock.patch('marathon_tools.read_monitoring_config', autospec=True, return_value=self.empty_monitor_config),
            mock.patch('marathon_tools.get_cluster', autospec=True, return_value='clustername'),
        ) as (
            service_configuration_lib_patch,
            read_service_patch,
            read_monitoring_patch,
            get_cluster_patch,
        ):
            actual = monitoring_tools.get_team(self.framework, self.service_name, self.instance, self.soa_dir)
            assert expected == actual
            service_configuration_lib_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)
            read_service_patch.assert_called_once_with(self.service_name, self.instance, 'clustername',
                                                       soa_dir=self.soa_dir)
            read_monitoring_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)

    def test_get_monitoring_config_value_with_defaults(self):
        expected = False
        with contextlib.nested(
            mock.patch('service_configuration_lib.read_service_configuration', autospec=True,
                       return_value=self.empty_job_config),
            mock.patch('marathon_tools.load_marathon_service_config', autospec=True,
                       return_value=self.empty_job_config),
            mock.patch('marathon_tools.read_monitoring_config', autospec=True, return_value=self.empty_monitor_config),
            mock.patch('marathon_tools.get_cluster', autospec=True, return_value='clustername'),
        ) as (
            service_configuration_lib_patch,
            read_service_patch,
            read_monitoring_patch,
            get_cluster_patch,
        ):
            actual = monitoring_tools.get_team(self.framework, self.service_name, self.instance, self.soa_dir)
            assert expected == actual
            service_configuration_lib_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)
            read_service_patch.assert_called_once_with(self.service_name, self.instance, 'clustername',
                                                       soa_dir=self.soa_dir)
            read_monitoring_patch.assert_called_once_with(self.service_name, soa_dir=self.soa_dir)

    def test_get_team_email_address_uses_instance_config_if_specified(self):
        expected = 'fake_email'
        with contextlib.nested(
            mock.patch('monitoring_tools.__get_monitoring_config_value', autospec=True),
        ) as (
            mock_get_monitoring_config_value,
        ):
            mock_get_monitoring_config_value.return_value = 'fake_email'
            actual = monitoring_tools.get_team_email_address('fake_service')
            assert actual == expected

    def test_get_team_email_address_uses_team_data_as_last_resort(self):
        expected = 'team_data_email'
        with contextlib.nested(
            mock.patch('monitoring_tools.__get_monitoring_config_value', autospec=True),
            mock.patch('monitoring_tools.get_sensu_team_data', autospec=True),
            mock.patch('monitoring_tools.get_team', autospec=True),
        ) as (
            mock_get_monitoring_config_value,
            mock_get_sensu_team_data,
            mock_get_team,
        ):
            mock_get_team.return_value = 'test_team'
            mock_get_monitoring_config_value.return_value = False
            mock_get_sensu_team_data.return_value = {
                'notification_email': expected
            }
            actual = monitoring_tools.get_team_email_address('fake_service')
            assert actual == expected

    def test_get_team_email_address_returns_none_if_not_available(self):
        with contextlib.nested(
            mock.patch('monitoring_tools.__get_monitoring_config_value', autospec=True),
            mock.patch('monitoring_tools.get_sensu_team_data', autospec=True),
            mock.patch('monitoring_tools.get_team', autospec=True),
        ) as (
            mock_get_monitoring_config_value,
            mock_get_sensu_team_data,
            mock_get_team,
        ):
            mock_get_team.return_value = 'test_team'
            mock_get_monitoring_config_value.return_value = False
            mock_get_sensu_team_data.return_value = {}
            actual = monitoring_tools.get_team_email_address('fake_service')
            assert actual is None
