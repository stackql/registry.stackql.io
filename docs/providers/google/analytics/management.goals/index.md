---
title: management.goals
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
<tr><td><b>Name</b></td><td><code>management.goals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.goals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Goal ID. |
| `name` | `string` | Goal name. |
| `accountId` | `string` | Account ID to which this goal belongs. |
| `type` | `string` | Goal type. Possible values are URL_DESTINATION, VISIT_TIME_ON_SITE, VISIT_NUM_PAGES, AND EVENT. |
| `visitTimeOnSiteDetails` | `object` | Details for the goal of the type VISIT_TIME_ON_SITE. |
| `profileId` | `string` | View (Profile) ID to which this goal belongs. |
| `active` | `boolean` | Determines whether this goal is active. |
| `webPropertyId` | `string` | Web property ID to which this goal belongs. The web property ID is of the form UA-XXXXX-YY. |
| `eventDetails` | `object` | Details for the goal of the type EVENT. |
| `parentLink` | `object` | Parent link for a goal. Points to the view (profile) to which this goal belongs. |
| `internalWebPropertyId` | `string` | Internal ID for the web property to which this goal belongs. |
| `selfLink` | `string` | Link for this goal. |
| `created` | `string` | Time this goal was created. |
| `visitNumPagesDetails` | `object` | Details for the goal of the type VISIT_NUM_PAGES. |
| `updated` | `string` | Time this goal was last modified. |
| `kind` | `string` | Resource type for an Analytics goal. |
| `value` | `number` | Goal value. |
| `urlDestinationDetails` | `object` | Details for the goal of the type URL_DESTINATION. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, goalId, profileId, webPropertyId` | Gets a goal to which the user has access. |
| `list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists goals to which the user has access. |
| `insert` | `INSERT` | `accountId, profileId, webPropertyId` | Create a new goal. |
| `patch` | `EXEC` | `accountId, goalId, profileId, webPropertyId` | Updates an existing goal. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, goalId, profileId, webPropertyId` | Updates an existing goal. |
