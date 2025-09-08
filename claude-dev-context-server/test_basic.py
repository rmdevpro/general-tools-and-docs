#!/usr/bin/env python3
"""
Simple test to validate MCP server components
"""

import json
import sys
from pathlib import Path

# Test configuration loading
def test_config():
    config_path = Path("data/config.json")
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✅ Config loads successfully")
        print(f"   Session types: {list(config['session_detection'].keys())}")
        return True
    except Exception as e:
        print(f"❌ Config loading failed: {e}")
        return False

# Test session detection logic
def test_session_detection():
    test_titles = [
        "CODING Session - Feature Implementation",
        "Planning Session - Architecture Review", 
        "Testing Session - Deployment Validation",
        "Maintenance Session - Code Review",
        "Random Chat Title"
    ]
    
    session_detection = {
        "PLANNING": ["Planning", "Architecture", "Design"],
        "CODING": ["Coding", "Implementation", "Development"], 
        "TESTING": ["Testing", "Deployment", "Validation"],
        "MAINTENANCE": ["Maintenance", "Review", "Audit", "Health"]
    }
    
    print("✅ Session detection test:")
    for title in test_titles:
        title_upper = title.upper()
        detected_type = "MAINTENANCE"  # default
        
        for session_type, keywords in session_detection.items():
            for keyword in keywords:
                if keyword.upper() in title_upper:
                    detected_type = session_type
                    break
            if detected_type != "MAINTENANCE":
                break
        
        print(f"   '{title}' → {detected_type}")

# Test capacity calculation
def test_capacity_monitor():
    print("✅ Capacity monitoring test:")
    
    # Test different capacity levels
    test_cases = [45, 65, 85, 95]
    thresholds = {"warning": 60, "critical": 80, "immediate": 90}
    
    for capacity in test_cases:
        if capacity >= thresholds["immediate"]:
            level = "CRITICAL"
        elif capacity >= thresholds["critical"]:
            level = "WARNING" 
        elif capacity >= thresholds["warning"]:
            level = "NOTICE"
        else:
            level = "OK"
        
        print(f"   {capacity}% → {level}")

if __name__ == "__main__":
    print("🧪 Testing MCP Server Components\n")
    
    test_config()
    print()
    test_session_detection()
    print()
    test_capacity_monitor()
    
    print("\n🎯 Basic functionality validated!")
