# !EXPERIMENTAL!
# Learncube Python
## Installation
Learncube-Python is available on PyPI:
* ``$ pip install learncube``
## Usage
### Virtual Classroom API
Note: For more information visit the [Learncube documentation](https://app.learncube.com/api/virtual-classroom/docs/#api-tab-1)
#### Classrooms API
##### Prerequisites
```python
from learncube import Classroom

public_key = "..."
private_key = "..."

v_c = Classroom(public_key=public_key, private_key=private_key)
```
##### List
```
response = v_c.list_virtual_classroom(room_token="...")
```
##### Create
Note: you can pass any information into the **kwargs`
```python
data = {
    'room_token': randint(0, 100),
    'cancelled': False,
    'description': "This is a test",
    'start': datetime.now().isoformat(),
    'end': datetime.now().isoformat(),
    'max_participants': 2,
    'audio_only': False,
    'return_url': "",
    'record_class': False
}
response = v_c.create_virtual_classroom(
    room_token=data['room_token'],
    cancelled=data['cancelled'],
    description=data['description'],
    start=data['start'],
    end=data['end'],
    max_participants=data['max_participants'],
    audio_only=data['audio_only'],
    return_url=data['return_url'],
    record_class=data['record_class']
)
```
##### Read
```python
response = v_c.read_virtual_classroom(uuid='...')
```
##### Update
Note: you can pass any information into the `**kwargs`
```python
data = {
    'room_token': randint(0, 100),
    'cancelled': False,
    'description': "This is a test",
    'start': datetime.now().isoformat(),
    'end': datetime.now().isoformat(),
    'max_participants': 2,
    'audio_only': False,
    'return_url': "",
    'record_class': False
}

response = v_c.update_virtual_classroom(uuid=uuid,
                                        room_token=data['room_token'],
                                        cancelled=data['cancelled'],
                                        description=data['description'],
                                        start=data['start'],
                                        end=data['end'],
                                        max_participants=data['max_participants'],
                                        audio_only=data['audio_only'],
                                        return_url=data['return_url'],
                                        record_class=data['record_class']
                                        )
```
##### Delete
```python
response = v_c.delete_virtual_classroom(uuid=uuid)
```
#### Participants API
##### Prerequisites
```python
from learncube import Participants

public_key = "..."
private_key = "..."

p_c = Participants(public_key=public_key, private_key=private_key)
```
##### Read
```python
response = p_c.read_participant(uuid='...')
```
##### List
Note: you can pass any information into the `**kwargs`
```python
response = p_c.list_participants(room_token="...")
```
#### Logs API
##### Prerequisites
```python
from learncube import Logs

public_key = "..."
private_key = "..."

logs = Logs(public_key=public_key, private_key=private_key)
```
##### Read
```python
response = logs.read_logs(uuid='...')
```
##### List
Note: you can pass any information into the `**kwargs`
```python
response = logs.list_logs(room_token="...")
```
### Options
#### Using a custom api base path
Besides the `public_key` and `private_key` you can provide an `api_base_path`
attribute, which will overwrite the default endpoint. 
## Links
* [Büffelheld](https://bueffelheld.de/)
* [Learncube](https://www.learncube.com/)