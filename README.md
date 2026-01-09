# Web Interaction Bot Detector

This project focuses on detecting automated bots by analyzing **behavioral patterns in web interaction sessions**, rather than relying on content, browser fingerprints, or IP-based heuristics.

Bots often differ from humans not by *what* they access, but by *how* they behave — such as request timing, interaction frequency, and variability. This project explores whether such behavioral differences can be captured using machine learning.

---

## Problem Overview

Web bots are commonly used for:
- scraping content
- credential stuffing
- automated form abuse
- API rate abuse

Traditional bot detection systems often depend on:
- IP reputation
- CAPTCHAs
- browser fingerprinting

These methods can be brittle or intrusive.  
This project instead models **interaction behavior at the session level** to distinguish human users from bots.

---

## Approach

The system treats each web session as a single data point and extracts **behavioral features**, such as:

- average time between events  
- variability in event timing  
- events per minute  
- session duration  
- number of unique pages visited  
- repetition patterns  
- mouse and scroll interaction ratios  

Using these features, classical machine learning models are trained to classify sessions as:

- `0` → Human  
- `1` → Bot  

The project intentionally prioritizes **interpretability and feature reasoning** over complex models.

---

## Dataset Strategy

Due to the scarcity of publicly available labeled interaction logs, this project uses **synthetically generated sessions** based on known human and bot behavior patterns.

This approach is common in bot-detection research and allows explicit encoding of behavioral assumptions.

Dataset structure: