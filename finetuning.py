import sys
import torch
from unsloth import FastLanguageModel
import json

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
    print("CUDA not available, using CPU instead")

def get_finetuning_args():
    with open('finetuning_args', 'r') as f:
        config = json.load(f)
        print('config')
        return config

# model, tokenizer = FastLanguageModel.from_pretrained(
#     model_name=""
# )

def main():
    config = get_finetuning_args()



if __name__ == "__main__":
    main()