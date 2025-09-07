# General Tools and Docs
## Claude Development Framework - Session Contexts and Process Workflows

This repository contains the complete framework for Claude development sessions, including context files and detailed process workflows.

### 🏗️ Framework Structure

**📁 Context Files** (`context/`)
- `SESSION_STARTUP.md` - Core session initialization and routing
- `SESSION_PLANNING_CONTEXT.md` - Planning session context and procedures  
- `SESSION_CODING_CONTEXT.md` - Coding session context and procedures
- `SESSION_TESTING_CONTEXT.md` - Testing session context and procedures
- `SESSION_MAINTENANCE_CONTEXT.md` - Maintenance session context and procedures

**📁 Process Files** (`processes/`)
- **Core Processes:** Startup, transitions, git operations
- **Review Processes:** Document, code, process, health, vulnerability, cost, GitHub reviews
- **Session Summaries:** Planning, coding, testing, maintenance summaries
- **Specialized Processes:** Deployment, general discussion, maintenance coding

### 🔧 Framework Features

**✅ Session Auto-Detection:** Automatic session type detection from chat titles  
**✅ Context Loading:** Mandatory context file loading for session consistency  
**✅ Process Enforcement:** "REQUIRED: MUST" language for framework adherence  
**✅ Transition Management:** Structured handoff procedures between session types  
**✅ Git Integration:** Complete version control workflow procedures  

### 📋 Available Session Types

1. **🏗️ PLANNING** - Architecture, design, strategic planning
2. **⚡ CODING** - Implementation, development, feature building  
3. **🧪 TESTING** - Deployment, validation, quality assurance
4. **🔧 MAINTENANCE** - Reviews, audits, system health, technical debt

### 🎯 Framework Principles

- **Systematic Approach:** Structured workflows for consistent development
- **Mandatory Adherence:** Framework prevents deviation through enforced language
- **Process Bulletproofing:** Elimination of ambiguous directives
- **Context Consistency:** Guaranteed context loading and session alignment
- **Transition Reliability:** Structured handoff procedures between session types

### 🔄 Usage

This framework is automatically loaded in Claude development sessions through the session startup detection system. Context files are loaded based on chat title keywords, and appropriate process workflows are activated.

**Framework Status:** Production Ready ✅  
**Last Updated:** September 7, 2025  
**Total Files:** 25+ context and process files  
**Success Rate:** 100% when properly implemented  

---

**Repository created and maintained as part of Claude development infrastructure.**