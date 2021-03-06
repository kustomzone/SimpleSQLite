#!/usr/bin/env python
# encoding: utf-8


import json
import simplesqlite
import six

table_name = "sample_table"
con = simplesqlite.connect_sqlite_db_mem()

# create table -----
data_matrix = [
    [1, 1.1, "aaa", 1,   1],
    [2, 2.2, "bbb", 2.2, 2.2],
    [3, 3.3, "ccc", 3,   "ccc"],
]
con.create_table_with_data(
    table_name,
    attribute_name_list=["attr_a", "attr_b", "attr_c", "attr_d", "attr_e"],
    data_matrix=data_matrix)

# display values in the table -----
six.print_(con.get_attribute_name_list(table_name))
result = con.select(select="*", table_name=table_name)
for record in result.fetchall():
    six.print_(record)

# display data type for each column in the table -----
six.print_(json.dumps(con.get_attr_type(table_name), indent=4))
