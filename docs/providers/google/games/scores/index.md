---
title: scores
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
<tr><td><b>Name</b></td><td><code>scores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.games.scores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `scoreValue` | `string` | The numerical value of this score. |
| `timeSpan` | `string` | The time span of this high score. |
| `formattedScore` | `string` | The localized string for the numerical value of this score. |
| `player` | `object` | A Player resource. |
| `writeTimestampMillis` | `string` | The timestamp at which this score was recorded, in milliseconds since the epoch in UTC. |
| `scoreRank` | `string` | The rank of this score for this leaderboard. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#leaderboardEntry`. |
| `scoreTag` | `string` | Additional information about the score. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. |
| `formattedScoreRank` | `string` | The localized string for the rank of this score for this leaderboard. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `leaderboardId, playerId, timeSpan` | Get high scores, and optionally ranks, in leaderboards for the currently authenticated player. For a specific time span, `leaderboardId` can be set to `ALL` to retrieve data for all leaderboards in a given time span. `NOTE: You cannot ask for 'ALL' leaderboards and 'ALL' timeSpans in the same request; only one parameter may be set to 'ALL'. |
| `list` | `SELECT` | `collection, leaderboardId, timeSpan` | Lists the scores in a leaderboard, starting from the top. |
| `listWindow` | `EXEC` | `collection, leaderboardId, timeSpan` | Lists the scores in a leaderboard around (and including) a player's score. |
| `submit` | `EXEC` | `leaderboardId, score` | Submits a score to the specified leaderboard. |
| `submitMultiple` | `EXEC` |  | Submits multiple scores to leaderboards. |
