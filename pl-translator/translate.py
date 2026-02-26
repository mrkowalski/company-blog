import argparse
import asyncio
import time

import llm

GEMINI_MODEL1 = "gemini-3.1-pro-preview"
GEMINI_MODEL2 = "gemini-3-flash-preview"
BIELIK_MODEL = "bielik"


async def gemini_translate(src: str) -> str:
    start = time.time()
    with open("prompt_gemini.md") as fp:
        system_prompt = fp.read()
    model = llm.get_async_model(GEMINI_MODEL2)
    response = await model.prompt(
        system=system_prompt, prompt=source_post, stream=False
    )
    end = time.time()
    print(f"Gemini translation took {end - start:.2f} seconds.")
    return await response.text()

def split_front_matter(s: str) -> tuple[str, str]:
    parts = s.split('---', maxsplit=2)
    return "---".join(parts[:-1]) + "---\n", parts[-1]

async def bielik_polish(src: str) -> str:
    with open("prompt_bielik_polish.md") as fp:
        system_prompt = fp.read()
    model = llm.get_model("bielik")
    fm, body = split_front_matter(src)
    start = time.time()
    response = await asyncio.to_thread(
        model.prompt, system=system_prompt, prompt=body, stream=False
    )
    translation = response.text()
    end = time.time()
    print(f"Bielik polishing took {end - start:.2f} seconds.")
    return fm + translation

async def bielik_translate(src: str) -> str:
    with open("prompt_bielik_translate.md") as fp:
        system_prompt = fp.read()
    model = llm.get_model("bielik")
    fm, body = split_front_matter(src)
    start = time.time()
    response = await asyncio.to_thread(
        model.prompt, system=system_prompt, prompt=body, stream=False
    )
    translation = response.text()
    end = time.time()
    print(f"Bielik translation took {end - start:.2f} seconds.")
    return fm + translation


async def main_both(source_post: str) -> None:
    print("Hello both mode.")
    translation = await gemini_translate(source_post)
    print("Translation:")
    print(translation)
    print("Now let's polish the translation with Bielik.")
    polished_translation = await bielik_polish(translation)
    print("Polished translation:")
    print(polished_translation)
    print("Goodbye.")

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
    parser.add_argument("mode", choices=["bielik", "both"], help="both = translate with Gemini, polish with Bielik.")
    parser.add_argument("src", type=str, help="The source file to translate.")
    args = parser.parse_args()
    with open(args.src) as fp:
        source_post = fp.read()
    asyncio.run(main_bielik(source_post) if args.mode == "bielik" else main_both(source_post))
