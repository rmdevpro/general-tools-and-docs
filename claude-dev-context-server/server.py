#!/usr/bin/env python3
"""
Claude Development Framework MCP Server
Main server implementing 8 core MCP tools for session management
"""

import json
import asyncio
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from fastmcp import FastMCP
from context_loader import ContextLoader
from session_manager import SessionManager  
from rule_enforcer import RuleEnforcer
from capacity_monitor import CapacityMonitor

# Initialize MCP server
mcp = FastMCP("Claude Development Framework")

# Initialize components
server_path = Path(__file__).parent
context_loader = ContextLoader(server_path)
session_manager = SessionManager(server_path)
rule_enforcer = RuleEnforcer(server_path)
capacity_monitor = CapacityMonitor(server_path)

@mcp.tool()
def session_startup(chat_title: str) -> Dict:
    """
    Auto-detect session type and load appropriate context
    
    Args:
        chat_title: The title or description of the chat session
        
    Returns:
        Session information with loaded context and next steps
    """
    try:
        # Detect session type
        session_type = session_manager.detect_session_type(chat_title)
        
        # Load appropriate context
        context_data = context_loader.load_session_context(session_type)
        
        # Prepare context for session manager
        loaded_contexts = [
            {
                "file": context_data["context_content"][:100] + "...",  # Preview
                "content": context_data["context_content"]
            },
            {
                "file": context_data["startup_content"][:100] + "...",  # Preview  
                "content": context_data["startup_content"]
            }
        ]
        
        # Start session
        session_info = session_manager.start_session(chat_title, loaded_contexts)
        
        # Load rules into enforcer
        rule_enforcer.load_rules(session_manager.state["active_rules"])
        
        return {
            "session_type": session_type,
            "loaded_contexts": context_data["loaded_files"],
            "mandatory_rules": session_info["mandatory_rules"],
            "next_steps": session_info["next_steps"],
            "context_preview": context_data["context_content"][:500] + "..." if len(context_data["context_content"]) > 500 else context_data["context_content"]
        }
        
    except Exception as e:
        return {
            "error": f"Session startup failed: {str(e)}",
            "session_type": "MAINTENANCE",
            "loaded_contexts": [],
            "mandatory_rules": ["REQUIRED: MUST ask permission before any actions"],
            "next_steps": ["Resolve startup error", "Manual context loading"]
        }

@mcp.tool()
def get_session_context() -> Dict:
    """
    Return current session context and active rules
    
    Returns:
        Current session information and context
    """
    try:
        current_session = session_manager.get_current_session()
        
        return {
            "session_type": current_session["session_type"],
            "context_content": current_session["context_content"],
            "active_rules": current_session["active_rules"][:10],  # Top 10 rules
            "session_progress": current_session["session_progress"],
            "session_status": session_manager.state["current_session"]["status"],
            "capacity_used": session_manager.state["current_session"]["capacity_used"]
        }
        
    except Exception as e:
        return {
            "error": f"Failed to get session context: {str(e)}",
            "session_type": "unknown",
            "context_content": "Context unavailable",
            "active_rules": [],
            "session_progress": "error"
        }

@mcp.tool()
def get_active_processes(process_type: str) -> Dict:
    """
    Load specific process workflow files
    
    Args:
        process_type: Type of process (startup, transition, git, etc.)
        
    Returns:
        Process workflow steps and requirements
    """
    try:
        # Load process file
        process_data = context_loader.load_process_file(process_type)
        
        # Extract structured information from process content
        content = process_data["content"]
        lines = content.split('\n')
        
        # Extract process steps
        process_steps = []
        mandatory_actions = []
        conditional_actions = []
        
        current_section = None
        for line in lines:
            line = line.strip()
            
            if line.startswith('##') or line.startswith('#'):
                current_section = line.replace('#', '').strip()
                if current_section:
                    process_steps.append(current_section)
            
            elif line.startswith('REQUIRED:') or 'MUST' in line.upper():
                mandatory_actions.append(line)
            
            elif line.startswith('- IF ') or line.startswith('* IF '):
                conditional_actions.append(line[2:].strip())
        
        return {
            "process_file": process_data["process_file"],
            "process_steps": process_steps[:10],  # Top 10 steps
            "mandatory_actions": mandatory_actions[:5],  # Top 5 mandatory
            "conditional_actions": conditional_actions[:5],  # Top 5 conditional
            "content_preview": content[:800] + "..." if len(content) > 800 else content
        }
        
    except Exception as e:
        return {
            "error": f"Failed to load process: {str(e)}",
            "process_file": f"PROCESS_{process_type.upper()}.md",
            "process_steps": [],
            "mandatory_actions": ["REQUIRED: Manual process execution due to loading error"],
            "conditional_actions": []
        }

@mcp.tool()
def enforce_compliance(action: str, context: Optional[Dict] = None) -> Dict:
    """
    Validate planned actions against framework rules
    
    Args:
        action: Description of the action to validate
        context: Additional context (file paths, session info, etc.)
        
    Returns:
        Compliance validation results
    """
    try:
        if context is None:
            context = {}
        
        # Add current session context
        current_session = session_manager.get_current_session()
        context["session_type"] = current_session["session_type"]
        context["capacity"] = session_manager.state["current_session"]["capacity_used"]
        
        # Validate compliance
        compliance_result = rule_enforcer.enforce_compliance(action, context)
        
        return compliance_result
        
    except Exception as e:
        return {
            "compliant": False,
            "warnings": [f"Compliance check failed: {str(e)}"],
            "required_steps": ["Manual compliance verification required"],
            "blocked_actions": [action]
        }

@mcp.tool()
def monitor_capacity(current_usage: int) -> Dict:
    """
    Track chat capacity and provide alerts
    
    Args:
        current_usage: Current usage (percentage, character count, or message count)
        
    Returns:
        Capacity status and recommendations
    """
    try:
        # Monitor capacity
        capacity_result = capacity_monitor.monitor_capacity(current_usage)
        
        # Update session state with current capacity
        percentage = capacity_result["capacity_status"]
        session_manager.update_progress({"capacity_used": percentage})
        
        # Get transition recommendations if needed
        if capacity_result["transition_needed"]:
            current_session = session_manager.get_current_session()
            session_type = current_session["session_type"] or "MAINTENANCE"
            
            transition_rec = capacity_monitor.get_transition_recommendations(
                int(percentage.replace("%", "")), 
                session_type
            )
            capacity_result["transition_recommendations"] = transition_rec
        
        return capacity_result
        
    except Exception as e:
        return {
            "capacity_status": "unknown",
            "alert_level": "ERROR",
            "message": f"Capacity monitoring failed: {str(e)}",
            "recommended_action": "Manual capacity assessment required",
            "urgency": "high"
        }

@mcp.tool()
def update_session_state(updates: Dict) -> Dict:
    """
    Persist session progress and decisions
    
    Args:
        updates: Dictionary of state updates
        
    Returns:
        Updated session state
    """
    try:
        # Update session progress
        result = session_manager.update_progress(updates)
        
        # Log decision if provided
        if "decision" in updates:
            rationale = updates.get("rationale", "")
            session_manager.log_decision(updates["decision"], rationale)
        
        return result
        
    except Exception as e:
        return {
            "updated": False,
            "error": f"State update failed: {str(e)}",
            "current_state": session_manager.state["current_session"]
        }

@mcp.tool()
def get_transition_options(current_session: str) -> Dict:
    """
    Provide structured handoff procedures for session transitions
    
    Args:
        current_session: Current session type
        
    Returns:
        Available transition options and handoff procedures
    """
    try:
        # Load transition process file
        transition_data = context_loader.load_process_file(f"TRANSITION_{current_session}")
        
        # Generate handoff blocks for each session type
        session_types = ["PLANNING", "CODING", "TESTING", "MAINTENANCE"]
        handoff_blocks = {}
        
        for session_type in session_types:
            if session_type != current_session:
                handoff_blocks[session_type] = f"""🆕 **New Chat Session Startup - {session_type}**

Previous Session: {current_session} Session Complete
Current Session: New Chat Session for {session_type}

REQUIRED STARTUP STEPS:
1. Load Context: Read framework files for {session_type} context
2. Validate Setup: Confirm {session_type} environment ready
3. Review Handoff: Check previous session summary
4. Begin Work: Start {session_type} procedures

Chat Title: "{session_type} Session - [Your specific focus]"
"""
        
        return {
            "current_session": current_session,
            "transition_file": f"PROCESS_TRANSITION_{current_session}.md",
            "available_transitions": [t for t in session_types if t != current_session],
            "handoff_blocks": handoff_blocks,
            "transition_instructions": transition_data.get("content", "Manual transition required")[:500]
        }
        
    except Exception as e:
        # Provide basic transition options even if process file fails
        session_types = ["PLANNING", "CODING", "TESTING", "MAINTENANCE"]
        basic_handoff = {}
        
        for session_type in session_types:
            if session_type != current_session:
                basic_handoff[session_type] = f"🆕 **New {session_type} Session**\nTransition from {current_session} to {session_type}\nManual setup required due to process loading error."
        
        return {
            "current_session": current_session,
            "transition_file": "ERROR - Process file not found",
            "available_transitions": [t for t in session_types if t != current_session],
            "handoff_blocks": basic_handoff,
            "error": f"Transition process loading failed: {str(e)}"
        }

@mcp.tool()
def validate_file_operation(operation: str, file_path: str) -> Dict:
    """
    Ensure file operations follow framework rules
    
    Args:
        operation: Type of operation (create, read, write, delete)
        file_path: Target file path
        
    Returns:
        Validation results and applicable rules
    """
    try:
        # Validate file operation
        validation_result = rule_enforcer.validate_file_operation(operation, file_path)
        
        return validation_result
        
    except Exception as e:
        return {
            "allowed": False,
            "requires_permission": True,
            "file_category": "unknown",
            "rules_applied": [f"Validation failed: {str(e)}"],
            "error": "File operation validation encountered an error"
        }

# Health check endpoint
@mcp.tool()
def server_health() -> Dict:
    """
    Check server health and component status
    
    Returns:
        Server health information
    """
    try:
        health_status = {
            "server_status": "healthy",
            "components": {
                "context_loader": "operational",
                "session_manager": "operational", 
                "rule_enforcer": "operational",
                "capacity_monitor": "operational"
            },
            "active_session": session_manager.state["current_session"]["type"],
            "server_uptime": datetime.now().isoformat(),
            "config_loaded": True
        }
        
        # Test each component briefly
        try:
            context_loader.get_cached_files()
        except:
            health_status["components"]["context_loader"] = "error"
            
        try:
            session_manager.get_current_session()
        except:
            health_status["components"]["session_manager"] = "error"
        
        return health_status
        
    except Exception as e:
        return {
            "server_status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
