import os
import argparse
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def get_gemini_response(prompt, use_stream=False):
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config=genai.types.GenerationConfig(
            temperature=0.7,
            top_p=0.9,
            top_k=40,
        )
    )

    if use_stream:
        print("Gemini: ", end="")
        response_stream = model.generate_content(prompt, stream=True)
        for chunk in response_stream:
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()
        return None
    else:
        print("Gemini thinking...")
        response = model.generate_content(prompt)
        return response.text


if __name__ == "__main__":

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    parser = argparse.ArgumentParser()
    parser.add_argument("--stream", action="store_true")
    args = parser.parse_args()

    print("--- Ask Gemini ---")

    while True:
        user_prompt = input("\nUser: ")

        if user_prompt.lower() == 'exit':
            break
        
        response_text = get_gemini_response(user_prompt, use_stream=args.stream)
        
        if not args.stream:
            print(response_text)