---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
  - service_fabric_managed_clusters
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
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.managed_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `loadBalancingRules` | `array` | Load balancing rules that are applied to the public load balancer of the cluster. |
| `sku` | `object` | Service Fabric managed cluster Sku definition |
| `etag` | `string` | Azure resource etag. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `clusterCodeVersion` | `string` | The Service Fabric runtime version of the cluster. This property is required when **clusterUpgradeMode** is set to 'Manual'. To get list of available Service Fabric versions for new clusters use ClusterVersion API. To get the list of available version for existing clusters use **availableClusterVersions**. |
| `addonFeatures` | `array` | List of add-on features to enable on the cluster. |
| `networkSecurityRules` | `array` | Custom Network Security Rules that are applied to the Virtual Network of the cluster. |
| `adminUserName` | `string` | VM admin user name. |
| `clients` | `array` | Client certificates that are allowed to manage the cluster. |
| `fabricSettings` | `array` | The list of custom fabric settings to configure the cluster. |
| `ipv4Address` | `string` | The IPv4 address associated with the public load balancer of the cluster. |
| `azureActiveDirectory` | `object` | The settings to enable AAD authentication on the cluster. |
| `enableAutoOSUpgrade` | `boolean` | Setting this to true enables automatic OS upgrade for the node types that are created using any platform OS image with version 'latest'. The default value for this setting is false. |
| `httpGatewayConnectionPort` | `integer` | The port used for HTTP connections to the cluster. |
| `clusterState` | `string` | The current state of the cluster.<br /> |
| `clusterCertificateThumbprints` | `array` | List of thumbprints of the cluster certificates. |
| `ipv6Address` | `string` | IPv6 address for the cluster if IPv6 is enabled. |
| `location` | `string` | Azure resource location. |
| `allowRdpAccess` | `boolean` | Setting this to true enables RDP access to the VM. The default NSG rule opens RDP port to Internet which can be overridden with custom Network Security Rules. The default value for this setting is false. |
| `provisioningState` | `string` | The provisioning state of the managed resource. |
| `enableServicePublicIP` | `boolean` | Setting this to true will link the IPv4 address as the ServicePublicIP of the IPv6 address. It can only be set to True if IPv6 is enabled on the cluster. |
| `tags` | `object` | Azure resource tags. |
| `enableIpv6` | `boolean` | Setting this to true creates IPv6 address space for the default VNet used by the cluster. This setting cannot be changed once the cluster is created. The default value for this setting is false. |
| `fqdn` | `string` | The fully qualified domain name associated with the public load balancer of the cluster. |
| `adminPassword` | `string` | VM admin user password. |
| `zonalResiliency` | `boolean` | Indicates if the cluster has zone resiliency. |
| `dnsName` | `string` | The cluster dns name. |
| `applicationTypeVersionsCleanupPolicy` | `object` | The policy used to clean up unused versions. When the policy is not specified explicitly, the default unused application versions to keep will be 3. |
| `type` | `string` | Azure resource type. |
| `serviceEndpoints` | `array` | Service endpoints for subnets in the cluster. |
| `clusterUpgradeMode` | `string` | The upgrade mode of the cluster when new Service Fabric runtime version is available.<br /> |
| `subnetId` | `string` | If specified, the node types for the cluster are created in this subnet instead of the default VNet. The **networkSecurityRules** specified for the cluster are also applied to this subnet. This setting cannot be changed once the cluster is created. |
| `clusterId` | `string` | A service generated unique identifier for the cluster resource. |
| `auxiliarySubnets` | `array` | Auxiliary subnets for the cluster. |
| `clusterUpgradeCadence` | `string` | Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0. |
| `ipTags` | `array` | The list of IP tags associated with the default public IP address of the cluster. |
| `clientConnectionPort` | `integer` | The port used for client connections to the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedClusters_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `ManagedClusters_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `ManagedClusters_CreateOrUpdate` | `INSERT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric managed cluster resource with the specified name. |
| `ManagedClusters_Delete` | `DELETE` | `api-version, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric managed cluster resource with the specified name. |
| `ManagedClusters_Get` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric managed cluster resource created or in the process of being created in the specified resource group. |
| `ManagedClusters_Update` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Update the tags of of a Service Fabric managed cluster resource with the specified name. |
