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
| `serviceEndpoint` | `string` | Region specific DataPath Endpoint of the cluster. |
| `provisioningState` | `string` | Provisioning state. |
| `cloudId` | `string` | Unique, immutable resource id. |
| `tags` | `object` | Resource tags. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `trialDaysRemaining` | `number` | Number of days remaining in the trial period. |
| `billingModel` | `string` | Type of billing applied to the resource. |
| `lastBillingTimestamp` | `string` | Most recent billing meter timestamp. |
| `aadApplicationObjectId` | `string` | Object id of cluster AAD identity. |
| `registrationTimestamp` | `string` | First cluster sync timestamp. |
| `aadServicePrincipalObjectId` | `string` | Id of cluster identity service principal. |
| `desiredProperties` | `object` | Desired properties of the cluster. |
| `aadClientId` | `string` | App id of cluster AAD identity. |
| `cloudManagementEndpoint` | `string` | Endpoint configured for management from the Azure portal. |
| `lastSyncTimestamp` | `string` | Most recent cluster sync timestamp. |
| `aadTenantId` | `string` | Tenant id of cluster AAD identity. |
| `location` | `string` | The geo-location where the resource lives |
| `status` | `string` | Status of the cluster agent. |
| `reportedProperties` | `object` | Properties reported by cluster agent. |
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
