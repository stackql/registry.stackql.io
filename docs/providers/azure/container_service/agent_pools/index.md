---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
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
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.agent_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `upgradeSettings` | `object` | Settings for upgrading an agentpool |
| `enableAutoScaling` | `boolean` | Whether to enable auto-scaler |
| `proximityPlacementGroupID` | `string` | The ID for Proximity Placement Group. |
| `enableEncryptionAtHost` | `boolean` | This is only supported on certain VM sizes and in certain Azure regions. For more information, see: https://docs.microsoft.com/azure/aks/enable-host-encryption |
| `linuxOSConfig` | `object` | See [AKS custom node configuration](https://docs.microsoft.com/azure/aks/custom-node-configuration) for more details. |
| `workloadRuntime` | `string` | Determines the type of workload a node can run. |
| `powerState` | `object` | Describes the Power State of the cluster |
| `vnetSubnetID` | `string` | If this is not specified, a VNET and subnet will be generated and used. If no podSubnetID is specified, this applies to nodes and pods, otherwise it applies to just nodes. This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;virtualNetworkName&#125;/subnets/&#123;subnetName&#125; |
| `hostGroupID` | `string` | This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/hostGroups/&#123;hostGroupName&#125;. For more information see [Azure dedicated hosts](https://docs.microsoft.com/azure/virtual-machines/dedicated-hosts). |
| `enableFIPS` | `boolean` | See [Add a FIPS-enabled node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#add-a-fips-enabled-node-pool-preview) for more details. |
| `nodePublicIPPrefixID` | `string` | This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/publicIPPrefixes/&#123;publicIPPrefixName&#125; |
| `vmSize` | `string` | VM size availability varies by region. If a node contains insufficient compute resources (memory, cpu, etc) pods might fail to run correctly. For more details on restricted VM sizes, see: https://docs.microsoft.com/azure/aks/quotas-skus-regions |
| `nodeImageVersion` | `string` | The version of node image |
| `count` | `integer` | Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default value is 1. |
| `creationData` | `object` | Data used when creating a target resource from a source resource. |
| `podSubnetID` | `string` | If omitted, pod IPs are statically assigned on the node subnet (see vnetSubnetID for more details). This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;virtualNetworkName&#125;/subnets/&#123;subnetName&#125; |
| `gpuInstanceProfile` | `string` | GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU. |
| `availabilityZones` | `array` | The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is 'VirtualMachineScaleSets'. |
| `kubeletConfig` | `object` | See [AKS custom node configuration](https://docs.microsoft.com/azure/aks/custom-node-configuration) for more details. |
| `maxPods` | `integer` | The maximum number of pods that can run on a node. |
| `osDiskType` | `string` | The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more information see [Ephemeral OS](https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os). |
| `osDiskSizeGB` | `integer` | OS Disk Size in GB to be used to specify the disk size for every machine in the master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified. |
| `provisioningState` | `string` | The current deployment or provisioning state. |
| `spotMaxPrice` | `number` | Possible values are any decimal value greater than zero or -1 which indicates the willingness to pay any on-demand price. For more details on spot pricing, see [spot VMs pricing](https://docs.microsoft.com/azure/virtual-machines/spot-vms#pricing) |
| `osType` | `string` | The operating system type. The default is Linux. |
| `osSKU` | `string` | Specifies an OS SKU. This value must not be specified if OSType is Windows. |
| `maxCount` | `integer` | The maximum number of nodes for auto-scaling |
| `currentOrchestratorVersion` | `string` | If orchestratorVersion is a fully specified version &lt;major.minor.patch&gt;, this field will be exactly equal to it. If orchestratorVersion is &lt;major.minor&gt;, this field will contain the full &lt;major.minor.patch&gt; version being used. |
| `nodeTaints` | `array` | The taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule. |
| `scaleDownMode` | `string` | Describes how VMs are added to or removed from Agent Pools. See [billing states](https://docs.microsoft.com/azure/virtual-machines/states-billing). |
| `scaleSetPriority` | `string` | The Virtual Machine Scale Set priority. |
| `type` | `string` | The type of Agent Pool. |
| `orchestratorVersion` | `string` | Both patch version &lt;major.minor.patch&gt; (e.g. 1.20.13) and &lt;major.minor&gt; (e.g. 1.20) are supported. When &lt;major.minor&gt; is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same &lt;major.minor&gt; once it has been created (e.g. 1.14.x -&gt; 1.14) will not trigger an upgrade, even if a newer patch version is available. As a best practice, you should upgrade all node pools in an AKS cluster to the same Kubernetes version. The node pool version must have the same major version as the control plane. The node pool minor version must be within two minor versions of the control plane version. The node pool version cannot be greater than the control plane version. For more information see [upgrading a node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#upgrade-a-node-pool). |
| `nodeLabels` | `object` | The node labels to be persisted across all nodes in agent pool. |
| `enableUltraSSD` | `boolean` | Whether to enable UltraSSD |
| `kubeletDiskType` | `string` | Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage. |
| `enableNodePublicIP` | `boolean` | Some scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. For more information see [assigning a public IP per node](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#assign-a-public-ip-per-node-for-your-node-pools). The default is false. |
| `minCount` | `integer` | The minimum number of nodes for auto-scaling |
| `tags` | `object` | The tags to be persisted on the agent pool virtual machine scale set. |
| `mode` | `string` | A cluster must have at least one 'System' Agent Pool at all times. For additional information on agent pool restrictions and best practices, see: https://docs.microsoft.com/azure/aks/use-system-pools |
| `scaleSetEvictionPolicy` | `string` | The eviction policy specifies what to do with the VM when it is evicted. The default is Delete. For more information about eviction see [spot VMs](https://docs.microsoft.com/azure/virtual-machines/spot-vms) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AgentPools_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_CreateOrUpdate` | `INSERT` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_Delete` | `DELETE` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_Get` | `EXEC` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_GetAvailableAgentPoolVersions` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [supported Kubernetes versions](https://docs.microsoft.com/azure/aks/supported-kubernetes-versions) for more details about the version lifecycle. |
| `AgentPools_GetUpgradeProfile` | `EXEC` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_UpgradeNodeImageVersion` | `EXEC` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` | Upgrading the node image version of an agent pool applies the newest OS and runtime updates to the nodes. AKS provides one new image per week with the latest updates. For more details on node image versions, see: https://docs.microsoft.com/azure/aks/node-image-upgrade |
