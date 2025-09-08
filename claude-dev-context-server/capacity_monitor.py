#!/usr/bin/env python3
"""
Capacity Monitor Module
Tracks chat capacity and provides transition alerts
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class CapacityMonitor:
    """Monitors chat capacity and provides proactive alerts"""
    
    def __init__(self, config_path: str):
        """Initialize with configuration"""
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.thresholds = self.config["capacity_thresholds"]
        
        # Capacity estimation parameters
        self.avg_chars_per_message = 500
        self.estimated_max_chars = 200000  # Rough estimate for Claude context
        
    def _load_config(self) -> Dict:
        """Load server configuration"""
        try:
            with open(self.config_path / "data" / "config.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Configuration file not found")
    
    def estimate_capacity_from_messages(self, message_count: int) -> int:
        """Estimate capacity percentage from message count"""
        estimated_chars = message_count * self.avg_chars_per_message
        percentage = min(100, int((estimated_chars / self.estimated_max_chars) * 100))
        return percentage
    
    def estimate_capacity_from_chars(self, total_chars: int) -> int:
        """Estimate capacity percentage from character count"""
        percentage = min(100, int((total_chars / self.estimated_max_chars) * 100))
        return percentage
    
    def monitor_capacity(self, current_usage: int) -> Dict:
        """
        Monitor capacity and return appropriate alerts
        Input can be percentage (0-100) or raw usage numbers
        """
        # Normalize input to percentage
        if current_usage > 100:
            # Assume it's character count or message count
            if current_usage > 1000:
                percentage = self.estimate_capacity_from_chars(current_usage)
            else:
                percentage = self.estimate_capacity_from_messages(current_usage)
        else:
            percentage = current_usage
        
        # Determine alert level
        alert_level = self._get_alert_level(percentage)
        
        # Generate appropriate message and recommendations
        alert_info = self._generate_alert_info(percentage, alert_level)
        
        return {
            "capacity_status": f"{percentage}%",
            "alert_level": alert_level,
            "message": alert_info["message"],
            "recommended_action": alert_info["action"],
            "urgency": alert_info["urgency"],
            "transition_needed": percentage >= self.thresholds["critical"]
        }
    
    def _get_alert_level(self, percentage: int) -> str:
        """Determine alert level based on percentage"""
        if percentage >= self.thresholds["immediate"]:
            return "CRITICAL"
        elif percentage >= self.thresholds["critical"]:
            return "WARNING"
        elif percentage >= self.thresholds["warning"]:
            return "NOTICE"
        else:
            return "OK"
    
    def _generate_alert_info(self, percentage: int, alert_level: str) -> Dict:
        """Generate alert message and recommendations"""
        if alert_level == "CRITICAL":
            return {
                "message": f"🚨 CRITICAL: Chat capacity at {percentage}% - IMMEDIATE transition required",
                "action": "Begin immediate handoff procedures - conversation may terminate soon",
                "urgency": "immediate"
            }
        
        elif alert_level == "WARNING":
            return {
                "message": f"⚠️ WARNING: Chat capacity at {percentage}% - Plan transition soon", 
                "action": "Begin preparing handoff procedures for next session",
                "urgency": "high"
            }
        
        elif alert_level == "NOTICE":
            return {
                "message": f"📊 NOTICE: Chat capacity at {percentage}% - Monitor usage",
                "action": "Start considering transition planning",
                "urgency": "medium"
            }
        
        else:
            return {
                "message": f"✅ OK: Chat capacity at {percentage}% - Continue normally",
                "action": "No action needed - continue with current session",
                "urgency": "low"
            }
    
    def get_transition_recommendations(self, current_percentage: int, session_type: str) -> Dict:
        """Get specific transition recommendations based on capacity and session type"""
        recommendations = {
            "should_transition": current_percentage >= self.thresholds["critical"],
            "time_remaining": self._estimate_time_remaining(current_percentage),
            "preferred_transition": self._get_preferred_transition(session_type),
            "handoff_priority": self._get_handoff_priority(current_percentage)
        }
        
        return recommendations
    
    def _estimate_time_remaining(self, current_percentage: int) -> str:
        """Estimate remaining conversation time"""
        remaining_percentage = 100 - current_percentage
        
        if remaining_percentage <= 5:
            return "Very limited - transition immediately"
        elif remaining_percentage <= 15:
            return "5-10 exchanges remaining"
        elif remaining_percentage <= 25:
            return "15-20 exchanges remaining"
        else:
            return "Sufficient capacity for continued work"
    
    def _get_preferred_transition(self, session_type: str) -> List[str]:
        """Get recommended next session types"""
        transitions = {
            "PLANNING": ["CODING", "TESTING"],
            "CODING": ["TESTING", "MAINTENANCE"], 
            "TESTING": ["MAINTENANCE", "PLANNING"],
            "MAINTENANCE": ["PLANNING", "CODING"]
        }
        
        return transitions.get(session_type, ["MAINTENANCE"])
    
    def _get_handoff_priority(self, percentage: int) -> str:
        """Determine handoff priority level"""
        if percentage >= self.thresholds["immediate"]:
            return "IMMEDIATE - Critical capacity reached"
        elif percentage >= self.thresholds["critical"]:
            return "HIGH - Begin handoff procedures"
        elif percentage >= self.thresholds["warning"]:
            return "MEDIUM - Start planning transition"
        else:
            return "LOW - No immediate action needed"
    
    def track_usage_trend(self, usage_history: List[int]) -> Dict:
        """Analyze usage trends to predict when transition will be needed"""
        if len(usage_history) < 3:
            return {"trend": "insufficient_data"}
        
        # Calculate trend (simple linear approximation)
        recent_usage = usage_history[-3:]
        trend = (recent_usage[-1] - recent_usage[0]) / len(recent_usage)
        
        # Predict when critical threshold will be reached
        current = usage_history[-1]
        if trend > 0:
            messages_to_critical = (self.thresholds["critical"] - current) / trend
            exchanges_to_critical = max(1, int(messages_to_critical))
        else:
            exchanges_to_critical = float('inf')
        
        return {
            "trend": "increasing" if trend > 0 else "stable" if trend == 0 else "decreasing",
            "trend_rate": round(trend, 2),
            "exchanges_to_critical": exchanges_to_critical if exchanges_to_critical != float('inf') else None,
            "recommendation": self._get_trend_recommendation(trend, current)
        }
    
    def _get_trend_recommendation(self, trend: float, current: int) -> str:
        """Get recommendation based on usage trend"""
        if trend > 2 and current > self.thresholds["warning"]:
            return "Rapid capacity increase - consider transitioning soon"
        elif trend > 1 and current > self.thresholds["warning"]:
            return "Steady capacity increase - monitor closely"
        elif current > self.thresholds["critical"]:
            return "High capacity regardless of trend - prepare for transition"
        else:
            return "Normal usage pattern - continue monitoring"
