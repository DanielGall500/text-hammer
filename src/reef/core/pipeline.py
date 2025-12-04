from dataloaders.txt_loader import TxtLoader

class ReefPipeline:
    def run(self, path_to_dataset: str) -> bool:
        txt_loader = TxtLoader()
        txt_loader.load(path_to_dataset)

    def load(self):
        pass

    def apply_obfuscation(self):
        pass

    def save(self, data):
        pass
