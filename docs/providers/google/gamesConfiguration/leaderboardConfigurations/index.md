---
title: leaderboardConfigurations
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
<tr><td><b>Name</b></td><td><code>leaderboardConfigurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gamesConfiguration.leaderboardConfigurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the leaderboard. |
| `draft` | `object` | A leaderboard configuration detail. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#leaderboardConfiguration`. |
| `published` | `object` | A leaderboard configuration detail. |
| `scoreMax` | `string` | Maximum score that can be posted to this leaderboard. |
| `scoreMin` | `string` | Minimum score that can be posted to this leaderboard. |
| `scoreOrder` | `string` |  |
| `token` | `string` | The token for this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `leaderboardId` | Retrieves the metadata of the leaderboard configuration with the given ID. |
| `list` | `SELECT` | `applicationId` | Returns a list of the leaderboard configurations in this application. |
| `insert` | `INSERT` | `applicationId` | Insert a new leaderboard configuration in this application. |
| `delete` | `DELETE` | `leaderboardId` | Delete the leaderboard configuration with the given ID. |
| `update` | `EXEC` | `leaderboardId` | Update the metadata of the leaderboard configuration with the given ID. |
