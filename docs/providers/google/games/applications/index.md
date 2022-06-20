---
title: applications
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.games.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the application. |
| `name` | `string` | The name of the application. |
| `description` | `string` | The description of the application. |
| `leaderboard_count` | `integer` | The number of leaderboards visible to the currently authenticated player. |
| `assets` | `array` | The assets of the application. |
| `instances` | `array` | The instances of the application. |
| `achievement_count` | `integer` | The number of achievements visible to the currently authenticated player. |
| `enabledFeatures` | `array` | A list of features that have been enabled for the application. |
| `themeColor` | `string` | A hint to the client UI for what color to use as an app-themed color. The color is given as an RGB triplet (e.g. "E0E0E0"). |
| `category` | `object` | An application category object. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#application`. |
| `lastUpdatedTimestamp` | `string` | The last updated timestamp of the application. |
| `author` | `string` | The author of the application. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationId` | Retrieves the metadata of the application with the given ID. If the requested application is not available for the specified `platformType`, the returned response will not include any instance data. |
| `getEndPoint` | `EXEC` |  | Returns a URL for the requested end point type. |
| `played` | `EXEC` |  | Indicate that the currently authenticated user is playing your application. |
| `verify` | `EXEC` | `applicationId` | Verifies the auth token provided with this request is for the application with the specified ID, and returns the ID of the player it was granted for. |