---
title: 'What is a large language model?'
description: 'LLMs are everywhere now. But how do they actually work? A plain-English explainer for the curious.'
pubDate: 'Mar 01 2026'
heroImage: '../../assets/blog-placeholder-1.jpg'
---

You've seen them in news headlines, product launches, and probably your own daily workflow by now. Large language models — LLMs — are the engines behind ChatGPT, Claude, Gemini, and dozens of other AI assistants. But what are they, really?

## A mathematical autocomplete

At the most basic level, an LLM is a function that predicts the next word (or more precisely, "token") given a sequence of words that came before it. Train that function on enough text — hundreds of billions of words scraped from books, websites, forums, and code repositories — and something surprising emerges: the model develops a broad, flexible understanding of language.

Not understanding in the way humans mean it. But functional understanding: it can answer questions, write code, translate languages, summarise documents, and carry on conversations.

## The architecture: Transformers

The "architecture" of virtually every major LLM today is called the **Transformer**, introduced in the landmark 2017 paper *Attention is All You Need* by researchers at Google.

The key innovation was the **attention mechanism** — a way for the model to weigh how relevant each word in the input is when predicting the next word. Instead of reading left-to-right like a human, the transformer can look at the entire context at once and decide which parts matter most.

This is why LLMs are so much better at long-context tasks than earlier models were.

## Scale changes everything

The "large" in large language model is doing a lot of work. Early neural language models had millions of parameters. GPT-3, released in 2020, had 175 billion. Today's frontier models are estimated to have over a trillion.

What researchers discovered — somewhat unexpectedly — is that as you scale up the number of parameters and the amount of training data, models don't just get *incrementally* better. They develop **emergent capabilities**: they start doing things they were never explicitly trained to do, like solving maths problems step by step, writing working code, or explaining jokes.

## What they can't do

LLMs are not databases. They don't have access to real-time information unless given tools to search the web. They can and do **hallucinate** — confidently stating untrue things, because they're optimised to produce plausible-sounding text, not verified facts.

They also have no persistent memory across conversations (unless that is explicitly built in), and they don't "think" in the way humans do — they are, at their core, extremely sophisticated pattern matching systems.

## Why it matters

Understanding LLMs at even a surface level helps you use them better, spot their mistakes faster, and think critically about the AI products being built on top of them. That's what ThinkingCats is here for.
