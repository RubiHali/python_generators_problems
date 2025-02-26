class LazyFileLoading:

    def read(self, file):
        with open(file, 'r') as lines:
            for line in lines:
                yield line

    def filter(self, file):
        for line in self.read(file):
            if "ERROR" in line:
                yield line

    def collect(self, file):
        error_logs = []
        for line in self.filter(file):
            error_logs.append(line)
            if len(error_logs) >= 100:
                return error_logs
        return error_logs


if __name__ == '__main__':
    lazy_file_loading = LazyFileLoading()
    print(lazy_file_loading.collect("../log.txt"))
