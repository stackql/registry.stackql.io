---
title: projects.zones.clusters
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects.zones.clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.projects.zones.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `clusters` | `array` | A list of clusters in the project in the specified zone, or across all ones. |
| `missingZones` | `array` | If any zones are listed here, the list of clusters returned may be missing those zones. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `clusterId, projectId, zone` | Gets the details of a specific cluster. |
| `list` | `SELECT` | `projectId, zone` | Lists all clusters owned by a project in either the specified zone or all zones. |
| `create` | `INSERT` | `projectId, zone` | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| `delete` | `DELETE` | `clusterId, projectId, zone` | Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |
| `addons` | `EXEC` | `clusterId, projectId, zone` | Sets the addons for a specific cluster. |
| `completeIpRotation` | `EXEC` | `clusterId, projectId, zone` | Completes master IP rotation. |
| `legacyAbac` | `EXEC` | `clusterId, projectId, zone` | Enables or disables the ABAC authorization mechanism on a cluster. |
| `locations` | `EXEC` | `clusterId, projectId, zone` | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| `logging` | `EXEC` | `clusterId, projectId, zone` | Sets the logging service for a specific cluster. |
| `master` | `EXEC` | `clusterId, projectId, zone` | Updates the master for a specific cluster. |
| `monitoring` | `EXEC` | `clusterId, projectId, zone` | Sets the monitoring service for a specific cluster. |
| `resourceLabels` | `EXEC` | `clusterId, projectId, zone` | Sets labels on a cluster. |
| `setMaintenancePolicy` | `EXEC` | `clusterId, projectId, zone` | Sets the maintenance policy for a cluster. |
| `setMasterAuth` | `EXEC` | `clusterId, projectId, zone` | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| `setNetworkPolicy` | `EXEC` | `clusterId, projectId, zone` | Enables or disables Network Policy for a cluster. |
| `startIpRotation` | `EXEC` | `clusterId, projectId, zone` | Starts master IP rotation. |
| `update` | `EXEC` | `clusterId, projectId, zone` | Updates the settings of a specific cluster. |
