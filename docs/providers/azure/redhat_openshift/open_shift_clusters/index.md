---
title: open_shift_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - open_shift_clusters
  - redhat_openshift
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_shift_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redhat_openshift.open_shift_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | ProvisioningState represents a provisioning state. |
| `tags` | `object` | Resource tags. |
| `ingressProfiles` | `array` | The cluster ingress profiles. |
| `consoleProfile` | `object` | ConsoleProfile represents a console profile. |
| `location` | `string` | The geo-location where the resource lives |
| `masterProfile` | `object` | MasterProfile represents a master profile. |
| `servicePrincipalProfile` | `object` | ServicePrincipalProfile represents a service principal profile. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `apiserverProfile` | `object` | APIServerProfile represents an API server profile. |
| `workerProfiles` | `array` | The cluster worker profiles. |
| `clusterProfile` | `object` | ClusterProfile represents a cluster profile. |
| `networkProfile` | `object` | NetworkProfile represents a network profile. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OpenShiftClusters_List` | `SELECT` | `subscriptionId` | The operation returns properties of each OpenShift cluster. |
| `OpenShiftClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | The operation returns properties of each OpenShift cluster. |
| `OpenShiftClusters_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a OpenShift cluster. |
| `OpenShiftClusters_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | The operation returns nothing. |
| `OpenShiftClusters_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a OpenShift cluster. |
| `OpenShiftClusters_ListAdminCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns the admin kubeconfig. |
| `OpenShiftClusters_ListCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns the credentials. |
| `OpenShiftClusters_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a OpenShift cluster. |
