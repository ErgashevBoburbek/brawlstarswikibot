import brawlstats
n = int(input())

clientd = brawlstats.Client("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjAzOTljZWM2LTIzZDQtNGFlMC1iMWZiLTk3Mzg2MmYyZDdkZiIsImlhdCI6MTczMDM2ODMyNCwic3ViIjoiZGV2ZWxvcGVyLzJlNDc3NGVkLWFlNmMtOWU0Yy00N2YxLWU1NjA2NzI4ZmExOCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg1LjIxMy4yMjkuNTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.k6eIhR2NGs5uF76GqJuGKcN_7yU2XjdJ_OBvNJFPqxf1EVLDWiYe8ZURvgf2UnVPrKW4cqXOfoz7wHycsaHPgQ")
br = clientd.get_brawlers(n).name

print(br)