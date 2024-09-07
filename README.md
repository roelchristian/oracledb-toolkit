# oracledb-toolkit
Python toolkit to connect to Oracle databases using the oracledb package. This package is created and tested on Windows 10 and 11.


## Installation and setup

1. Create a .env file in the root directory of the project with the following content:

```
HOST=the_oracle_host
PORT=the_oracle_port
SERVICE_NAME=the_oracle_service_name
ORACLE_USERNAME=your_oracle_username
PASSWORD=your_oracle_password
ORACLE_CLIENT_PATH=your_oracle_client_path
```

The `ORACLE_CLIENT_PATH` is the path to the Oracle Instant Client directory. You can download the Oracle Instant Client from the [Oracle website](https://www.oracle.com/database/technologies/instant-client.html).

2. (Optional) Create a virtual environment, activate it and install the required packages (found in the `requirements.txt` file in the root directory of the project):

```bash
python -m venv venv
cd venv
.\Scripts\activate
pip install -r requirements.txt
```

3. Build and install the package:

```bash
python -m pip install --upgrade build
python -m build
pip install -e .
```

## Usage


See the `example.py` file for an example of how to use the toolkit.