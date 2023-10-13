*Postmortem*

Start: 11/10/2023, 12:00 noon and 16:30 pm EAT, Duration 4 hours.

*IMPACT*
The outage affected our primary customer-facing web application,
resulting in a 70% decrease in user accessibility and functionality
during the incident. 

*Root Cause:*
1. The root cause of the outage was identifeied as a misconfigured
load balancer, which caused an overload on one of the application
servers, leading to cascade of failures. 
2. There was a bug in our Nginx server configuration. The bug caused
Nginx to crash when it recieved a certain type of HTTP request.


*Timeline*
12:00 noon: Issue detected through a monitoring alert indicating unusually high server load.
12:15 PM: Engineers began investigating the issue, suspecting a potential DDoS attack.
13:00 PM: Misleading path: Focus shifted towards network security, conducting an in-depth analysis of incoming traffic patterns.
14:00 PM: Escalated incident to the on-call DevOps and Networking teams for further assistance.
14:30 PM: Misleading path: Database performance was investigated due  to high traffic suspicions.
15:00 PM: Root cause identified: Misconfigured load balancer causing server overload.
15:30 PM: Load balancer settings were adjusted to distribute traffic evenly among application servers. The engineers deployed a fix for the bug in the Nginx server configuration. This fix prevented Nginx from crashing when it received the type of HTTP request that had caused the outage.
16:00 PM: Service gradually restored as servers stabilized. website comes back online.
16:30 PM: Normal service functionality resumed. Outage resolved. 

*Root Cause and Resolution*

1. The root cause of the outage was a bug in the Nginx server configuration. The bug caused Nginx to crash when it received a certain type of HTTP request. The issue was fixed by deploying a patch to the Nginx server configuration. The patch prevented Nginx from crashing when it received the type of HTTP request that had caused the outage.

2. The load balancer misconfiguration led to an uneven distribution of traffic, overloading one server and causing a cascade failure.Load balancer settings were reconfigured to ensure even traffic
distribution, preventing future overloads.

**Corrective and Preventative Measures**
*Improvements/Fixes*
1. Implement automated load testing to simulate high traffic scenarios and identify potential weaknesses.
2. Regularly review and update load balancer configurations to align with evolving traffic patterns.
3. Enhance monitoring to provide more granular insights into server loads and distribution.
4. Implementing a new process for testing changes to our Nginx server configuration before they are deployed to production.

**Task**
1. Develop and implement a load balancer configuration checklist for new deployments.
2. Conduct a comprehensive review of monitoring alerts and thresholds for early detection of anomalies.

