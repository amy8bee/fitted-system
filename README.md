# Outfit Recommendation System

## Overview
The Outfit Recommendation System is a Python-based decision-support application that generates and ranks outfit combinations based on **weather conditions**, **occasion type**, and **user style preferences**.  

It simulates how modern recommendation systems work by generating all possible outfit combinations from a wardrobe and scoring them using a weighted algorithm.

---

## Features

-  Weather-aware outfit filtering (cold, mild, warm)
-  Occasion-based recommendations (10+ scenarios)
-  Weighted scoring system:
  - Style Match (35%)
  - Wardrobe Compatibility (30%)
  - Weather Match (20%)
  - Occasion Match (15%)
- Full outfit generation (tops * bottoms * shoes)
- Interactive user feedback (like/dislike system)
- Top-3 fallback recommendations
- Automated test for validation
- Structured JSON wardrobe input system

---

## Algorithm Summary

The system works in three main stages:

### 1. Outfit Generation
All possible combinations of:
- Tops
- Bottoms
- Shoes

are generated using a Cartesian product.

### 2. Filtering
Outfits are filtered based on:
- Weather compatibility
- Occasion appropriateness
- Style constraints

### 3. Scoring
Each outfit is assigned a score:

```
Score =
0.35 × Style Match +
0.30 × Wardrobe Match +
0.20 × Weather Match +
0.15 × Occasion Match
```

Outfits are then sorted in descending order.

---

## 📂 Project Structure

```
fitted/
│
├── main.py                  # Interactive recommendation system
├── recommendation.py        # Core scoring & ranking algorithm
├── wardrobe.py              # Loads wardrobe data
├── wardrobe.json            # Clothing dataset
├── test_recommendation.py   # Automated test cases
└── README.md                # Project documentation
```

---

##  How to Run

### 1. Clone the repository
```bash
git clone https://github.com/amy8bee/fitted-system.git
cd fitted-system
```

### 2. Run the application
```bash
python main.py
```

### 3. Run automated tests
```bash
python test_recommendation.py
```

---

## Test Cases

The system is validated using multiple scenarios:

- Warm weather + College Class
- Cold weather + Work
- Formal Wedding
- Gym environment
- Vacation scenario

Each test checks:
- Valid outfit generation
- Proper filtering
- Ranked output correctness

---

## Design Decisions

### Weighted Scoring Model
Weights were chosen to prioritize:
- Personal style preference (highest influence)
- Practical wardrobe constraints
- Environmental suitability
- Context/occasion relevance

### Trade-offs
- More combinations improve accuracy but increase computation time
- Simplified style classification improves speed but reduces nuance

---

## Limitations

- Style classification is rule-based (not learned)
- No real-time user preference training yet
- Limited color/texture compatibility analysis

---

## Future Improvements

- Machine learning-based preference learning
- Color compatibility graph system
- Fashion trend integration

---

## Versioning

Final submission tag:

```
v1.0-final
```

GitHub Repository:
```
https://github.com/amy8bee/fitted-system
```

---

## Author

Built as a Python-based recommendation system project demonstrating:
- Algorithm design
- Weighted decision systems
- Combinatorial generation
- Practical ML-style filtering logic