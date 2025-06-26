approved_jobs = [
    "Admin", "Customer Service", "Human Resources", "ITC", "Production",
    "Legal", "Finance", "Sales", "General Management",
    "Research & Development", "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name="John Doe", job="Admin"):
        self.name = name    # Use property
        self.job = job      # Use property

    # Name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Job property
    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
