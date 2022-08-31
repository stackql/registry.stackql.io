---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
  - container_service
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
<tr><td><b>Name</b></td><td><code>managed_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.managed_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nodeResourceGroup` | `string` | The name of the resource group containing agent pool nodes. |
| `publicNetworkAccess` | `string` | Allow or deny public network access for AKS |
| `privateLinkResources` | `array` | Private link resources associated with the cluster. |
| `maxAgentPools` | `integer` | The max number of agent pools for the managed cluster. |
| `enablePodSecurityPolicy` | `boolean` | (DEPRECATING) Whether to enable Kubernetes pod security policy (preview). This feature is set for removal on October 15th, 2020. Learn more at aka.ms/aks/azpodpolicy. |
| `azurePortalFQDN` | `string` | The Azure Portal requires certain Cross-Origin Resource Sharing (CORS) headers to be sent in some responses, which Kubernetes APIServer doesn't handle by default. This special FQDN supports CORS, allowing the Azure Portal to function properly. |
| `currentKubernetesVersion` | `string` | If kubernetesVersion was a fully specified version &lt;major.minor.patch&gt;, this field will be exactly equal to it. If kubernetesVersion was &lt;major.minor&gt;, this field will contain the full &lt;major.minor.patch&gt; version being used. |
| `storageProfile` | `object` | Storage profile for the container service cluster. |
| `enableRBAC` | `boolean` | Whether to enable Kubernetes Role-Based Access Control. |
| `securityProfile` | `object` | Security profile for the container service cluster. |
| `kubernetesVersion` | `string` | Both patch version &lt;major.minor.patch&gt; (e.g. 1.20.13) and &lt;major.minor&gt; (e.g. 1.20) are supported. When &lt;major.minor&gt; is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same &lt;major.minor&gt; once it has been created (e.g. 1.14.x -&gt; 1.14) will not trigger an upgrade, even if a newer patch version is available. When you upgrade a supported AKS cluster, Kubernetes minor versions cannot be skipped. All upgrades must be performed sequentially by major version number. For example, upgrades between 1.14.x -&gt; 1.15.x or 1.15.x -&gt; 1.16.x are allowed, however 1.14.x -&gt; 1.16.x is not allowed. See [upgrading an AKS cluster](https://docs.microsoft.com/azure/aks/upgrade-cluster) for more details. |
| `autoUpgradeProfile` | `object` | Auto upgrade profile for a managed cluster. |
| `identityProfile` | `object` | Identities associated with the cluster. |
| `tags` | `object` | Resource tags. |
| `windowsProfile` | `object` | Profile for Windows VMs in the managed cluster. |
| `autoScalerProfile` | `object` | Parameters to be applied to the cluster-autoscaler when enabled |
| `fqdnSubdomain` | `string` | This cannot be updated once the Managed Cluster has been created. |
| `networkProfile` | `object` | Profile of network configuration. |
| `podIdentityProfile` | `object` | See [use AAD pod identity](https://docs.microsoft.com/azure/aks/use-azure-ad-pod-identity) for more details on pod identity integration. |
| `powerState` | `object` | Describes the Power State of the cluster |
| `httpProxyConfig` | `object` | Cluster HTTP proxy configuration. |
| `sku` | `object` | The SKU of a Managed Cluster. |
| `disableLocalAccounts` | `boolean` | If set to true, getting static credentials will be disabled for this cluster. This must only be used on Managed Clusters that are AAD enabled. For more details see [disable local accounts](https://docs.microsoft.com/azure/aks/managed-aad#disable-local-accounts-preview). |
| `identity` | `object` | Identity for the managed cluster. |
| `dnsPrefix` | `string` | This cannot be updated once the Managed Cluster has been created. |
| `provisioningState` | `string` | The current provisioning state. |
| `aadProfile` | `object` | For more details see [managed AAD on AKS](https://docs.microsoft.com/azure/aks/managed-aad). |
| `servicePrincipalProfile` | `object` | Information about a service principal identity for the cluster to use for manipulating Azure APIs. |
| `agentPoolProfiles` | `array` | The agent pool properties. |
| `linuxProfile` | `object` | Profile for Linux VMs in the container service cluster. |
| `fqdn` | `string` | The FQDN of the master pool. |
| `addonProfiles` | `object` | The profile of managed cluster add-on. |
| `privateFQDN` | `string` | The FQDN of private cluster. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `apiServerAccessProfile` | `object` | Access profile for managed cluster API server. |
| `diskEncryptionSetID` | `string` | This is of the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{encryptionSetName}' |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedClusters_List` | `SELECT` | `subscriptionId` |  |
| `ManagedClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `ManagedClusters_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_GetAccessProfile` | `EXEC` | `resourceGroupName, resourceName, roleName, subscriptionId` | **WARNING**: This API will be deprecated. Instead use [ListClusterUserCredentials](https://docs.microsoft.com/rest/api/aks/managedclusters/listclusterusercredentials) or [ListClusterAdminCredentials](https://docs.microsoft.com/rest/api/aks/managedclusters/listclusteradmincredentials) . |
| `ManagedClusters_GetCommandResult` | `EXEC` | `commandId, resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_GetOSOptions` | `EXEC` | `location, subscriptionId` |  |
| `ManagedClusters_GetUpgradeProfile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListClusterAdminCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListClusterMonitoringUserCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListClusterUserCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. The operation returns properties of each egress endpoint. |
| `ManagedClusters_ResetAADProfile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ResetServicePrincipalProfile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__clientId` | This action cannot be performed on a cluster that is not using a service principal |
| `ManagedClusters_RotateClusterCertificates` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [Certificate rotation](https://docs.microsoft.com/azure/aks/certificate-rotation) for more details about rotating managed cluster certificates. |
| `ManagedClusters_RunCommand` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__command` | AKS will create a pod to run the command. This is primarily useful for private clusters. For more information see [AKS Run Command](https://docs.microsoft.com/azure/aks/private-clusters#aks-run-command-preview). |
| `ManagedClusters_Start` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [starting a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about starting a cluster. |
| `ManagedClusters_Stop` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | This can only be performed on Azure Virtual Machine Scale set backed clusters. Stopping a cluster stops the control plane and agent nodes entirely, while maintaining all object and cluster state. A cluster does not accrue charges while it is stopped. See [stopping a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about stopping a cluster. |
| `ManagedClusters_UpdateTags` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
