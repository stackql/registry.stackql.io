---
title: management.profiles
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
<tr><td><b>Name</b></td><td><code>management.profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | View (Profile) ID. |
| `name` | `string` | Name of this view (profile). |
| `siteSearchCategoryParameters` | `string` | Site search category parameters for this view (profile). |
| `updated` | `string` | Time this view (profile) was last modified. |
| `parentLink` | `object` | Parent link for this view (profile). Points to the web property to which this view (profile) belongs. |
| `defaultPage` | `string` | Default page for this view (profile). |
| `siteSearchQueryParameters` | `string` | The site search query parameters for this view (profile). |
| `type` | `string` | View (Profile) type. Supported types: WEB or APP. |
| `enhancedECommerceTracking` | `boolean` | Indicates whether enhanced ecommerce tracking is enabled for this view (profile). This property can only be enabled if ecommerce tracking is enabled. |
| `stripSiteSearchQueryParameters` | `boolean` | Whether or not Analytics will strip search query parameters from the URLs in your reports. |
| `permissions` | `object` | Permissions the user has for this view (profile). |
| `webPropertyId` | `string` | Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs. |
| `stripSiteSearchCategoryParameters` | `boolean` | Whether or not Analytics will strip search category parameters from the URLs in your reports. |
| `childLink` | `object` | Child link for this view (profile). Points to the list of goals for this view (profile). |
| `botFilteringEnabled` | `boolean` | Indicates whether bot filtering is enabled for this view (profile). |
| `websiteUrl` | `string` | Website URL for this view (profile). |
| `created` | `string` | Time this view (profile) was created. |
| `internalWebPropertyId` | `string` | Internal ID for the web property to which this view (profile) belongs. |
| `starred` | `boolean` | Indicates whether this view (profile) is starred or not. |
| `excludeQueryParameters` | `string` | The query parameters that are excluded from this view (profile). |
| `selfLink` | `string` | Link for this view (profile). |
| `accountId` | `string` | Account ID to which this view (profile) belongs. |
| `eCommerceTracking` | `boolean` | Indicates whether ecommerce tracking is enabled for this view (profile). |
| `kind` | `string` | Resource type for Analytics view (profile). |
| `currency` | `string` | The currency type associated with this view (profile), defaults to USD. The supported values are:<br />USD, JPY, EUR, GBP, AUD, KRW, BRL, CNY, DKK, RUB, SEK, NOK, PLN, TRY, TWD, HKD, THB, IDR, ARS, MXN, VND, PHP, INR, CHF, CAD, CZK, NZD, HUF, BGN, LTL, ZAR, UAH, AED, BOB, CLP, COP, EGP, HRK, ILS, MAD, MYR, PEN, PKR, RON, RSD, SAR, SGD, VEF, LVL |
| `timezone` | `string` | Time zone for which this view (profile) has been configured. Time zones are identified by strings from the TZ database. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, profileId, webPropertyId` | Gets a view (profile) to which the user has access. |
| `list` | `SELECT` | `accountId, webPropertyId` | Lists views (profiles) to which the user has access. |
| `insert` | `INSERT` | `accountId, webPropertyId` | Create a new view (profile). |
| `delete` | `DELETE` | `accountId, profileId, webPropertyId` | Deletes a view (profile). |
| `patch` | `EXEC` | `accountId, profileId, webPropertyId` | Updates an existing view (profile). This method supports patch semantics. |
| `update` | `EXEC` | `accountId, profileId, webPropertyId` | Updates an existing view (profile). |
