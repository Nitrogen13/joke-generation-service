from pathlib import Path

ROOT_DIR = Path(__file__).parent
DATA_DIR = ROOT_DIR / "data"

API_TOKEN = "1181606773:AAE24QtUEn0at0UW6VcuC2LgOuIFIkET4eU"

CHECKPOINT_PATH = DATA_DIR.parent / "gpt2_345m"
TOKENIZER_PATH = DATA_DIR.parent / "gpt2_345m" / "vocab_50000.bpe"
MPSIZE = 1
NLAYERS = 24
NHIDDEN = 1024
NATT = 16
MAXSEQLEN = 32

# SAMPLING ARGS

TEMP = 0.9
# If TOPK/TOPP are 0 it defaults to greedy sampling, top-k will also override top-p
TOPK = 0
TOPP = 0

WORLD_SIZE=1
CUDA_VISIBLE_DEVICES=0


