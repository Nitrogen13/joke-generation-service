from matplotlib import pyplot as plt


def read_umoreski(path="data/umoreski.txt"):
    with open(path, "r", encoding="utf-8") as f:
        posts = f.read().split("<|endoftext|>")
    return [p.strip() for p in posts]


def analyse_posts(data):
    print(f"Samples: {len(data)}")
    lens = [len(anecdote.split()) for anecdote in data]
    lens = [l for l in lens if l < 600]
    plt.hist(lens, bins=600)
    plt.title("Anecdote tokens number histogram")
    plt.show()


if __name__ == '__main__':
    analyse_posts(read_umoreski())
