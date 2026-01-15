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

## Baseline Model Results

A Logistic Regression model was trained as a baseline classifier using the synthetic session-level behavioral features.

**Observation:**
The baseline model achieves perfect classification on the current synthetic dataset. This outcome is expected, as the simulated human and bot behaviors are intentionally well-separated to validate the feature design.

**Note:**
This result does not imply real-world performance. In subsequent iterations, overlapping and edge-case behaviors will be introduced to better reflect realistic bot and human interactions.

## Results & Observations

A Logistic Regression model was used as a baseline classifier on session-level behavioral features.

Initial experiments on clean synthetic data showed near-perfect separation between human and bot sessions, validating the feature design. To better reflect real-world conditions, overlapping behaviors such as fast humans and stealthy bots were introduced.

Under these more realistic conditions, the model exhibits meaningful trade-offs:
- Some bots evade detection (false negatives)
- A small number of humans may be flagged incorrectly (false positives)

These outcomes reflect the inherent ambiguity in behavior-based bot detection.

## Decision Threshold and System Design

Rather than relying on hard class labels, the system uses probability-based predictions. A configurable decision threshold is applied to control the trade-off between false positives and false negatives.

- Lower thresholds favor aggressive bot detection (higher recall)
- Higher thresholds reduce false positives at the cost of allowing some bots through

This separation between model confidence and decision policy mirrors real-world bot detection systems, where actions such as blocking, CAPTCHA challenges, or logging are chosen based on risk tolerance.

## Limitations

- The dataset is synthetically generated and based on assumed behavior patterns.
- Real-world bot behavior may evolve to better mimic human interactions.
- The current model operates at session level and does not capture fine-grained event sequences.

These limitations are acknowledged and provide opportunities for future extension.