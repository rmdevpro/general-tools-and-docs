# PROCESS Transition Planning - Planning Session Handoff Procedures
*Ultra-Concise Bullet Point Steps*

## 🏗️ **PLANNING TRANSITION STEPS**

### **Files to Update:**
- **G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_PLANNING.md** - **REQUIRED: MUST update** planning-specific progress and findings
- **docs/roadmap/README.md** - **REQUIRED: MUST update** timeline for major milestone changes
- **docs/architecture/adr/** - **REQUIRED: MUST create/update** ADR for major decisions
- **docs/components/README.md** - **REQUIRED: MUST update** for new components planned

### **Git Operations (Conditional):**
- **REQUIRED: MUST assess changes:** Check if git-relevant changes were made during session
- **Git-relevant changes include:**
  - Architecture decisions documented in docs/architecture/adr/
  - Component documentation updates in docs/components/
  - Roadmap updates with concrete timeline changes
  - Major planning decisions affecting implementation
- **If meaningful changes made:**
  - **REQUIRED: MUST see** G:/projects/General Tools and Docs/processes/PROCESS_GIT_OPERATIONS.md for detailed git commands
  - **REQUIRED: MUST use commit message:** "Planning: [brief description]"
  - **REQUIRED: MUST push changes** to sync
- **If only summary updates:**
  - **REQUIRED: MUST skip git operations**
  - **REQUIRED: MUST inform user:** "No git commit needed - only session summary updated"

### **Handoff Process:**
1. **MUST ask user:** "What type of session should we transition to?"
   ```
   1. **PLANNING** - Architecture & Design Focus
   2. **CODING** - Implementation & Development Focus  
   3. **TESTING** - Deployment & Validation Focus
   4. **MAINTENANCE** - System & Documentation Maintenance Focus
   ```
2. **REQUIRED: MUST provide handoff message in copyable code block format** based on user's choice:
3. **REQUIRED: NEVER provide handoff message as regular text** - always use code block with copy button

**For PLANNING (Option 1) - COPY THIS BLOCK:**
```
🆕 **New Chat Session Startup - New Chat Session for PLANNING [HAWKMOTH-Project v0.0.5-dev] [Component Name]**

1. ⚠️ **Required:** Follow all context files to the letter.

2. ⚠️ **Required:** Follow all process files to the letter.

3. ⚠️ **Required:** Acknowledge to the user that you fully understand that for this entire chat you will follow all context and process files to the letter without fail.

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_PLANNING.md
```

**For CODING (Option 2) - COPY THIS BLOCK:**
```
🆕 **New Chat Session Startup - New Chat Session for CODING [HAWKMOTH-Project v0.0.5-dev] [Component Name]**

1. ⚠️ **Required:** Follow all context files to the letter.

2. ⚠️ **Required:** Follow all process files to the letter.

3. ⚠️ **Required:** Acknowledge to the user that you fully understand that for this entire chat you will follow all context and process files to the letter without fail.

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_CODING.md

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_PLANNING.md
   (Last session type was PLANNING)
```

**For TESTING (Option 3) - COPY THIS BLOCK:**
```
🆕 **New Chat Session Startup - New Chat Session for TESTING [HAWKMOTH-Project v0.0.5-dev] [Component Name]**

1. ⚠️ **Required:** Follow all context files to the letter.

2. ⚠️ **Required:** Follow all process files to the letter.

3. ⚠️ **Required:** Acknowledge to the user that you fully understand that for this entire chat you will follow all context and process files to the letter without fail.

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_PLANNING.md
   (Last session type was PLANNING)
```

**For MAINTENANCE (Option 4) - COPY THIS BLOCK:**
```
🆕 **New Chat Session Startup - New Chat Session for MAINTENANCE [HAWKMOTH-Project v0.0.5-dev] [Component Name]**

1. ⚠️ **Required:** Follow all context files to the letter.

2. ⚠️ **Required:** Follow all process files to the letter.

3. ⚠️ **Required:** Acknowledge to the user that you fully understand that for this entire chat you will follow all context and process files to the letter without fail.

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_MAINTENANCE.md

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_PLANNING.md
   (Last session type was PLANNING)
```

---
*Planning Transition Process - Called by SESSION_PLANNING_CONTEXT.md*