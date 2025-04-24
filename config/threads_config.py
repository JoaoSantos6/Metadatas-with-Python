class ThreadsConfig:
    def __init__(self):
        self.threads_min = 1
        self.threads_max = 10
        self.threads_default = 3

    def get_threads_min(self):
        return self.threads_min
    
    def get_threads_max(self):
        return self.threads_max