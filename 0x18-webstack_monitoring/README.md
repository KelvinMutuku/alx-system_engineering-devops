0x18. Webstack monitoring
This project involves using Datadog to measure what's going on with my server.

Resources
Configuring NGINX Logging
Why monitor servers
Application Performance Management
How to get Sumo Logic Access Keys
Google SRE book - Monitoring Distributed Systems
Tasks :page_with_curl
0. Sign up for Datadog and install datadog-agent

Datadog: Signed up, installed datadog-agent on my server.
Created application key
1. Monitor some metrics System metrics were setup using using System Check

Setup system metrics to monitor the number of read requests issued to the device per second.
Setup system metrics to monitor the number of write requests issued to the device per second.
2. Create a dashboard

Created a new dashboard on Datadog
Added 4 widgets to the dashboard
retrieved dashboard_id using Datadog's API. The id can be found at 2-setup_datadog
