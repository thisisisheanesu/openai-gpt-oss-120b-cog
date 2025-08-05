import torch
from transformers import pipeline
from cog import BasePredictor, Input
from typing import List, Dict, Any


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        model_id = "openai/gpt-oss-120b"
        
        self.pipe = pipeline(
            "text-generation",
            model=model_id,
            torch_dtype="auto",
            device_map="auto",
        )

    def predict(
        self,
        messages: List[Dict[str, str]] = Input(description="List of messages for multi-turn conversation"),
        max_new_tokens: int = Input(description="Maximum number of tokens to generate", default=256),
    ) -> Dict[str, Any]:
        """Run a single prediction on the model"""
        outputs = self.pipe(
            messages,
            max_new_tokens=max_new_tokens,
        )
        
        return outputs[0]["generated_text"][-1]