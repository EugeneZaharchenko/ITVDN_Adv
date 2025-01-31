def get_first_name(self):
    return self.first_name


def get_last_name(self):
    return self.last_name


def get_middle_name(self):
    return self.middle_name


def init(self, first_name, last_name, middle_name):
    self.first_name = first_name
    self.last_name = last_name
    self.middle_name = middle_name


class BaseUser(object):
    def __str__(self):
        return 'Some string just to output\n<user-object/>'


attrs = {
    'first_name': '',
    'last_name': '',
    'middle_name': '',
    'get_first_name': get_first_name,
    'get_last_name': get_last_name,
    'get_middle_name': get_middle_name,
    '__init__': init
}

bases = (
    BaseUser,
)

User = type('User', bases, attrs)

user1 = User('Eugene', 'Захарч', 'Анатольевич')

print(str(user1))
print(user1.get_first_name())
print(user1.get_last_name())
print(user1.get_middle_name())


def build_class(class_name, base_classes, attrs):
    new_attrs = {}
    for attr, value in attrs.items():
        new_attrs[attr.lower()] = value
    return type(class_name, base_classes, new_attrs)
