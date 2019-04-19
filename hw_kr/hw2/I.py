import copy

class FragileDict():
    def __init__(self, d = {}, flag = True):
        self._data = copy.deepcopy(d)
        self._lock = flag

    def __getitem__(self, key):
        if self._lock == False:
            return self._data_copy[key]
        else:
            return copy.deepcopy(self._data[key])

    def __setitem__(self, key, value):
        if not self._lock:
            self._data_copy[key] = value
        else:
            raise RuntimeError("Protected state")

    def __contains__(self, value):
        if not self._lock:
            return value in self._data_copy
        else:
            return  value in self._data

    def __enter__(self):
        self._lock = False
        self._data_copy = copy.deepcopy(self._data)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._lock = True
        if exc_type is not None and issubclass(exc_type, Exception):
            print("Exception has been suppressed.")
            # self._data = copy.deepcopy(self._data_copy)
            del self._data_copy
            return True
        elif exc_type is None:
            self._data = copy.deepcopy(self._data_copy)
            del self._data_copy




# d = FragileDict({'key': 5})

# with d:
#     d['key'] = 6
#     d['ord'] = 7

# print(d['key'])
# print(d['ord'])

# # >>
# # 6
# # 7
# # >>

#############################

# d = FragileDict({'key': 5})

# try:
#     d['key'] = 6
# except RuntimeError as e:
#     print(e)

# try:
#     d['ord'] = 7
# except RuntimeError as e:
#     print(e)

# print(d['key'] == 5)
# print('ord' not in d)

# # >>
# # Protected state
# # Protected state
# # True
# # True
# # >>

#############################

# d = FragileDict({'key': 5})

# with d:
#     d['key'] = 6
#     print(d['key'])
#     d['ord'] = 7
#     print('ord' in d and d['ord'] == 7)
#     raise Exception()

# print(d['key'])
# print('ord' not in d)

# # 6
# # True
# # Exception has been suppressed.
# # 5
# # True

#############################

# d = FragileDict({'key': []})

# with d:
#     a = d['key']
#     d['key'].append(10)
#     a.append(10)

# a.append(10)
# print(a == [10, 10, 10] and d['key'] == [10, 10])
# # >>
# # True
# # >>