---
title: application_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways
  - network
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
<tr><td><b>Name</b></td><td><code>application_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `enableHttp2` | `boolean` | Whether HTTP2 is enabled on the application gateway resource. |
| `autoscaleConfiguration` | `object` | Application Gateway autoscale configuration. |
| `sslPolicy` | `object` | Application Gateway Ssl policy. |
| `trustedRootCertificates` | `array` | Trusted Root certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `httpListeners` | `array` | Http listeners of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `gatewayIPConfigurations` | `array` | Subnets of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `sslProfiles` | `array` | SSL profiles of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `backendAddressPools` | `array` | Backend address pool of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `urlPathMaps` | `array` | URL path map of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `location` | `string` | Resource location. |
| `backendHttpSettingsCollection` | `array` | Backend http settings of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `listeners` | `array` | Listeners of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `privateLinkConfigurations` | `array` | PrivateLink configurations on application gateway. |
| `redirectConfigurations` | `array` | Redirect configurations of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
| `firewallPolicy` | `object` | Reference to another subresource. |
| `identity` | `object` | Identity for the resource. |
| `sku` | `object` | SKU of an application gateway. |
| `enableFips` | `boolean` | Whether FIPS is enabled on the application gateway resource. |
| `rewriteRuleSets` | `array` | Rewrite rules for the application gateway resource. |
| `authenticationCertificates` | `array` | Authentication certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `requestRoutingRules` | `array` | Request routing rules of the application gateway resource. |
| `frontendIPConfigurations` | `array` | Frontend IP addresses of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `resourceGuid` | `string` | The resource GUID property of the application gateway resource. |
| `globalConfiguration` | `object` | Application Gateway global configuration. |
| `type` | `string` | Resource type. |
| `operationalState` | `string` | Operational state of the application gateway resource. |
| `customErrorConfigurations` | `array` | Custom error configurations of the application gateway resource. |
| `backendSettingsCollection` | `array` | Backend settings of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `privateEndpointConnections` | `array` | Private Endpoint connections on application gateway. |
| `trustedClientCertificates` | `array` | Trusted client certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `forceFirewallPolicyAssociation` | `boolean` | If true, associates a firewall policy with an application gateway regardless whether the policy differs from the WAF Config. |
| `frontendPorts` | `array` | Frontend ports of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `sslCertificates` | `array` | SSL certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | The current provisioning state. |
| `loadDistributionPolicies` | `array` | Load distribution policies of the application gateway resource. |
| `routingRules` | `array` | Routing rules of the application gateway resource. |
| `probes` | `array` | Probes of the application gateway resource. |
| `webApplicationFirewallConfiguration` | `object` | Application gateway web application firewall configuration. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationGateways_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all application gateways in a resource group. |
| `ApplicationGateways_ListAll` | `SELECT` | `subscriptionId` | Gets all the application gateways in a subscription. |
| `ApplicationGateways_CreateOrUpdate` | `INSERT` | `applicationGatewayName, resourceGroupName, subscriptionId` | Creates or updates the specified application gateway. |
| `ApplicationGateways_Delete` | `DELETE` | `applicationGatewayName, resourceGroupName, subscriptionId` | Deletes the specified application gateway. |
| `ApplicationGateways_BackendHealth` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the backend health of the specified application gateway in a resource group. |
| `ApplicationGateways_BackendHealthOnDemand` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group. |
| `ApplicationGateways_Get` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the specified application gateway. |
| `ApplicationGateways_GetSslPredefinedPolicy` | `EXEC` | `predefinedPolicyName, subscriptionId` | Gets Ssl predefined policy with the specified policy name. |
| `ApplicationGateways_ListAvailableRequestHeaders` | `EXEC` | `subscriptionId` | Lists all available request headers. |
| `ApplicationGateways_ListAvailableResponseHeaders` | `EXEC` | `subscriptionId` | Lists all available response headers. |
| `ApplicationGateways_ListAvailableServerVariables` | `EXEC` | `subscriptionId` | Lists all available server variables. |
| `ApplicationGateways_ListAvailableSslOptions` | `EXEC` | `subscriptionId` | Lists available Ssl options for configuring Ssl policy. |
| `ApplicationGateways_ListAvailableSslPredefinedPolicies` | `EXEC` | `subscriptionId` | Lists all SSL predefined policies for configuring Ssl policy. |
| `ApplicationGateways_ListAvailableWafRuleSets` | `EXEC` | `subscriptionId` | Lists all available web application firewall rule sets. |
| `ApplicationGateways_Start` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Starts the specified application gateway. |
| `ApplicationGateways_Stop` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Stops the specified application gateway in a resource group. |
| `ApplicationGateways_UpdateTags` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Updates the specified application gateway tags. |
