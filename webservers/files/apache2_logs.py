__author__ = 'Ed Epstein'

from pygtail import Pygtail
import diamond.collector
import re
import os


class Apache2LogsCollector(diamond.collector.Collector):

    def get_default_config_help(self):
        config_help = super(Apache2LogsCollector, self).get_default_config_help()
        config_help.update({
            'log_file_paths': 'Comma separated list of vhost:path pairs.'
        })
        return config_help

    def get_default_config(self):
        """
        Returns the default collector settings
        """
        config = super(Apache2LogsCollector, self).get_default_config()
        config.update({
            'log_file_paths': ['default:/var/log/apache2/access.log'],
            'path': 'http.response'
        })
        return config

    def collect(self):
        log_file_path_tuples = self.config['log_file_paths']
        regular_expression = re.compile(
            '^(\S+) \S+ \S+ \[([^\]]+)\] "([A-Z]+)[^"]*" (?P<code>\d+) \d+ "[^"]*" "([^"]*)"$'
        )
        # The below reduce call takes a list containing a vhost and a path and turns them into a dictionary where
        # the vhost is the key and the path is the value, so that iteritems() can return them nicely in the for loop.
        for log_file_path_tuple in log_file_path_tuples:
            for vhost, vhost_log_path in reduce(lambda vh, ph: {vh: ph}, log_file_path_tuple.split(':')).iteritems():
                if os.path.exists(vhost_log_path):
                    codes = {'1xx': 0, '2xx': 0, '3xx': 0, '4xx': 0, '5xx': 0}
                    for line in Pygtail(vhost_log_path):
                        code = regular_expression.match(line).group('code')[0]
                        if codes[code + 'xx']:
                            codes[code + 'xx'] += 1
                    for code, count in codes.iteritems():
                        metric_name = vhost + '.' + code
                        metric_value = count
                        self.publish(metric_name, metric_value)


