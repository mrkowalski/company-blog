import argparse
import asyncio
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from openai import OpenAI

load_dotenv()

GEMINI_MODEL1 = "gemini-3.1-pro-preview"
GEMINI_MODEL2 = "gemini-3-flash-preview"
BIELIK_MODEL = "bielik"

cf_client = OpenAI(
    api_key=os.environ.get("CLOUDFERRO_API_KEY"),
    base_url="https://api-sherlock.cloudferro.com/openai/v1/",
)

gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def gemini_translate(src: str) -> str:
    start = time.time()
    with open("prompt_gemini.md") as fp:
        system_prompt = fp.read()
    gemini_response = gemini_client.models.generate_content(
        model=GEMINI_MODEL2,
        contents=source_post,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    end = time.time()
    print(f"Gemini translation took {end - start:.2f} seconds.")
    return gemini_response.text


def split_front_matter(s: str) -> tuple[str, str]:
    parts = s.split("---", maxsplit=2)
    return "---".join(parts[:-1]) + "---\n", parts[-1]


def bielik_polish(src: str) -> str:
    with open("prompt_bielik_polish.md") as fp:
        system_prompt = fp.read()
    fm, body = split_front_matter(src)
    start = time.time()
    response = cf_client.chat.completions.create(
        model="Bielik-11B-v3.0-Instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": body},
        ],
    )
    translation = response.choices[0].message.content
    end = time.time()
    print(f"Bielik polishing took {end - start:.2f} seconds.")
    return fm + translation


async def bielik_translate(src: str) -> str:
    with open("prompt_bielik_translate.md") as fp:
        system_prompt = fp.read()
    fm, body = split_front_matter(src)
    start = time.time()
    response = cf_client.chat.completions.create(
        model="Bielik-11B-v3.0-Instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": body},
        ],
    )
    translation = response.choices[0].message.content
    end = time.time()
    print(f"Bielik translation took {end - start:.2f} seconds.")
    return fm + translation


def main_both(source_post: str, basename) -> None:
    basea, baseb = os.path.splitext(basename)
    print(f"Hello both mode for {basename}.")
    translation = gemini_translate(source_post)
    with open(f"{basea}_gemini{baseb}", "w") as f:
        f.write(translation)
    print("Now let's polish the translation with Bielik.")
    polished_translation = bielik_polish(translation)
    with open(f"{basea}_bielik{baseb}", "w") as f:
        f.write(polished_translation)


async def main_bielik(src: str) -> None:
    print("Hello Bielik mode.")
    translation = await bielik_translate(src)
    print("Translation:")
    print(translation)
    print("Goodbye.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Translate a post from English to Polish."
    )
    parser.add_argument(
        "mode",
        choices=["bielik", "both"],
        help="both = translate with Gemini, polish with Bielik.",
    )
    parser.add_argument("src", type=str, help="The source file to translate.")
    args = parser.parse_args()
    with open(args.src) as fp:
        source_post = fp.read()
    basename = os.path.basename(args.src)
    if args.mode == "bielik":
        asyncio.run(main_bielik(source_post))
    else:
        main_both(source_post, basename)
