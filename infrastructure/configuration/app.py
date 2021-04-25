class StorageOptions(object):
    def __init__(
            self,
            save_location: str = "/data",
            read_chunk_size: int = 1024
    ):
        self.save_location = save_location
        self.read_chunk_size = read_chunk_size


class AppOptions(object):
    def __init__(self):
        self.project_name = "storage-api"
        self.storage_options = StorageOptions(save_location="/data")


APP_OPTIONS = AppOptions()
