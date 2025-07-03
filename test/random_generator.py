from faker import Faker


class RandomGenerator:
    faker = Faker()

    @classmethod
    def uuid(cls) -> str:
        return cls.faker.uuid4()

    @classmethod
    def version(cls) -> str:
        major = cls.faker.random_int(min=0, max=2)
        minor = cls.faker.random_int(min=0, max=50)
        patch = cls.faker.random_int(min=0, max=99)
        return f"{major}.{minor}.{patch}"
    
    @classmethod
    def operating_system(cls) -> str:
        os_list = ["Windows", "macOS", "Linux", "Ubuntu", "Debian", "CentOS", "Fedora", "FreeBSD", "iOS", "Android"]
        return cls.faker.random_element(elements=os_list)
