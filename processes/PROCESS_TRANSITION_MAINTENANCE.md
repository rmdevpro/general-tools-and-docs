# PROCESS Transition Maintenance - Maintenance Session Handoff Procedures
*Ultra-Concise Bullet Point Steps*

## 🔧 **MAINTENANCE TRANSITION STEPS**

### **Files to Update:**
- **G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_MAINTENANCE.md** - **REQUIRED: MUST update** maintenance-specific findings and system health status
- **version.json** - **REQUIRED: MUST update** for any version changes from maintenance
- **working/maintenance_report.md** - **REQUIRED: MUST create** comprehensive maintenance findings report
- **docs/maintenance/** - **REQUIRED: MUST archive** detailed maintenance reports and metrics

### **Maintenance Documentation:**
- **Document review results** - **REQUIRED: MUST document** file cleanup and improvement tracking
- **Code review findings** - **REQUIRED: MUST document** technical debt and improvement recommendations
- **Process review outcomes** - **REQUIRED: MUST document** session framework optimization results
- **Health check reports** - **REQUIRED: MUST document** system performance and availability metrics
- **Vulnerability assessments** - **REQUIRED: MUST document** security findings and remediation status
- **Cost optimization results** - **REQUIRED: MUST document** spending analysis and savings achieved

### **Git Operations (Conditional):**
- **REQUIRED: MUST assess changes:** Check if git-relevant changes were made during session
- **Git-relevant changes include:**
  - Security fixes or vulnerability remediation
  - Performance improvements affecting code
  - Documentation restructuring or major updates
  - Process improvements affecting workflow files
  - System configuration changes
- **If meaningful changes made:**
  - **REQUIRED: MUST see** G:/projects/General Tools and Docs/processes/PROCESS_GIT_OPERATIONS.md for detailed git commands
  - **REQUIRED: MUST use commit message:** "Maintenance: [maintenance type] - [summary of findings/actions]"
  - **REQUIRED: MUST tag** significant improvements: `v[version]-maintenance` for major optimizations
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

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_MAINTENANCE.md
   (Last session type was MAINTENANCE)
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

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_MAINTENANCE.md
   (Last session type was MAINTENANCE)
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

7. ⚠️ **Required - Read:** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_MAINTENANCE.md
   (Last session type was MAINTENANCE)
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
```

### **Maintenance Metrics Tracking:**
- **System health scores** before and after maintenance
- **Technical debt reduction** measurements
- **Cost optimization** savings achieved
- **Security posture** improvements
- **Documentation quality** improvements
- **Process efficiency** gains

### **Follow-up Actions:**
- **Schedule next maintenance cycle** based on findings
- **Create action items** for high-priority issues discovered
- **Update monitoring and alerting** based on health check findings
- **Plan resource allocation** for addressing technical debt
- **Document lessons learned** for future maintenance cycles

---
*Maintenance Transition Process - Called by SESSION_MAINTENANCE_CONTEXT.md*