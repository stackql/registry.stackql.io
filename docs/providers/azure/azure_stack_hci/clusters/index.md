---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - azure_stack_hci
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_stack_hci.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cloudManagementEndpoint` | `string` | Endpoint configured for management from the Azure portal. |
| `registrationTimestamp` | `string` | First cluster sync timestamp. |
| `provisioningState` | `string` | Provisioning state. |
| `location` | `string` | The geo-location where the resource lives |
| `lastSyncTimestamp` | `string` | Most recent cluster sync timestamp. |
| `reportedProperties` | `object` | Properties reported by cluster agent. |
| `cloudId` | `string` | Unique, immutable resource id. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `aadClientId` | `string` | App id of cluster AAD identity. |
| `aadServicePrincipalObjectId` | `string` | Id of cluster identity service principal. |
| `tags` | `object` | Resource tags. |
| `desiredProperties` | `object` | Desired properties of the cluster. |
| `billingModel` | `string` | Type of billing applied to the resource. |
| `status` | `string` | Status of the cluster agent. |
| `aadTenantId` | `string` | Tenant id of cluster AAD identity. |
| `lastBillingTimestamp` | `string` | Most recent billing meter timestamp. |
| `trialDaysRemaining` | `number` | Number of days remaining in the trial period. |
| `aadApplicationObjectId` | `string` | Object id of cluster AAD identity. |
| `serviceEndpoint` | `string` | Region specific DataPath Endpoint of the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all HCI clusters in a resource group. |
| `Clusters_ListBySubscription` | `SELECT` | `subscriptionId` | List all HCI clusters in a subscription. |
| `Clusters_Create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create an HCI cluster. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Delete an HCI cluster. |
| `Clusters_CreateIdentity` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Create cluster identity. |
| `Clusters_Get` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Get HCI cluster. |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Update an HCI cluster. |
| `Clusters_UploadCertificate` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Upload certificate. |
