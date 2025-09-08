# PROCESS Transition Testing - Testing Session Handoff Procedures
*Ultra-Concise Bullet Point Steps*

## 🧪 **TESTING TRANSITION STEPS**

### **Files to Update:**
- **G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md** - **REQUIRED: MUST update** testing-specific progress and deployment status
- **version.json** - **REQUIRED: MUST confirm** version reflects deployment
- **working/test_results.md** - **REQUIRED: MUST document** issues found during testing

### **Deployment Process:**
- **For deployments:** **REQUIRED: MUST read** `G:/projects/General Tools and Docs/processes/PROCESS_DEPLOYMENT.md` for complete deployment workflow
- **Always check:** **REQUIRED: MUST check** DEPLOYMENT_STEPS.md in deployment folder for special instructions

### **Git Operations (Conditional):**
- **REQUIRED: MUST assess changes:** Check if git-relevant changes were made during session
- **Git-relevant changes include:**
  - Successful production deployments
  - Version confirmations in version.json
  - Test results affecting code or deployment files
  - Deployment status changes or validation outcomes
- **If meaningful changes made:**
  - **REQUIRED: MUST see** G:/projects/General Tools and Docs/processes/PROCESS_GIT_OPERATIONS.md for detailed git commands
  - **REQUIRED: MUST use commit message:** "Testing: [version] deployment - [status]"
  - **REQUIRED: MUST tag release** for successful deployments (v0.0.4a, v0.0.5, etc.)
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

3. ⚠️ **Required:** State to the user that you fully understand that for this entire chat you will:
   - Follow all context and process files to the letter without fail
   - Your judgment is INFERIOR to the documentation
   - When your judgment conflicts with documentation, the documentation is ALWAYS correct
   - When you feel the urge to "prioritize" or "be helpful" instead of following documentation exactly, the documentation takes precedence

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_PLANNING.md

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md
   (Last session type was TESTING)
```

**For CODING (Option 2) - COPY THIS BLOCK:**
```
🆕 **New Chat Session Startup - New Chat Session for CODING [HAWKMOTH-Project v0.0.5-dev] [Component Name]**

1. ⚠️ **Required:** Follow all context files to the letter.

2. ⚠️ **Required:** Follow all process files to the letter.

3. ⚠️ **Required:** State to the user that you fully understand that for this entire chat you will:
   - Follow all context and process files to the letter without fail
   - Your judgment is INFERIOR to the documentation
   - When your judgment conflicts with documentation, the documentation is ALWAYS correct
   - When you feel the urge to "prioritize" or "be helpful" instead of following documentation exactly, the documentation takes precedence

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_CODING.md

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md
   (Last session type was TESTING)
```

**For TESTING (Option 3) - COPY THIS BLOCK:**
```
🆕 **New Chat Session Startup - New Chat Session for TESTING [HAWKMOTH-Project v0.0.5-dev] [Component Name]**

1. ⚠️ **Required:** Follow all context files to the letter.

2. ⚠️ **Required:** Follow all process files to the letter.

3. ⚠️ **Required:** State to the user that you fully understand that for this entire chat you will:
   - Follow all context and process files to the letter without fail
   - Your judgment is INFERIOR to the documentation
   - When your judgment conflicts with documentation, the documentation is ALWAYS correct
   - When you feel the urge to "prioritize" or "be helpful" instead of following documentation exactly, the documentation takes precedence

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md
```

**For MAINTENANCE (Option 4) - COPY THIS BLOCK:**
```
🆕 **New Chat Session Startup - New Chat Session for MAINTENANCE [HAWKMOTH-Project v0.0.5-dev] [Component Name]**

1. ⚠️ **Required:** Follow all context files to the letter.

2. ⚠️ **Required:** Follow all process files to the letter.

3. ⚠️ **Required:** State to the user that you fully understand that for this entire chat you will:
   - Follow all context and process files to the letter without fail
   - Your judgment is INFERIOR to the documentation
   - When your judgment conflicts with documentation, the documentation is ALWAYS correct
   - When you feel the urge to "prioritize" or "be helpful" instead of following documentation exactly, the documentation takes precedence

4. ⚠️ **Required:** Ask the user for permission to proceed to step 5.

5. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/context/SESSION_STARTUP.md

6. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_MAINTENANCE.md

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md
   (Last session type was TESTING)
```

---
*Testing Transition Process - Called by SESSION_TESTING_CONTEXT.md*