# Simple frequency-based summarizer (no external deps)
import re
from collections import Counter, defaultdict

STOPWORDS = set("i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now".split())

def split_sentences(text):
    s = re.split(r'(?<=[.!?])\s+', text.strip())
    s = [sent.strip() for sent in s if sent.strip()]
    return s

def tokenize(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return [w for w in words if w not in STOPWORDS]

def score_sentences(sentences):
    freq = Counter()
    for s in sentences:
        for w in tokenize(s):
            freq[w] += 1
    if not freq:
        return {i:0 for i in range(len(sentences))}
    maxf = max(freq.values())
    for k in freq:
        freq[k] = freq[k] / maxf
    scores = {}
    for i,s in enumerate(sentences):
        sc = 0.0
        for w in tokenize(s):
            sc += freq.get(w,0)
        scores[i] = sc / (len(tokenize(s)) + 1e-6)
    return scores

def summarize_text(text, num_sentences=2):
    sentences = split_sentences(text)
    if not sentences:
        return ""
    scores = score_sentences(sentences)
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_idxs = sorted([i for i,_ in ranked[:num_sentences]])
    summary = " ".join([sentences[i] for i in top_idxs])
    return summary
