"""
Bloom's Revised Taxonomy Definitions, Action Verbs, and Cognitive Analysis Engine.
"""

from typing import Dict, List, Any

BLOOM_TAXONOMY_LEVELS = {
    "L1": {
        "name": "Remember",
        "description": "Recall facts and basic concepts without necessarily understanding them.",
        "verbs": ["define", "identify", "describe", "recognize", "retrieve", "name", "state", "match", "select", "list", "reproduce"],
        "weight": 1,
        "typical_marks": (1, 3)
    },
    "L2": {
        "name": "Understand",
        "description": "Explain ideas or concepts, interpret, summarize, paraphrase, or classify.",
        "verbs": ["explain", "summarize", "paraphrase", "classify", "clarify", "interpret", "illustrate", "discuss", "predict", "translate"],
        "weight": 2,
        "typical_marks": (2, 6)
    },
    "L3": {
        "name": "Apply",
        "description": "Use information in new situations, solve concrete problems, execute algorithms or procedures.",
        "verbs": ["apply", "solve", "calculate", "demonstrate", "implement", "execute", "use", "compute", "operate", "modify"],
        "weight": 3,
        "typical_marks": (4, 10)
    },
    "L4": {
        "name": "Analyze",
        "description": "Draw connections among ideas, distinguish parts, deconstruct systems, find evidence to support generalizations.",
        "verbs": ["analyze", "differentiate", "distinguish", "examine", "compare", "contrast", "deconstruct", "investigate", "correlate", "categorize"],
        "weight": 4,
        "typical_marks": (6, 12)
    },
    "L5": {
        "name": "Evaluate",
        "description": "Justify a stand or decision, critique, appraise, judge based on standards or criteria.",
        "verbs": ["evaluate", "judge", "critique", "justify", "defend", "assess", "prioritize", "validate", "rate", "appraise"],
        "weight": 5,
        "typical_marks": (8, 16)
    },
    "L6": {
        "name": "Create",
        "description": "Produce new or original work, design architectures, formulate plans, construct novel solutions.",
        "verbs": ["create", "design", "construct", "formulate", "develop", "compose", "propose", "synthesize", "invent", "devise"],
        "weight": 6,
        "typical_marks": (10, 20)
    }
}


def rule_based_bloom_classify(question_text: str) -> Dict[str, Any]:
    """
    Fast deterministic heuristic pass for Bloom level based on syntactic cues and action verbs.
    Provides fallback and baseline before or alongside LLM verification.
    """
    text_lower = question_text.lower()
    matches = {}
    
    for level, data in BLOOM_TAXONOMY_LEVELS.items():
        found_verbs = [v for v in data["verbs"] if f"{v} " in text_lower or text_lower.startswith(f"{v} ") or f" {v}" in text_lower]
        if found_verbs:
            matches[level] = len(found_verbs)
            
    if matches:
        # Pick the highest matched cognitive level (or level with most verb occurrences)
        predicted_level = max(matches, key=lambda k: (matches[k], BLOOM_TAXONOMY_LEVELS[k]["weight"]))
    else:
        # Default heuristic based on question length and complexity
        if any(w in text_lower for w in ["what", "who", "when", "which"]):
            predicted_level = "L1"
        elif any(w in text_lower for w in ["how", "why"]):
            predicted_level = "L2"
        elif any(w in text_lower for w in ["calculate", "find", "determine"]):
            predicted_level = "L3"
        elif any(w in text_lower for w in ["difference", "compare", "contrast"]):
            predicted_level = "L4"
        elif any(w in text_lower for w in ["optimal", "best", "tradeoff", "trade-off", "justify"]):
            predicted_level = "L5"
        elif any(w in text_lower for w in ["design", "architecture", "develop"]):
            predicted_level = "L6"
        else:
            predicted_level = "L2"
            
    return {
        "level": predicted_level,
        "level_name": BLOOM_TAXONOMY_LEVELS[predicted_level]["name"],
        "confidence": 0.85 if matches else 0.60,
        "heuristic_matched": list(matches.keys())
    }


def compute_exam_cognitive_distribution(questions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Computes marks and percentage breakdown across Bloom's levels (L1 - L6).
    """
    distribution = {f"L{i}": {"marks": 0, "count": 0, "percentage": 0.0, "name": BLOOM_TAXONOMY_LEVELS[f"L{i}"]["name"]} for i in range(1, 7)}
    total_marks = 0
    
    for q in questions:
        level = q.get("bloom_level", "L2")
        marks = int(q.get("marks", 5))
        if level in distribution:
            distribution[level]["marks"] += marks
            distribution[level]["count"] += 1
            total_marks += marks
            
    if total_marks > 0:
        for lvl in distribution:
            distribution[lvl]["percentage"] = round((distribution[lvl]["marks"] / total_marks) * 100, 2)
            
    return {
        "total_marks": total_marks,
        "distribution": distribution,
        "low_order_pct": sum(distribution[f"L{i}"]["percentage"] for i in [1, 2]),
        "medium_order_pct": sum(distribution[f"L{i}"]["percentage"] for i in [3, 4]),
        "high_order_pct": sum(distribution[f"L{i}"]["percentage"] for i in [5, 6]),
    }

