#!/usr/bin/env python3
"""
Topic breakdown helper for the Topic Simplifier skill.
"""

def generate_mind_map(topic, subtopics):
    """
    Generate a mind map for a given topic and its subtopics.

    Args:
        topic: Main topic name
        subtopics: List of subtopics with their details

    Returns:
        String representation of the mind map
    """
    mind_map = f"{topic}\n"

    for i, (subtopic, details) in enumerate(subtopics):
        mind_map += f"├── {subtopic}\n"
        for j, detail in enumerate(details):
            if j == len(details) - 1:
                mind_map += f"    └── {detail}\n"
            else:
                mind_map += f"    ├── {detail}\n"

    return mind_map

def generate_flow_diagram(steps):
    """
    Generate a flow diagram for a process with given steps.

    Args:
        steps: List of steps in the process

    Returns:
        String representation of the flow diagram
    """
    if not steps:
        return ""

    flow = " → ".join(steps)
    return flow

def identify_related_concepts(topic):
    """
    Identify related concepts that help understand the main topic.

    Args:
        topic: Main topic name

    Returns:
        List of related concepts with brief explanations
    """
    # This would be implemented with a knowledge base in a real implementation
    related = {
        "machine learning": [
            ("Algorithms", "Mathematical procedures that power ML models"),
            ("Training Data", "Examples used to teach the model"),
            ("Features", "Measurable properties used as input"),
            ("Overfitting", "When a model learns training data too well"),
            ("Accuracy", "How often the model makes correct predictions")
        ],
        "blockchain": [
            ("Cryptographic Hash", "Digital fingerprint of data"),
            ("Decentralization", "No single authority controlling the system"),
            ("Consensus Mechanism", "How nodes agree on the ledger state"),
            ("Smart Contracts", "Self-executing contracts with coded terms"),
            ("Public/Private Keys", "Digital signatures for authentication")
        ]
    }

    return related.get(topic.lower(), [])

def identify_clarifications(topic):
    """
    Identify potential points of confusion for a topic.

    Args:
        topic: Main topic name

    Returns:
        List of clarifications to address confusion
    """
    clarifications = {
        "machine learning": [
            "ML is a subset of AI, not the same thing",
            "Models don't 'understand' like humans - they find statistical patterns",
            "More data doesn't always mean better results"
        ],
        "blockchain": [
            "Blockchain is not just for cryptocurrencies",
            "Not all blockchains are public or anonymous",
            "Blockchains aren't always faster than traditional databases"
        ]
    }

    return clarifications.get(topic.lower(), [])