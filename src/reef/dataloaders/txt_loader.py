from dataloaders.base import DataLoader

class TxtLoader(DataLoader):
    def load(self, path_to_dataset: str) -> bool:
        with open(path_to_dataset, 'r') as f:
            full_text = f.read()
            print(full_text)
        return True