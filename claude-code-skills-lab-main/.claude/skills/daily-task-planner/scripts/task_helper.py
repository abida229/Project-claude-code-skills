#!/usr/bin/env python3
"""
Task prioritization helper for the Daily Time-Aware Task Planner skill.
"""

def estimate_task_duration(task_description):
    """
    Estimate task duration based on keywords in the description.

    Args:
        task_description: String describing the task

    Returns:
        Estimated duration in minutes
    """
    task_lower = task_description.lower()

    # Keywords that indicate task complexity/duration
    short_keywords = ['email', 'reply', 'call', 'quick', 'brief', 'check', 'review', 'scan']
    medium_keywords = ['write', 'draft', 'meeting', 'prep', 'prepare', 'research', 'analyze']
    long_keywords = ['project', 'complete', 'develop', 'create', 'design', 'implement', 'deep work']

    # Base duration estimates
    if any(keyword in task_lower for keyword in short_keywords):
        return 15  # 15 minutes for short tasks
    elif any(keyword in task_lower for keyword in long_keywords):
        return 120  # 2 hours for long tasks
    elif any(keyword in task_lower for keyword in medium_keywords):
        return 45  # 45 minutes for medium tasks
    else:
        return 30  # Default 30 minutes for unclear tasks

def categorize_task_priority(task_description):
    """
    Categorize task priority based on keywords in the description.

    Args:
        task_description: String describing the task

    Returns:
        Priority level: 'high', 'medium', or 'low'
    """
    task_lower = task_description.lower()

    high_priority_keywords = [
        'urgent', 'asap', 'important', 'deadline', 'critical', 'crucial',
        'priority', 'top', 'emergency', 'time-sensitive', 'client', 'boss',
        'ceo', 'president', 'executive', 'due today', 'today', 'immediate'
    ]

    medium_priority_keywords = [
        'normal', 'regular', 'standard', 'routine', 'usual', 'typical',
        'follow up', 'update', 'maintain', 'monitor'
    ]

    # Check for high priority indicators
    for keyword in high_priority_keywords:
        if keyword in task_lower:
            return 'high'

    # Check for medium priority indicators
    for keyword in medium_priority_keywords:
        if keyword in task_lower:
            return 'medium'

    # Default to low priority if no indicators found
    return 'medium'

def categorize_task_effort(task_description):
    """
    Categorize task effort level based on keywords in the description.

    Args:
        task_description: String describing the task

    Returns:
        Effort level: 'high_focus', 'medium_focus', or 'low_focus'
    """
    task_lower = task_description.lower()

    high_focus_keywords = [
        'think', 'analyze', 'solve', 'design', 'create', 'write', 'code',
        'research', 'plan', 'strategy', 'deep work', 'concentrate', 'focus'
    ]

    medium_focus_keywords = [
        'attend', 'meeting', 'discuss', 'collaborate', 'coordinate', 'organize'
    ]

    low_focus_keywords = [
        'email', 'reply', 'admin', 'schedule', 'sort', 'file', 'archive',
        'clean', 'organize', 'update', 'monitor', 'check'
    ]

    # Check for high focus indicators
    for keyword in high_focus_keywords:
        if keyword in task_lower:
            return 'high_focus'

    # Check for medium focus indicators
    for keyword in medium_focus_keywords:
        if keyword in task_lower:
            return 'medium_focus'

    # Default to low focus if no specific indicators found
    return 'low_focus'