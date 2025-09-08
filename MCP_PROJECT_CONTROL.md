# MCP PROJECT CONTROL DOCUMENT
*Master Control File for Claude MCP Context Automation Server Project*
*Current Status: Phase 1 Complete → Phase 2 Ready*
*Updated: September 8, 2025*

## 🔥 **CRITICAL SESSION STARTUP INSTRUCTIONS**

### **For ANY new chat session working on this project:**

1. **REQUIRED:** Read this entire control document first
2. **REQUIRED:** Check current project status (see below)
3. **REQUIRED:** Execute current phase instructions exactly
4. **REQUIRED:** Update status when phase complete
5. **REQUIRED:** Create transition artifacts for next session

---

## 📊 **CURRENT PROJECT STATUS**

### **✅ COMPLETED PHASES:**
- **Phase 1: Analysis & Design** ✅ COMPLETE (September 8, 2025)

### **🎯 CURRENT PHASE:**
- **Phase 2: Core MCP Server Development** 🔄 READY TO START

### **📋 PENDING PHASES:**
- Phase 3: Framework Integration (NOT STARTED)
- Phase 4: Testing & Refinement (NOT STARTED)  
- Phase 5: Production Deployment (NOT STARTED)

---

## 🎯 **PHASE 2 INSTRUCTIONS** (Current Session)

### **OBJECTIVE:** Build working MCP server with core functionality

### **REQUIRED DELIVERABLES:**
1. **server.py** - Main MCP server implementation
2. **session_manager.py** - Session detection logic
3. **context_loader.py** - File loading functionality
4. **requirements.txt** - Dependencies list
5. **config.json** - Server configuration
6. **Working MCP server** that connects to Claude Desktop

### **STEP-BY-STEP EXECUTION:**

#### **Step 1: Environment Setup**
- [ ] Create directory: `G:/projects/General Tools and Docs/claude-dev-context-server/`
- [ ] Install dependencies: `pip install fastmcp watchdog`
- [ ] Validate MCP SDK availability

#### **Step 2: Core Server Implementation**
- [ ] Implement `server.py` with 8 core MCP tools (see MCP_ARCHITECTURE.md)
- [ ] Implement `session_manager.py` for session detection
- [ ] Implement `context_loader.py` for file operations
- [ ] Create `requirements.txt` and `config.json`

#### **Step 3: Basic Integration Test**
- [ ] Test MCP server startup
- [ ] Validate tool availability
- [ ] Test session detection with sample chat titles
- [ ] Verify file loading from context directory

#### **Step 4: Claude Desktop Connection**
- [ ] Configure Claude Desktop MCP settings
- [ ] Test tool accessibility from Claude
- [ ] Validate basic functionality

### **SUCCESS CRITERIA FOR PHASE 2:**
- [ ] MCP server starts without errors
- [ ] All 8 tools respond correctly
- [ ] Session detection works for all 4 types
- [ ] Context files load successfully
- [ ] Claude Desktop integration functional

### **WHEN PHASE 2 COMPLETE:**
1. Update this document: Change status to "Phase 2 Complete → Phase 3 Ready"
2. Create transition summary
3. Commit changes to git repository

---

## 📁 **PROJECT FILE INVENTORY**

### **Control Documents:**
- **`MCP_PROJECT_CONTROL.md`** ← THIS FILE (Master control)
- **`MCP_PROJECT_PLAN.md`** - Complete project plan
- **`MCP_ARCHITECTURE.md`** - Technical specifications
- **`PHASE_1_COMPLETE.md`** - Phase 1 summary

### **Framework Files (DO NOT MODIFY):**
- **`context/`** - Session context files (4 files)
- **`processes/`** - Process workflow files (20+ files)
- **`README.md`** - Framework overview

### **Phase 2 Target Directory:**
```
claude-dev-context-server/
├── server.py                 # Main MCP server
├── session_manager.py        # Session detection
├── context_loader.py         # File loading
├── data/
│   ├── session_state.json    # Runtime state
│   └── config.json           # Configuration
├── requirements.txt          # Dependencies
└── README.md                 # Setup instructions
```

---

## 🔧 **TECHNICAL REFERENCE**

### **MCP Tools to Implement (Phase 2):**
1. `session_startup(chat_title)` - Auto-detect session type
2. `get_session_context()` - Return current context
3. `get_active_processes(type)` - Load process files
4. `enforce_compliance(action)` - Validate against rules
5. `monitor_capacity(usage)` - Track chat capacity
6. `update_session_state(updates)` - Persist progress
7. `get_transition_options(session)` - Handoff procedures
8. `validate_file_operation(op, file)` - Check file rules

### **Dependencies:**
- `fastmcp` - MCP server framework
- `watchdog` - File monitoring
- `pathlib` - File operations
- `json` - Data persistence

### **Configuration Values:**
- **Context Directory:** `G:/projects/General Tools and Docs`
- **Session Keywords:** PLANNING, CODING, TESTING, MAINTENANCE
- **Capacity Thresholds:** 60%, 80%, 90%

---

## 🔄 **SESSION TRANSITION PROCEDURES**

### **When Current Phase Complete:**

#### **Step 1: Update Status**
Edit this file (`MCP_PROJECT_CONTROL.md`):
- Move current phase to "COMPLETED PHASES"
- Update "CURRENT PHASE" to next phase
- Update "Updated" timestamp

#### **Step 2: Create Transition Summary**
Create file: `PHASE_[N]_COMPLETE.md` with:
- Deliverables completed
- Success criteria met
- Issues encountered
- Next phase readiness

#### **Step 3: Git Operations**
```bash
git add .
git commit -m "Phase [N] Complete: [brief description]"
git push
```

#### **Step 4: Next Session Handoff**
Provide this message to user:
```
🆕 **MCP Project - Phase [N+1] Ready**

Hand this to next chat session:
Path: G:/projects/General Tools and Docs/MCP_PROJECT_CONTROL.md

Instructions: Read control document and execute current phase instructions.
```

---

## 📋 **QUICK REFERENCE**

### **Emergency Recovery:**
If session gets confused or off-track:
1. Read `MCP_PROJECT_CONTROL.md` (this file)
2. Check current project status
3. Follow current phase instructions exactly
4. Do not deviate from documented procedures

### **Critical File Paths:**
- **Project Root:** `G:/projects/General Tools and Docs/`
- **Control Document:** `G:/projects/General Tools and Docs/MCP_PROJECT_CONTROL.md`
- **Architecture Spec:** `G:/projects/General Tools and Docs/MCP_ARCHITECTURE.md`
- **Target Server Dir:** `G:/projects/General Tools and Docs/claude-dev-context-server/`

### **Success Validation:**
Each phase has clear success criteria. Do not proceed to next phase until all criteria are met and documented.

---

## 🎯 **CURRENT ACTION REQUIRED**

**FOR THIS SESSION:** Execute Phase 2 instructions above  
**DELIVERABLE:** Working MCP server with Claude Desktop integration  
**SUCCESS CRITERIA:** All 8 tools functional and tested  
**NEXT SESSION:** Phase 3 - Framework Integration  

---

**Control Document Status:** ✅ ACTIVE  
**Last Updated:** September 8, 2025  
**Project Phase:** 2 of 5 (Core Development)  
**Estimated Completion:** 3-4 more sessions
