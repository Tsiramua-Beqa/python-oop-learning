class DoorLock:
    def __init__(self, name, max_attempts):
        self.name = name
        self.is_locked = True
        self.attempts = 0
        self.max_attempts = max_attempts
        self.is_blocked = False

    def unlock(self, correct_code: bool):
        if self.is_blocked:
            return

        if correct_code:
            if not self.is_locked:
                return
            self.is_locked = False
            self.attempts = 0
        else:
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                self.is_blocked = True
                self.is_locked = True

    def lock(self):
        if self.is_locked:
            return
        self.is_locked = True

    def reset(self):
        self.attempts = 0
        self.is_blocked = False
        self.is_locked = True

    def __str__(self):
        return (
            f"Door: {self.name} | "
            f"Locked: {self.is_locked} | "
            f"Attempts: {self.attempts}/{self.max_attempts} | "
            f"Blocked: {self.is_blocked}"
        )