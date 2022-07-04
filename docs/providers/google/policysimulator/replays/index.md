---
title: replays
hide_title: false
hide_table_of_contents: false
keywords:
  - replays
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
<tr><td><b>Name</b></td><td><code>replays</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.policysimulator.replays</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the `Replay`, which has the following format: `{projects\|folders\|organizations}/{resource-id}/locations/global/replays/{replay-id}`, where `{resource-id}` is the ID of the project, folder, or organization that owns the Replay. Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36` |
| `resultsSummary` | `object` | Summary statistics about the replayed log entries. |
| `state` | `string` | Output only. The current state of the `Replay`. |
| `config` | `object` | The configuration used for a Replay. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_locations_replays_get` | `SELECT` | `name` | Gets the specified Replay. Each `Replay` is available for at least 7 days. |
| `organizations_locations_replays_get` | `SELECT` | `name` | Gets the specified Replay. Each `Replay` is available for at least 7 days. |
| `projects_locations_replays_get` | `SELECT` | `name` | Gets the specified Replay. Each `Replay` is available for at least 7 days. |
| `folders_locations_replays_create` | `INSERT` | `parent` | Creates and starts a Replay using the given ReplayConfig. |
| `organizations_locations_replays_create` | `INSERT` | `parent` | Creates and starts a Replay using the given ReplayConfig. |
| `projects_locations_replays_create` | `INSERT` | `parent` | Creates and starts a Replay using the given ReplayConfig. |
