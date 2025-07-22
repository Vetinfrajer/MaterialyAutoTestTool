import yaml
import requests
import re

# Načtení endpointu
try:
    with open("endpoint.txt", "r", encoding="utf-8") as f:
        ENDPOINT = f.read().strip()
except Exception:
    ENDPOINT = "http://127.0.0.1:1234"

# Načtení obou kontextových souborů a jejich spojení
with open("context1.txt", "r", encoding="utf-8") as f1:
    context = f1.read()

def ask_question(question, context=None):
    url = ENDPOINT + "/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    messages = []
    if context:
        messages.append({"role": "system", "content": context})
    messages.append({"role": "user", "content": question})
    payload = {
        "model": "gemma:7b",
        "messages": messages,
        "temperature": 0.2
    }
    r = requests.post(url, headers=headers, json=payload)
    try:
        response = r.json()
    except Exception as e:
        print("Chyba při parsování JSON:", e)
        print("Text odpovědi:", r.text)
        raise
    if "choices" not in response:
        print("Odpověď neobsahuje klíč 'choices':", response)
        raise KeyError("choices")
    return response["choices"][0]["message"]["content"]

def evaluate_answer(answer, expected_keywords):
    return all(
        any(re.search(re.escape(str(keyword)), answer, re.IGNORECASE) for keyword in (group if isinstance(group, (list, tuple)) else [group]))
        for group in expected_keywords
    )

with open("test_core_messenger_and_inbox.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

passed_count = 0
failed_count = 0
total_count = 0

for difficulty, tests in data["tests"].items():
    print(f"\n=== {difficulty.upper()} TESTS ===")
    for t in tests:
        question = t["question"]
        expected = t["expected_keywords"]
        print(f"\nQ: {question}")
        answer = ask_question(question, context)
        print(f"A: {answer}")
        passed = evaluate_answer(answer, expected)
        print("✅ Passed" if passed else "❌ Failed")
        total_count += 1
        if passed:
            passed_count += 1
        else:
            failed_count += 1

# Souhrn na konci
print("\n====================")
print(f"Celkem otázek: {total_count}")
print(f"✅ Passed: {passed_count}")
print(f"❌ Failed: {failed_count}")
if total_count > 0:
    success_rate = 100 * passed_count / total_count
    print(f"Úspěšnost: {success_rate:.1f}%")
else:
    print("Úspěšnost: 0%") 