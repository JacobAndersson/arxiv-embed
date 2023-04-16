from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForSeq2SeqLM
import torch

model_name = 'cross-encoder/ms-marco-MiniLM-L-12-v2'

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

def rerank(query, docs):
    document = docs[0]
    q_input = [query] * len(docs)
    p_input = [doc['abstract'] for doc in docs]
    features = tokenizer(q_input, p_input,  padding=True, truncation=True, return_tensors="pt")

    with torch.no_grad():
        scores = model(**features).logits

    for (doc, score) in zip(docs, scores):
        doc['rank_score'] = score

    scored_docs = sorted(docs, key=lambda x: x['rank_score'], reverse=True)
    return scored_docs

if __name__ == "__main__":
    scored_docs = rerank("what is the capital of france", ["paris", "parisa", "Marseille", "london"])
    print(scored_docs)
