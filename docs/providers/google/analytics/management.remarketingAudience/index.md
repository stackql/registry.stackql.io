---
title: management.remarketingAudience
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>management.remarketingAudience</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.remarketingAudience</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Remarketing Audience ID. |
| `name` | `string` | The name of this remarketing audience. |
| `description` | `string` | The description of this remarketing audience. |
| `linkedAdAccounts` | `array` | The linked ad accounts associated with this remarketing audience. A remarketing audience can have only one linkedAdAccount currently. |
| `webPropertyId` | `string` | Web property ID of the form UA-XXXXX-YY to which this remarketing audience belongs. |
| `kind` | `string` | Collection type. |
| `audienceType` | `string` | The type of audience, either SIMPLE or STATE_BASED. |
| `linkedViews` | `array` | The views (profiles) that this remarketing audience is linked to. |
| `audienceDefinition` | `object` | The simple audience definition that will cause a user to be added to an audience. |
| `stateBasedAudienceDefinition` | `object` | A state based audience definition that will cause a user to be added or removed from an audience. |
| `accountId` | `string` | Account ID to which this remarketing audience belongs. |
| `updated` | `string` | Time this remarketing audience was last modified. |
| `internalWebPropertyId` | `string` | Internal ID for the web property to which this remarketing audience belongs. |
| `created` | `string` | Time this remarketing audience was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, remarketingAudienceId, webPropertyId` | Gets a remarketing audience to which the user has access. |
| `list` | `SELECT` | `accountId, webPropertyId` | Lists remarketing audiences to which the user has access. |
| `insert` | `INSERT` | `accountId, webPropertyId` | Creates a new remarketing audience. |
| `delete` | `DELETE` | `accountId, remarketingAudienceId, webPropertyId` | Delete a remarketing audience. |
| `patch` | `EXEC` | `accountId, remarketingAudienceId, webPropertyId` | Updates an existing remarketing audience. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, remarketingAudienceId, webPropertyId` | Updates an existing remarketing audience. |
