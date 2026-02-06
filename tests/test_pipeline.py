from tmallet import TMallet
from tmallet.shannon import ShannonAnalyser, ShannonVisualiser

sample_texts = [
    """
    Discover the cosmos! Each day a different image or photograph of our fascinating universe is featured, along with a brief explanation written by a professional astronomer.
    2012 June 23
    Explanation: As seen from Frösön island in northern Sweden the Sun did set a day after the summer solstice. From that location below the arctic circle it settled slowly behind the northern horizon. During the sunset's final minute, this remarkable sequence of 7 images follows the distorted edge of the solar disk as it just disappears against a distant tree line, capturing both a green and blue flash. Not a myth even in a land of runes, the colorful but elusive glints are caused by atmospheric refraction enhanced by long, low, sight lines and strong atmospheric temperature gradients.
    """,
    """
    May 19, 2008 A vaccine created by University of Rochester Medical Center scientists prevents the development of Alzheimer's disease-like pathology in mice without causing inflammation or significant side effects.
    Vaccinated mice generated an immune response to the protein known as amyloid-beta peptide, which accumulates in what are called "amyloid plaques" in brains of people with Alzheimer's. The vaccinated mice demonstrated normal learning skills and functioning memory in spite of being genetically designed to develop an aggressive form of the disease.
    The Rochester scientists reported the findings in an article in the May issue of Molecular Therapy, the journal of The American Society of Gene Therapy.
    Our study demonstrates that we can create a potent but safe version of a vaccine that utilizes the strategy of immune response shaping to prevent Alzheimer's-related pathologies and memory deficits," said William Bowers, associate professor of neurology and of microbiology and immunology at the Medical Center and lead author of the article. "The vaccinated mice not only performed better, we found no evidence of signature amyloid plaque in their brains.
    Alzheimer's is a progressive neurodegenerative disease associated with dementia and a decline in performance of normal activities. Hallmarks of the disease include the accumulation of amyloid plaques in the brains of patients and the loss of normal functioning tau, a protein that stabilizes the transport networks in neurons. Abnormal tau function eventually leads to another classic hallmark of Alzheimer's, neurofibrillary tangle in nerve cells. After several decades of exposure to these insults, neurons ultimately succumb and die, leading to progressively damaged learning and memory centers in the brain.
    The mice that received the vaccines were genetically engineered to express large amounts of amyloid beta protein. They also harbored a mutation that causes the tau-related tangle pathology. Prior to the start of the vaccine study, the mice were trained to navigate a maze using spatial clues.
    """
]

mallet = TMallet()
obfuscation_techniques = [
    # "noun",
    # "noun-propn",
    # "no-noun",
    # "no-noun-propn",
    # "lemmatization",
    # "scramble-BoW",
    # "scramble-BoW-by-sentence",
    # "scramble-shuffle-siblings",
    # "scramble-reverse-head",
    "shannon",
]

for technique in obfuscation_techniques:
    for text in sample_texts:
        print(technique)
        obfuscated_text = mallet.obfuscate(text, config={
            "algorithm": technique
        }, device="cuda")
        print("====")
        print(technique, obfuscated_text)
        print("====")

analyser = ShannonAnalyser()
visualiser = ShannonVisualiser()

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

