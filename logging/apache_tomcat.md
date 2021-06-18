

```
<source>
  @type tail
  format multiline
  # Match the date at the beginning of each entry, which can be in one of two
  # different formats.
  format_firstline /^(\w+\s\d+,\s\d+)|(\d+-\d+-\d+\s)/
  format1 /(?<message>.*)/
  multiline_flush_interval 5s
  path /var/log/tomcat*/catalina.out,/var/log/tomcat*/localhost.*.log
  pos_file /var/lib/google-fluentd/pos/tomcat-multiline.pos
  read_from_head true
  tag tomcat
</source>
```
