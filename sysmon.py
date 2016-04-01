#!/usr/bin/python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import importlib

def sysmon():
	f = open('config.json', 'r')
	str = f.read()

	d = json.loads(str)

	print(d)

	for config in d['monitors']:

		if config['type'] == 'resque':
			print('resque')
			print(config)

		elif config['type'] == 'PyMySQL':

			print('PyMySQL')
			print(config)

			mod = importlib.import_module('monitors.monpymysql')

			mod.monpymysql_run(config);

sysmon()