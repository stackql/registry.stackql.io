---
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types
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
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.node_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `additionalDataDisks` | `array` | Additional managed data disks. |
| `ephemeralPorts` | `object` | Port range details |
| `evictionPolicy` | `string` | Specifies the eviction policy for virtual machines in a SPOT node type. |
| `zones` | `array` | Specifies the availability zones where the node type would span across. If the cluster is not spanning across availability zones, initiates az migration for the cluster. |
| `vmImagePublisher` | `string` | The publisher of the Azure Virtual Machines Marketplace image. For example, Canonical or MicrosoftWindowsServer. |
| `placementProperties` | `object` | The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run. |
| `dataDiskLetter` | `string` | Managed data disk letter. It can not use the reserved letter C or D and it can not change after created. |
| `sku` | `object` | Describes a node type sku. |
| `isPrimary` | `boolean` | Indicates the Service Fabric system services for the cluster will run on this node type. This setting cannot be changed once the node type is created. |
| `vmManagedIdentity` | `object` | Identities for the virtual machine scale set under the node type. |
| `hostGroupId` | `string` | Specifies the full host group resource Id. This property is used for deploying on azure dedicated hosts. |
| `dataDiskType` | `string` | Managed data disk type. IOPS and throughput are given by the disk size, to see more information go to https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types.<br /> |
| `vmSecrets` | `array` | The secrets to install in the virtual machines. |
| `tags` | `object` | Azure resource tags. |
| `vmInstanceCount` | `integer` | The number of nodes in the node type. &lt;br /&gt;&lt;br /&gt;**Values:** &lt;br /&gt;-1 - Use when auto scale rules are configured or sku.capacity is defined &lt;br /&gt; 0 - Not supported &lt;br /&gt; &gt;0 - Use for manual scale. |
| `applicationPorts` | `object` | Port range details |
| `vmSize` | `string` | The size of virtual machines in the pool. All virtual machines in a pool are the same size. For example, Standard_D3. |
| `spotRestoreTimeout` | `string` | Indicates the time duration after which the platform will not try to restore the VMSS SPOT instances specified as ISO 8601. |
| `useEphemeralOSDisk` | `boolean` | Indicates whether to use ephemeral os disk. The sku selected on the vmSize property needs to support this feature. |
| `vmImageSku` | `string` | The SKU of the Azure Virtual Machines Marketplace image. For example, 14.04.0-LTS or 2012-R2-Datacenter. |
| `multiplePlacementGroups` | `boolean` | Indicates if scale set associated with the node type can be composed of multiple placement groups. |
| `useTempDataDisk` | `boolean` | Specifies whether to use the temporary disk for the service fabric data root, in which case no managed data disk will be attached and the temporary disk will be used. It is only allowed for stateless node types. |
| `useDefaultPublicLoadBalancer` | `boolean` | Specifies whether the use public load balancer. If not specified and the node type doesn't have its own frontend configuration, it will be attached to the default load balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is true, then the frontend has to be an Internal Load Balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is false or not set, then the custom load balancer must include a public load balancer to provide outbound connectivity. |
| `provisioningState` | `string` | The provisioning state of the managed resource. |
| `capacities` | `object` | The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has. |
| `isSpotVM` | `boolean` | Indicates whether the node type will be Spot Virtual Machines. Azure will allocate the VMs if there is capacity available and the VMs can be evicted at any time. |
| `dataDiskSizeGB` | `integer` | Disk size for the managed disk attached to the vms on the node type in GBs. |
| `type` | `string` | Azure resource type. |
| `isStateless` | `boolean` | Indicates if the node type can only host Stateless workloads. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `enableAcceleratedNetworking` | `boolean` | Specifies whether the network interface is accelerated networking-enabled. |
| `vmImageVersion` | `string` | The version of the Azure Virtual Machines Marketplace image. A value of 'latest' can be specified to select the latest version of an image. If omitted, the default is 'latest'. |
| `vmImageOffer` | `string` | The offer type of the Azure Virtual Machines Marketplace image. For example, UbuntuServer or WindowsServer. |
| `enableEncryptionAtHost` | `boolean` | Enable or disable the Host Encryption for the virtual machines on the node type. This will enable the encryption for all the disks including Resource/Temp disk at host itself. Default: The Encryption at host will be disabled unless this property is set to true for the resource. |
| `networkSecurityRules` | `array` | The Network Security Rules for this node type. This setting can only be specified for node types that are configured with frontend configurations. |
| `enableOverProvisioning` | `boolean` | Specifies whether the node type should be overprovisioned. It is only allowed for stateless node types. |
| `frontendConfigurations` | `array` | Indicates the node type uses its own frontend configurations instead of the default one for the cluster. This setting can only be specified for non-primary node types and can not be added or removed after the node type is created. |
| `vmExtensions` | `array` | Set of extensions that should be installed onto the virtual machines. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NodeTypes_ListByManagedClusters` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all Node types of the specified managed cluster. |
| `NodeTypes_CreateOrUpdate` | `INSERT` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Create or update a Service Fabric node type of a given managed cluster. |
| `NodeTypes_Delete` | `DELETE` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Delete a Service Fabric node type of a given managed cluster. |
| `NodeTypes_DeleteNode` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId, data__nodes` | Deletes one or more nodes on the node type. It will disable the fabric nodes, trigger a delete on the VMs and removes the state from the cluster. |
| `NodeTypes_Get` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Get a Service Fabric node type of a given managed cluster. |
| `NodeTypes_Reimage` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId, data__nodes` | Reimages one or more nodes on the node type. It will disable the fabric nodes, trigger a reimage on the VMs and activate the nodes back again. |
| `NodeTypes_Restart` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId, data__nodes` | Restarts one or more nodes on the node type. It will disable the fabric nodes, trigger a restart on the VMs and activate the nodes back again. |
| `NodeTypes_Update` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Update the configuration of a node type of a given managed cluster, only updating tags. |
