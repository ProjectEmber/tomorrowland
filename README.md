# Tomorrow Land
Project Ember official city simulator

##### Requirements
The following libraries needs to be installed:

- KafkaPython: https://github.com/dpkp/kafka-python
- Requests: https://docs.python-requests.org/


##### Usage
You can start the simulator by launching `main.py` providing
this mandatory parameters:

- `--lamps_per_street`: Number of lamps per street
- `--control_unit`: ip address of the control unit
- `--kafka`: ip address of the kafka cluster

Another parameter can be:

- `test`: 0 or 1 - send data to kafka or print them

