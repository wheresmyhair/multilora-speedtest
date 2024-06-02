from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

model_path = "facebook/opt-125m"
quant_path = "opt-125m-awq"
quant_config = {"zero_point": True, "q_group_size": 128, "w_bit": 4, "version":"GEMM"}

# Load model
model = AutoAWQForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# Quantize
model.quantize(tokenizer, quant_config=quant_config)