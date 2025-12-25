#!/usr/bin/env python3
"""
Standup Bullshit Generator - Because sounding productive is half the battle.
"""

import random
import sys

def generate_yesterday():
    """What I allegedly did yesterday"""
    actions = [
        "investigated", "researched", "explored", "analyzed", "prototyped",
        "refactored", "optimized", "debugged", "documented", "reviewed"
    ]
    
    subjects = [
        "the performance bottleneck", "the caching layer", "the API integration",
        "the deployment pipeline", "the database schema", "the legacy code",
        "the edge cases", "the third-party dependency", "the race condition",
        "the configuration management"
    ]
    
    return f"{random.choice(actions)} {random.choice(subjects)}"

def generate_today():
    """What I'll pretend to do today"""
    plans = [
        "continue investigating", "finalize the approach", "implement the solution",
        "write tests for", "deploy the fix for", "collaborate on", "document",
        "optimize", "monitor", "validate"
    ]
    
    targets = [
        "the remaining issues", "the performance improvements", "the integration",
        "the refactoring", "the feature", "the bug fixes", "the documentation",
        "the deployment", "the testing suite", "the code review"
    ]
    
    return f"{random.choice(plans)} {random.choice(targets)}"

def generate_blocker():
    """Why I'm not actually blocked (but sound like I am)"""
    blockers = [
        "Waiting on clarification from the PM",
        "Need to sync with the design team",
        "Dependencies are still being resolved",
        "Investigating an unexpected behavior",
        "Aligning with other teams on approach",
        "No blockers, just being thorough",
        "Considering multiple implementation strategies",
        "Awaiting environment access",
        "Reviewing security implications",
        "No blockers - everything's going smoothly!"
    ]
    
    return random.choice(blockers)

def main():
    """Generate your daily dose of productivity theater"""
    print("\n=== STANDUP BULLSHIT GENERATOR ===\n")
    print(f"Yesterday: {generate_yesterday()}")
    print(f"Today: {generate_today()}")
    print(f"Blockers: {generate_blocker()}")
    print("\nRemember: It's not lying, it's agile!\n")

if __name__ == "__main__":
    main()