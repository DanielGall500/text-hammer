from tmallet import TMallet
from tmallet.shannon import ShannonAnalyser, ShannonVisualiser
from datasets import load_dataset

dataset_repo = "DanielGallagherIRE/fineweb-edu-1B-obfuscated"
dataset = load_dataset(dataset_repo)
threshold = 10
mallet = TMallet()

obfuscated_text = mallet.obfuscate_dataset(
    dataset, 
    "text", 
    f"text_shannon_{threshold}",
    config={
        "algorithm": "shannon",
        "threshold": threshold,
        "replace_with": "_"
})
    # save_chunks_to_folder="./test_chunks")

analyser = ShannonAnalyser()
visualiser = ShannonVisualiser()

"""
processed_texts = analyser.get_distribution_by_word(sample_texts, "test_dist.png")
print(processed_texts)

for text in processed_texts:
    print("====")
    print(text)
    print("====")

words = [[w.word for w in text.word_stats] for text in processed_texts]
mi = [[w.mutual_information for w in text.word_stats] for text in processed_texts]
heatmap = visualiser.display_sentence_heatmap(words, mi)
print(heatmap)

with open("example.html", "w") as f:
    f.write(f"<html><body>{heatmap}</body></html>")

    def obfuscate_dataset_by_chunk(
        self,
        dataset,
        column: str,
        column_obfuscated: str,
        config: Dict,
        save_chunks_to_folder: Path,
        chunk_size: int = 5_000,
        batch_size: int = 100,
        num_proc: Optional[int] = None,
    ) -> None:

"""
