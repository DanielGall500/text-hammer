from reef.core.pipeline import ReefPipeline

if __name__ == "__main__":
    reef = ReefPipeline()
    reef.run("./datasets/leipzig.txt")
    print("Successfully run pipeline.")
