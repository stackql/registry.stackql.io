---
title: compute
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
Creates and runs virtual machines on Google Cloud Platform.  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>google.compute</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Compute Engine API</td></tr>
<tr><td><b>Description</b></td><td>Creates and runs virtual machines on Google Cloud Platform.</td></tr>
<tr><td><b>Id</b></td><td><code>compute:beta</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/google/compute/acceleratorTypes/">acceleratorTypes</a><br />
<a href="/providers/google/compute/addresses/">addresses</a><br />
<a href="/providers/google/compute/autoscalers/">autoscalers</a><br />
<a href="/providers/google/compute/backendBuckets/">backendBuckets</a><br />
<a href="/providers/google/compute/backendServices/">backendServices</a><br />
<a href="/providers/google/compute/diskTypes/">diskTypes</a><br />
<a href="/providers/google/compute/disks/">disks</a><br />
<a href="/providers/google/compute/externalVpnGateways/">externalVpnGateways</a><br />
<a href="/providers/google/compute/firewallPolicies/">firewallPolicies</a><br />
<a href="/providers/google/compute/firewalls/">firewalls</a><br />
<a href="/providers/google/compute/forwardingRules/">forwardingRules</a><br />
<a href="/providers/google/compute/globalAddresses/">globalAddresses</a><br />
<a href="/providers/google/compute/globalForwardingRules/">globalForwardingRules</a><br />
<a href="/providers/google/compute/globalNetworkEndpointGroups/">globalNetworkEndpointGroups</a><br />
<a href="/providers/google/compute/globalOperations/">globalOperations</a><br />
<a href="/providers/google/compute/globalOrganizationOperations/">globalOrganizationOperations</a><br />
<a href="/providers/google/compute/globalPublicDelegatedPrefixes/">globalPublicDelegatedPrefixes</a><br />
<a href="/providers/google/compute/healthChecks/">healthChecks</a><br />
<a href="/providers/google/compute/httpHealthChecks/">httpHealthChecks</a><br />
<a href="/providers/google/compute/httpsHealthChecks/">httpsHealthChecks</a><br />
<a href="/providers/google/compute/imageFamilyViews/">imageFamilyViews</a><br />
<a href="/providers/google/compute/images/">images</a><br />
<a href="/providers/google/compute/instanceGroupManagers/">instanceGroupManagers</a><br />
<a href="/providers/google/compute/instanceGroups/">instanceGroups</a><br />
<a href="/providers/google/compute/instanceTemplates/">instanceTemplates</a><br />
<a href="/providers/google/compute/instances/">instances</a><br />
<a href="/providers/google/compute/interconnectAttachments/">interconnectAttachments</a><br />
<a href="/providers/google/compute/interconnectLocations/">interconnectLocations</a><br />
<a href="/providers/google/compute/interconnects/">interconnects</a><br />
<a href="/providers/google/compute/licenseCodes/">licenseCodes</a><br />
<a href="/providers/google/compute/licenses/">licenses</a><br />
<a href="/providers/google/compute/machineTypes/">machineTypes</a><br />
<a href="/providers/google/compute/networkEndpointGroups/">networkEndpointGroups</a><br />
<a href="/providers/google/compute/networks/">networks</a><br />
<a href="/providers/google/compute/nodeGroups/">nodeGroups</a><br />
<a href="/providers/google/compute/nodeTemplates/">nodeTemplates</a><br />
<a href="/providers/google/compute/nodeTypes/">nodeTypes</a><br />
<a href="/providers/google/compute/packetMirrorings/">packetMirrorings</a><br />
<a href="/providers/google/compute/projects/">projects</a><br />
<a href="/providers/google/compute/publicAdvertisedPrefixes/">publicAdvertisedPrefixes</a><br />
<a href="/providers/google/compute/publicDelegatedPrefixes/">publicDelegatedPrefixes</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/google/compute/regionAutoscalers/">regionAutoscalers</a><br />
<a href="/providers/google/compute/regionBackendServices/">regionBackendServices</a><br />
<a href="/providers/google/compute/regionCommitments/">regionCommitments</a><br />
<a href="/providers/google/compute/regionDiskTypes/">regionDiskTypes</a><br />
<a href="/providers/google/compute/regionDisks/">regionDisks</a><br />
<a href="/providers/google/compute/regionHealthCheckServices/">regionHealthCheckServices</a><br />
<a href="/providers/google/compute/regionHealthChecks/">regionHealthChecks</a><br />
<a href="/providers/google/compute/regionInstanceGroupManagers/">regionInstanceGroupManagers</a><br />
<a href="/providers/google/compute/regionInstanceGroups/">regionInstanceGroups</a><br />
<a href="/providers/google/compute/regionInstances/">regionInstances</a><br />
<a href="/providers/google/compute/regionNetworkEndpointGroups/">regionNetworkEndpointGroups</a><br />
<a href="/providers/google/compute/regionNotificationEndpoints/">regionNotificationEndpoints</a><br />
<a href="/providers/google/compute/regionOperations/">regionOperations</a><br />
<a href="/providers/google/compute/regionSslCertificates/">regionSslCertificates</a><br />
<a href="/providers/google/compute/regionTargetHttpProxies/">regionTargetHttpProxies</a><br />
<a href="/providers/google/compute/regionTargetHttpsProxies/">regionTargetHttpsProxies</a><br />
<a href="/providers/google/compute/regionUrlMaps/">regionUrlMaps</a><br />
<a href="/providers/google/compute/regions/">regions</a><br />
<a href="/providers/google/compute/reservations/">reservations</a><br />
<a href="/providers/google/compute/resourcePolicies/">resourcePolicies</a><br />
<a href="/providers/google/compute/routers/">routers</a><br />
<a href="/providers/google/compute/routes/">routes</a><br />
<a href="/providers/google/compute/securityPolicies/">securityPolicies</a><br />
<a href="/providers/google/compute/serviceAttachments/">serviceAttachments</a><br />
<a href="/providers/google/compute/snapshots/">snapshots</a><br />
<a href="/providers/google/compute/sslCertificates/">sslCertificates</a><br />
<a href="/providers/google/compute/sslPolicies/">sslPolicies</a><br />
<a href="/providers/google/compute/subnetworks/">subnetworks</a><br />
<a href="/providers/google/compute/targetGrpcProxies/">targetGrpcProxies</a><br />
<a href="/providers/google/compute/targetHttpProxies/">targetHttpProxies</a><br />
<a href="/providers/google/compute/targetHttpsProxies/">targetHttpsProxies</a><br />
<a href="/providers/google/compute/targetInstances/">targetInstances</a><br />
<a href="/providers/google/compute/targetPools/">targetPools</a><br />
<a href="/providers/google/compute/targetSslProxies/">targetSslProxies</a><br />
<a href="/providers/google/compute/targetTcpProxies/">targetTcpProxies</a><br />
<a href="/providers/google/compute/targetVpnGateways/">targetVpnGateways</a><br />
<a href="/providers/google/compute/urlMaps/">urlMaps</a><br />
<a href="/providers/google/compute/vpnGateways/">vpnGateways</a><br />
<a href="/providers/google/compute/vpnTunnels/">vpnTunnels</a><br />
<a href="/providers/google/compute/zoneOperations/">zoneOperations</a><br />
<a href="/providers/google/compute/zones/">zones</a><br />
</div>
</div>
