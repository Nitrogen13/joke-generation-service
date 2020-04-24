import sys

import torch

sys.path.append("./ruGPT2")
from ruGPT2.arguments import get_args
from ruGPT2.generate_samples import prepare_tokenizer, setup_model
from ruGPT2.pretrain_gpt2 import initialize_distributed

from constants import (
    MPSIZE,
    NLAYERS,
    NHIDDEN,
    CHECKPOINT_PATH,
    NATT,
    TOKENIZER_PATH,
    MAXSEQLEN,
    TEMP,
    TOPK,
    TOPP, MAX_POSITIONAL_EMBEDDING,
)

torch.backends.cudnn.enabled = True

# Arguments.
ARGS = get_args()
ARGS.model_parallel_size = MPSIZE
ARGS.num_layers = NLAYERS
ARGS.num_layers = NLAYERS
ARGS.hidden_size = NHIDDEN
ARGS.load = str(CHECKPOINT_PATH)
ARGS.num_attention_heads = NATT
ARGS.max_position_embeddings = MAX_POSITIONAL_EMBEDDING
ARGS.tokenizer_type = "RubertaBPETokenizer"
ARGS.tokenizer_path = str(TOKENIZER_PATH)
ARGS.fp16 = True
ARGS.cache_dir = "cache"
ARGS.out_seq_length = MAXSEQLEN
ARGS.temperature = TEMP
ARGS.top_k = TOPK
ARGS.num_samples = 0
ARGS.top_p = TOPP
ARGS.recompute = True

# Pytorch distributed.
initialize_distributed(ARGS)

# get the tokenizer
TOKENIZER = prepare_tokenizer(ARGS)

# Model, optimizer, and learning rate.
MODEL = setup_model(ARGS)

# setting default batch size to 1
# args.batch_size = 1

ARGS.device = torch.cuda.current_device()
