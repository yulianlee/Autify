import os
from transformers import pipeline
import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--model_path",
    type=str,
    default="HuggingFaceH4/starchat-beta",
    help="Hugging Face model name or local path",
)
args = parser.parse_args()


def load_pipeline(model_path: str = args.model_path, use_gpu: bool = True):
    """
    Load a custom pipeline from a Hugging Face endpoint or from a local file.

    Parameters:
    - model_path (str): The Hugging Face model name or the local path to the model directory.
    - use_gpu (bool): Whether to use the GPU if available.

    Returns:
    - pipe: The loaded language model pipeline.
    """  # noqa: E501
    # Check if a GPU is available
    device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"

    # Check if the model name_or_path is a local path
    if os.path.exists(model_path):
        # Load the model from the local path
        pipe = pipeline("text-generation", model=model_path, device=device)
    else:
        # Load the model from the Hugging Face model hub
        pipe = pipeline("text-generation", model=model_path, device=device)

    return pipe


def generate_code(
    pipe, prompt, max_tokens=256, temperature=0.2, top_k=50, top_p=0.95
):  # noqa: E501
    generate_code_prompt = f"""
    The following is an agent that only outputs python code to a user question.
    The agent answers non-coding questions with an error message.

    Customer: How do I bake a chocolate cake?
    Agent: Invalid request. Please provide a programming-related question.

    Customer: Explain the theory of relativity.
    Agent: Invalid request. Please provide a programming-related question.

    Customer: Write code to sort a list of integers in ascending order.
    Agent: def sort_list(lst):
               sorted_list = sorted(lst)
               return sorted_list

    Customer: Write me python code to my question: "{prompt}". Return an error message if my question is not programming related.
    Agent:
    """  # noqa: E501
    outputs = pipe(
        generate_code_prompt,
        max_length=max_tokens,
        do_sample=True,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
    )  # noqa
    generated_output = outputs[0]["generated_text"]
    return generated_output


def improve_code(
    pipe, prompt, max_tokens=256, temperature=0.2, top_k=50, top_p=0.95
):  # noqa: E501
    feedback_prompt = f"""
    The following is an agent that improves the previous code given by the agent based on feedback from the user.
    The agent answers non-coding feedback with an error message.

    Customer: Update the previous code based on my feedback here: "{prompt}". Return an error message if my feedback is not programming related.
    Agent:
    """  # noqa: E501
    outputs = pipe(
        feedback_prompt,
        max_length=max_tokens,
        do_sample=True,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
    )
    generated_output = outputs[0]["generated_text"]
    return generated_output
