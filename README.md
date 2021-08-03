# PyAutoWebAPI
a simple tool for accessing web APIs

## Usage

```python
from pyautowebapi.api import Api

api = Api('http://example.com/api/v1')

api['key'] = 'abcdefghijklmnopqrstuvwxyz'

api['parameter1'] = 'value1'
api['parameter2'] = 'value2'

print(api)

data = api.call()

print(data)
```
