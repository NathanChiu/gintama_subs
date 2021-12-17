# Subtitle aggregation tool

Many subtitle files for shows appear in this format:
```
1
00:00:32,041 --> 00:00:34,377
Line one dialog

2
00:00:34,377 --> 00:00:36,395
Line two dialog

3
00:00:36,395 --> 00:00:39,565
Line 3 dialog
...
```
and have one ```.srt``` file for each episode in the series.

This makes a number of common tasks difficult for community subbers who  reference these ```.srt``` files to produce subbed content.
  - ```Ctrl+F``` cannot be used to quickly find occurrences of strings when using a standard text editor (e.g. MSWord), due to the subtitles being spread over multiple files.
  - When a certain string is found, the search result does not clearly indicate which file the string was found in.

To alleviate this, this tool aggregates the content of all ```.srt``` files in a directory into a single ```collection.srt```, which takes the form

```
Episode_001.srt>>1
Episode_001.srt>>00:00:32,041 --> 00:00:34,377
Episode_001.srt>>Line one dialog
Episode_001.srt>>
Episode_001.srt>>2
Episode_001.srt>>00:00:34,377 --> 00:00:36,395
Episode_001.srt>>Line two dialog
Episode_001.srt>>
...
Episode_002.srt>>1
Episode_002.srt>>00:00:32,041 --> 00:00:34,377
Episode_002.srt>>Line one dialog
Episode_002.srt>>
Episode_002.srt>>2
Episode_002.srt>>00:00:34,377 --> 00:00:36,395
Episode_002.srt>>Line two dialog
Episode_002.srt>>
```
