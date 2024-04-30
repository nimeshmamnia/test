class Parent:
    raise_amount = 1.04
    no_of_adults = 0

    def __init__(self, first, last, age, salary):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + '.' + last + '@gmail.com'
        self.salary = salary
        Parent.no_of_adults += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * Parent.raise_amount)

    @classmethod
    def alter_adults(cls, adults):
        cls.no_of_adults = adults

    @classmethod
    def from_string(cls, prnt_str):
        first, last = prnt_str.split('-')
        return cls(first, last, age=35, salary=40000)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Parent({}, {}, {})".format(self.first, self.last, self.age)

    def __str__(self):
        return "Hi! I am {} {}. My age is {}. You can contact me at {}".format(self.first, self.last, self.age,
                                                                               self.email)

    def __add__(self, other):
        return self.age + other.age

    def __len__(self):
        return len(self.fullname())


class Children(Parent):
    raise_amount = 1.02

    def __init__(self, first, last, age, salary, mood):
        # Method 1
        super().__init__(first, last, age, salary)
        self.mood = mood
        # Method 2
        # --> Parent.__init__(self, first, last, age, salary)


class Manager(Parent):
    raise_amount = 1.10

    def __init__(self, first, last, age, salary, bachhe=None):
        super().__init__(first, last, age, salary)
        if bachhe is None:
            bachhe = []
        else:
            self.bachhe = bachhe

    def add_bachhe(self, bch):
        if bch not in self.bachhe:
            self.bachhe.append(bch)

    def remove_bachhe(self, bch):
        if bch in self.bachhe:
            self.bachhe.remove(bch)

    def print_bachhe(self):
        for bch in self.bachhe:
            print(bch.fullname())


print("0th Print: ", Parent.no_of_adults)
prnt_1 = Parent("Nimesh", "Mamnia", 40, 20000)
prnt_2 = Parent("Sneha", "Savla", 30, 30000)
# If both __repr__ and __str__ methods are present, __str__ takes precedence over __repr__.
# However, we can explicitly call both of them as well.
print("1st Print: ", prnt_1)
print("2nd Print: ", prnt_1.__repr__())
print("3rd Print: ", prnt_2.__str__())
print("4th Print: ", prnt_2.email)

# Another way of calling prnt1.fullname()
print("5th Print: ", Parent.fullname(prnt_1))
print("6th Print: ", prnt_1.salary)
prnt_1.apply_raise()
print("7th Print: ", prnt_1.salary)
print("8th Print: ", prnt_1.raise_amount)
print("9th Print: ", Parent.raise_amount)
print("10th Print: ", prnt_2.raise_amount)
# Below statement will change raise_amount attribute only for prnt_2 instance and not for others
prnt_2.raise_amount = 1.05
print("11th Print: ", prnt_1.raise_amount)
print("12th Print: ", Parent.raise_amount)
print("13th Print: ", prnt_2.raise_amount)

prnt_2.apply_raise()
print("14th Print: ", prnt_2.salary)
print("15th Print: ", Parent.__dict__)
print("16th Print: ", prnt_1.__dict__)
print("17th Print: ", prnt_2.__dict__)
print("18th Print: ", Parent.no_of_adults)

print("19th Print: ", prnt_1.no_of_adults)
print("20th Print: ", prnt_2.no_of_adults)
Parent.alter_adults(3)
print("21st Print: ", prnt_1.no_of_adults)
print("22nd Print: ", prnt_2.no_of_adults)

new_prnt = "Sneha-Mamnia"
prnt_3 = Parent.from_string(new_prnt)
print("23rd Print: ", prnt_3)
print("24th Print: ", Parent.no_of_adults)

import datetime

today1 = datetime.date(2023, 9, 10)
print("25th Print: ", Parent.is_weekday(today1))
today2 = datetime.date(2023, 2, 7)
print("25th Print: ", Parent.is_weekday(today2))

d1 = Children("Zuvi", "Mamnia", 1, 0, "happy")
s1 = Children("Joey", "Mamnia", 4, 100000, "zoomies")
print("26th Print: ", d1)
print("27th Print: ", d1.__dict__)
print("28th Print: ", d1.mood)
print("29th Print: ", s1.mood)

mgr_1 = Manager("Deepa", "Savla", 50, 200000, [d1])
print("30th Print: ", mgr_1.email)
mgr_1.print_bachhe()
mgr_1.add_bachhe(s1)
print("31st Print: After Adding another attribute")
mgr_1.print_bachhe()
mgr_1.remove_bachhe(d1)
print("32nd Print: After Removing earlier attribute")
mgr_1.print_bachhe()

print("33rd Print: Combined Age --> ", prnt_1 + prnt_2)

print("34th Print: ", len(prnt_3))
