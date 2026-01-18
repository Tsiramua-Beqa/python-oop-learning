class Task:
    def __init__(self, task_id):
        self.task_id = task_id
        self.status = "created"
        self.fail_count = 0
        self.__max_retries = 3

    def start(self):
        if self.status == "running":
            return
        if self.status == "completed":
            return
        if self.fail_count >= self.__max_retries:
            return

        self.status = "running"

    def fail(self):
        if self.status != "running":
            return

        self.fail_count += 1
        self.status = "failed"

    def complete(self):
        if self.status != "running":
            return

        self.status = "completed"

    def __str__(self):
        return (
            f"Task ID: {self.task_id} | "
            f"Status: {self.status} | "
            f"Fails: {self.fail_count}/{self.__max_retries}"
        )