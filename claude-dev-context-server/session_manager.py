#!/usr/bin/env python3
"""
Session Manager Module
Handles session detection, state management, and type classification
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class SessionManager:
    """Manages session detection and state persistence"""
    
    def __init__(self, config_path: str):
        """Initialize with configuration"""
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.state_file = self.config_path.parent / "data" / "session_state.json"
        self.state = self._load_state()
    
    def _load_config(self) -> Dict:
        """Load server configuration"""
        try:
            with open(self.config_path / "data" / "config.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Configuration file not found")
    
    def _load_state(self) -> Dict:
        """Load current session state"""
        try:
            with open(self.state_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._get_default_state()
    
    def _get_default_state(self) -> Dict:
        """Get default session state"""
        return {
            "current_session": {
                "type": None,
                "start_time": None,
                "chat_title": None,
                "capacity_used": "0%",
                "status": "inactive"
            },
            "loaded_contexts": [],
            "active_rules": [],
            "session_progress": {
                "completed_steps": [],
                "current_step": None,
                "next_actions": []
            },
            "decisions_log": []
        }
    
    def _save_state(self):
        """Persist session state"""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def detect_session_type(self, chat_title: str) -> str:
        """
        Detect session type from chat title
        Returns: session type (PLANNING, CODING, TESTING, MAINTENANCE)
        """
        title_upper = chat_title.upper()
        
        # Check each session type for keyword matches
        for session_type, keywords in self.config["session_detection"].items():
            for keyword in keywords:
                if keyword.upper() in title_upper:
                    return session_type
        
        # Default to MAINTENANCE if no keywords found
        return "MAINTENANCE"
    
    def extract_rules_from_content(self, content: str) -> List[str]:
        """Extract REQUIRED rules from context content"""
        rules = []
        
        # Look for lines starting with "REQUIRED:" or containing "MUST"
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('REQUIRED:') or 'MUST' in line.upper():
                rules.append(line)
            elif line.startswith('- REQUIRED:') or line.startswith('* REQUIRED:'):
                rules.append(line[2:].strip())  # Remove bullet point
        
        return rules
    
    def start_session(self, chat_title: str, loaded_contexts: List[Dict]) -> Dict:
        """
        Initialize new session
        Returns session startup information
        """
        session_type = self.detect_session_type(chat_title)
        
        # Extract rules from loaded contexts
        active_rules = []
        for context in loaded_contexts:
            if "content" in context:
                rules = self.extract_rules_from_content(context["content"])
                active_rules.extend(rules)
        
        # Update session state
        self.state["current_session"] = {
            "type": session_type,
            "start_time": datetime.now().isoformat(),
            "chat_title": chat_title,
            "capacity_used": "0%",
            "status": "active"
        }
        
        self.state["loaded_contexts"] = loaded_contexts
        self.state["active_rules"] = active_rules
        self.state["session_progress"] = {
            "completed_steps": ["startup"],
            "current_step": "context_loaded",
            "next_actions": ["Load working directory", "Check capacity"]
        }
        
        # Log session start
        self.log_decision(f"Session started: {session_type}", f"Auto-detected from title: {chat_title}")
        
        self._save_state()
        
        return {
            "session_type": session_type,
            "loaded_contexts": [ctx.get("file", "unknown") for ctx in loaded_contexts],
            "mandatory_rules": active_rules[:5],  # Top 5 most important
            "next_steps": self.state["session_progress"]["next_actions"]
        }
    
    def get_current_session(self) -> Dict:
        """Get current session information"""
        return {
            "session_type": self.state["current_session"]["type"],
            "context_content": self._get_context_summary(),
            "active_rules": self.state["active_rules"],
            "session_progress": self.state["session_progress"]["current_step"]
        }
    
    def _get_context_summary(self) -> str:
        """Generate context summary from loaded contexts"""
        if not self.state["loaded_contexts"]:
            return "No context loaded"
        
        summary = []
        for context in self.state["loaded_contexts"]:
            if "file" in context:
                summary.append(f"Loaded: {context['file']}")
        
        return "; ".join(summary)
    
    def update_progress(self, updates: Dict) -> Dict:
        """Update session progress"""
        current_state = self.state["session_progress"]
        
        if "completed_steps" in updates:
            completed = updates["completed_steps"]
            if isinstance(completed, str):
                completed = [completed]
            current_state["completed_steps"].extend(completed)
        
        if "current_step" in updates:
            current_state["current_step"] = updates["current_step"]
        
        if "next_actions" in updates:
            current_state["next_actions"] = updates["next_actions"]
        
        # Update capacity if provided
        if "capacity_used" in updates:
            self.state["current_session"]["capacity_used"] = updates["capacity_used"]
        
        self._save_state()
        
        return {
            "updated": True,
            "current_state": self.state["current_session"],
            "progress": current_state
        }
    
    def log_decision(self, decision: str, rationale: str = ""):
        """Log important decisions"""
        self.state["decisions_log"].append({
            "timestamp": datetime.now().isoformat(),
            "decision": decision,
            "rationale": rationale
        })
        self._save_state()
    
    def end_session(self) -> Dict:
        """End current session and prepare for transition"""
        if self.state["current_session"]["status"] == "inactive":
            return {"message": "No active session to end"}
        
        # Mark session as complete
        self.state["current_session"]["status"] = "completed"
        self.state["session_progress"]["current_step"] = "session_complete"
        
        self.log_decision("Session ended", "Transition procedures initiated")
        self._save_state()
        
        return {
            "session_ended": True,
            "session_type": self.state["current_session"]["type"],
            "duration": self._calculate_session_duration(),
            "decisions_made": len(self.state["decisions_log"])
        }
    
    def _calculate_session_duration(self) -> str:
        """Calculate session duration"""
        if not self.state["current_session"]["start_time"]:
            return "Unknown"
        
        start = datetime.fromisoformat(self.state["current_session"]["start_time"])
        duration = datetime.now() - start
        
        hours = duration.total_seconds() // 3600
        minutes = (duration.total_seconds() % 3600) // 60
        
        if hours > 0:
            return f"{int(hours)}h {int(minutes)}m"
        else:
            return f"{int(minutes)}m"
