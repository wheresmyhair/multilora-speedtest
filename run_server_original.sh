CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server \
    --model /home/yizhenjia/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3-70B/snapshots/b4d08b7db49d488da3ac49adf25a6b9ac01ae338 \
    --tensor-parallel-size 4
