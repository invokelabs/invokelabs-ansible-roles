__author__ = 'Ed Epstein'

from pygtail import Pygtail
import diamond.collector
import re
import os


class PhpFpmLogsCollector(diamond.collector.Collector):

    def get_default_config_help(self):
        config_help = super(PhpFpmLogsCollector, self).get_default_config_help()
        config_help.update({
            'log_file_paths': 'Comma separated list of pool:path pairs.'
        })
        return config_help

    def get_default_config(self):
        """
        Returns the default collector settings
        """
        config = super(PhpFpmLogsCollector, self).get_default_config()
        config.update({
            'log_file_paths': ['default:/var/log/php-fpm.log'],
            'path': 'fpm'
        })
        return config

    def collect(self):
        log_file_path_tuples = self.config['log_file_paths']
        regular_expression = re.compile(
            '^(\S+) \[([^\]]+)\] "([A-Z]+)[^"]*" "[^"]*" (?P<time>\d+) (?P<mem>\d+)$'
        )
        # The below reduce call takes a list containing a pool name and a path and turns them into a dictionary where
        # the vhost is the key and the path is the value, so that iteritems() can return them nicely in the for loop.
        for log_file_path_tuple in log_file_path_tuples:
            for pool, pool_log_path in reduce(lambda vh, ph: {vh: ph}, log_file_path_tuple.split(':')).iteritems():
                if os.path.exists(pool_log_path):
                    for line in Pygtail(pool_log_path):
                        time = regular_expression.match(line).group('time')
                        mem = regular_expression.match(line).group('mem')
                        metric = pool + '.'
                        self.publish(metric + 'req_time', time)
                        self.publish(metric + 'req_mem', mem)