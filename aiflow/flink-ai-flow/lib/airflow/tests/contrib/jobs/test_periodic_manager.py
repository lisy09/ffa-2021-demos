# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import datetime
import unittest

from airflow.events.scheduler_events import EXECUTION_DATE_FORMAT
from airflow.utils import timezone
from airflow.utils.mailbox import Mailbox
from airflow.contrib.jobs.periodic_manager import PeriodicManager
from dateutil import tz

NOW = timezone.utcnow()


class TestPeriodicManager(unittest.TestCase):
    def test_add_task(self):
        mailbox = Mailbox()
        periodic_manager = PeriodicManager(mailbox)
        periodic_manager.start()
        periodic_manager.add_task('1', NOW, '1', {'cron': '*/1 * * * * * *'})
        event = mailbox.get_message()
        periodic_manager.remove_task('1', NOW, '1')
        self.assertEqual('.'.join(['1', NOW.strftime(EXECUTION_DATE_FORMAT)]), event.key)

        periodic_manager.add_task('2', NOW, '2', {'cron': '*/1 * * * * *'})
        event = mailbox.get_message()
        self.assertEqual('.'.join(['2', NOW.strftime(EXECUTION_DATE_FORMAT)]), event.key)
        periodic_manager.remove_task('2', NOW, '2')

        periodic_manager.add_task('3', NOW, '3', {'interval': '0,0,0,0,1'})
        event = mailbox.get_message()
        self.assertEqual('.'.join(['3', NOW.strftime(EXECUTION_DATE_FORMAT)]), event.key)
        periodic_manager.remove_task('3', NOW, '3')

        now_gmt = timezone.utcnow().astimezone(tz.gettz('gmt'))
        cron_gmt = now_gmt + datetime.timedelta(seconds=1)
        print(now_gmt)
        periodic_manager.add_task('4', now_gmt, '4',
                                  {'cron': '{} {} {} * * * *'.format(cron_gmt.second, cron_gmt.minute, cron_gmt.hour),
                                   'timezone': 'gmt'})
        print(cron_gmt)
        event = mailbox.get_message()
        periodic_manager.remove_task('4', now_gmt, '4')
        self.assertEqual('.'.join(['4', now_gmt.strftime(EXECUTION_DATE_FORMAT)]), event.key)

        periodic_manager.shutdown()

    def test_add_task_invalidated(self):
        mailbox = Mailbox()
        periodic_manager = PeriodicManager(mailbox)
        periodic_manager.start()
        with self.assertRaises(Exception) as context:
            periodic_manager.add_task('1', NOW, '1', {'cron': '*/1 * * * *'})
        self.assertTrue('The cron expression' in str(context.exception))

        with self.assertRaises(Exception) as context:
            periodic_manager.add_task('2', NOW, '2', {'interval': '0,0,0,1'})
        self.assertTrue('The interval expression' in str(context.exception))

        periodic_manager.shutdown()


if __name__ == '__main__':
    unittest.main()
