---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - service_fabric
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
<tr><td><b>Id</b></td><td><code>azure.service_fabric.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `tags` | `object` | Azure resource tags. |
| `applicationTypeVersionsCleanupPolicy` | `object` |  |
| `notifications` | `array` | Indicates a list of notification channels for cluster events. |
| `clientCertificateCommonNames` | `array` | The list of client certificates referenced by common name that are allowed to manage the cluster. |
| `eventStoreServiceEnabled` | `boolean` | Indicates if the event store service is enabled. |
| `vmImage` | `string` | The VM image VMSS has been configured with. Generic names such as Windows or Linux can be used. |
| `reliabilityLevel` | `string` | The reliability level sets the replica set size of system services. Learn about [ReliabilityLevel](https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-capacity).<br /><br />  - None - Run the System services with a target replica set count of 1. This should only be used for test clusters.<br />  - Bronze - Run the System services with a target replica set count of 3. This should only be used for test clusters.<br />  - Silver - Run the System services with a target replica set count of 5.<br />  - Gold - Run the System services with a target replica set count of 7.<br />  - Platinum - Run the System services with a target replica set count of 9.<br /> |
| `vmssZonalUpgradeMode` | `string` | This property defines the upgrade mode for the virtual machine scale set, it is mandatory if a node type with multiple Availability Zones is added. |
| `certificateCommonNames` | `object` | Describes a list of server certificates referenced by common name that are used to secure the cluster. |
| `clientCertificateThumbprints` | `array` | The list of client certificates referenced by thumbprint that are allowed to manage the cluster. |
| `clusterId` | `string` | A service generated unique identifier for the cluster resource. |
| `sfZonalUpgradeMode` | `string` | This property controls the logical grouping of VMs in upgrade domains (UDs). This property can't be modified if a node type with multiple Availability Zones is already present in the cluster. |
| `nodeTypes` | `array` | The list of node types in the cluster. |
| `clusterEndpoint` | `string` | The Azure Resource Provider endpoint. A system service in the cluster connects to this  endpoint. |
| `type` | `string` | Azure resource type. |
| `fabricSettings` | `array` | The list of custom fabric settings to configure the cluster. |
| `upgradeDescription` | `object` | Describes the policy used when upgrading the cluster. |
| `clusterState` | `string` | The current state of the cluster.<br /><br />  - WaitingForNodes - Indicates that the cluster resource is created and the resource provider is waiting for Service Fabric VM extension to boot up and report to it.<br />  - Deploying - Indicates that the Service Fabric runtime is being installed on the VMs. Cluster resource will be in this state until the cluster boots up and system services are up.<br />  - BaselineUpgrade - Indicates that the cluster is upgrading to establishes the cluster version. This upgrade is automatically initiated when the cluster boots up for the first time.<br />  - UpdatingUserConfiguration - Indicates that the cluster is being upgraded with the user provided configuration.<br />  - UpdatingUserCertificate - Indicates that the cluster is being upgraded with the user provided certificate.<br />  - UpdatingInfrastructure - Indicates that the cluster is being upgraded with the latest Service Fabric runtime version. This happens only when the **upgradeMode** is set to 'Automatic'.<br />  - EnforcingClusterVersion - Indicates that cluster is on a different version than expected and the cluster is being upgraded to the expected version.<br />  - UpgradeServiceUnreachable - Indicates that the system service in the cluster is no longer polling the Resource Provider. Clusters in this state cannot be managed by the Resource Provider.<br />  - AutoScale - Indicates that the ReliabilityLevel of the cluster is being adjusted.<br />  - Ready - Indicates that the cluster is in a stable state.<br /> |
| `azureActiveDirectory` | `object` | The settings to enable AAD authentication on the cluster. |
| `upgradeWave` | `string` | Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0. |
| `addOnFeatures` | `array` | The list of add-on features to enable in the cluster. |
| `reverseProxyCertificateCommonNames` | `object` | Describes a list of server certificates referenced by common name that are used to secure the cluster. |
| `upgradeMode` | `string` | The upgrade mode of the cluster when new Service Fabric runtime version is available. |
| `diagnosticsStorageAccountConfig` | `object` | The storage account information for storing Service Fabric diagnostic logs. |
| `clusterCodeVersion` | `string` | The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to 'Manual'. To get list of available Service Fabric versions for new clusters use ClusterVersion API. To get the list of available version for existing clusters use **availableClusterVersions**. |
| `upgradePauseEndTimestampUtc` | `string` | Indicates the end date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC). |
| `etag` | `string` | Azure resource etag. |
| `upgradePauseStartTimestampUtc` | `string` | Indicates the start date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC). |
| `provisioningState` | `string` | The provisioning state of the cluster resource. |
| `infrastructureServiceManager` | `boolean` | Indicates if infrastructure service manager is enabled. |
| `location` | `string` | Azure resource location. |
| `reverseProxyCertificate` | `object` | Describes the certificate details. |
| `waveUpgradePaused` | `boolean` | Boolean to pause automatic runtime version upgrades to the cluster. |
| `availableClusterVersions` | `array` | The Service Fabric runtime versions available for this cluster. |
| `managementEndpoint` | `string` | The http management endpoint of the cluster. |
| `certificate` | `object` | Describes the certificate details. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_List` | `SELECT` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `Clusters_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `Clusters_CreateOrUpdate` | `INSERT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric cluster resource with the specified name. |
| `Clusters_Delete` | `DELETE` | `api-version, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric cluster resource with the specified name. |
| `Clusters_Get` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric cluster resource created or in the process of being created in the specified resource group. |
| `Clusters_ListUpgradableVersions` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId, data__targetVersion` | If a target is not provided, it will get the minimum and maximum versions available from the current cluster version. If a target is given, it will provide the required path to get from the current cluster version to the target version. |
| `Clusters_Update` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Update the configuration of a Service Fabric cluster resource with the specified name. |
