import logging
from collections.abc import Mapping


class DummyClient:
    """This is a "fake" boto3 client that allows us to test the system without actually doing a real deployment.
    It will log any method calls for later evaluation.

    Attempts to access attributes (specifically service client methods) will return DummyClientAttributes.
    """
    def __init__(self, service_name: str):
        self.service_name = service_name

    def __getattr__(self, item):
        return DummyClientAttribute(self.service_name, item)


class DummyClientAttribute:
    """This is a "fake" boto3 client attribute, which will mostly serve to immitate the methods called on the client.

    Method invocations will be logged and will return DummyReturnValues, which will indicate attribute accesses.

    For example, you could see something like this logged:
        Calling ecr.batch_get_image(registryId=031871504755, repositoryName=gaia_ui)
        Calling ecr.put_image(registryId=031871504755, imageManifest=<DummyReturnValue: ecr.batch_get_image()[images][0][imageManifest]>)

    Notice above how you can clearly see that the imageManifest passed to the second function is a product of the return
    value from the first function.
    """
    def __init__(self, service_name: str, attribute_name: str):
        self.service_name = service_name
        self.attribute_name = attribute_name

    def __call__(self, *args, **kwargs):
        logging.info(
            f"Calling {self.service_name}.{self.attribute_name}("
                f"{', '.join(args)}"
                f"{', '.join(key + '=' + str(value) for key, value in kwargs.items())}"
            ')'
        )
        return DummyReturnValue(self.service_name, self.attribute_name)

    def __getattr__(self, item):
        return DummyClientAttribute(f'{self.service_name}.{self.attribute_name}', item)


class DummyReturnValue(Mapping):
    """This is a "fake" return value from a DummyClientAttribute invocation. It can stand in place of a dictionary
    (or list accessed by indexes) and will record item access, returning new DummyReturnValues each time an item is
    accessed.

    The product of multiple, sequential item accesses will look something like this:

    <DummyReturnValue: ecr.batch_get_image()[images][0][imageManifest]>

    Notice above that the return-value's repr indicates the originating attribute of the return value as well as the
    sequential key/index accesses.

    """
    def __init__(self, service_name, attribute_name, keys=None):
        self.service_name = service_name
        self.attribute_name = attribute_name
        self.keys = keys or []

    @property
    def __full_name(self):
        full_name = f'{self.service_name}.{self.attribute_name}()'
        if self.keys:
            full_name += ''.join([f'[{key}]' for key in self.keys])
        return full_name

    def __getitem__(self, key):
        return DummyReturnValue(self.service_name, self.attribute_name, self.keys + [key])

    def get(self, key, default=None):
        return self[key]

    def __len__(self) -> int:
        return 1

    def __iter__(self):
        iteration_index = 0
        while iteration_index < len(self):
            keys = self.keys + [self.iteration_index]
            yield self.__class__(self.service_name, self.attribute_name, keys)
            iteration_index += 1

    def __repr__(self):
        return f'<DummyReturnValue: {self.__full_name}>'

    def __getattr__(self, item):
        """Handle call methods with attributes such as:
        ecs.get_waiter(cluster=debugging, services=['debugging'], WaiterConfig={'Delay': 5, 'MaxAttempts': 60})
        """
        return DummyClientAttribute(self.__full_name, item)
