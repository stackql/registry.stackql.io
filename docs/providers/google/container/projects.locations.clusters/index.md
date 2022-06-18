---
title: projects.locations.clusters
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
<tr><td><b>Name</b></td><td><code>projects.locations.clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.projects.locations.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `clusters` | `array` | A list of clusters in the project in the specified zone, or across all ones. |
| `missingZones` | `array` | If any zones are listed here, the list of clusters returned may be missing those zones. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `clustersId, locationsId, projectsId` | Gets the specified operation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all clusters owned by a project in either the specified zone or all zones. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| `delete` | `DELETE` | `clustersId, locationsId, projectsId` | Deletes a node pool from a cluster. |
| `completeIpRotation` | `EXEC` | `clustersId, locationsId, projectsId` | Completes master IP rotation. |
| `getJwks` | `EXEC` | `clustersId, locationsId, projectsId` | Gets the public component of the cluster signing keys in JSON Web Key format. This API is not yet intended for general use, and is not available for all clusters. |
| `setAddons` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the addons for a specific cluster. |
| `setLegacyAbac` | `EXEC` | `clustersId, locationsId, projectsId` | Enables or disables the ABAC authorization mechanism on a cluster. |
| `setLocations` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| `setLogging` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the logging service for a specific cluster. |
| `setMaintenancePolicy` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the maintenance policy for a cluster. |
| `setMasterAuth` | `EXEC` | `clustersId, locationsId, projectsId` | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| `setMonitoring` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the monitoring service for a specific cluster. |
| `setNetworkPolicy` | `EXEC` | `clustersId, locationsId, projectsId` | Enables or disables Network Policy for a cluster. |
| `setResourceLabels` | `EXEC` | `clustersId, locationsId, projectsId` | Sets labels on a cluster. |
| `startIpRotation` | `EXEC` | `clustersId, locationsId, projectsId` | Starts master IP rotation. |
| `update` | `EXEC` | `clustersId, locationsId, projectsId` | Updates the version and/or image type for the specified node pool. |
| `updateMaster` | `EXEC` | `clustersId, locationsId, projectsId` | Updates the master for a specific cluster. |
