# Final Summary - T1: Planning and Designing an Interactive ‘Minichess’ Command-Line Simulator

## Overview

This project delivers a fully documented design plan for an interactive Minichess simulator based on the Los Alamos variant. The game is designed as a **command-line application** with support for both **two-player** and **single-player (CPU)** modes. The implementation plan is tailored to Python but remains language-agnostic for C++ or F# adaptation.

---

## Objectives Covered

### ✅ Game Functionalities

| Requirement                                | Fulfilled |
|--------------------------------------------|-----------|
| Start a new 2-player game                  | ✅        |
| Allow each player to take turns            | ✅        |
| Judge when a player wins                   | ✅        |
| Single-player mode against CPU             | ✅        |

---

## Design Artifacts Included

| File                             | Purpose                                                                 |
|----------------------------------|-------------------------------------------------------------------------|
| `01_UserInteractionDesign.md`   | Gherkin specs and Hoare Logic-based command-line interaction model     |
| `02_DataModelDesign.md`         | Set Theory definitions and language-specific types for game components |
| `03_BehaviourDesign.md`         | Mathematical functions and graph-based turn management                 |
| `04_CPUDesign.md`               | Rule-based and heuristic CPU AI model                                   |
| `diagrams/*.puml`               | UML class and state diagrams in PlantUML                                |
| `README.md`                     | High-level overview and project setup                                   |

---

## Design Principles Followed

### 🔍 Theoretical Foundations

- **Set Theory:** Used for defining piece types, players, and positions.
- **Hoare Logic:** Used for specifying interaction invariants.
- **Mathematical Functions & Relations:** Defined game behaviors (e.g., move validation, checkmate).
- **Graph Theory:** Modeled board states and turn transitions.

---

## Development Recommendations

| Stage         | Tools/Tech | Notes                                                |
|---------------|------------|------------------------------------------------------|
| Prototyping   | Python     | Easy to implement core logic and debug               |
| Diagrams      | PlantUML   | Visualize transitions, classes, and behaviors        |
| Versioning    | Git        | Track progress and collaborative contributions       |
| Future AI     | Minimax    | Can replace heuristic logic for smarter CPU          |

---

## Conclusion

This document set represents a **FAANG-level** software architecture approach to the Minichess game. It enables clear implementation steps, modular design, and academic rigor by grounding decisions in formal logic, set theory, and functional mappings.

**Next Steps:**
- Convert each design section into working Python/C++ code.
- Expand CPU intelligence with deeper evaluation trees.
- Consider GUI or Web interface in future versions.

---

## Acknowledgments

Inspired by:
- Los Alamos Chess Rules
- Formal Methods (Hoare Logic, Set Theory)
- Modern Object-Oriented Design

---
