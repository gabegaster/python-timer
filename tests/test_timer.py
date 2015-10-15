from unittest import TestCase
import sys
import StringIO
import time

import timer


class TimerTestCase(TestCase):
    def setUp(self):
        self._stderr = sys.stderr
        sys.stderr = StringIO.StringIO()

    def tearDown(self):
        sys.stderr = self._stderr

    def test_n_messages(self):
        """should only display 3 messages"""
        for j in timer.show_progress(xrange(30), update_time=1, length=30):
            time.sleep(.1)
        msgs = sys.stderr.getvalue().split("\n")
        msgs = [i for i in msgs if i]
        self.assertEqual(len(msgs), 3, "too many messages displayed to stderr")
