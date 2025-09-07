# PROCESS GitHub Check - Repository Health & Alignment Verification
*Step-by-Step GitHub Repository Maintenance Procedures*
*Updated: September 7, 2025*

## 📋 **GITHUB HEALTH CHECK WORKFLOW**

### **STEP 1: Repository State Assessment**
1. **REQUIRED: MUST check repository integrity:**
   - Git history consistency and completeness
   - Branch structure and alignment (main, development branches)
   - Remote vs local synchronization status
   - Repository size and performance metrics
2. **REQUIRED: MUST verify content alignment:**
   - Local project state vs GitHub repository contents
   - Missing or extra files in repository
   - .gitignore effectiveness (no unwanted files tracked)
   - Large file identification and LFS usage assessment
3. **REQUIRED: MUST review repository metadata:**
   - Repository description accuracy
   - Topic tags relevance and completeness
   - README.md visibility and current status
   - License file presence and accuracy

### **STEP 2: Commit & Branch Health Analysis**
1. **REQUIRED: MUST analyze commit history quality:**
   - Commit message clarity and conventions
   - Commit size appropriateness (atomic changes)
   - Author information consistency
   - Frequency and timing patterns
2. **REQUIRED: MUST review branch management:**
   - Active branch count and purpose
   - Stale branch identification
   - Merge conflict resolution status
   - Protected branch settings verification
3. **REQUIRED: MUST analyze repository activity:**
   - Recent activity patterns
   - Collaboration patterns (if applicable)
   - Issue tracking alignment with development
   - Pull request status and quality

### **STEP 3: Security & Access Review**
1. **REQUIRED: MUST review security posture:**
   - SSH key functionality and security
   - Access permissions appropriateness
   - Secret scanning results
   - Vulnerability alerts status
2. **REQUIRED: MUST review repository settings:**
   - Visibility settings alignment with project needs
   - Collaboration settings (if applicable)
   - Security features enabled (dependabot, etc.)
   - Backup and disaster recovery considerations

### **STEP 4: Alignment Verification**
1. **REQUIRED: MUST verify project-repository alignment:**
   - Local development state vs repository state
   - Version numbers and tagging consistency
   - Documentation accuracy in repository
   - Deployment readiness verification
2. **REQUIRED: MUST verify development workflow alignment:**
   - WOW process adherence in repository practices
   - Consistent development patterns
   - Integration with development tools
   - Automated workflow functionality (if applicable)

### **STEP 5: Repository Optimization**
1. **REQUIRED: MUST perform performance optimization:**
   - Repository size optimization
   - Large file management
   - Git garbage collection if needed
   - Archive old branches if appropriate
2. **REQUIRED: MUST make organization improvements:**
   - File structure optimization
   - Documentation organization
   - Tag and release management
   - Repository description and metadata updates

## 🔍 **GITHUB CHECK CHECKLIST**

### **Repository Health:**
- [ ] Git history is clean and consistent
- [ ] All branches are purposeful and current
- [ ] Local and remote repositories are synchronized
- [ ] .gitignore is properly configured
- [ ] No large or inappropriate files tracked
- [ ] Repository size is reasonable and optimized

### **Security & Access:**
- [ ] SSH authentication working properly
- [ ] Repository visibility settings appropriate
- [ ] No secrets or sensitive data in repository
- [ ] Security features enabled and configured
- [ ] Access permissions are appropriate

### **Project Alignment:**
- [ ] Repository accurately reflects project state
- [ ] Documentation is current and accurate
- [ ] Version tagging is consistent
- [ ] Development workflow is followed
- [ ] Repository supports project goals effectively

### **Metadata & Organization:**
- [ ] Repository description is accurate
- [ ] Topic tags are relevant and complete
- [ ] README.md is visible and current
- [ ] File organization is logical and clean
- [ ] License and legal files are appropriate

## 📊 **GITHUB CHECK REPORTING**

### **Repository Health Summary:**
```
📋 **GITHUB CHECK COMPLETE**
🔗 **Repository:** [repository URL]
📊 **Health Score:** [Excellent/Good/Fair/Poor]
📈 **Key Metrics:**
   📁 Repository Size: [size]
   🌿 Active Branches: [count]
   📝 Recent Commits: [count in last 30 days]
   🔒 Security Status: [status]
   ⚡ Sync Status: [up to date/behind/ahead]

🔧 **Actions Taken:**
   - [list optimization actions]
   - [list security improvements]
   - [list organization improvements]
   - [list synchronization actions]

⚠️ **Issues Found:**
   - [list critical repository issues]
   - [recommended follow-up actions]
   
🎯 **Recommendations:**
   - [repository optimization suggestions]
   - [security enhancement recommendations]
   - [workflow improvement suggestions]
```

### **Repository Alignment Status:**
```
✅ **ALIGNED ITEMS:**
   - [list items where repository matches project state]
   
⚠️ **MISALIGNMENT ITEMS:**
   - [list items needing synchronization]
   - [recommended alignment actions]
```

---
*GitHub Check Process - Called by SESSION_MAINTENANCE_CONTEXT.md*