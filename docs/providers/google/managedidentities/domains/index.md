---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The unique name of the domain using the form: `projects/{project_id}/locations/global/domains/{domain_name}`. |
| `state` | `string` | Output only. The current state of this domain. |
| `statusMessage` | `string` | Output only. Additional information about the current status of this domain, if available. |
| `updateTime` | `string` | Output only. The last update time. |
| `admin` | `string` | Optional. The name of delegated administrator account used to perform Active Directory operations. If not specified, `setupadmin` will be used. |
| `trusts` | `array` | Output only. The current trusts associated with the domain. |
| `auditLogsEnabled` | `boolean` | Optional. Configuration for audit logs. True if audit logs are enabled, else false. Default is audit logs disabled. |
| `labels` | `object` | Optional. Resource labels that can contain user-provided metadata. |
| `locations` | `array` | Required. Locations where domain needs to be provisioned. regions e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block. |
| `authorizedNetworks` | `array` | Optional. The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) the domain instance is connected to. Networks can be added using UpdateDomain. The domain is only available on networks listed in `authorized_networks`. If CIDR subnets overlap between networks, domain creation will fail. |
| `createTime` | `string` | Output only. The time the instance was created. |
| `fqdn` | `string` | Output only. The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would be chosen for an Active Directory set up on an internal network. |
| `reservedIpRange` | `string` | Required. The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. Ranges must be unique and non-overlapping with existing subnets in [Domain].[authorized_networks]. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_domains_get` | `SELECT` | `name` | Gets information about a domain. |
| `projects_locations_global_domains_list` | `SELECT` | `parent` | Lists domains in a project. |
| `projects_locations_global_domains_create` | `INSERT` | `parent` | Creates a Microsoft AD domain. |
| `projects_locations_global_domains_delete` | `DELETE` | `name` | Deletes a domain. |
| `projects_locations_global_domains_attachTrust` | `EXEC` | `name` | Adds an AD trust to a domain. |
| `projects_locations_global_domains_detachTrust` | `EXEC` | `name` | Removes an AD trust. |
| `projects_locations_global_domains_patch` | `EXEC` | `name` | Updates the metadata and configuration of a domain. |
| `projects_locations_global_domains_reconfigureTrust` | `EXEC` | `name` | Updates the DNS conditional forwarder. |
| `projects_locations_global_domains_resetAdminPassword` | `EXEC` | `name` | Resets a domain's administrator password. |
| `projects_locations_global_domains_restore` | `EXEC` | `name` | RestoreDomain restores domain backup mentioned in the RestoreDomainRequest |
| `projects_locations_global_domains_updateLdapssettings` | `EXEC` | `name` | Patches a single ldaps settings. |
| `projects_locations_global_domains_validateTrust` | `EXEC` | `name` | Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests. |