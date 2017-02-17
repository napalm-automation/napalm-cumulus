ifndef NAPALM_TEST_MOCK
	mock:='1'
endif

export NAPALM_TEST_MOCK=$(mock)
export NAPALM_HOSTNAME=127.0.0.1
export NAPALM_USERNAME=vagrant
export NAPALM_PASSWORD=vagrant
export NAPALM_OPTIONAL_ARGS={"port": 65022}

start_vm:
	# vagrant plugin install vagrant-cumulus
	vagrant up

stop_vm:
	vagrant destroy

tests:
	py.test

test_vm: NAPALM_TEST_MOCK=0
test_vm: start_vm tests
	py.test test/unit/TestCumulusDriver.py
