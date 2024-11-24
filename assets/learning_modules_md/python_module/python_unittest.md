## Python Unittest

Ref:
1. Unittest: https://docs.python.org/3/library/unittest.html
2. Mock: 
    1. https://docs.python.org/3/library/unittest.mock.html
    2. https://realpython.com/python-mock-library/

### Unittest:

provides a rich set of tools for constructing and running tests. 

#### Example 1: Unittest with Assert Methods

Ref Assert Methods: https://docs.python.org/3/library/unittest.html#assert-methods

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

# call the testcases
# if __name__ == '__main__':
#     unittest.main()

# run below code  if you are running from a notebook
res = unittest.main(argv=[''], verbosity=3, exit=False)
```

#### Example 2: setUp() and tearDown() methods 

The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method. <br>

<u>**Setup**</u> allows you to create and configure necessary resources and conditions for tests like initializing required classes, database or network connections, defining test objects, fixtures or variables and so on.<br>

While <u>**Teardown**</u> helps you clean and reset the resources and configurations created using Setup.

```python
import unittest

class TestAddition(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        print("__init__")
        
    def setUp(self):
        print("Setup")

    def test_one_plus_two(self):
        self.assertEqual(1+2, 3)
        
    def test_two_plus_two(self):
        self.assertEqual(2+2, 4)
    
    def tearDown(self):
        print("teardown")

# run below code  if you are running from a notebook
res = unittest.main(argv=[''], verbosity=3, exit=False)
```
output: <br>
test_one_plus_two (__main__.TestAddition) ... ok <br>
test_two_plus_two (__main__.TestAddition) ... ok <br>

---------------------------------------------------------------------- <br>
Ran 2 tests in 0.009s <br>

OK <br>
__init__ <br>
__init__ <br>
Setup <br>
teardown <br>
Setup <br>
teardown <br>

### Mock & Patch:

unittest.mock provides a class called <u>**Mock**</u>, which you’ll use to imitate real objects in your codebase. <br>
<u>**patch()**</u>, replaces the real objects in your code with Mock instances.<br>
<u>**Monkey patching**</u> is the replacement of one object with another at runtime.

#### some special attributes of Mock:

```python
from unittest.mock import Mock

mock = Mock()

print(mock.some_attribute)
print(mock.do_something())

mock1 = Mock(side_effect=Exception)
# mock1.configure_mock(return_value=True)
mock2 = Mock(return_value=True)
# mock2.name = "Real Python Mock"
mock3 = Mock(name="Real Python Mock")
```

```python
from unittest.mock import Mock

json = Mock()
json.loads('{"key": "value"}')

# Number of times you called loads():
print("Number of times you called loads():", json.loads.call_count)

# The last loads() call:
print("The last loads() call:", json.loads.call_args)

# List of loads() calls:
print("List of loads() calls", json.loads.call_args_list)

# List of calls to json's methods (recursively):
print("List of calls to json's methods (recursively)", json.method_calls)
```
output: <br>
Number of times you called loads(): 1<br>
The last loads() call: call('{"key": "value"}')<br>
List of loads() calls [call('{"key": "value"}')]<br>
List of calls to json's methods (recursively) [call.loads('{"key": "value"}')]<br>

#### Unittest with Mock()

```python
from datetime import datetime
from unittest.mock import Mock

# original function
def is_weekday():
    today = datetime.today()
    return (0 <= today.weekday() < 5)

# Test if today is a weekday
# assert is_weekday()

# Save a couple of test days
wednesday = datetime(year=2025, month=1, day=1)
sunday = datetime(year=2025, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()

# Mock .today() to return Wednesday
datetime.today.return_value = wednesday
# Test Wednesday is a weekday
assert is_weekday()

# Mock .today() to return Wednesday
datetime.today.return_value = sunday
# Test Wednesday is a weekday
assert not is_weekday()
```

#### You can control your code’s behavior by specifying a mocked function’s side effects.

```python
import unittest
from unittest.mock import Mock
from requests.exceptions import Timeout

requests = Mock()

# original function
def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None


class TestHolidays(unittest.TestCase):
    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f"Making a request to {url}.")
        print("Request received!")

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response_mock
    
    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout  # [Timeout, response_mock]
        with self.assertRaises(Timeout):
            get_holidays()
        assert requests.get.call_count == 2
            
    def test_get_holidays_logging(self):
        # set the .side_effect of .get() to .log_request(), .get() forwards its arguments to .log_request()
        requests.get.side_effect = self.log_request
        assert get_holidays()["12/25"] == "Christmas"
            
res = unittest.main(argv=[''], verbosity=3, exit=False)
```

#### Patch

```python
# holidays.py
from datetime import datetime

import requests

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None
```

#### Patch as decorator

```python
# test_holidays.py
import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

from holidays import get_holidays

class TestHolidays(unittest.TestCase):
    @patch("holidays.requests")
    def test_get_holidays_timeout(self, mock_requests):
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == "__main__":
    unittest.main()
```

#### Patch as context manager

```python
# test_holidays.py
import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

from holidays import get_holidays

class TestHolidays(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch("holidays.requests") as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == "__main__":
    unittest.main()
```

Originally, you created a Mock and patched requests in the local scope. Now, you need to access the requests library in holidays.py from tests.py.<br>

In this case, you used patch() as a decorator and passed the target object’s path. The target path was "holidays.requests", which consists of the module name and the object. <br>

You also defined a new parameter, mock_requests, for the test function. patch() uses this parameter to pass the mocked object into your test. From there, you can modify the mock or make assertions as necessary. <br>

#### Patching an Object’s Attributes

```python
# test_holidays.py
import unittest
from unittest.mock import patch

from holidays import get_holidays, requests

class TestHolidays(unittest.TestCase):
    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

if __name__ == "__main__":
    unittest.main()
```


### Pytest:

Third-party unittest framework with a lighter-weight syntax for writing tests.

