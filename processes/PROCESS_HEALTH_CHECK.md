# PROCESS Health Check - Deployed System Monitoring & Performance Review
*Step-by-Step System Health Assessment Procedures*
*Updated: September 7, 2025*

## 🏥 **HEALTH CHECK WORKFLOW**

### **STEP 1: Deployment Inventory & Status**
1. **REQUIRED: MUST identify deployed systems:**
   - HuggingFace Spaces (active deployments)
   - Component 99 (hawkmoth-99-secrets)
   - Future HAWKMOTH components (SPHINX, 17, HYMIE, GRACE-v2)
   - Development/staging deployments
2. **REQUIRED: MUST verify deployment status:**
   - Service availability and uptime
   - Current version deployed
   - Configuration status
   - Resource allocation and usage
3. **REQUIRED: MUST check access and authentication:**
   - API endpoint accessibility
   - Authentication mechanism status
   - JWT token validation
   - Service-to-service communication

### **STEP 2: Functional Health Assessment**
1. **REQUIRED: MUST perform core functionality testing:**
   - All API endpoints responding
   - Expected response formats
   - Error handling behavior
   - Data validation working
2. **REQUIRED: MUST perform integration testing:**
   - Component-to-component communication
   - External service dependencies
   - Database connectivity (if applicable)
   - File system access
3. **REQUIRED: MUST perform performance baseline testing:**
   - Response time measurements
   - Throughput capacity
   - Resource consumption patterns
   - Concurrent user handling

### **STEP 3: System Resource Analysis**
1. **REQUIRED: MUST analyze resource utilization:**
   - CPU usage patterns
   - Memory consumption
   - Storage usage and growth
   - Network bandwidth utilization
2. **REQUIRED: MUST perform capacity planning:**
   - Current vs allocated resources
   - Growth trends and projections
   - Bottleneck identification
   - Scaling requirements
3. **REQUIRED: MUST analyze reliability metrics:**
   - Error rate analysis
   - Uptime/downtime tracking
   - Recovery time measurement
   - Failure pattern analysis

### **STEP 4: Health Classification**
**Categories for each deployed system:**
- **🟢 HEALTHY** - All systems operational, good performance
- **🟡 WARNING** - Minor issues, monitoring required
- **🟠 DEGRADED** - Performance issues, intervention needed
- **🔴 CRITICAL** - Major problems, immediate action required
- **⚫ DOWN** - System unavailable, emergency response

### **STEP 5: Issue Remediation & Optimization**
1. **REQUIRED: MUST handle healthy systems:**
   - Performance optimization opportunities
   - Preventive maintenance tasks
   - Monitoring enhancement
2. **REQUIRED: MUST handle warning systems:**
   - Address minor configuration issues
   - Optimize resource allocation
   - Improve monitoring thresholds
3. **REQUIRED: MUST handle degraded systems:**
   - Performance tuning and optimization
   - Resource scaling decisions
   - Code or configuration fixes
4. **REQUIRED: MUST handle critical/Down systems:**
   - Emergency response procedures
   - Immediate issue resolution
   - Recovery and restoration
   - Post-incident analysis

## 🔍 **HEALTH CHECK PROCEDURES**

### **Automated Health Checks:**
1. **API endpoint testing:**
   ```bash
   # Health endpoint testing
   curl -X GET https://[deployment-url]/health
   curl -X GET https://[deployment-url]/api/v1/status
   ```
2. **Authentication testing:**
   ```bash
   # JWT token validation
   curl -X POST https://[deployment-url]/auth/validate
   ```
3. **Performance testing:**
   ```bash
   # Response time measurement
   time curl -X GET https://[deployment-url]/api/v1/endpoint
   ```

### **Manual Verification Steps:**
1. **User interface testing (if applicable)**
2. **Complex workflow validation**
3. **Data integrity verification**
4. **Configuration validation**

### **Performance Benchmarking:**
1. **Baseline metrics establishment**
2. **Performance regression detection**
3. **Load testing results**
4. **Comparative analysis with previous checks**

## 📊 **HEALTH MONITORING METRICS**

### **System Availability:**
- Uptime percentage
- Response time averages
- Error rate trends
- Service availability SLA compliance

### **Performance Metrics:**
- Average response time
- 95th percentile response time
- Requests per second capacity
- Concurrent user handling

### **Resource Utilization:**
- CPU usage percentage
- Memory utilization
- Storage consumption
- Network I/O rates

### **Error Analysis:**
- Error frequency and types
- Error recovery success rate
- User impact assessment
- Trend analysis

## 🚨 **HEALTH ALERTING THRESHOLDS**

### **Warning Levels:**
- Response time > 2 seconds
- Error rate > 1%
- CPU usage > 70%
- Memory usage > 80%

### **Critical Levels:**
- Response time > 5 seconds
- Error rate > 5%
- CPU usage > 90%
- Memory usage > 95%
- Any service unavailability

## 📋 **HEALTH CHECK REPORTING**

### **Health Check Summary:**
```
🏥 **SYSTEM HEALTH CHECK COMPLETE**
📅 **Check Date:** [timestamp]
🎯 **Scope:** [systems checked]

📊 **System Status:**
   🟢 Healthy: [count] systems
   🟡 Warning: [count] systems
   🟠 Degraded: [count] systems
   🔴 Critical: [count] systems
   ⚫ Down: [count] systems

📈 **Performance Summary:**
   ⏱️ Avg Response Time: [ms]
   📊 Error Rate: [%]
   💾 Resource Usage: CPU [%], Memory [%]
   ⏳ Uptime: [%]

🔧 **Actions Taken:**
   - [immediate fixes applied]
   - [optimization changes made]
   - [monitoring improvements]

⚠️ **Issues Requiring Attention:**
   - [critical issues needing follow-up]
   - [performance optimization opportunities]
   - [capacity planning recommendations]

🎯 **Next Check:** [scheduled date/trigger]
```

### **Detailed System Reports:**
- Individual system health scores
- Performance trend analysis
- Resource utilization graphs
- Comparative performance data

---
*Health Check Process - Called by SESSION_MAINTENANCE_CONTEXT.md*