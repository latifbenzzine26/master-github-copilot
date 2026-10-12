def clean_text(line: str) -> list[str]:
    """Lowercase a line, remove commas and periods, and split into tokens."""
    line = line.lower()
    line = line.replace(",", "").replace(".", "")
    return line.split()


def count_tokens(tokens: list[str], counts: dict[str, int]) -> None:
    """Update counts with the tokens from a line."""
    for token in tokens:
        if token in counts:
            counts[token] += 1
        else:
            counts[token] = 1


def process_transcript(lines: list[str]) -> dict[str, int]:
    """Return word‑count mapping for a chat transcript."""
    counts: dict[str, int] = {}
    for ln in lines:
        tokens = clean_text(ln)
        count_tokens(tokens, counts)
    most_common = max(counts.items(), key=lambda kv: kv[1])
    print(f"Most common word → {most_common[0]} ({most_common[1]})")
    return counts

# Sample input and function call
lines = [
  "Hello, how are you?",
  "I am fine. How are you doing?",
  "I am doing well. Thank you!"
]

# Call the function and store the result
word_counts = process_transcript(lines)

# Print the full word count dictionary
print(word_counts)

