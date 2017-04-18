# Tomorrow Land
Project Ember official city simulator

##### Requirements
The following libraries needs to be installed:

- KafkaPython: https://github.com/dpkp/kafka-python
- Requests: http://docs.python-requests.org/en/master/
- namesake: https://github.com/RealSalmon/python-namesake

##### Usage
You can start the simulator by launching `main.py` providing
this mandatory parameters:

- `--lamps_per_street`: Number of lamps per street
- `--control_unit`: ip address of the control unit
- `--kafka`: ip address of the kafka cluster

Another parameter is:

- `test`: 0 or 1 - send data to kafka or print them

The simulator will start `lamp_per_street` * 100 thread each one emitting JSON
strings (you can find the format in `datatype` folder) in lamps, lumen and traffic kafka topics
every 10 seconds. 

The lamps will be registered to the local control unit (see documentation at
https://github.com/ProjectEmber/metropolis) while lumen and traffic will be routed directly
to the Apache Kafka cluster.


