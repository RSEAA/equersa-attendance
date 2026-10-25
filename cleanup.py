from rapidfuzz import fuzz, utils

FUZZ_THRESHOLD = 90       # character-level similarity
MIN_SHARED_WORDS = 2      # need at least this many words in common
OVERLAP_THRESHOLD = 0.75  # shared words / words in the shorter value
STOPWORDS = {"the", "and", "of", "pty", "ltd", "inc", "co", "llc"}  # ignored in word test

def tokens(s):
    return {w for w in utils.default_process(s).split() if w not in STOPWORDS}

def why_duplicate(a, ta, b, tb):
    if fuzz.token_sort_ratio(a, b, processor=utils.default_process) >= FUZZ_THRESHOLD:
        return "fuzzy"
    shared = ta & tb
    if len(shared) >= MIN_SHARED_WORDS and len(shared) / min(len(ta), len(tb)) >= OVERLAP_THRESHOLD:
        return "words"
    return None

with open("output.txt", encoding="utf-8") as f:
    items = [line.strip() for line in f if line.strip()]

kept = []      # list of (original, token set)
removed = []   # (dropped, matched kept value, reason)

for item in items:
    t = tokens(item)
    for k, kt in kept:
        reason = why_duplicate(item, t, k, kt)
        if reason:
            removed.append((item, k, reason))
            break
    else:
        kept.append((item, t))

with open("deduped.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(k for k, _ in kept) + "\n")

with open("removed_review.txt", "w", encoding="utf-8") as f:
    for item, k, reason in removed:
        f.write(f"{reason}\t{item}\t-> {k}\n")

print(f"{len(items)} in, {len(kept)} kept, {len(removed)} removed")
