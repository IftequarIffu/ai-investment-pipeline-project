import os
from typing import Any, List, Optional, Type, Callable
from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_chat_content(
    prompt: str,
    model: str = "gemini-2.5-flash",
    system_instruction: Optional[str] = None,
    tools: Optional[List[Callable]] = None,
    response_schema: Optional[Type[BaseModel]] = None,
    enable_search: bool = False  # New parameter for Google Search
) -> Any:
    """
    A highly generic wrapper for Gemini that supports standard text, 
    custom python tools, Pydantic JSON schemas, and Google Search grounding.
    """
    config_args = {}

    if system_instruction:
        config_args["system_instruction"] = system_instruction

    # 1. Build out tools list dynamically
    actual_tools = []
    if tools:
        actual_tools.extend(tools)
        
    if enable_search:
        # Append the native Google Search grounding tool
        actual_tools.append(types.Tool(google_search=types.GoogleSearch()))

    if actual_tools:
        config_args["tools"] = actual_tools

    # 2. Configure structured output if requested
    if response_schema:
        config_args["response_mime_type"] = "application/json"
        config_args["response_schema"] = response_schema

    config = types.GenerateContentConfig(**config_args)

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=config
        )

        if response_schema:
            return response.parsed

        return response

    except Exception as e:
        print(f"Error generating content: {e}")
        raise e